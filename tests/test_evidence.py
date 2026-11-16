from noah_factory.evidence import Claim, EvidenceStore, validate_claim


def _store():
    s = EvidenceStore()
    s.add("metric", "decap_distance_mm", 1.43, unit="mm", limit=3.0, passed=True,
          refs=["C3", "U1"], nets=["+3V3"])
    s.add("drc", "unconnected_count", 0, limit=0, passed=True)
    return s


def test_verified_claim_with_matching_numbers_and_identifiers():
    s = _store()
    c = validate_claim(Claim("c1", "decap", "`C3`는 `U1`의 `+3V3` 핀에서 1.4 mm (기준 3.0 mm 이내).",
                             ["ev_0001"]), s)
    assert c.status == "verified", c.reason


def test_rejects_number_not_in_evidence():
    s = _store()
    c = validate_claim(Claim("c1", "decap", "`C3`는 `U1`에서 0.8 mm 떨어져 있습니다.", ["ev_0001"]), s)
    assert c.status == "rejected"
    assert "0.8" in c.reason


def test_rejects_identifier_not_in_evidence():
    s = _store()
    c = validate_claim(Claim("c1", "decap", "`C9`는 `U1`에서 1.4 mm 떨어져 있습니다.", ["ev_0001"]), s)
    assert c.status == "rejected"
    assert "C9" in c.reason


def test_rejects_missing_or_empty_evidence():
    s = _store()
    assert validate_claim(Claim("c1", "x", "미배선 0개", []), s).status == "rejected"
    assert validate_claim(Claim("c2", "x", "미배선 0개", ["ev_9999"]), s).status == "rejected"


def test_number_next_to_korean_text_is_checked():
    s = _store()
    assert validate_claim(Claim("c1", "x", "미배선 연결은 0개입니다.", ["ev_0002"]), s).status == "verified"
    assert validate_claim(Claim("c2", "x", "미배선 연결은 5개입니다.", ["ev_0002"]), s).status == "rejected"
