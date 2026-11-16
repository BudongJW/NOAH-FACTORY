"""Command line: python -m noah_factory run BOARD.kicad_pcb --out runs/x [options]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .pipeline import RunConfig, run


def _refs(s: str | None) -> set[str]:
    return {r.strip() for r in (s or "").split(",") if r.strip()}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="noah_factory", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="place, route, verify and report one KiCad board")
    r.add_argument("board", type=Path)
    r.add_argument("--out", type=Path, required=True)
    r.add_argument("--lock", help="comma-separated refs to keep fixed (e.g. J1,U1)")
    r.add_argument("--edge", help="comma-separated refs to keep at the board edge")
    r.add_argument("--seeds", type=int, default=4)
    r.add_argument("--candidates", type=int, default=3)
    r.add_argument("--place-time", type=float, default=30.0, help="seconds per seed")
    r.add_argument("--init", choices=("random", "current"), default="current",
                   help="start from random positions or refine the current placement")
    r.add_argument("--no-place", action="store_true", help="keep the input placement (route and check only)")
    r.add_argument("--congestion", type=float, default=None,
                   help="weight of the routing-congestion term in the placement cost (0 = off)")
    r.add_argument("--no-route", action="store_true")
    r.add_argument("--route-passes", type=int, default=30)
    r.add_argument("--route-timeout", type=int, default=300)
    r.add_argument("--no-export", action="store_true")
    a = ap.parse_args(argv)

    if a.cmd == "run":
        if not a.board.exists():
            print(f"not found: {a.board}", file=sys.stderr)
            return 2
        run(RunConfig(input=a.board.resolve(), out=a.out.resolve(), lock=_refs(a.lock), edge=_refs(a.edge),
                      seeds=a.seeds, candidates=a.candidates, place_time_s=a.place_time, init=a.init,
                      place=not a.no_place, route=not a.no_route,
                      **({"w_congestion": a.congestion} if a.congestion is not None else {}), route_passes=a.route_passes, route_timeout_s=a.route_timeout,
                      export=not a.no_export))
    return 0


if __name__ == "__main__":
    sys.exit(main())
