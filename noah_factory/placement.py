"""Component placement: simulated annealing with design-rule terms, then legalization.

Cost = sum of weighted net HPWL
     + overlap area between courtyards (same side, or either through-hole)
     + area outside the board outline
     + decoupling-capacitor distance beyond its limit (squared)
     + distance of external connectors from the board edge (squared)
Locked components never move.
"""

from __future__ import annotations

import math
import multiprocessing as mp
import random
import re
import time
from dataclasses import dataclass, field

import numpy as np

from .congestion import CongestionConfig, CongestionGrid
from .ir import EXTERNAL_CONNECTOR, DesignIR, net_role, rotate


@dataclass
class PlacementConfig:
    seed: int = 0
    time_limit_s: float = 30.0
    moves_per_component: int = 3000
    clearance_mm: float = 0.25
    decap_limit_small_mm: float = 3.0
    decap_limit_bulk_mm: float = 8.0
    edge_margin_mm: float = 1.0
    w_overlap: float = 4.0
    w_outside: float = 40.0
    w_decap: float = 3.0
    w_edge: float = 2.0
    big_net_pins: int = 12
    ground_net_weight: float = 0.3
    allow_rotation: bool = True
    grid_mm: float = 0.05
    init: str = "random"  # "random" or "current"
    edge_refs: tuple[str, ...] = ()
    # Routing congestion (RUDY) term; 0 disables it in the cost (metrics are still reported).
    w_congestion: float = 0.0
    congestion: CongestionConfig = field(default_factory=CongestionConfig)


@dataclass
class DecapTerm:
    cap: int
    cap_pin: int
    net: str
    ic_pins: np.ndarray
    limit: float


@dataclass
class PlacementResult:
    seed: int
    x: np.ndarray
    y: np.ndarray
    k: np.ndarray
    cost: float
    breakdown: dict
    stats: dict
    legalization_failures: list[str] = field(default_factory=list)


_CAP_VALUE = re.compile(r"(\d+)(?:[.,](\d+))?\s*([pnuµμm])?(\d+)?", re.IGNORECASE)
_SCALE = {"p": 1e-12, "n": 1e-9, "u": 1e-6, "µ": 1e-6, "μ": 1e-6, "m": 1e-3, None: 1.0}


def parse_farads(value: str) -> float | None:
    m = _CAP_VALUE.search(value or "")
    if not m:
        return None
    whole, frac, unit, trailing = m.groups()
    unit_key = unit.lower() if unit and unit.lower() in _SCALE else unit
    digits = frac if frac is not None else (trailing or "")
    number = float(f"{whole}.{digits}") if digits else float(whole)
    if unit is None:
        return number if number < 1 else None  # bare "100" is ambiguous
    return number * _SCALE.get(unit_key, 1.0)


def _rotated_bbox(bbox, deg):
    l, t, r, b = bbox
    pts = [rotate(x, y, deg) for x, y in ((l, t), (r, t), (l, b), (r, b))]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


class PlacementProblem:
    def __init__(self, ir: DesignIR, cfg: PlacementConfig):
        self.ir = ir
        self.cfg = cfg
        comps = ir.components
        n = len(comps)
        self.n = n
        self.refs = [c.ref for c in comps]
        self.locked = np.array([c.locked for c in comps], dtype=bool)
        self.thru = np.array([c.has_through_hole for c in comps], dtype=bool)
        self.side = np.array([1 if c.flipped else 0 for c in comps], dtype=int)
        self.base_rot = np.array([c.rotation for c in comps], dtype=float)
        self.bb = np.zeros((n, 4, 4))
        for i, c in enumerate(comps):
            for k in range(4):
                self.bb[i, k] = _rotated_bbox(c.bbox, c.rotation + 90 * k)
        self.area = (self.bb[:, 0, 2] - self.bb[:, 0, 0]) * (self.bb[:, 0, 3] - self.bb[:, 0, 1])

        pin_comp, pin_off = [], []
        pad_global: dict[tuple[int, int], int] = {}
        for i, c in enumerate(comps):
            for pi, p in enumerate(c.pads):
                pad_global[(i, pi)] = len(pin_comp)
                pin_comp.append(i)
                pin_off.append([rotate(p.dx, p.dy, c.rotation + 90 * k) for k in range(4)])
        self.pin_comp = np.array(pin_comp, dtype=int)
        self.pin_off = np.array(pin_off, dtype=float).reshape(len(pin_comp), 4, 2)

        self.nets: list[np.ndarray] = []
        self.net_w: list[float] = []
        self.net_names: list[str] = []
        comp_nets: list[set[int]] = [set() for _ in range(n)]
        net_pins_by_name: dict[str, np.ndarray] = {}
        for net in ir.nets:
            pins = np.array([pad_global[p] for p in net.pins], dtype=int)
            net_pins_by_name[net.name] = pins
            comps_in = set(self.pin_comp[pins].tolist())
            if len(comps_in) < 2:
                continue
            k = len(self.nets)
            self.nets.append(pins)
            w = 1.0 if len(pins) <= cfg.big_net_pins else cfg.big_net_pins / len(pins)
            if net.role == "ground":
                w *= cfg.ground_net_weight
            self.net_w.append(w)
            self.net_names.append(net.name)
            for ci in comps_in:
                comp_nets[ci].add(k)
        self.comp_nets = [sorted(s) for s in comp_nets]
        self.net_w_arr = np.array(self.net_w)

        # Congestion model inputs: pins per routed net, plane-carried nets, each part's routed pins.
        pour = set(ir.board.pour_nets)
        self.net_npins = [len(p) for p in self.nets]
        self.net_factor = [cfg.congestion.pour_factor if name in pour else 1.0 for name in self.net_names]
        routed_pins = np.zeros(len(pin_comp), dtype=bool)
        for pins in self.nets:
            routed_pins[pins] = True
        order = np.argsort(self.pin_comp, kind="stable")
        bounds = np.searchsorted(self.pin_comp[order], np.arange(n + 1))
        self.comp_conn_pins = [order[bounds[i]:bounds[i + 1]][routed_pins[order[bounds[i]:bounds[i + 1]]]]
                               for i in range(n)]
        self.routing_layers = ir.board.routing_layers
        self.track_pitch = ir.board.track_pitch_mm

        self.decaps: list[DecapTerm] = []
        comp_decaps: list[list[int]] = [[] for _ in range(n)]
        for i, c in enumerate(comps):
            if c.kind != "capacitor" or len(c.pads) != 2 or c.locked:
                continue
            roles = [net_role(p.net) for p in c.pads]
            if sorted(roles) != ["ground", "power"]:
                continue
            pw = roles.index("power")
            net = c.pads[pw].net
            ic_pins = [g for g in net_pins_by_name.get(net, [])
                       if comps[self.pin_comp[g]].kind == "ic"]
            if not ic_pins:
                continue
            farads = parse_farads(c.value)
            limit = cfg.decap_limit_small_mm if (farads is None or farads <= 1.1e-6) else cfg.decap_limit_bulk_mm
            t = len(self.decaps)
            self.decaps.append(DecapTerm(i, pad_global[(i, pw)], net, np.array(ic_pins), limit))
            comp_decaps[i].append(t)
            for g in ic_pins:
                if t not in comp_decaps[self.pin_comp[g]]:
                    comp_decaps[self.pin_comp[g]].append(t)
        self.comp_decaps = comp_decaps

        edge = set()
        for i, c in enumerate(comps):
            if c.locked:
                continue
            text = f"{c.footprint} {c.value}"
            if (c.kind == "connector" and EXTERNAL_CONNECTOR.search(text)) or c.ref in cfg.edge_refs:
                edge.add(i)
        self.edge = np.zeros(n, dtype=bool)
        self.edge[list(edge)] = True

        obs = ir.board.obstacles
        self.obs_bb = np.array([o[:4] for o in obs], dtype=float).reshape(len(obs), 4)
        self.obs_side = np.array([o[4] for o in obs], dtype=int)
        self.obs_label = [o[5] for o in obs]

        self.board_bbox = np.array(ir.board.bbox, dtype=float)
        self.mask = np.array(ir.board.mask, dtype=bool) if ir.board.mask else None
        self.mask_origin = np.array(ir.board.mask_origin)
        self.mask_pitch = ir.board.mask_pitch
        self.movable = np.where(~self.locked)[0]

    def density(self) -> dict:
        """Courtyard bounding-box area per side / board area (through-hole parts count on both)."""
        if self.mask is not None:
            board_area = float(self.mask.sum()) * self.mask_pitch ** 2
        else:
            bx0, by0, bx1, by1 = self.board_bbox
            board_area = (bx1 - bx0) * (by1 - by0)
        out = {}
        for name, s in (("front", 0), ("back", 1)):
            sel = (self.side == s) | self.thru
            out[name] = round(float(self.area[sel].sum()) / board_area * 100, 1) if board_area > 0 else 0.0
        out["board_area_mm2"] = round(board_area, 1)
        return out

    # ----- geometry helpers -------------------------------------------------
    def abs_bb(self, X, Y, K, idx=None):
        if idx is None:
            idx = np.arange(self.n)
        b = self.bb[idx, K[idx]]
        return b + np.stack([X[idx], Y[idx], X[idx], Y[idx]], axis=-1)

    def inside_points(self, px, py):
        bx0, by0, bx1, by1 = self.board_bbox
        ok = (px >= bx0) & (px <= bx1) & (py >= by0) & (py <= by1)
        if self.mask is None:
            return ok
        ix = ((px - self.mask_origin[0]) / self.mask_pitch).astype(int)
        iy = ((py - self.mask_origin[1]) / self.mask_pitch).astype(int)
        h, w = self.mask.shape
        valid = ok & (ix >= 0) & (ix < w) & (iy >= 0) & (iy < h)
        res = np.zeros_like(ok)
        res[valid] = self.mask[iy[valid], ix[valid]]
        return res

    def _samples(self, bb):
        """9 sample points per bbox row: corners, edge midpoints, centre."""
        l, t, r, b = bb[..., 0], bb[..., 1], bb[..., 2], bb[..., 3]
        mx, my = (l + r) / 2, (t + b) / 2
        xs = np.stack([l, r, l, r, mx, mx, l, r, mx], axis=-1)
        ys = np.stack([t, t, b, b, t, b, my, my, my], axis=-1)
        return xs, ys

    # ----- cost terms --------------------------------------------------------
    def pins_xy(self, pins, X, Y, K):
        pc = self.pin_comp[pins]
        off = self.pin_off[pins, K[pc]]
        return X[pc] + off[:, 0], Y[pc] + off[:, 1]

    def net_hpwl(self, k, X, Y, K):
        px, py = self.pins_xy(self.nets[k], X, Y, K)
        return (px.max() - px.min()) + (py.max() - py.min())

    # ----- congestion (RUDY) --------------------------------------------------
    def new_grid(self) -> CongestionGrid:
        return CongestionGrid(tuple(self.board_bbox), self.routing_layers, self.track_pitch, self.cfg.congestion)

    def net_rect(self, grid, k, X, Y, K):
        px, py = self.pins_xy(self.nets[k], X, Y, K)
        return grid.net_rect(px, py, self.net_npins[k], self.net_factor[k])

    def comp_pin_bins(self, grid, i, X, Y, K):
        pins = self.comp_conn_pins[i]
        if not len(pins):
            return np.zeros(0, dtype=int), np.zeros(0, dtype=int)
        px, py = self.pins_xy(pins, X, Y, K)
        return grid.pin_bins(px, py)

    def build_congestion(self, X, Y, K):
        """Full congestion state: grid, per-net rectangles, per-part pin bins."""
        grid = self.new_grid()
        rects = [self.net_rect(grid, k, X, Y, K) for k in range(len(self.nets))]
        for r in rects:
            grid.add_rect(r)
        pbins = [self.comp_pin_bins(grid, i, X, Y, K) for i in range(self.n)]
        for b in pbins:
            grid.add_pins(b)
        return grid, rects, pbins

    def update_congestion(self, state, S, X, Y, K):
        """Move the contributions of parts S (already moved in X/Y/K) to their new place.
        Returns (penalty change, undo record)."""
        grid, rects, pbins = state
        nets = sorted({k for i in S for k in self.comp_nets[i]})
        old_r = [rects[k] for k in nets]
        new_r = [self.net_rect(grid, k, X, Y, K) for k in nets]
        old_p = [pbins[i] for i in S]
        new_p = [self.comp_pin_bins(grid, i, X, Y, K) for i in S]
        region = grid.region_of(old_r + new_r, old_p + new_p)
        if region is None:
            return 0.0, None
        before = grid.penalty(region)
        for r in old_r:
            grid.add_rect(r, -1.0)
        for k, r in zip(nets, new_r):
            grid.add_rect(r, 1.0)
            rects[k] = r
        for b in old_p:
            grid.add_pins(b, -1.0)
        for i, b in zip(S, new_p):
            grid.add_pins(b, 1.0)
            pbins[i] = b
        return grid.penalty(region) - before, (nets, old_r, new_r, list(S), old_p, new_p)

    def undo_congestion(self, state, undo) -> None:
        if undo is None:
            return
        grid, rects, pbins = state
        nets, old_r, new_r, S, old_p, new_p = undo
        for r in new_r:
            grid.add_rect(r, -1.0)
        for k, r in zip(nets, old_r):
            grid.add_rect(r, 1.0)
            rects[k] = r
        for b in new_p:
            grid.add_pins(b, -1.0)
        for i, b in zip(S, old_p):
            grid.add_pins(b, 1.0)
            pbins[i] = b

    def overlap_row(self, i, X, Y, K, AB):
        c = self.cfg.clearance_mm
        bi = AB[i]
        ox = np.minimum(bi[2] + c, AB[:, 2]) - np.maximum(bi[0] - c, AB[:, 0])
        oy = np.minimum(bi[3] + c, AB[:, 3]) - np.maximum(bi[1] - c, AB[:, 1])
        a = np.clip(ox, 0, None) * np.clip(oy, 0, None)
        relevant = (self.side == self.side[i]) | self.thru | self.thru[i]
        relevant[i] = False
        return float(a[relevant].sum())

    def obstacle_relevant(self, i) -> np.ndarray:
        """Which fixed copper obstacles can collide with component i."""
        s = self.obs_side
        if self.thru[i]:
            return np.ones(len(s), dtype=bool)
        return (s == self.side[i]) | (s == 3)

    def obstacle_overlap(self, i, AB) -> float:
        if not len(self.obs_bb):
            return 0.0
        c = self.cfg.clearance_mm
        bi = AB[i]
        ob = self.obs_bb
        ox = np.minimum(bi[2] + c, ob[:, 2]) - np.maximum(bi[0] - c, ob[:, 0])
        oy = np.minimum(bi[3] + c, ob[:, 3]) - np.maximum(bi[1] - c, ob[:, 1])
        a = np.clip(ox, 0, None) * np.clip(oy, 0, None)
        return float(a[self.obstacle_relevant(i)].sum())

    def pair_overlap(self, i, j, AB):
        if not ((self.side[i] == self.side[j]) or self.thru[i] or self.thru[j]):
            return 0.0
        c = self.cfg.clearance_mm
        bi, bj = AB[i], AB[j]
        ox = min(bi[2] + c, bj[2]) - max(bi[0] - c, bj[0])
        oy = min(bi[3] + c, bj[3]) - max(bi[1] - c, bj[1])
        return max(0.0, ox) * max(0.0, oy)

    def outside(self, i, AB):
        bb = AB[i]
        xs, ys = self._samples(bb)
        ins = self.inside_points(xs, ys)
        frac_out = 1.0 - ins.mean()
        bx0, by0, bx1, by1 = self.board_bbox
        beyond = max(0.0, bx0 - bb[0]) + max(0.0, by0 - bb[1]) + max(0.0, bb[2] - bx1) + max(0.0, bb[3] - by1)
        return frac_out * (self.area[i] + 1.0) + beyond * beyond

    def decap_distance(self, t, X, Y, K):
        d = self.decaps[t]
        c = d.cap
        cx = X[c] + self.pin_off[d.cap_pin, K[c], 0]
        cy = Y[c] + self.pin_off[d.cap_pin, K[c], 1]
        pc = self.pin_comp[d.ic_pins]
        off = self.pin_off[d.ic_pins, K[pc]]
        dist = np.hypot(X[pc] + off[:, 0] - cx, Y[pc] + off[:, 1] - cy)
        j = int(np.argmin(dist))
        return float(dist[j]), int(pc[j])

    def edge_distance(self, i, AB):
        bb = AB[i]
        bx0, by0, bx1, by1 = self.board_bbox
        return max(0.0, min(bb[0] - bx0, bb[1] - by0, bx1 - bb[2], by1 - bb[3]))

    def local_cost(self, S, X, Y, K, AB, w_ov):
        cfg = self.cfg
        nets = set()
        dec = set()
        for i in S:
            nets.update(self.comp_nets[i])
            dec.update(self.comp_decaps[i])
        cost = 0.0
        for k in nets:
            cost += self.net_w[k] * self.net_hpwl(k, X, Y, K)
        ov = sum(self.overlap_row(i, X, Y, K, AB) + self.obstacle_overlap(i, AB) for i in S)
        if len(S) == 2:
            ov -= self.pair_overlap(S[0], S[1], AB)
        cost += w_ov * ov
        for i in S:
            cost += cfg.w_outside * self.outside(i, AB)
            if self.edge[i]:
                e = max(0.0, self.edge_distance(i, AB) - cfg.edge_margin_mm)
                cost += cfg.w_edge * e * e
        for t in dec:
            dist, _ = self.decap_distance(t, X, Y, K)
            ex = max(0.0, dist - self.decaps[t].limit)
            cost += cfg.w_decap * ex * ex
        return cost

    # ----- evaluation --------------------------------------------------------
    def evaluate(self, X, Y, K) -> dict:
        AB = self.abs_bb(X, Y, K)
        hpwl = sum(self.net_hpwl(k, X, Y, K) for k in range(len(self.nets)))
        whpwl = sum(self.net_w[k] * self.net_hpwl(k, X, Y, K) for k in range(len(self.nets)))
        overlaps = []
        for i in range(self.n):
            # true courtyard overlaps only (no clearance inflation)
            ox = np.minimum(AB[i, 2], AB[i + 1:, 2]) - np.maximum(AB[i, 0], AB[i + 1:, 0])
            oy = np.minimum(AB[i, 3], AB[i + 1:, 3]) - np.maximum(AB[i, 1], AB[i + 1:, 1])
            rel = (self.side[i + 1:] == self.side[i]) | self.thru[i + 1:] | self.thru[i]
            for off in np.where((ox > 0.01) & (oy > 0.01) & rel)[0]:
                j = i + 1 + int(off)
                overlaps.append((self.refs[i], self.refs[j], round(float(ox[off] * oy[off]), 3)))
            if len(self.obs_bb) and not self.locked[i]:
                ob = self.obs_bb
                ox = np.minimum(AB[i, 2], ob[:, 2]) - np.maximum(AB[i, 0], ob[:, 0])
                oy = np.minimum(AB[i, 3], ob[:, 3]) - np.maximum(AB[i, 1], ob[:, 1])
                for k in np.where((ox > 0.01) & (oy > 0.01) & self.obstacle_relevant(i))[0]:
                    overlaps.append((self.refs[i], f"copper:{self.obs_label[k]}",
                                     round(float(ox[k] * oy[k]), 3)))
        # Locked parts may overhang the edge on purpose (edge connectors); only movable parts count.
        outside = [self.refs[i] for i in self.movable if self.outside(i, AB) > 1e-6]
        locked_overhang = [self.refs[i] for i in np.where(self.locked)[0] if self.outside(i, AB) > 1e-6]
        decaps = []
        for t, d in enumerate(self.decaps):
            dist, ic = self.decap_distance(t, X, Y, K)
            decaps.append({"cap": self.refs[d.cap], "ic": self.refs[ic], "net": d.net,
                           "distance_mm": round(dist, 2), "limit_mm": d.limit,
                           "pass": dist <= d.limit})
        edges = [{"ref": self.refs[i], "distance_mm": round(self.edge_distance(i, AB), 2),
                  "limit_mm": self.cfg.edge_margin_mm,
                  "pass": self.edge_distance(i, AB) <= self.cfg.edge_margin_mm}
                 for i in np.where(self.edge)[0]]
        congestion = self.build_congestion(X, Y, K)[0].metrics()
        return {"hpwl_mm": round(hpwl, 1), "weighted_hpwl": round(whpwl, 1),
                "overlaps": overlaps, "outside": outside, "locked_overhang": locked_overhang,
                "decaps": decaps, "edges": edges, "congestion": congestion}


def _initial_state(p: PlacementProblem, rng: random.Random):
    comps = p.ir.components
    X = np.array([c.x for c in comps], dtype=float)
    Y = np.array([c.y for c in comps], dtype=float)
    K = np.zeros(p.n, dtype=int)
    if p.cfg.init == "random":
        bx0, by0, bx1, by1 = p.board_bbox
        for i in p.movable:
            l, t, r, b = p.bb[i, 0]
            x_lo, x_hi = bx0 - l, bx1 - r
            y_lo, y_hi = by0 - t, by1 - b
            X[i] = rng.uniform(x_lo, x_hi) if x_hi > x_lo else (bx0 + bx1) / 2
            Y[i] = rng.uniform(y_lo, y_hi) if y_hi > y_lo else (by0 + by1) / 2
    return X, Y, K


def anneal(p: PlacementProblem, seed: int) -> PlacementResult:
    cfg = p.cfg
    rng = random.Random(seed)
    X, Y, K = _initial_state(p, rng)
    AB = p.abs_bb(X, Y, K)
    movable = p.movable
    if len(movable) == 0:
        bd = p.evaluate(X, Y, K)
        return PlacementResult(seed, X, Y, K, 0.0, bd, {"moves": 0, "accepted": 0, "time_s": 0.0})

    bx0, by0, bx1, by1 = p.board_bbox
    R0 = 0.5 * max(bx1 - bx0, by1 - by0)
    total_moves = cfg.moves_per_component * len(movable)
    t_start = time.monotonic()

    def propose(progress):
        r = rng.random()
        i = int(movable[rng.randrange(len(movable))])
        if r < 0.55:
            rad = R0 * (1 - progress) ** 1.5 + 0.2
            return ("move", [i], (X[i] + rng.uniform(-rad, rad), Y[i] + rng.uniform(-rad, rad)))
        if r < 0.70 and p.comp_nets[i]:
            # pull toward the centroid of connected pins
            xs, ys = [], []
            for k in p.comp_nets[i]:
                pins = p.nets[k]
                pc = p.pin_comp[pins]
                sel = pc != i
                if not sel.any() or len(pins) > cfg.big_net_pins:
                    continue
                off = p.pin_off[pins[sel], K[pc[sel]]]
                xs.extend((X[pc[sel]] + off[:, 0]).tolist())
                ys.extend((Y[pc[sel]] + off[:, 1]).tolist())
            if xs:
                jitter = 1.0 + 3.0 * (1 - progress)
                return ("move", [i], (float(np.mean(xs)) + rng.uniform(-jitter, jitter),
                                      float(np.mean(ys)) + rng.uniform(-jitter, jitter)))
        if r < 0.85 and len(movable) > 1:
            j = int(movable[rng.randrange(len(movable))])
            if j != i:
                return ("swap", [i, j], None)
        if cfg.allow_rotation:
            return ("rot", [i], (K[i] + rng.choice((1, 2, 3))) % 4)
        return ("move", [i], (X[i] + rng.uniform(-1, 1), Y[i] + rng.uniform(-1, 1)))

    def apply(kind, S, arg):
        saved = [(i, X[i], Y[i], K[i]) for i in S]
        if kind == "move":
            i = S[0]
            X[i] = min(max(arg[0], bx0), bx1)
            Y[i] = min(max(arg[1], by0), by1)
        elif kind == "swap":
            i, j = S
            X[i], X[j] = X[j], X[i]
            Y[i], Y[j] = Y[j], Y[i]
        else:
            K[S[0]] = arg
        AB[S] = p.abs_bb(X, Y, K, np.array(S))
        return saved

    def revert(saved):
        for i, x, y, k in saved:
            X[i], Y[i], K[i] = x, y, k
        idx = np.array([s[0] for s in saved])
        AB[idx] = p.abs_bb(X, Y, K, idx)

    use_cong = cfg.w_congestion > 0
    cong = p.build_congestion(X, Y, K) if use_cong else None

    def cong_weight(progress):
        # congestion matters most once parts have settled near their nets
        return cfg.w_congestion * (0.2 + 0.8 * progress)

    # Estimate the starting temperature from random uphill moves.
    ups = []
    for _ in range(min(200, 20 * len(movable))):
        kind, S, arg = propose(0.0)
        before = p.local_cost(S, X, Y, K, AB, cfg.w_overlap)
        saved = apply(kind, S, arg)
        after = p.local_cost(S, X, Y, K, AB, cfg.w_overlap)
        if use_cong:
            dpen, undo = p.update_congestion(cong, S, X, Y, K)
            after += cong_weight(0.0) * dpen
            p.undo_congestion(cong, undo)
        revert(saved)
        if after > before:
            ups.append(after - before)
    T0 = (np.mean(ups) / -math.log(0.8)) if ups else 1.0
    if cfg.init == "current":
        # Refinement of an existing (usually legal) placement: start cold, move locally.
        T0 *= 0.02
        R0 *= 0.1
    T_end = T0 * 1e-4

    moves = accepted = 0
    progress = 0.0
    while True:
        if moves % 256 == 0:
            elapsed = time.monotonic() - t_start
            progress = max(moves / total_moves, elapsed / cfg.time_limit_s)
            if progress >= 1.0:
                break
        T = T0 * (T_end / T0) ** progress
        w_ov = cfg.w_overlap * (1.0 + 30.0 * progress)
        kind, S, arg = propose(progress)
        before = p.local_cost(S, X, Y, K, AB, w_ov)
        saved = apply(kind, S, arg)
        after = p.local_cost(S, X, Y, K, AB, w_ov)
        delta = after - before
        undo = None
        if use_cong:
            dpen, undo = p.update_congestion(cong, S, X, Y, K)
            delta += cong_weight(progress) * dpen
        moves += 1
        if delta <= 0 or rng.random() < math.exp(-delta / max(T, 1e-12)):
            accepted += 1
        else:
            if use_cong:
                p.undo_congestion(cong, undo)
            revert(saved)

    anneal_time = time.monotonic() - t_start
    # Snap to the placement grid before legalization (whose offsets are grid multiples).
    # Off-grid coordinates make Freerouting fail (NegativeArraySizeException in DrillPageArray).
    g = cfg.grid_mm
    X[movable] = np.round(X[movable] / g) * g
    Y[movable] = np.round(Y[movable] / g) * g
    failures = legalize(p, X, Y, K)
    bd = p.evaluate(X, Y, K)
    cost = bd["weighted_hpwl"] + 1000.0 * (len(bd["overlaps"]) + len(bd["outside"])) + \
        sum(cfg.w_decap * max(0.0, d["distance_mm"] - d["limit_mm"]) ** 2 for d in bd["decaps"]) + \
        sum(cfg.w_edge * max(0.0, e["distance_mm"] - e["limit_mm"]) ** 2 for e in bd["edges"]) + \
        cfg.w_congestion * bd["congestion"]["penalty"]
    stats = {"moves": moves, "accepted": accepted, "anneal_time_s": round(anneal_time, 2),
             "time_s": round(time.monotonic() - t_start, 2), "T0": float(T0)}
    return PlacementResult(seed, X.copy(), Y.copy(), K.copy(), float(cost), bd, stats, failures)


def legalize(p: PlacementProblem, X, Y, K, step: float = 0.25, max_radius: float = 30.0) -> list[str]:
    """Greedy overlap removal: keep each component at the nearest free spot."""
    c = p.cfg.clearance_mm
    order = list(np.where(p.locked)[0]) + sorted(p.movable.tolist(), key=lambda i: -p.area[i])
    # Fixed copper obstacles start the "placed" set. side codes: 0/1 outer, 2 inner, 3 all sides.
    placed_bb = p.obs_bb.copy()
    placed_side = p.obs_side.copy()
    placed_thru = np.zeros(len(placed_bb), dtype=bool)
    failures = []

    def relevant_to(i):
        if p.thru[i]:
            return np.ones(len(placed_side), dtype=bool)
        return (placed_side == p.side[i]) | (placed_side == 3) | placed_thru

    # Candidate offsets on concentric square rings, sorted by distance.
    rings = [(0.0, 0.0)]
    r = step
    while r <= max_radius:
        n_side = int(round(2 * r / step))
        for a in range(n_side):
            s = -r + a * step
            rings.extend([(s, -r), (r, s), (-s, r), (-r, -s)])
        r += step
    offs = np.array(rings)
    offs = offs[np.argsort(np.hypot(offs[:, 0], offs[:, 1]), kind="stable")]

    for i in order:
        i = int(i)
        base = p.bb[i, K[i]]
        if p.locked[i]:
            placed_bb = np.vstack([placed_bb, base + [X[i], Y[i], X[i], Y[i]]])
            placed_side = np.append(placed_side, p.side[i])
            placed_thru = np.append(placed_thru, p.thru[i])
            continue
        others = placed_bb[relevant_to(i)]
        chosen = None
        for start in range(0, len(offs), 2048):
            chunk = offs[start:start + 2048]
            cx = X[i] + chunk[:, 0]
            cy = Y[i] + chunk[:, 1]
            cand = np.stack([cx + base[0], cy + base[1], cx + base[2], cy + base[3]], axis=-1)
            if len(others):
                ox = np.minimum(cand[:, None, 2] + c, others[None, :, 2]) - np.maximum(cand[:, None, 0] - c, others[None, :, 0])
                oy = np.minimum(cand[:, None, 3] + c, others[None, :, 3]) - np.maximum(cand[:, None, 1] - c, others[None, :, 1])
                free = ~((ox > 1e-9) & (oy > 1e-9)).any(axis=1)
            else:
                free = np.ones(len(cand), dtype=bool)
            xs, ys = p._samples(cand)
            inside = p.inside_points(xs.ravel(), ys.ravel()).reshape(xs.shape).all(axis=1)
            ok = np.where(free & inside)[0]
            if len(ok):
                chosen = ok[0]
                X[i], Y[i] = cx[chosen], cy[chosen]
                break
        if chosen is None:
            failures.append(p.refs[i])
        placed_bb = np.vstack([placed_bb, base + [X[i], Y[i], X[i], Y[i]]])
        placed_side = np.append(placed_side, p.side[i])
        placed_thru = np.append(placed_thru, p.thru[i])
    return failures


_WORKER_PROBLEM: PlacementProblem | None = None


def _init_worker(problem: PlacementProblem) -> None:
    global _WORKER_PROBLEM
    _WORKER_PROBLEM = problem


def _run_seed(seed: int) -> PlacementResult:
    assert _WORKER_PROBLEM is not None
    return anneal(_WORKER_PROBLEM, seed)


def place_candidates(ir: DesignIR, cfg: PlacementConfig, seeds: list[int],
                     workers: int = 0) -> tuple[PlacementProblem, list[PlacementResult]]:
    """Run one annealing per seed (in parallel) and return results sorted by cost.

    Workers use the "spawn" start method: forking a process that has pcbnew loaded
    corrupts SWIG state in the parent. This module never imports pcbnew.
    """
    problem = PlacementProblem(ir, cfg)
    workers = workers or min(len(seeds), mp.cpu_count())
    if workers > 1 and len(seeds) > 1:
        ctx = mp.get_context("spawn")
        with ctx.Pool(workers, initializer=_init_worker, initargs=(problem,)) as pool:
            results = pool.map(_run_seed, seeds)
    else:
        results = [anneal(problem, s) for s in seeds]
    results.sort(key=lambda r: r.cost)
    return problem, results


def apply_result(ir: DesignIR, problem: PlacementProblem, result: PlacementResult) -> None:
    for i, c in enumerate(ir.components):
        if c.locked:
            continue
        c.x = float(result.x[i])
        c.y = float(result.y[i])
        rot = (problem.base_rot[i] + 90.0 * int(result.k[i])) % 360.0
        c.rotation = rot - 360.0 if rot > 180.0 else rot


def current_metrics(ir: DesignIR, cfg: PlacementConfig | None = None) -> dict:
    """Evaluate the placement already in the IR (e.g. the human-made original)."""
    p = PlacementProblem(ir, cfg or PlacementConfig())
    X = np.array([c.x for c in ir.components])
    Y = np.array([c.y for c in ir.components])
    K = np.zeros(p.n, dtype=int)
    return p.evaluate(X, Y, K)
