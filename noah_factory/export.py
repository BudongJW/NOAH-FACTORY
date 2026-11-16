"""Manufacturing outputs through kicad-cli."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def _run(cmd: list[str]) -> tuple[bool, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    return proc.returncode == 0, (proc.stderr or proc.stdout)[-500:]


def export_fabrication(board: Path, out_dir: Path) -> dict:
    gerber_dir = out_dir / "gerber"
    gerber_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    results["gerbers"] = _run(["kicad-cli", "pcb", "export", "gerbers", "-o", str(gerber_dir) + "/", str(board)])
    results["drill"] = _run(["kicad-cli", "pcb", "export", "drill", "-o", str(gerber_dir) + "/", str(board)])
    results["positions"] = _run(["kicad-cli", "pcb", "export", "pos", "--format", "csv", "--units", "mm",
                                 "-o", str(out_dir / "positions.csv"), str(board)])
    archive = shutil.make_archive(str(out_dir / "fabrication"), "zip", root_dir=str(gerber_dir))
    files = sorted(p.name for p in gerber_dir.iterdir())
    return {
        "ok": all(ok for ok, _ in results.values()),
        "errors": {k: msg for k, (ok, msg) in results.items() if not ok},
        "files": files,
        "archive": Path(archive).name,
    }
