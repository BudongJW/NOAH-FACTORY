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
    summary = run(RunConfig(input=DEMO, out=out, lock={"P1"}, seeds=2, candidates=2, place_time_s=4,
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
