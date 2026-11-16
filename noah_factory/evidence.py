"""Evidence records and claims.

Every sentence in the design-rationale report is a Claim that must cite Evidence.
A claim is shown as verified only if:
  * every cited evidence id exists,
  * every number in its text matches a value carried by the cited evidence, and
  * every identifier in backticks (component ref or net name) appears in that evidence.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class Evidence:
    id: str
    kind: str  # metric | drc | lock_check | tool_report
    metric: str
    value: float | int | None
    unit: str = ""
    limit: float | None = None
    passed: bool | None = None
    refs: list[str] = field(default_factory=list)
    nets: list[str] = field(default_factory=list)
    tool: str = ""
    detail: dict = field(default_factory=dict)

    def numbers(self) -> list[float]:
        out: list[float] = []

        def walk(v):
            if isinstance(v, bool):
                return
            if isinstance(v, (int, float)):
                out.append(float(v))
            elif isinstance(v, dict):
                for x in v.values():
                    walk(x)
            elif isinstance(v, (list, tuple)):
                for x in v:
                    walk(x)

        walk(self.value)
        walk(self.limit)
        walk(self.detail)
        return out


@dataclass
class Claim:
    id: str
    section: str
    text: str
    evidence_ids: list[str]
    status: str = "pending"  # verified | rejected
    reason: str = ""


class EvidenceStore:
    def __init__(self):
        self._items: dict[str, Evidence] = {}

    def add(self, kind: str, metric: str, value, **kw) -> Evidence:
        ev = Evidence(id=f"ev_{len(self._items) + 1:04d}", kind=kind, metric=metric, value=value, **kw)
        self._items[ev.id] = ev
        return ev

    def get(self, eid: str) -> Evidence | None:
        return self._items.get(eid)

    def all(self) -> list[Evidence]:
        return list(self._items.values())

    def dump(self, path: Path) -> None:
        path.write_text(json.dumps([asdict(e) for e in self.all()], ensure_ascii=False, indent=2))


_IDENT = re.compile(r"`([^`]+)`")
# Numbers glued to Latin identifiers (e.g. "U12", "F.Cu") are not quantities; numbers next to
# Korean text ("3개") are, so the look-behind only excludes ASCII word characters.
_NUMBER = re.compile(r"(?<![A-Za-z0-9_.])-?\d+(?:\.\d+)?")


def _matches(num_text: str, values: list[float]) -> bool:
    decimals = len(num_text.split(".")[1]) if "." in num_text else 0
    x = float(num_text)
    tol = 0.5 * 10 ** (-decimals) + 1e-9
    return any(abs(round(v, decimals) - x) <= tol or abs(abs(round(v, decimals)) - abs(x)) <= tol
               for v in values)


def validate_claim(claim: Claim, store: EvidenceStore) -> Claim:
    evs = [store.get(e) for e in claim.evidence_ids]
    if not claim.evidence_ids or any(e is None for e in evs):
        claim.status, claim.reason = "rejected", "missing evidence"
        return claim
    idents_allowed: set[str] = set()
    values: list[float] = []
    for e in evs:
        idents_allowed.update(e.refs)
        idents_allowed.update(e.nets)
        values.extend(e.numbers())
    for ident in _IDENT.findall(claim.text):
        if ident not in idents_allowed:
            claim.status, claim.reason = "rejected", f"identifier `{ident}` not in cited evidence"
            return claim
    plain = _IDENT.sub(" ", claim.text)
    for num in _NUMBER.findall(plain):
        if not _matches(num, values):
            claim.status, claim.reason = "rejected", f"number {num} not supported by cited evidence"
            return claim
    claim.status, claim.reason = "verified", ""
    return claim
