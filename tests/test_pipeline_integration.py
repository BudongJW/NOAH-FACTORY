"""End-to-end run on a KiCad demo board. Skipped when KiCad or Freerouting is unavailable."""

import json
import shutil
from pathlib import Path

import pytest

DEMO = Path("/usr/share/kicad/demos/ecc83/ecc83-pp.kicad_pcb")
JAR = Path("/opt/freerouting/freerouting.jar")

pcbnew = pytest.importorskip("pcbnew")
pytestmark = pytest.mark.skipif(not (DEMO.exists() and JAR.exists() and shutil.which("kicad-cli")),
                                reason="KiCad demos, kicad-cli or Freerouting not installed")


def test_pipeline_routes_and_reports(tmp_path):
    from noah_factory.pipeline import RunConfig, run

    out = tmp_path / "run"
    summary = run(RunConfig(input=DEMO, out=out, lock={"P1"}, seeds=2, candidates=2, place_time_s=8,
                            route_passes=20, route_timeout_s=120), log=lambda *_: None)
    assert summary["placement"]["best"]["overlaps"] == 0
    assert summary["placement"]["best"]["outside"] == 0
    assert summary["drc"]["unconnected"] == 0
    assert summary["drc"]["by_category"].get("electrical", 0) == 0
    assert summary["claims"]["rejected"] == 0
    assert summary["fabrication"]["ok"]
    report = (out / "report.md").read_text()
    assert "검증하지 않은 항목" in report
    claims = json.loads((out / "claims.json").read_text())
    assert all(c["evidence_ids"] for c in claims)
    # the locked part did not move
    evidence = json.loads((out / "evidence.json").read_text())
    lock = next(e for e in evidence if e["metric"] == "locked_moved_count")
    assert lock["value"] == 0 and "P1" in lock["refs"]

    # A stub with a free end, as the router sometimes leaves, is found by DRC and removed.
    from noah_factory.kicad import load_board, save_board
    from noah_factory.pipeline import cleanup_dangling
    board_path = next((out / "final").glob("*.kicad_pcb"))
    b = load_board(board_path)
    # Put the stub in an empty spot (placement is random), on a net without a pour (a pour would
    # connect it): at least 5 mm from every pad and track, inside the board.
    anchor = next(t for t in b.GetTracks() if t.GetClass() == "PCB_TRACK" and t.GetNetname() != "GND")
    copper = [p.GetPosition() for p in b.GetPads()] + \
             [pt for t in b.GetTracks() for pt in (t.GetStart(), t.GetEnd())]
    edge = b.GetBoardEdgesBoundingBox()
    mm = 1_000_000
    spot = next(pcbnew.VECTOR2I(x, y)
                for x in range(edge.GetLeft() + 3 * mm, edge.GetRight() - 5 * mm, mm)
                for y in range(edge.GetTop() + 3 * mm, edge.GetBottom() - 3 * mm, mm)
                if all(abs(c.x - x) > 5 * mm or abs(c.y - y) > 5 * mm for c in copper))
    stub = pcbnew.PCB_TRACK(b)
    stub.SetStart(spot)
    stub.SetEnd(pcbnew.VECTOR2I(spot.x + 2 * mm, spot.y))
    stub.SetWidth(anchor.GetWidth())
    stub.SetLayer(anchor.GetLayer())
    stub.SetNet(anchor.GetNet())
    b.Add(stub)
    save_board(b, board_path)
    before = sum(1 for _ in load_board(board_path).GetTracks())
    result = cleanup_dangling(board_path, tmp_path)
    assert result["removed"] >= 1
    assert sum(1 for _ in load_board(board_path).GetTracks()) == before - result["removed"]
