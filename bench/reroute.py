"""Re-route existing placements with the current routing code (placement kept as is).

Isolates routing changes from placement changes: take the best candidate of each run in an
A/B directory (runs/ab/<arm>/<board>/noah/candidates/candidate_1.kicad_pcb), route it again,
and compare with how the same placement routed in the original run.

    python bench/reroute.py runs/ab --out runs/reroute [--boards a,b] [--route-timeout 300]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from noah_factory.pipeline import RunConfig, run  # noqa: E402

ELECTRICAL_DETAIL = ("track_dangling", "via_dangling", "starved_thermal", "shorting_items", "clearance")


def outcome(run_json: dict) -> dict:
    d = run_json["drc"]
    by_type = d.get("by_type", {})
    return {"unrouted": d.get("unconnected"), "electrical": d.get("by_category", {}).get("electrical", 0),
            **{t: by_type.get(t, 0) for t in ELECTRICAL_DETAIL},
            "route_s": run_json["timings"].get("routing_s"),
            "dangling_removed": (run_json.get("routing") or {}).get("cleanup", {}).get("removed", 0)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ab_root", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--boards", default="")
    ap.add_argument("--arms", default="", help="comma-separated arm names to include")
    ap.add_argument("--route-timeout", type=int, default=300)
    a = ap.parse_args()
    wanted = {b for b in a.boards.split(",") if b}
    arms = {x for x in a.arms.split(",") if x}
    rows = []
    for arm in sorted(p for p in a.ab_root.iterdir() if p.is_dir() and (not arms or p.name in arms)):
        for board_dir in sorted(p for p in arm.iterdir() if p.is_dir()):
            if wanted and board_dir.name not in wanted:
                continue
            cand = board_dir / "noah" / "candidates" / "candidate_1.kicad_pcb"
            old = board_dir / "noah" / "run.json"
            if not (cand.exists() and old.exists()):
                continue
            print(f"=== {arm.name} {board_dir.name}", flush=True)
            new = run(RunConfig(input=cand.resolve(), out=(a.out / arm.name / board_dir.name).resolve(),
                                place=False, init="current", route_passes=40,
                                route_timeout_s=a.route_timeout, export=False))
            rows.append({"arm": arm.name, "board": board_dir.name,
                         "before": outcome(json.loads(old.read_text())), "after": outcome(new)})
            (a.out / "reroute.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    lines = ["| 조건 | 보드 | 미배선 전→후 | 전기 DRC 전→후 | dangling 전→후 | starved_thermal 전→후 | 제거한 조각 |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        b, f = r["before"], r["after"]
        dang_b = b["track_dangling"] + b["via_dangling"]
        dang_f = f["track_dangling"] + f["via_dangling"]
        lines.append(f"| {r['arm']} | {r['board']} | {b['unrouted']} → {f['unrouted']} | "
                     f"{b['electrical']} → {f['electrical']} | {dang_b} → {dang_f} | "
                     f"{b['starved_thermal']} → {f['starved_thermal']} | {f['dangling_removed']} |")
    text = "\n".join(lines) + "\n"
    (a.out / "reroute.md").write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
