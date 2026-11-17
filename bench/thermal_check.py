"""What blocks thermal-relief spokes? (KiCad DRC `starved_thermal`)

For every starved pad in the given run directories, build the corridor each of its spokes
would occupy (pad edge -> thermal gap + spoke, spoke width + zone clearance on each side) and
check which copper of *other* nets intersects it: tracks, vias, pads, or the board edge.

    python bench/thermal_check.py RUN_DIR [RUN_DIR ...]

RUN_DIR is a pipeline output directory (drc.json + final/*.kicad_pcb).
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from shapely.geometry import LineString, Point, box  # noqa: E402

from noah_factory.kicad import load_board  # noqa: E402

NM = 1_000_000


def mm(v):
    return v / NM


def other_net_copper(board, layer, net):
    """Shapely geometries (mm) of copper on `layer` that belongs to other nets."""
    out = []
    for t in board.GetTracks():
        if t.GetNetCode() == net or not t.IsOnLayer(layer):
            continue
        if t.GetClass() == "PCB_VIA":
            p = t.GetPosition()
            out.append(("via", Point(mm(p.x), mm(p.y)).buffer(mm(t.GetWidth(layer)) / 2)))
        else:
            s, e = t.GetStart(), t.GetEnd()
            out.append(("track", LineString([(mm(s.x), mm(s.y)), (mm(e.x), mm(e.y))]).buffer(mm(t.GetWidth()) / 2)))
    for pad in board.GetPads():
        if pad.GetNetCode() == net or not pad.IsOnLayer(layer):
            continue
        bb = pad.GetBoundingBox()
        out.append(("pad", box(mm(bb.GetLeft()), mm(bb.GetTop()), mm(bb.GetRight()), mm(bb.GetBottom()))))
    return out


def analyse(run_dir: Path) -> list[dict]:
    drc = json.loads((run_dir / "drc.json").read_text())
    starved = [v for v in drc["violations"] if v["type"] == "starved_thermal"]
    if not starved:
        return []
    board = load_board(next((run_dir / "final").glob("*.kicad_pcb")))
    pads = {p.m_Uuid.AsString(): p for p in board.GetPads()}
    zones = {z.m_Uuid.AsString(): z for z in board.Zones()}
    edge = board.GetBoardEdgesBoundingBox()
    outline = box(mm(edge.GetLeft()), mm(edge.GetTop()), mm(edge.GetRight()), mm(edge.GetBottom()))
    min_clear = mm(board.GetDesignSettings().m_MinClearance)
    cache: dict = {}
    rows = []
    for v in starved:
        pad = next((pads[i["uuid"]] for i in v["items"] if i.get("uuid") in pads), None)
        zone = next((zones[i["uuid"]] for i in v["items"] if i.get("uuid") in zones), None)
        if pad is None or zone is None:
            continue
        layer = next(l for l in zone.GetLayerSet().CuStack() if pad.IsOnLayer(l))
        gap = mm(pad.GetLocalThermalGapOverride() or zone.GetThermalReliefGap())
        spoke = mm(pad.GetLocalThermalSpokeWidthOverride() or zone.GetThermalReliefSpokeWidth())
        clear = max(mm(zone.GetLocalClearance() or 0), min_clear)
        key = (layer, pad.GetNetCode())
        if key not in cache:
            cache[key] = other_net_copper(board, layer, pad.GetNetCode())
        copper = cache[key]
        bb = pad.GetBoundingBox()
        l, t, r, b = mm(bb.GetLeft()), mm(bb.GetTop()), mm(bb.GetRight()), mm(bb.GetBottom())
        cx, cy = (l + r) / 2, (t + b) / 2
        reach = gap + max(spoke, mm(zone.GetMinThickness()))
        half = spoke / 2 + clear
        corridors = {
            "right": box(r, cy - half, r + reach, cy + half),
            "left": box(l - reach, cy - half, l, cy + half),
            "down": box(cx - half, b, cx + half, b + reach),
            "up": box(cx - half, t - reach, cx + half, t),
        }
        blocked = {}
        for d, corr in corridors.items():
            kinds = sorted({k for k, g in copper if g.intersects(corr)})
            if not corr.within(outline):
                kinds.append("edge")
            if kinds:
                blocked[d] = kinds
        rows.append({"pad": v["items"][0]["description"] if pads.get(v["items"][0].get("uuid")) else
                     next(i["description"] for i in v["items"] if i.get("uuid") in pads),
                     "smd": not pad.HasHole(), "gap_mm": round(gap, 3), "spoke_mm": round(spoke, 3),
                     "blocked": blocked})
    return rows


def main() -> int:
    total = Counter()
    pads = 0
    smd = 0
    fixable = 0
    for arg in sys.argv[1:]:
        for row in analyse(Path(arg)):
            pads += 1
            smd += row["smd"]
            for kinds in row["blocked"].values():
                for k in kinds:
                    total[k] += 1
            total["blocked spokes"] += len(row["blocked"])
            # spokes that only routed copper (tracks, vias) blocks could be freed by the router
            hard = sum(1 for kinds in row["blocked"].values() if set(kinds) & {"pad", "edge"})
            if 4 - hard >= 2:  # KiCad requires 2 spokes by default
                fixable += 1
    print(f"starved pads: {pads} (SMD {smd}, through-hole {pads - smd})")
    print("blocked spoke corridors by blocker (a corridor can have several):", dict(total))
    print(f"pads that would keep >= 2 spokes if routed copper stayed out of the corridors: {fixable}/{pads}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
