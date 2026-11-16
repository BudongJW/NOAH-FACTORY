"""Routing through Freerouting (GPL-3.0), run as a separate headless process."""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

SCORE_LINE = re.compile(r"\((\d+) unrouted and (\d+) violations\)")


def _default_java() -> str:
    for cand in (os.environ.get("NOAH_JAVA"), "/opt/jdk25/bin/java", shutil.which("java")):
        if cand and Path(cand).exists():
            return cand
    return "java"


@dataclass
class RoutingConfig:
    jar: str = os.environ.get("NOAH_FREEROUTING_JAR", "/opt/freerouting/freerouting.jar")
    java: str = ""
    max_passes: int = 30
    timeout_s: int = 300
    threads: int = 2
    # Narrowest trace the router may use when necking into pads. Freerouting reads it from
    # .kicad_pro but truncates to whole micrometres (198.12 um -> 198 um < KiCad minimum),
    # so the pipeline passes the board minimum rounded up.
    neck_width_um: int | None = None

    def __post_init__(self):
        if not self.java:
            self.java = _default_java()


def freerouting_version(cfg: RoutingConfig) -> str:
    p = Path(cfg.jar)
    if not p.exists():
        return "missing"
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return f"freerouting.jar sha256:{h.hexdigest()[:12]}"


def run_freerouting(dsn: Path, ses: Path, cfg: RoutingConfig, log_path: Path,
                    extra_inputs: list[Path] | None = None) -> dict:
    """extra_inputs: .kicad_pro (minimum track width) and .kicad_dru (custom clearance rules);
    the Specctra export drops both, so Freerouting would otherwise route below KiCad's rules."""
    # Absolute paths: Freerouting runs with cwd=dsn.parent, so relative paths would not resolve.
    dsn, ses, log_path = dsn.resolve(), ses.resolve(), log_path.resolve()
    design = "+".join([str(dsn)] + [str(p.resolve()) for p in (extra_inputs or []) if p.exists()])
    # Freerouting's own job timeout stops the router gracefully and still writes the session
    # (best result so far). Killing the process instead loses all routing work.
    job_s = max(30, cfg.timeout_s - 40)
    cmd = [
        cfg.java, "-jar", cfg.jar,
        "-de", design, "-do", str(ses),
        "--gui.enabled=false",
        f"--router.autorouter.max_passes={cfg.max_passes}",
        f"--router.max_threads={cfg.threads}",
        f"--router.job_timeout={job_s // 3600:02d}:{job_s % 3600 // 60:02d}:{job_s % 60:02d}",
    ]
    if cfg.neck_width_um:
        cmd.append(f"--router.neck_width_um={cfg.neck_width_um}")
    t0 = time.monotonic()
    killed = False
    with log_path.open("w") as log:
        try:
            proc = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, timeout=cfg.timeout_s + 60,
                                  cwd=str(dsn.parent))
            code = proc.returncode
        except subprocess.TimeoutExpired:
            killed = True
            code = -1
    elapsed = time.monotonic() - t0
    text = log_path.read_text(errors="replace")
    scores = SCORE_LINE.findall(text)
    last = scores[-1] if scores else None
    timed_out = killed or "state: TIMED_OUT" in text
    return {
        "ok": code == 0 and ses.exists() and not timed_out,
        "returncode": code,
        "timed_out": timed_out,
        "killed": killed,
        "time_s": round(elapsed, 2),
        "reported_unrouted": int(last[0]) if last else None,
        "reported_violations": int(last[1]) if last else None,
        "max_passes": cfg.max_passes,
    }
