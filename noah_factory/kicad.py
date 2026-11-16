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
    ir_board = Board(
        bbox=bbox,
        copper_layers=board.GetCopperLayerCount(),
        mask_origin=(bbox[0], bbox[1]),
        mask_pitch=mask_pitch,
        mask=mask,
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


def export_dsn(board, path: str | Path) -> bool:
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        return bool(pcbnew.ExportSpecctraDSN(board, str(path)))


def import_ses(board, path: str | Path) -> bool:
    pcbnew = _pcbnew()
    with quiet_native_stderr():
        return bool(pcbnew.ImportSpecctraSES(board, str(path)))
