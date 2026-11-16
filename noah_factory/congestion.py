"""Routing congestion estimate for placement: RUDY (Rectangular Uniform wire DensitY).

* Each net's expected wire length (HPWL x a Steiner correction for multi-pin nets) is spread
  evenly over the grid bins its bounding box covers.
* Each connected pin also uses a little capacity in its own bin (escape routing).
* Nets carried by a board-wide pour (a plane) count with a reduced weight.
* Capacity per bin = routing layers x usable share / track pitch x bin area, in millimetres of
  track. Utilisation u = demand / capacity; bins above `target` are penalised quadratically.

The same functions serve the full evaluation and the incremental updates in the annealer, so the
two always agree (see tests/test_congestion.py).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass
class CongestionConfig:
    bins_long_side: int = 32  # bins along the longer board side
    min_bin_mm: float = 1.0
    max_bin_mm: float = 5.0
    utilization: float = 0.5  # usable share of the theoretical track capacity
    pin_cost_mm: float = 0.5  # capacity consumed by each connected pin
    pour_factor: float = 0.2  # demand weight of nets carried by a plane
    target: float = 1.0  # utilisation above which a bin is penalised


def steiner_factor(n_pins: int) -> float:
    """Approximate ratio of Steiner-tree length to HPWL for an n-pin net."""
    return 1.0 if n_pins <= 3 else 1.0 + 0.45 * math.log(n_pins / 3.0)


class CongestionGrid:
    def __init__(self, bbox, routing_layers: int, pitch_mm: float, cfg: CongestionConfig):
        bx0, by0, bx1, by1 = bbox
        w, h = bx1 - bx0, by1 - by0
        b = min(cfg.max_bin_mm, max(cfg.min_bin_mm, max(w, h) / cfg.bins_long_side))
        self.cfg = cfg
        self.bin = b
        self.x0, self.y0 = bx0, by0
        self.nx = max(1, math.ceil(w / b))
        self.ny = max(1, math.ceil(h / b))
        self.cap = max(routing_layers, 1) * cfg.utilization / max(pitch_mm, 1e-3) * b * b
        self.demand = np.zeros((self.ny, self.nx))

    # ----- geometry ------------------------------------------------------------
    def _ix(self, x):
        return np.clip(((np.asarray(x) - self.x0) / self.bin).astype(int), 0, self.nx - 1)

    def _iy(self, y):
        return np.clip(((np.asarray(y) - self.y0) / self.bin).astype(int), 0, self.ny - 1)

    def net_rect(self, px: np.ndarray, py: np.ndarray, n_pins: int, factor: float) -> tuple:
        """(iy0, iy1, ix0, ix1, demand per bin) for one net."""
        x0, x1, y0, y1 = px.min(), px.max(), py.min(), py.max()
        length = ((x1 - x0) + (y1 - y0)) * steiner_factor(n_pins) * factor
        ix0, ix1 = int(self._ix(x0)), int(self._ix(x1))
        iy0, iy1 = int(self._iy(y0)), int(self._iy(y1))
        nb = (ix1 - ix0 + 1) * (iy1 - iy0 + 1)
        return (iy0, iy1, ix0, ix1, length / nb)

    def pin_bins(self, px: np.ndarray, py: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        return self._iy(py), self._ix(px)

    # ----- updates ------------------------------------------------------------
    def add_rect(self, r: tuple, sign: float = 1.0) -> None:
        iy0, iy1, ix0, ix1, v = r
        self.demand[iy0:iy1 + 1, ix0:ix1 + 1] += sign * v

    def add_pins(self, bins: tuple[np.ndarray, np.ndarray], sign: float = 1.0) -> None:
        if len(bins[0]):
            np.add.at(self.demand, bins, sign * self.cfg.pin_cost_mm)

    # ----- scores -------------------------------------------------------------
    def penalty(self, region=None) -> float:
        d = self.demand if region is None else self.demand[region]
        excess = np.clip(d / self.cap - self.cfg.target, 0.0, None)
        return float(self.cap * np.square(excess).sum())

    def metrics(self) -> dict:
        u = (self.demand / self.cap).ravel()
        top = np.sort(u)[::-1]
        k = max(1, int(round(0.05 * len(top))))
        return {
            "ace5": round(float(top[:k].mean()), 3),  # mean utilisation of the 5% busiest bins
            "max_util": round(float(top[0]), 3),
            "hot_bins_pct": round(float((u > 1.0).mean() * 100), 1),
            "overflow_mm": round(float(np.clip(self.demand - self.cap, 0, None).sum()), 1),
            "penalty": round(self.penalty(), 1),
            "bin_mm": round(self.bin, 2),
            "capacity_mm_per_bin": round(self.cap, 2),
        }

    def region_of(self, rects: list[tuple], pin_sets: list[tuple[np.ndarray, np.ndarray]]):
        iy0, iy1, ix0, ix1 = self.ny, -1, self.nx, -1
        for r in rects:
            iy0, iy1 = min(iy0, r[0]), max(iy1, r[1])
            ix0, ix1 = min(ix0, r[2]), max(ix1, r[3])
        for iy, ix in pin_sets:
            if len(iy):
                iy0, iy1 = min(iy0, int(iy.min())), max(iy1, int(iy.max()))
                ix0, ix1 = min(ix0, int(ix.min())), max(ix1, int(ix.max()))
        if iy1 < 0:
            return None
        return (slice(iy0, iy1 + 1), slice(ix0, ix1 + 1))
