"""KiCad adapter: board file <-> Design IR, using the pcbnew Python API (KiCad 9/10)."""

from __future__ import annotations

import contextlib
import os
import sys
from pathlib import Path

from .ir import Board, Component, DesignIR, Net, Pad, classify_ref, net_role, rotate

NM_PER_MM = 1_000_000


@contextlib.contextmanager
def quiet_native_stderr():
    """Silence wxWidgets/SWIG chatter written straight to file descriptor 2."""
    sys.stderr.flush()
    saved = os.dup(2)
    devnull = os.open(os.devnull, os.O_WRONLY)
    try:
        os.dup2(devnull, 2)
        yield
    finally:
        os.dup2(saved, 2)
        os.close(devnull)
        os.close(saved)


def _pcbnew():
    with quiet_native_stderr():
        import pcbnew  # noqa: PLC0415 - heavy native import, done lazily
    return pcbnew


def kicad_version() -> str:
    return _pcbnew().Version()


def load_board(path: str | Path):
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        return pcbnew.LoadBoard(str(path))


def save_board(board, path: str | Path) -> None:
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        pcbnew.SaveBoard(str(path), board)


def _mm(v: int) -> float:
    return v / NM_PER_MM


def _courtyard_bbox_abs(pcbnew, fp):
    """Absolute courtyard bounding box (nm) or a pad-based fallback."""
    layer = pcbnew.B_CrtYd if fp.IsFlipped() else pcbnew.F_CrtYd
    with quiet_native_stderr():
        fp.BuildCourtyardCaches()
        cy = fp.GetCourtyard(layer)
    if cy.OutlineCount() > 0:
        bb = cy.BBox()
        return bb.GetLeft(), bb.GetTop(), bb.GetRight(), bb.GetBottom()
    pads = list(fp.Pads())
    if pads:
        lefts, tops, rights, bottoms = [], [], [], []
        for p in pads:
            bb = p.GetBoundingBox()
            lefts.append(bb.GetLeft())
            tops.append(bb.GetTop())
            rights.append(bb.GetRight())
            bottoms.append(bb.GetBottom())
        margin = 250_000  # 0.25 mm
        return min(lefts) - margin, min(tops) - margin, max(rights) + margin, max(bottoms) + margin
    p = fp.GetPosition()
    return p.x - 500_000, p.y - 500_000, p.x + 500_000, p.y + 500_000


def _local_bbox(abs_bbox, pos, rot_deg):
    """Express an absolute bbox in the component's rotation-0 frame (conservative)."""
    l, t, r, b = abs_bbox
    corners = [(l, t), (r, t), (l, b), (r, b)]
    xs, ys = [], []
    for cx, cy in corners:
        dx, dy = _mm(cx - pos.x), _mm(cy - pos.y)
        lx, ly = rotate(dx, dy, -rot_deg)
        xs.append(lx)
        ys.append(ly)
    return min(xs), min(ys), max(xs), max(ys)


def _board_mask(pcbnew, board, bbox, pitch):
    minx, miny, maxx, maxy = bbox
    nx = max(1, int((maxx - minx) / pitch) + 1)
    ny = max(1, int((maxy - miny) / pitch) + 1)
    outlines = pcbnew.SHAPE_POLY_SET()
    with quiet_native_stderr():
        ok = board.GetBoardPolygonOutlines(outlines, True)
    if not ok or outlines.OutlineCount() == 0:
        return []
    mask = []
    for iy in range(ny):
        y = miny + (iy + 0.5) * pitch
        row = []
        for ix in range(nx):
            x = minx + (ix + 0.5) * pitch
            pt = pcbnew.VECTOR2I(int(x * NM_PER_MM), int(y * NM_PER_MM))
            row.append(bool(outlines.Contains(pt)))
        mask.append(row)
    return mask


def _routing_resources(pcbnew, board, bbox) -> tuple[int, float, list[str]]:
    """Routing layers, track pitch and pour nets, for the congestion model.

    An inner layer counts as a plane (not a routing layer) when copper pours cover more than
    60% of the board on it; KiCad demo boards mark every layer as "signal", so the layer type
    alone cannot tell."""
    board_area = max((bbox[2] - bbox[0]) * (bbox[3] - bbox[1]), 1e-9)
    pours = [z for z in board.Zones() if not z.GetIsRuleArea()]
    cu = list(board.GetEnabledLayers().CuStack())
    routing = 0
    for layer in cu:
        if layer in (pcbnew.F_Cu, pcbnew.B_Cu):
            routing += 1
            continue
        covered = sum(z.CalculateOutlineArea() / NM_PER_MM ** 2 for z in pours
                      if z.GetLayerSet().Contains(layer))
        if covered / board_area <= 0.6:
            routing += 1
    ds = board.GetDesignSettings()
    nc = ds.m_NetSettings.GetDefaultNetclass()
    width = max(nc.GetTrackWidth(), ds.m_TrackMinWidth)
    clearance = max(nc.GetClearance(), ds.m_MinClearance)
    pitch = _mm(int(width + clearance)) or 0.5
    # Only board-wide pours (planes) carry a net; small local pours and teardrops do not.
    pour_nets = sorted({z.GetNetname() for z in pours if z.GetNetname() and not z.IsTeardropArea()
                        and z.CalculateOutlineArea() / NM_PER_MM ** 2 / board_area >= PLANE_SHARE})
    return max(routing, 1), pitch, pour_nets


PLANE_SHARE = 0.3  # a pour covering at least this share of the board is treated as a plane


def remove_layout_bound_zones(board) -> dict:
    """Delete copper that was drawn for the old placement: teardrops and local pours.

    KiCad stores teardrops as zones at fixed coordinates, and small pours are usually shaped
    around specific parts. After re-placement they would sit where the old pads were (stale
    copper). Board-wide pours (>= PLANE_SHARE of the board) are kept and refilled."""
    edges = board.GetBoardEdgesBoundingBox()
    board_area = max(_mm(edges.GetWidth()) * _mm(edges.GetHeight()), 1e-9)
    teardrops, local = [], []
    for z in board.Zones():
        if z.GetIsRuleArea():
            continue
        if z.IsTeardropArea():
            teardrops.append(z)
        elif z.CalculateOutlineArea() / NM_PER_MM ** 2 / board_area < PLANE_SHARE:
            local.append(z)
    local_nets = sorted({z.GetNetname() for z in local})
    with quiet_native_stderr():
        for z in teardrops + local:
            board.Delete(z)
    return {"teardrops": len(teardrops), "local_pours": len(local), "local_pour_nets": local_nets}


def board_to_ir(board, name: str = "", source_path: str = "", mask_pitch: float = 0.5) -> DesignIR:
    pcbnew = _pcbnew()
    comps: list[Component] = []
    net_pins: dict[str, list[tuple[int, int]]] = {}

    for fp in board.GetFootprints():
        pos = fp.GetPosition()
        rot = fp.GetOrientationDegrees()
        pads: list[Pad] = []
        has_tht = False
        for pad in fp.Pads():
            net = pad.GetNetname() or None
            pp = pad.GetPosition()
            lx, ly = rotate(_mm(pp.x - pos.x), _mm(pp.y - pos.y), -rot)
            pads.append(Pad(number=str(pad.GetNumber()), net=net, dx=lx, dy=ly))
            if pad.GetAttribute() in (pcbnew.PAD_ATTRIB_PTH, pcbnew.PAD_ATTRIB_NPTH):
                has_tht = True
        ref = fp.GetReference()
        comp = Component(
            ref=ref,
            value=fp.GetValue(),
            footprint=str(fp.GetFPID().GetUniStringLibItemName()),
            x=_mm(pos.x),
            y=_mm(pos.y),
            rotation=rot,
            flipped=fp.IsFlipped(),
            locked=fp.IsLocked(),
            has_through_hole=has_tht,
            bbox=_local_bbox(_courtyard_bbox_abs(pcbnew, fp), pos, rot),
            pads=pads,
            kind=classify_ref(ref),
        )
        ci = len(comps)
        comps.append(comp)
        for pi, pad in enumerate(pads):
            if pad.net:
                net_pins.setdefault(pad.net, []).append((ci, pi))

    edges = board.GetBoardEdgesBoundingBox()
    bbox = (_mm(edges.GetLeft()), _mm(edges.GetTop()), _mm(edges.GetRight()), _mm(edges.GetBottom()))
    if bbox[2] - bbox[0] <= 0 or bbox[3] - bbox[1] <= 0:
        raise ValueError("board has no usable Edge.Cuts outline")
    mask = _board_mask(pcbnew, board, bbox, mask_pitch)
    obstacles = []
    for d in board.GetDrawings():
        if not d.IsOnCopperLayer():
            continue
        layer = d.GetLayer()
        side = 0 if layer == pcbnew.F_Cu else 1 if layer == pcbnew.B_Cu else 2
        bb = d.GetBoundingBox()
        label = d.GetText() if d.GetClass() == "PCB_TEXT" else d.GetClass()
        obstacles.append((_mm(bb.GetLeft()), _mm(bb.GetTop()), _mm(bb.GetRight()), _mm(bb.GetBottom()),
                          side, str(label)))
    for z in board.Zones():
        if z.GetIsRuleArea() and z.GetDoNotAllowFootprints():
            bb = z.GetBoundingBox()
            # conservative: a footprint keepout blocks parts on every side
            obstacles.append((_mm(bb.GetLeft()), _mm(bb.GetTop()), _mm(bb.GetRight()), _mm(bb.GetBottom()),
                              3, "keepout"))
    routing_layers, pitch, pour_nets = _routing_resources(pcbnew, board, bbox)
    ir_board = Board(
        bbox=bbox,
        copper_layers=board.GetCopperLayerCount(),
        mask_origin=(bbox[0], bbox[1]),
        mask_pitch=mask_pitch,
        mask=mask,
        obstacles=obstacles,
        routing_layers=routing_layers,
        track_pitch_mm=pitch,
        pour_nets=pour_nets,
    )
    nets = [Net(name=n, pins=pins, role=net_role(n)) for n, pins in sorted(net_pins.items())]
    return DesignIR(name=name, components=comps, nets=nets, board=ir_board, source_path=source_path)


def apply_placement(board, ir: DesignIR) -> int:
    """Write component positions/rotations from the IR back to the board. Returns moved count."""
    pcbnew = _pcbnew()
    by_ref = {c.ref: c for c in ir.components}
    moved = 0
    for fp in board.GetFootprints():
        c = by_ref.get(fp.GetReference())
        if c is None or c.locked:
            continue
        fp.SetOrientationDegrees(c.rotation)
        fp.SetPosition(pcbnew.VECTOR2I(int(round(c.x * NM_PER_MM)), int(round(c.y * NM_PER_MM))))
        moved += 1
    return moved


def strip_routing(board) -> int:
    """Remove tracks and vias (zones are kept). Returns the number removed."""
    items = list(board.GetTracks())
    with quiet_native_stderr():
        for t in items:
            # Delete frees the C++ object; Remove would hand ownership to a Python wrapper
            # that SWIG cannot destroy (it then logs "memory leak" warnings).
            board.Delete(t)
    return len(items)


def delete_tracks_by_uuid(board, uuids: set[str]) -> int:
    """Delete tracks/vias whose KiCad UUID is in `uuids` (e.g. the ones DRC reports dangling)."""
    doomed = [t for t in board.GetTracks() if t.m_Uuid.AsString() in uuids]
    with quiet_native_stderr():
        for t in doomed:
            board.Delete(t)
    return len(doomed)


def lock_refs(board, refs: set[str]) -> None:
    for fp in board.GetFootprints():
        if fp.GetReference() in refs:
            fp.SetLocked(True)


def routing_stats(board) -> dict:
    tracks = 0.0
    vias = 0
    segments = 0
    for t in board.GetTracks():
        if t.GetClass() == "PCB_VIA":
            vias += 1
        elif t.GetClass() in ("PCB_TRACK", "PCB_ARC"):
            tracks += _mm(int(t.GetLength()))
            segments += 1
    return {"track_length_mm": round(tracks, 1), "via_count": vias, "segment_count": segments}


def prepare_for_router(board, clearance_mm: float = 0.3, drop_pour_nets: set[str] | None = None) -> dict:
    """Make a board copy safe for Freerouting before DSN export.

    * Free copper texts and graphics are turned into keepout rule areas: the Specctra export
      does not carry them, so the router would run tracks through them.
    * drop_pour_nets: delete the *outer-layer* copper pours of these nets. Freerouting treats a
      plane net as already connected; after parts move, a refilled outer pour can split and
      strand pads, so stage 2 of the pipeline routes those nets with tracks. Pours that lie only
      on inner layers (planes) are always kept, so plane nets can still be reached with a via;
      removing them made the router lay fan-out stubs that later dangled.
    Use this on a throw-away copy only; import the session into the real board.
    """
    pcbnew = _pcbnew()
    clamped = clamp_netclasses_to_board_minimums(board)
    pours = []
    if drop_pour_nets:
        for z in board.Zones():
            if z.GetIsRuleArea() or z.GetNetname() not in drop_pour_nets:
                continue
            layers = z.GetLayerSet()
            if layers.Contains(pcbnew.F_Cu) or layers.Contains(pcbnew.B_Cu):
                pours.append(z)
    with quiet_native_stderr():
        for z in pours:
            board.Delete(z)
    keepouts = 0
    margin = int(clearance_mm * NM_PER_MM)
    for item in list(board.GetDrawings()):
        if not item.IsOnCopperLayer():
            continue
        bb = item.GetBoundingBox()
        zone = pcbnew.ZONE(board)
        zone.SetIsRuleArea(True)
        zone.SetDoNotAllowTracks(True)
        zone.SetDoNotAllowVias(True)
        zone.SetDoNotAllowPads(False)
        zone.SetDoNotAllowFootprints(False)
        zone.SetDoNotAllowZoneFills(False)
        zone.SetLayer(item.GetLayer())
        l, t = bb.GetLeft() - margin, bb.GetTop() - margin
        r, b = bb.GetRight() + margin, bb.GetBottom() + margin
        outline = zone.Outline()
        outline.NewOutline()
        for x, y in ((l, t), (r, t), (r, b), (l, b)):
            outline.Append(x, y)
        board.Add(zone)
        keepouts += 1
    return {"pours_removed": len(pours), "copper_graphics_keepouts": keepouts, "netclasses_clamped": clamped}


def min_track_width_um(board) -> int:
    """Board minimum track width in whole micrometres, rounded up (0 if unset)."""
    nm = int(board.GetDesignSettings().m_TrackMinWidth)
    return -(-nm // 1000)


def clamp_netclasses_to_board_minimums(board) -> list[str]:
    """Raise net-class track width, clearance and via size to the board's minimum constraints.

    The Specctra export writes net-class values; when a net class is looser than the board
    minimums (e.g. 0.2 mm tracks under a 0.3 mm board minimum), the router produces copper that
    KiCad's DRC then rejects. Returns the names of the classes that were changed."""
    ds = board.GetDesignSettings()
    ns = ds.m_NetSettings
    classes = [ns.GetDefaultNetclass()]
    try:
        classes += list(dict(ns.GetNetclasses()).values())
    except (TypeError, AttributeError):
        pass
    # The Specctra file is written in whole micrometres: round minimums *up* to 1 um, otherwise a
    # 0.1981 mm minimum becomes 0.198 mm tracks and every one fails DRC by 0.1 um.
    def up(nm: int) -> int:
        return -(-int(nm) // 1000) * 1000

    min_w, min_c = up(ds.m_TrackMinWidth), up(ds.m_MinClearance)
    min_via, min_ring = up(ds.m_ViasMinSize), up(ds.m_ViasMinAnnularWidth)
    min_drill = up(getattr(ds, "m_MinThroughDrill", 0))
    changed = []
    for nc in classes:
        before = (nc.GetTrackWidth(), nc.GetClearance(), nc.GetViaDiameter(), nc.GetViaDrill())
        drill = max(nc.GetViaDrill(), min_drill)
        nc.SetTrackWidth(up(max(nc.GetTrackWidth(), min_w)))
        nc.SetClearance(up(max(nc.GetClearance(), min_c)))
        nc.SetViaDrill(drill)
        nc.SetViaDiameter(up(max(nc.GetViaDiameter(), min_via, drill + 2 * min_ring)))
        if before != (nc.GetTrackWidth(), nc.GetClearance(), nc.GetViaDiameter(), nc.GetViaDrill()):
            changed.append(nc.GetName())
    return changed


def export_dsn(board, path: str | Path) -> bool:
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        return bool(pcbnew.ExportSpecctraDSN(board, str(path)))


def import_ses(board, path: str | Path) -> bool:
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        return bool(pcbnew.ImportSpecctraSES(board, str(path)))
