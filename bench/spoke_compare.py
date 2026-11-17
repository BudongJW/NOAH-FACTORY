"""Compare re-route runs of the same placements (e.g. without / with spoke protection).

    python bench/spoke_compare.py DIR [DIR ...] [--labels a,b,c] [--out FILE]

Each DIR is a bench/reroute.py output (<arm>/<board>/run.json + drc.json).
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ARMS = ("w0_s0", "w0_s4", "w10_s0", "w10_s4")
BOARDS = ("complex_hierarchy", "interf_u", "kit_dev_coldfire")


def stats(run: Path) -> dict:
    drc = json.loads((run / "drc.json").read_text())
    r = json.loads((run / "run.json").read_text())
    kinds = Counter()
    for v in drc["violations"]:
        if v["type"] == "starved_thermal":
            kinds["island" if "isolated island" in v["description"] else "spokes"] += 1
    return {"unrouted": len(drc["unconnected_items"]),
            "electrical": r["drc"].get("by_category", {}).get("electrical", 0),
            "starved": kinds["island"] + kinds["spokes"], "island": kinds["island"], "spokes": kinds["spokes"],
            "route_s": r["timings"].get("routing_s", 0)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", type=Path, nargs="+")
    ap.add_argument("--labels", default="")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    labels = a.labels.split(",") if a.labels else [d.name for d in a.dirs]
    keys = [("starved", "starved_thermal"), ("spokes", "그중 스포크 부족"), ("island", "그중 고립 섬"),
            ("electrical", "전기 DRC"), ("unrouted", "미배선"), ("route_s", "배선 시간 s")]
    head = "| 조건 | 보드 | " + " | ".join(name for _, name in keys) + " |"
    lines = [f"값은 {' / '.join(labels)} 순서입니다.", "", head, "|" + "---|" * (len(keys) + 2)]
    tot = [Counter() for _ in a.dirs]
    for arm in ARMS:
        for b in BOARDS:
            st = [stats(d / arm / b) for d in a.dirs]
            for t, x in zip(tot, st):
                for k in x:
                    t[k] += x[k]
            cells = [" / ".join(f"{x[k]:.0f}" for x in st) for k, _ in keys]
            lines.append(f"| {arm} | {b} | " + " | ".join(cells) + " |")
    cells = [" / ".join(f"**{t[k]:.0f}**" for t in tot) for k, _ in keys]
    lines.append("| **합계** | | " + " | ".join(cells) + " |")
    text = "\n".join(lines) + "\n"
    if a.out:
        a.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
