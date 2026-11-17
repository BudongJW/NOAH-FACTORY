"""Verification through kicad-cli DRC (and schematic parity when a schematic exists)."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ENVIRONMENT = {"lib_footprint_issues", "lib_footprint_mismatch"}
PARITY = {"missing_footprint", "extra_footprint", "duplicate_footprints", "net_conflict",
          "footprint_symbol_mismatch", "footprint_filters_mismatch"}
MANUFACTURING = {"solder_mask_bridge", "hole_to_hole", "drill_out_of_range", "annular_width",
                 "via_diameter", "track_width", "copper_sliver", "micro_via_drill_out_of_range",
                 "connection_width", "npth_inside_courtyard", "pth_inside_courtyard"}
PLACEMENT = {"courtyards_overlap", "missing_courtyard", "malformed_courtyard"}
DANGLING = {"track_dangling", "via_dangling"}
_NET_IN_ITEM = re.compile(r"\[([^\]]+)\]")  # e.g. "PTH pad 2 [GND] of C5"


def categorize(violation_type: str) -> str:
    if violation_type in ENVIRONMENT:
        return "environment"
    if violation_type in PARITY or violation_type.startswith("schematic"):
        return "parity"
    if violation_type in MANUFACTURING:
        return "manufacturing"
    if violation_type in PLACEMENT:
        return "placement"
    if violation_type.startswith(("silk_", "text_", "lib_")):
        return "cosmetic"
    return "electrical"


def kicad_cli_version() -> str:
    try:
        out = subprocess.run(["kicad-cli", "version"], capture_output=True, text=True, timeout=30)
        return f"kicad-cli {out.stdout.strip()}"
    except (OSError, subprocess.SubprocessError):
        return "kicad-cli missing"


def run_drc(board: Path, out_json: Path, schematic_parity: bool = False,
            refill_zones: bool = True) -> dict:
    cmd = ["kicad-cli", "pcb", "drc", "--format", "json", "--severity-all", "-o", str(out_json)]
    if refill_zones:
        cmd += ["--refill-zones", "--save-board"]
    if schematic_parity:
        cmd += ["--schematic-parity"]
    cmd.append(str(board))
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if not out_json.exists():
        return {"ok": False, "error": (proc.stderr or proc.stdout)[-2000:]}
    data = json.loads(out_json.read_text())
    violations = data.get("violations", []) + data.get("schematic_parity", [])
    by_type = Counter(v.get("type", "unknown") for v in violations)
    by_cat = Counter()
    errors_by_cat = Counter()
    for v in violations:
        cat = categorize(v.get("type", "unknown"))
        by_cat[cat] += 1
        if v.get("severity") == "error":
            errors_by_cat[cat] += 1
    examples = []
    for v in violations:
        if categorize(v.get("type", "")) in ("electrical", "manufacturing", "placement") and len(examples) < 10:
            items = [it.get("description", "") for it in v.get("items", [])][:2]
            examples.append({"type": v.get("type"), "severity": v.get("severity"),
                             "description": v.get("description"), "items": items})
    unconnected_nets = sorted({m.group(1) for u in data.get("unconnected_items", [])
                               for it in u.get("items", [])
                               if (m := _NET_IN_ITEM.search(it.get("description", "")))})
    dangling = [it["uuid"] for v in violations if v.get("type") in DANGLING
                for it in v.get("items", [])[:1] if it.get("uuid")]
    return {
        "ok": True,
        "parity_checked": schematic_parity,
        "unconnected": len(data.get("unconnected_items", [])),
        "unconnected_nets": unconnected_nets,
        "dangling_uuids": dangling,
        "violations_total": len(violations),
        "by_category": dict(by_cat),
        "errors_by_category": dict(errors_by_cat),
        "by_type": dict(by_type.most_common()),
        "examples": examples,
    }
