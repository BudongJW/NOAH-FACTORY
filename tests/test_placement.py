"""Placement tests on a synthetic board (no KiCad needed)."""

import numpy as np

from noah_factory.ir import Board, Component, DesignIR, Net, Pad, rotate
from noah_factory.placement import (PlacementConfig, PlacementProblem, anneal, apply_result,
                                    parse_farads)


def _two_pin(ref, kind, net_a, net_b, x, y, value="", locked=False):
    return Component(ref=ref, value=value, footprint="R_0603", x=x, y=y, rotation=0.0, flipped=False,
                     locked=locked, has_through_hole=False, bbox=(-1.0, -0.5, 1.0, 0.5),
                     pads=[Pad("1", net_a, -0.8, 0.0), Pad("2", net_b, 0.8, 0.0)], kind=kind)


def _board(n_chain=8, locked_ref="J1"):
    comps = [Component(ref="U1", value="MCU", footprint="QFN", x=25, y=15, rotation=0, flipped=False,
                       locked=False, has_through_hole=False, bbox=(-3, -3, 3, 3),
                       pads=[Pad("1", "+3V3", -2.5, 0), Pad("2", "GND", 2.5, 0), Pad("3", "N0", 0, -2.5)],
                       kind="ic"),
             Component(ref="J1", value="USB_C", footprint="USB_C_Receptacle", x=2.5, y=15, rotation=0,
                       flipped=False, locked=locked_ref == "J1", has_through_hole=True,
                       bbox=(-2, -4, 2, 4), pads=[Pad("1", "+3V3", 0, -2), Pad("2", "GND", 0, 2)],
                       kind="connector"),
             _two_pin("C1", "capacitor", "+3V3", "GND", 40, 25, value="100n")]
    for i in range(n_chain):
        comps.append(_two_pin(f"R{i + 1}", "resistor", f"N{i}", f"N{i + 1}", 5 + 4 * i, 5))
    nets: dict[str, list] = {}
    for ci, c in enumerate(comps):
        for pi, p in enumerate(c.pads):
            nets.setdefault(p.net, []).append((ci, pi))
    from noah_factory.ir import net_role
    ir = DesignIR("synthetic", comps, [Net(n, pins, net_role(n)) for n, pins in nets.items()],
                  Board(bbox=(0, 0, 50, 30), copper_layers=2))
    return ir


def test_parse_farads():
    assert abs(parse_farads("100n") - 1e-7) < 1e-15
    assert abs(parse_farads("4u7") - 4.7e-6) < 1e-12
    assert abs(parse_farads("10uF/16V") - 1e-5) < 1e-12
    assert parse_farads("") is None


def test_rotation_convention_matches_kicad():
    # +90 deg turns (x, y) into (y, -x) in KiCad's y-down frame (checked against pcbnew).
    x, y = rotate(3.45, 4.80, 90)
    assert abs(x - 4.80) < 1e-9 and abs(y + 3.45) < 1e-9


def test_anneal_is_legal_respects_locks_and_rules():
    ir = _board()
    cfg = PlacementConfig(time_limit_s=600, moves_per_component=2000, init="random")
    p = PlacementProblem(ir, cfg)
    res = anneal(p, seed=7)
    bd = res.breakdown
    assert bd["overlaps"] == []
    assert bd["outside"] == []
    assert res.legalization_failures == []
    j = p.refs.index("J1")
    assert res.x[j] == 2.5 and res.y[j] == 15 and res.k[j] == 0
    decap = bd["decaps"][0]
    assert decap["cap"] == "C1" and decap["ic"] == "U1"
    assert decap["pass"], decap
    # positions are on the placement grid
    movable = p.movable
    assert np.allclose(np.round(res.x[movable] / cfg.grid_mm) * cfg.grid_mm, res.x[movable], atol=1e-6)


def test_parts_avoid_copper_obstacles():
    ir = _board()
    # a copper text block across the middle of the front side, and a keepout on all sides
    ir.board.obstacles = [(10.0, 12.0, 40.0, 18.0, 0, "LOGO"), (42.0, 2.0, 48.0, 8.0, 3, "keepout")]
    cfg = PlacementConfig(time_limit_s=600, moves_per_component=2000, init="random")
    p = PlacementProblem(ir, cfg)
    res = anneal(p, seed=11)
    assert res.legalization_failures == []
    assert [o for o in res.breakdown["overlaps"] if o[1].startswith("copper:")] == []


def test_anneal_shortens_a_scrambled_chain():
    ir = _board()
    cfg = PlacementConfig(time_limit_s=600, moves_per_component=2000, init="random")
    p = PlacementProblem(ir, cfg)
    X0 = np.array([c.x for c in ir.components])
    Y0 = np.array([c.y for c in ir.components])
    rng = np.random.default_rng(0)
    X0[p.movable] = rng.uniform(5, 45, len(p.movable))
    Y0[p.movable] = rng.uniform(5, 25, len(p.movable))
    scrambled = p.evaluate(X0, Y0, np.zeros(p.n, dtype=int))["hpwl_mm"]
    res = anneal(p, seed=3)
    assert res.breakdown["hpwl_mm"] < scrambled
    apply_result(ir, p, res)
    assert ir.components[1].x == 2.5  # locked connector unchanged in IR
