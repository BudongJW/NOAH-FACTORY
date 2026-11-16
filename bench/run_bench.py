"""Phase 0 benchmark: re-place and re-route KiCad demo boards and compare with the human originals.

Protocol (per board)
  1. Copy the project. Lock connectors, mounting holes, fiducials and already-locked parts
     (what a user would pin, like MODI Factory's Lock).
  2. Start every other part from a random position (init=random): the original placement is
     not used as a hint.
  3. Run the full pipeline: placement (4 seeds) -> Freerouting -> kicad-cli DRC -> report.
  4. Measure the human original the same way (HPWL, decoupling distances, DRC, track length, vias).

Usage:  python bench/run_bench.py [--boards a,b] [--place-time S] [--out bench/results]
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from noah_factory.kicad import board_to_ir, load_board, routing_stats  # noqa: E402
from noah_factory.pipeline import RunConfig, copy_project, run  # noqa: E402
from noah_factory.placement import PlacementConfig, PlacementProblem, current_metrics  # noqa: E402
from noah_factory.verify import run_drc  # noqa: E402

DEMOS = Path("/usr/share/kicad/demos")
BOARDS = {
    "ecc83": "ecc83/ecc83-pp.kicad_pcb",
    "sonde_xilinx": "sonde xilinx/sonde xilinx.kicad_pcb",
    "interf_u": "interf_u/interf_u.kicad_pcb",
    "pic_programmer": "pic_programmer/pic_programmer.kicad_pcb",
    "complex_hierarchy": "complex_hierarchy/complex_hierarchy.kicad_pcb",
    "stickhub": "stickhub/StickHub.kicad_pcb",
    "multichannel_mixer": "multichannel/multichannel_mixer.kicad_pcb",
    "kit_dev_coldfire": "kit-dev-coldfire-xilinx_5213/kit-dev-coldfire-xilinx_5213.kicad_pcb",
}
LOCK_KINDS = {"connector", "mounting", "fiducial"}


def baseline(board_path: Path, work: Path) -> dict:
    """Metrics of the human-made original, measured with the same tools."""
    src = copy_project(board_path, work)
    board = load_board(src)
    ir = board_to_ir(board, name=board_path.stem)
    m = current_metrics(ir)
    density = PlacementProblem(ir, PlacementConfig()).density()
    parity = src.with_suffix(".kicad_sch").exists()
    drc = run_drc(src, work / "drc_original.json", schematic_parity=parity)
    return {
        "hpwl_mm": m["hpwl_mm"],
        "decap_pass": sum(d["pass"] for d in m["decaps"]),
        "decap_total": len(m["decaps"]),
        "route_stats": routing_stats(load_board(src)),
        "drc": {k: v for k, v in drc.items() if k != "examples"},
        "lock": sorted(c.ref for c in ir.components if c.locked or c.kind in LOCK_KINDS),
        "parts": len(ir.components),
        "density_pct": density,
    }


def fill_density(rows: list[dict]) -> None:
    """Older result files lack the density figure; it depends only on the board, so recompute it."""
    for r in rows:
        if "density_pct" in r["baseline"]:
            continue
        ir = board_to_ir(load_board(DEMOS / BOARDS[r["board"]]))
        r["baseline"]["density_pct"] = PlacementProblem(ir, PlacementConfig()).density()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--boards", default=",".join(BOARDS))
    ap.add_argument("--place-time", type=float, default=0.0, help="seconds per seed (0 = scale with size)")
    ap.add_argument("--seeds", type=int, default=4)
    ap.add_argument("--route-timeout", type=int, default=600)
    ap.add_argument("--out", type=Path, default=ROOT / "bench" / "results")
    ap.add_argument("--summary-only", action="store_true", help="rewrite summary.md from results.json")
    a = ap.parse_args()

    a.out.mkdir(parents=True, exist_ok=True)
    if a.summary_only:
        rows = json.loads((a.out / "results.json").read_text())
        fill_density(rows)
        (a.out / "results.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2, default=str))
        write_summary(rows, a.out / "summary.md")
        print(f"wrote {a.out / 'summary.md'}")
        return 0
    work_root = ROOT / "runs" / "bench"
    rows = []
    for name in [b.strip() for b in a.boards.split(",") if b.strip()]:
        path = DEMOS / BOARDS[name]
        if not path.exists():
            print(f"skip {name}: {path} missing")
            continue
        print(f"=== {name}")
        t0 = time.monotonic()
        base = baseline(path, work_root / name / "original")
        place_time = a.place_time or min(90.0, 5.0 + 0.4 * base["parts"])
        try:
            summary = run(RunConfig(input=path, out=work_root / name / "noah", lock=set(base["lock"]),
                                    seeds=a.seeds, candidates=3, place_time_s=place_time, init="random",
                                    route_passes=40, route_timeout_s=a.route_timeout))
            error = None
        except Exception as exc:  # keep benchmarking the other boards
            summary, error = None, f"{type(exc).__name__}: {exc}"
            print(f"  failed: {error}")
        rows.append({"board": name, "baseline": base, "noah": summary, "error": error,
                     "place_time_per_seed_s": place_time, "wall_s": round(time.monotonic() - t0, 1)})
        (a.out / "results.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2, default=str))

    write_summary(rows, a.out / "summary.md")
    print(f"wrote {a.out / 'summary.md'}")
    return 0


def _ratio(a, b):
    return f"{a / b:.2f}" if a is not None and b else "–"


def write_summary(rows: list[dict], path: Path) -> None:
    lines = [
        "# Phase 0 벤치마크 결과",
        "",
        f"- 환경: {platform.machine()}, CPU {__import__('os').cpu_count()}코어, Python {platform.python_version()}",
        "- 방법: 커넥터·장착 홀·피듀셜을 고정하고 나머지 부품은 **무작위 위치에서 시작**해 자동 배치 → Freerouting "
        "자동 배선 → kicad-cli DRC. 비교 대상은 사람이 설계한 원본 보드(같은 도구로 측정).",
        "- 비율 = NOAH ÷ 원본 (1.00보다 작으면 NOAH가 더 짧음/적음).",
        "",
        "| 보드 | 부품(고정) | 층 | 부품 면적 앞/뒤 % | 배치 s | 배선 s | 전체 s | 미배선 | 전기 DRC (원본) | HPWL 비율 | 배선 길이 비율 | 비아 (원본) | 디커플링 통과 (원본) | 근거 문장 검증/제외 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        b, n = r["baseline"], r["noah"]
        dens = b.get("density_pct") or {}
        dtext = f"{dens.get('front', '–')}/{dens.get('back', '–')}"
        if dens and max(dens["front"], dens["back"]) > 85:
            dtext = f"**{dtext}** ⚠"
        if n is None:
            lines.append(f"| {r['board']} | {b['parts']} | – | {dtext} | – | – | – | 실패 | – | – | – | – | – | {r['error']} |")
            continue
        t = n["timings"]
        drc_o = b["drc"].get("by_category", {}).get("electrical", 0)
        drc_n = n["drc"].get("by_category", {}).get("electrical", 0)
        rs_n, rs_o = n.get("route_stats") or {}, b["route_stats"]
        pb = n["placement"]["best"]
        lines.append(
            f"| {r['board']} | {n['parts']} ({len(n['locked'])}) | {n['layers']} | {dtext} | {t.get('placement_s')} | "
            f"{t.get('routing_s', '–')} | {t.get('total_s')} | {n['drc'].get('unconnected', '–')} | "
            f"{drc_n} ({drc_o}) | {_ratio(pb['hpwl_mm'], b['hpwl_mm'])} | "
            f"{_ratio(rs_n.get('track_length_mm'), rs_o.get('track_length_mm'))} | "
            f"{rs_n.get('via_count', '–')} ({rs_o.get('via_count')}) | "
            f"{pb['decap_pass']}/{pb['decap_total']} ({b['decap_pass']}/{b['decap_total']}) | "
            f"{n['claims']['verified']}/{n['claims']['rejected']} |")
    lines += ["", "## 해석 시 주의", "",
              "- 원본은 사람이 기능·기구·SI를 고려해 배치한 결과이고, NOAH는 배선 길이·겹침·디커플링·커넥터 규칙만 "
              "최적화합니다. HPWL이 짧다고 더 좋은 설계라는 뜻은 아닙니다.",
              "- '전기 DRC'는 kicad-cli가 보고한 전기 규칙 위반(클리어런스·단락·미연결 비아 등) 수입니다. "
              "라이브러리 미설치 경고, 실크 문제, 회로도 라이브러리 이름 불일치는 제외했습니다.",
              "- '부품 면적'은 코트야드를 감싸는 사각형 면적의 합 ÷ 보드 면적(관통홀 부품은 양면 모두 계산)입니다. "
              "85%를 넘는 보드(⚠)는 현재 사각형 근사 배치기의 한계를 넘는 밀집 설계입니다.",
              "- 각 보드 1회 실행 결과이며 시드에 따라 달라집니다.", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
