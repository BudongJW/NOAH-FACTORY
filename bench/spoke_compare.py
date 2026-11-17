"""Compare two re-route runs of the same placements (e.g. without / with spoke protection).

    python bench/spoke_compare.py BASE_DIR NEW_DIR [--out FILE]
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
    ap.add_argument("base", type=Path)
    ap.add_argument("new", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    lines = ["| 조건 | 보드 | starved_thermal (전→후) | 그중 스포크 부족 | 그중 고립 섬 | 전기 DRC | 미배선 | 배선 시간 s |",
             "|---|---|---|---|---|---|---|---|"]
    tot = {"base": Counter(), "new": Counter()}
    for arm in ARMS:
        for b in BOARDS:
            x, y = stats(a.base / arm / b), stats(a.new / arm / b)
            for k in x:
                tot["base"][k] += x[k]
                tot["new"][k] += y[k]
            lines.append(f"| {arm} | {b} | {x['starved']} → {y['starved']} | {x['spokes']} → {y['spokes']} | "
                         f"{x['island']} → {y['island']} | {x['electrical']} → {y['electrical']} | "
                         f"{x['unrouted']} → {y['unrouted']} | {x['route_s']:.0f} → {y['route_s']:.0f} |")
    t0, t1 = tot["base"], tot["new"]
    lines.append(f"| **합계** | | **{t0['starved']} → {t1['starved']}** | {t0['spokes']} → {t1['spokes']} | "
                 f"{t0['island']} → {t1['island']} | **{t0['electrical']} → {t1['electrical']}** | "
                 f"{t0['unrouted']} → {t1['unrouted']} | {t0['route_s']:.0f} → {t1['route_s']:.0f} |")
    text = "\n".join(lines) + "\n"
    if a.out:
        a.out.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
