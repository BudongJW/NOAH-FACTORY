"""Congestion (RUDY) model: incremental updates must match a full rebuild."""

import random

import numpy as np

from noah_factory.congestion import CongestionConfig, CongestionGrid, steiner_factor
from noah_factory.placement import PlacementConfig, PlacementProblem, anneal

from test_placement import _board


def test_rect_spreads_net_length_over_covered_bins():
    g = CongestionGrid((0, 0, 32, 32), routing_layers=2, pitch_mm=0.5, cfg=CongestionConfig(bins_long_side=32))
    r = g.net_rect(np.array([0.5, 4.5]), np.array([0.5, 2.5]), n_pins=2, factor=1.0)
    g.add_rect(r)
    assert abs(g.demand.sum() - (4.0 + 2.0)) < 1e-9  # HPWL preserved
    assert r[:4] == (0, 2, 0, 4)


def test_steiner_factor_grows_with_pins():
    assert steiner_factor(2) == 1.0 and steiner_factor(3) == 1.0
    assert 1.4 < steiner_factor(10) < 1.7
    assert steiner_factor(50) > steiner_factor(10)


def test_incremental_updates_match_full_rebuild():
    ir = _board(n_chain=10)
    p = PlacementProblem(ir, PlacementConfig())
    rng = random.Random(5)
    X = np.array([c.x for c in ir.components], dtype=float)
    Y = np.array([c.y for c in ir.components], dtype=float)
    K = np.zeros(p.n, dtype=int)
    state = p.build_congestion(X, Y, K)
    for step in range(300):
        S = [int(p.movable[rng.randrange(len(p.movable))])]
        if rng.random() < 0.3:
            S.append(int(p.movable[rng.randrange(len(p.movable))]))
            S = sorted(set(S))
        saved = [(i, X[i], Y[i], K[i]) for i in S]
        for i in S:
            X[i] = rng.uniform(2, 48)
            Y[i] = rng.uniform(2, 28)
            K[i] = rng.randrange(4)
        dpen, undo = p.update_congestion(state, S, X, Y, K)
        if step % 3 == 0:  # reject: roll back both the map and the positions
            p.undo_congestion(state, undo)
            for i, x, y, k in saved:
                X[i], Y[i], K[i] = x, y, k
    fresh, _, _ = p.build_congestion(X, Y, K)
    assert np.allclose(state[0].demand, fresh.demand, atol=1e-9)
    assert abs(state[0].penalty() - fresh.penalty()) < 1e-6


def test_congestion_weight_lowers_penalty_on_a_tight_board():
    # Many crossing nets on a small 1-layer board: the congestion term should spread them out.
    ir = _board(n_chain=14)
    ir.board.routing_layers = 1
    ir.board.track_pitch_mm = 2.0  # little capacity, so congestion is visible
    base = anneal(PlacementProblem(ir, PlacementConfig(time_limit_s=4, init="random")), seed=2)
    cong = anneal(PlacementProblem(ir, PlacementConfig(time_limit_s=4, init="random", w_congestion=5.0)), seed=2)
    assert cong.breakdown["congestion"]["penalty"] <= base.breakdown["congestion"]["penalty"]
    assert cong.breakdown["overlaps"] == []
