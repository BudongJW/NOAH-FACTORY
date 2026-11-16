"""Summarise an A/B benchmark: one results.json per arm/seed set.

    python bench/ab_summary.py DIR [--out bench/results/congestion_ab.md]

DIR holds sub-directories named w<weight>_s<seed offset>, each with results.json from
run_bench.py. Rows: board x arm; values per seed set and their mean.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics as st
from collections import defaultdict
from pathlib import Path


def load(root: Path) -> dict:
    data: dict = defaultdict(lambda: defaultdict(list))  # board -> arm -> [row per seed set]
    for d in sorted(root.iterdir()):
        m = re.fullmatch(r"w([\d.]+)_s(\d+)", d.name)
        if not m or not (d / "results.json").exists():
            continue
        for r in json.loads((d / "results.json").read_text()):
            if r.get("noah"):
                data[r["board"]][float(m.group(1))].append((int(m.group(2)), r))
    return data


def metrics(r: dict) -> dict:
    n = r["noah"]
    best = n["placement"]["best"]
    cong = best.get("congestion", {})
    return {
        "unrouted": n["drc"].get("unconnected", 0),
        "electrical": n["drc"].get("by_category", {}).get("electrical", 0),
        "ace5": cong.get("ace5"),
        "hot": cong.get("hot_bins_pct"),
        "hpwl": best["hpwl_mm"],
        "route_s": n["timings"].get("routing_s"),
    }


def fmt(vals: list, d: int = 0) -> str:
    vals = [v for v in vals if v is not None]
    if not vals:
        return "–"
    each = " / ".join(f"{v:.{d}f}" for v in vals)
    return f"{each} (평균 {st.mean(vals):.{d}f})" if len(vals) > 1 else each


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    data = load(a.root)
    lines = ["| 보드 | 혼잡도 가중치 | 미배선 | 전기 DRC | ACE5 | 과밀 구간 % | HPWL mm | 배선 시간 s |",
             "|---|---|---|---|---|---|---|---|"]
    for board in sorted(data):
        for w in sorted(data[board]):
            rows = [metrics(r) for _, r in sorted(data[board][w], key=lambda t: t[0])]
            col = lambda k: [m[k] for m in rows]  # noqa: E731
            lines.append(f"| {board} | {w:g} | {fmt(col('unrouted'))} | {fmt(col('electrical'))} | "
                         f"{fmt(col('ace5'), 2)} | {fmt(col('hot'), 1)} | {fmt(col('hpwl'))} | "
                         f"{fmt(col('route_s'))} |")
    text = "\n".join(lines) + "\n"
    if a.out:
        a.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
