"""Does the congestion estimate explain routing outcomes?

For each benchmark board, compare the congestion of the human placement with the NOAH
placement from a previous benchmark run, next to how each placement actually routed
(bench/results/results.json). Usage:

    python bench/congestion_check.py [--runs runs/bench] [--results bench/results/results.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from noah_factory.congestion import CongestionConfig  # noqa: E402
from noah_factory.kicad import board_to_ir, load_board  # noqa: E402
from noah_factory.placement import PlacementConfig, current_metrics  # noqa: E402

from run_bench import BOARDS, DEMOS  # noqa: E402


def congestion_of(path: Path, ccfg: CongestionConfig) -> dict:
    ir = board_to_ir(load_board(path))
    return current_metrics(ir, PlacementConfig(congestion=ccfg))["congestion"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=Path, default=ROOT / "runs" / "bench")
    ap.add_argument("--results", type=Path, default=ROOT / "bench" / "results" / "results.json")
    ap.add_argument("--utilization", type=float, default=CongestionConfig().utilization)
    a = ap.parse_args()
    ccfg = CongestionConfig(utilization=a.utilization)
    outcomes = {r["board"]: r for r in json.loads(a.results.read_text())}

    print("| 보드 | 원본 ACE5 | NOAH ACE5 | 비율 | 원본 과밀 % | NOAH 과밀 % | 원본 배치 미배선/전기 | NOAH 배치 미배선/전기 |")
    print("|---|---|---|---|---|---|---|---|")
    for name, rel in BOARDS.items():
        cand = a.runs / name / "noah" / "candidates" / "candidate_1.kicad_pcb"
        if not cand.exists():
            continue
        orig = congestion_of(DEMOS / rel, ccfg)
        noah = congestion_of(cand, ccfg)
        r = outcomes.get(name, {})

        def outcome(s):
            if not s:
                return "–"
            return f"{s['drc'].get('unconnected', '–')}/{s['drc'].get('by_category', {}).get('electrical', 0)}"

        ratio = noah["ace5"] / orig["ace5"] if orig["ace5"] else float("nan")
        print(f"| {name} | {orig['ace5']:.2f} | {noah['ace5']:.2f} | {ratio:.2f} | {orig['hot_bins_pct']} | "
              f"{noah['hot_bins_pct']} | {outcome(r.get('control'))} | {outcome(r.get('noah'))} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
