"""End-to-end Phase 0 pipeline:

KiCad board -> IR -> placement candidates -> routing (best candidate) -> DRC
-> evidence -> verified claims -> report -> fabrication files.
"""

from __future__ import annotations

import copy
import json
import shutil
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from . import __version__
from .evidence import EvidenceStore
from .export import export_fabrication
from .kicad import (apply_placement, board_to_ir, export_dsn, import_ses, kicad_version, load_board,
                    lock_refs, prepare_for_router, routing_stats, save_board, strip_routing)
import numpy as np

from .placement import (PlacementConfig, PlacementProblem, PlacementResult, apply_result, current_metrics,
                        place_candidates)
from .rationale import build_claims, build_evidence, render_report
from .routing import RoutingConfig, freerouting_version, run_freerouting
from .verify import kicad_cli_version, run_drc

PROJECT_SUFFIXES = (".kicad_pro", ".kicad_sch", ".kicad_dru")
# Above this courtyard-bbox area share of the board (per side), the axis-aligned bbox placer
# cannot reliably find an overlap-free placement (measured: StickHub at 96-101% fails).
DENSITY_LIMIT_PCT = 85.0
PROJECT_FILES = ("sym-lib-table", "fp-lib-table")


@dataclass
class RunConfig:
    input: Path
    out: Path
    lock: set[str] = field(default_factory=set)
    edge: set[str] = field(default_factory=set)
    seeds: int = 4
    candidates: int = 3
    place_time_s: float = 30.0
    init: str = "random"
    place: bool = True
    route: bool = True
    route_passes: int = 30
    route_timeout_s: int = 300
    export: bool = True
    workers: int = 0


def copy_project(board: Path, dest: Path) -> Path:
    """Copy the board and its sibling project files (schematics, rules) into dest."""
    dest.mkdir(parents=True, exist_ok=True)
    src_dir = board.parent
    for f in src_dir.iterdir():
        if f.is_file() and (f.suffix in PROJECT_SUFFIXES or f.name in PROJECT_FILES or f == board):
            shutil.copy2(f, dest / f.name)
    return dest / board.name


def _route_stage(board_path: Path, route_dir: Path, stem: str, tag: str, rcfg: RoutingConfig,
                 rules: list[Path], drop_pours: bool) -> tuple[dict, Path]:
    copy_ = load_board(board_path)
    prep = prepare_for_router(copy_, drop_pours=drop_pours)
    dsn, ses = route_dir / f"{stem}.{tag}.dsn", route_dir / f"{stem}.{tag}.ses"
    export_dsn(copy_, dsn)
    res = run_freerouting(dsn, ses, rcfg, route_dir / f"freerouting.{tag}.log", extra_inputs=rules)
    res["stage"] = tag
    res["prepared"] = prep
    return res, ses


def route_two_stage(board_path: Path, out: Path, stem: str, rcfg: RoutingConfig) -> dict:
    """Stage 1 routes with copper pours kept (plane nets connect through the pour).
    The pours are then refilled; if anything is still unconnected (a pour split after the parts
    moved), stage 2 routes the rest with pours removed and the stage-1 tracks kept.
    The session from each stage is imported into the board at board_path in place."""
    route_dir = out / "routing"
    route_dir.mkdir(exist_ok=True)
    rules = [out / "input" / f"{stem}.kicad_pro", out / "input" / f"{stem}.kicad_dru"]
    stages = []

    res, ses = _route_stage(board_path, route_dir, stem, "stage1", rcfg, rules, drop_pours=False)
    stages.append(res)
    if ses.exists():
        b = load_board(board_path)
        res["imported"] = import_ses(b, ses)
        save_board(b, board_path)
    check = run_drc(board_path, route_dir / "drc_stage1.json", schematic_parity=False)  # refills pours
    res["unconnected_after_refill"] = check.get("unconnected")

    if check.get("ok") and check["unconnected"] > 0:
        res2, ses2 = _route_stage(board_path, route_dir, stem, "stage2", rcfg, rules, drop_pours=True)
        stages.append(res2)
        if ses2.exists():
            b = load_board(board_path)
            res2["imported"] = import_ses(b, ses2)
            save_board(b, board_path)
    last = stages[-1]
    return {
        "ok": all(s["ok"] for s in stages),
        "stages": stages,
        "time_s": round(sum(s["time_s"] for s in stages), 2),
        "reported_unrouted": last.get("reported_unrouted"),
        "reported_violations": last.get("reported_violations"),
        "max_passes": rcfg.max_passes,
    }


def run(cfg: RunConfig, log=print) -> dict:
    t_all = time.monotonic()
    timings: dict[str, float] = {}
    out = cfg.out
    out.mkdir(parents=True, exist_ok=True)
    stem = cfg.input.stem

    # 1. Intake -------------------------------------------------------------
    t = time.monotonic()
    work_input = copy_project(cfg.input, out / "input")
    board = load_board(work_input)
    lock_refs(board, cfg.lock)
    ir = board_to_ir(board, name=stem, source_path=str(cfg.input))
    locked = sorted(c.ref for c in ir.components if c.locked)
    before = current_metrics(ir, PlacementConfig(edge_refs=tuple(cfg.edge)))
    timings["intake_s"] = round(time.monotonic() - t, 2)
    log(f"[intake] {len(ir.components)} parts, {len(ir.nets)} nets, {ir.board.copper_layers} layers, "
        f"{len(locked)} locked ({timings['intake_s']}s)")

    # 2. Placement ----------------------------------------------------------
    t = time.monotonic()
    pcfg = PlacementConfig(time_limit_s=cfg.place_time_s, init=cfg.init, edge_refs=tuple(cfg.edge))
    if cfg.place:
        seeds = list(range(1, max(cfg.seeds, cfg.candidates) + 1))
        problem, results = place_candidates(ir, pcfg, seeds, workers=cfg.workers)
    else:
        # Keep the input placement (control runs: same router and checks on the original layout).
        seeds = [0]
        problem = PlacementProblem(ir, pcfg)
        X = np.array([c.x for c in ir.components])
        Y = np.array([c.y for c in ir.components])
        K = np.zeros(problem.n, dtype=int)
        results = [PlacementResult(0, X, Y, K, 0.0, problem.evaluate(X, Y, K),
                                   {"moves": 0, "accepted": 0, "time_s": 0.0}, [])]
    timings["placement_s"] = round(time.monotonic() - t, 2)
    density = problem.density()
    if max(density["front"], density["back"]) > DENSITY_LIMIT_PCT:
        log(f"[placement] warning: part area is {density['front']}% (front) / {density['back']}% (back) "
            f"of the board, above the {DENSITY_LIMIT_PCT}% the bounding-box placer handles")
    cand_dir = out / "candidates"
    cand_dir.mkdir(exist_ok=True)
    candidates = []
    for rank, res in enumerate(results[:cfg.candidates], start=1):
        cir = copy.deepcopy(ir)
        apply_result(cir, problem, res)
        b = load_board(work_input)
        lock_refs(b, cfg.lock)
        apply_placement(b, cir)
        strip_routing(b)
        path = cand_dir / f"candidate_{rank}.kicad_pcb"
        save_board(b, path)
        candidates.append({"rank": rank, "seed": res.seed, "cost": round(res.cost, 1),
                           "hpwl_mm": res.breakdown["hpwl_mm"], "overlaps": len(res.breakdown["overlaps"]),
                           "outside": len(res.breakdown["outside"]),
                           "legalization_failures": res.legalization_failures,
                           "stats": res.stats, "file": str(path.relative_to(out))})
    best = results[0]
    after = best.breakdown
    log(f"[placement] {len(seeds)} seeds, best HPWL {after['hpwl_mm']} mm (input {before['hpwl_mm']} mm), "
        f"overlaps {len(after['overlaps'])}, outside {len(after['outside'])} ({timings['placement_s']}s)")

    # 3. Routing ------------------------------------------------------------
    final_dir = out / "final"
    final_dir.mkdir(exist_ok=True)
    for f in (out / "input").iterdir():
        if f.suffix in PROJECT_SUFFIXES or f.name in PROJECT_FILES:
            shutil.copy2(f, final_dir / f.name)
    final_board_path = final_dir / f"{stem}.kicad_pcb"
    best_ir = copy.deepcopy(ir)
    apply_result(best_ir, problem, best)
    board = load_board(work_input)
    lock_refs(board, cfg.lock)
    apply_placement(board, best_ir)
    strip_routing(board)
    locked_moved = [c.ref for c, o in zip(best_ir.components, ir.components)
                    if c.locked and (abs(c.x - o.x) > 1e-6 or abs(c.y - o.y) > 1e-6 or c.rotation != o.rotation)]

    rcfg = RoutingConfig(max_passes=cfg.route_passes, timeout_s=cfg.route_timeout_s)
    routing = None
    save_board(board, final_board_path)
    if cfg.route:
        t = time.monotonic()
        routing = route_two_stage(final_board_path, out, stem, rcfg)
        timings["routing_s"] = round(time.monotonic() - t, 2)
        log(f"[routing] stages={len(routing['stages'])} ok={routing['ok']} "
            f"unrouted(reported)={routing['reported_unrouted']} ({timings['routing_s']}s)")

    # 4. Verification -------------------------------------------------------
    t = time.monotonic()
    parity = (final_dir / f"{stem}.kicad_sch").exists()
    drc = run_drc(final_board_path, out / "drc.json", schematic_parity=parity)
    final = load_board(final_board_path)
    rstats = routing_stats(final) if cfg.route else None
    timings["verification_s"] = round(time.monotonic() - t, 2)
    if drc.get("ok"):
        log(f"[verify] unconnected {drc['unconnected']}, violations {drc['by_category']} "
            f"({timings['verification_s']}s)")
    else:
        log(f"[verify] DRC failed: {drc.get('error', '')[:200]}")

    # 5. Evidence, claims, report ----------------------------------------------
    t = time.monotonic()
    tools = {"placer": f"noah-placer {__version__}", "router": freerouting_version(rcfg),
             "drc": kicad_cli_version()}
    store = EvidenceStore()
    ids = build_evidence(store, before=before, after=after, locked=locked, locked_moved=locked_moved,
                         legal_failures=best.legalization_failures, drc=drc, routing=routing,
                         route_stats=rstats, tools=tools, density=density, density_limit=DENSITY_LIMIT_PCT)
    claims = build_claims(store, ids, before=before, after=after, locked=locked, drc=drc, route_stats=rstats)
    store.dump(out / "evidence.json")
    (out / "claims.json").write_text(json.dumps([asdict(c) for c in claims], ensure_ascii=False, indent=2))
    timings["report_s"] = round(time.monotonic() - t, 2)

    # 6. Export -------------------------------------------------------------
    fab = None
    if cfg.export:
        t = time.monotonic()
        fab = export_fabrication(final_board_path, out / "fab")
        timings["export_s"] = round(time.monotonic() - t, 2)
    timings["total_s"] = round(time.monotonic() - t_all, 2)

    run_info = {
        "입력": cfg.input.name,
        "부품·넷·층": f"{len(ir.components)}개 · {len(ir.nets)}개 · {ir.board.copper_layers}층",
        "배치 시드·후보": f"{len(seeds)}개 시드 중 상위 {len(candidates)}안, 최적 시드 {best.seed}",
        "단계별 시간(초)": ", ".join(f"{k}={v}" for k, v in timings.items()),
        "도구": f"{tools['placer']}; {tools['router']}; {tools['drc']}; pcbnew {kicad_version()}",
    }
    render_report(out / "report.md", title=stem, claims=claims, drc=drc, run_info=run_info,
                  parity_checked=parity)

    summary = {
        "input": str(cfg.input), "parts": len(ir.components), "nets": len(ir.nets),
        "layers": ir.board.copper_layers, "locked": locked, "timings": timings, "density_pct": density,
        "placement": {"input": {k: before[k] for k in ("hpwl_mm",)} | {
            "decap_pass": sum(d["pass"] for d in before["decaps"]), "decap_total": len(before["decaps"])},
            "best": {"hpwl_mm": after["hpwl_mm"], "overlaps": len(after["overlaps"]),
                     "outside": len(after["outside"]),
                     "decap_pass": sum(d["pass"] for d in after["decaps"]),
                     "decap_total": len(after["decaps"]),
                     "legalization_failures": best.legalization_failures},
            "candidates": candidates},
        "routing": routing, "route_stats": rstats, "drc": {k: v for k, v in drc.items() if k != "examples"},
        "claims": {"verified": sum(c.status == "verified" for c in claims),
                   "rejected": sum(c.status != "verified" for c in claims)},
        "fabrication": fab,
    }
    (out / "run.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str))
    log(f"[done] {timings['total_s']}s -> {out / 'report.md'}")
    return summary
