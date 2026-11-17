"""Design-rationale report: evidence -> claims (rule-based templates) -> validation -> Markdown.

Phase 0 writes claims from templates. An LLM phrasing step can be added later, but its
output must pass the same `validate_claim` gate before it reaches the report.
"""

from __future__ import annotations

from pathlib import Path

from .evidence import Claim, EvidenceStore, validate_claim

MAX_DECAP_LINES = 15

NOT_CHECKED = [
    ("신호 무결성(SI)", "반사·크로스토크·타이밍 해석을 수행하지 않았습니다."),
    ("전원 무결성(PI)", "전압 강하·PDN 임피던스 해석을 수행하지 않았습니다."),
    ("발열", "부품 온도·열 분포 해석을 수행하지 않았습니다."),
    ("EMC", "방사·전도 노이즈 검토를 수행하지 않았습니다."),
    ("임피던스·차동쌍", "제어 임피던스, 차동쌍 간격·길이 매칭을 검증하지 않았습니다."),
    ("제조사별 DFM", "보드 파일의 설계 규칙만 적용했고, 특정 제조사의 공정 규칙은 적용하지 않았습니다."),
    ("기구·높이 간섭", "부품 높이와 케이스 간섭(3D)을 검사하지 않았습니다."),
]


def _fmt(v: float, d: int = 1) -> str:
    return f"{v:.{d}f}"


def build_evidence(store: EvidenceStore, *, before: dict, after: dict, locked: list[str],
                   locked_moved: list[str], legal_failures: list[str], drc: dict | None,
                   routing: dict | None, route_stats: dict | None, tools: dict,
                   density: dict | None = None, density_limit: float = 85.0,
                   zones_removed: dict | None = None, congestion: dict | None = None) -> dict:
    """Turn engine outputs into evidence records. Returns ids grouped by topic."""
    ids: dict = {"decaps": [], "edges": []}
    if zones_removed and (zones_removed["teardrops"] or zones_removed["local_pours"]):
        ids["zones"] = store.add("metric", "layout_bound_zones_removed",
                                 zones_removed["teardrops"] + zones_removed["local_pours"],
                                 nets=zones_removed["local_pour_nets"], tool=tools["placer"],
                                 detail={"teardrops": zones_removed["teardrops"],
                                         "local_pours": zones_removed["local_pours"]}).id
    if congestion:
        ids["congestion"] = store.add("metric", "routing_congestion", congestion["after"]["ace5"],
                                      tool=tools["placer"],
                                      detail={"top_share_pct": 5,  # ACE5 = mean of the busiest 5% bins
                                              "input_ace5": congestion["before"]["ace5"],
                                              "hot_bins_pct": congestion["after"]["hot_bins_pct"],
                                              "input_hot_bins_pct": congestion["before"]["hot_bins_pct"]}).id
    if density:
        worst = max(density["front"], density["back"])
        ids["density"] = store.add("metric", "part_area_share_pct", worst, unit="%", limit=density_limit,
                                   passed=worst <= density_limit, tool=tools["placer"],
                                   detail={"front": density["front"], "back": density["back"]}).id
    hb, ha = before["hpwl_mm"], after["hpwl_mm"]
    pct = (ha - hb) / hb * 100 if hb else 0.0
    ids["hpwl"] = store.add("metric", "hpwl_mm", ha, unit="mm", tool=tools["placer"],
                            detail={"input_hpwl_mm": hb, "change_pct": round(pct, 1),
                                    "abs_change_pct": round(abs(pct), 1)}).id
    ids["overlap"] = store.add("metric", "courtyard_overlap_count", len(after["overlaps"]),
                               limit=0, passed=len(after["overlaps"]) == 0, tool=tools["placer"],
                               detail={"pairs": after["overlaps"][:20]}).id
    ids["outside"] = store.add("metric", "outside_board_count", len(after["outside"]), limit=0,
                               passed=len(after["outside"]) == 0, refs=after["outside"],
                               tool=tools["placer"]).id
    ids["legal"] = store.add("metric", "legalization_failures", len(legal_failures), limit=0,
                             passed=not legal_failures, refs=legal_failures, tool=tools["placer"]).id
    ids["lock"] = store.add("lock_check", "locked_moved_count", len(locked_moved), limit=0,
                            passed=not locked_moved, refs=sorted(set(locked) | set(locked_moved)),
                            tool=tools["placer"], detail={"locked_count": len(locked)}).id
    for d in after["decaps"]:
        ev = store.add("metric", "decap_distance_mm", d["distance_mm"], unit="mm", limit=d["limit_mm"],
                       passed=d["pass"], refs=[d["cap"], d["ic"]], nets=[d["net"]], tool=tools["placer"])
        ids["decaps"].append((ev.id, d))
    if after["decaps"]:
        n_pass = sum(1 for d in after["decaps"] if d["pass"])
        n_pass_in = sum(1 for d in before["decaps"] if d["pass"])
        ids["decap_summary"] = store.add("metric", "decap_pass_count", n_pass,
                                         detail={"total": len(after["decaps"]), "input_pass": n_pass_in},
                                         tool=tools["placer"]).id
    for e in after["edges"]:
        ev = store.add("metric", "edge_distance_mm", e["distance_mm"], unit="mm", limit=e["limit_mm"],
                       passed=e["pass"], refs=[e["ref"]], tool=tools["placer"])
        ids["edges"].append((ev.id, e))
    if drc and drc.get("ok"):
        ids["unrouted"] = store.add("drc", "unconnected_count", drc["unconnected"], limit=0,
                                    passed=drc["unconnected"] == 0, tool=tools["drc"]).id
        cats = drc["by_category"]
        ids["drc"] = store.add("drc", "violations_by_category", drc["violations_total"], tool=tools["drc"],
                               detail={c: cats.get(c, 0) for c in
                                       ("electrical", "manufacturing", "placement", "cosmetic",
                                        "environment", "parity")}).id
        if drc.get("parity_checked"):
            ids["parity"] = store.add("drc", "schematic_parity_issues", cats.get("parity", 0), limit=0,
                                      passed=cats.get("parity", 0) == 0, tool=tools["drc"]).id
    if route_stats:
        ids["route_stats"] = store.add("metric", "routing_stats", route_stats["track_length_mm"],
                                       unit="mm", tool=tools["router"],
                                       detail={"via_count": route_stats["via_count"]}).id
    if routing and routing.get("cleanup", {}).get("removed"):
        ids["cleanup"] = store.add("tool_report", "dangling_items_removed", routing["cleanup"]["removed"],
                                   tool=tools["drc"], detail={"rounds": routing["cleanup"]["rounds"]}).id
    if routing:
        ids["router_report"] = store.add("tool_report", "router_final_score", routing.get("reported_unrouted"),
                                         tool=tools["router"],
                                         detail={"violations": routing.get("reported_violations"),
                                                 "time_s": routing.get("time_s"),
                                                 "max_passes": routing.get("max_passes")}).id
    return ids


def build_claims(store: EvidenceStore, ids: dict, *, before: dict, after: dict, locked: list[str],
                 drc: dict | None, route_stats: dict | None) -> list[Claim]:
    claims: list[Claim] = []

    def add(section, text, evs):
        claims.append(validate_claim(Claim(id=f"cl_{len(claims) + 1:03d}", section=section, text=text,
                                           evidence_ids=evs), store))

    if "density" in ids:
        ev = store.get(ids["density"])
        text = (f"부품 면적(코트야드를 감싸는 사각형 기준)은 보드 면적의 앞면 {_fmt(ev.detail['front'])}%, "
                f"뒷면 {_fmt(ev.detail['back'])}%입니다.")
        if not ev.passed:
            text += (f" 현재 배치 모델이 다룰 수 있는 {_fmt(ev.limit)}%를 넘어, 겹침 없는 배치를 찾지 못할 수 "
                     f"있습니다. 기존 배치를 유지한 부분 재배치나 다각형 기반 배치가 필요합니다.")
        add("placement", text, [ids["density"]])
    if "zones" in ids:
        ev = store.get(ids["zones"])
        add("placement", f"원래 배치에 맞춰 그려진 티어드롭 {ev.detail['teardrops']}개와 국소 구리 영역 "
            f"{ev.detail['local_pours']}개를 제거했습니다. 부품이 움직이면 옛 위치에 남는 구리이기 "
            f"때문입니다. 보드 전체를 덮는 구리 영역(평면)은 유지하고 다시 채웠습니다.", [ids["zones"]])
    if "congestion" in ids:
        ev = store.get(ids["congestion"])
        add("placement", f"배선 혼잡도(상위 5% 구간 평균 사용률)는 {_fmt(ev.value, 2)}로, 입력 배치"
            f"({_fmt(ev.detail['input_ace5'], 2)})와 비교됩니다. 용량을 넘는 구간은 전체의 "
            f"{_fmt(ev.detail['hot_bins_pct'])}%입니다(입력 배치 {_fmt(ev.detail['input_hot_bins_pct'])}%).",
            [ids["congestion"]])
    hb, ha = before["hpwl_mm"], after["hpwl_mm"]
    pct = store.get(ids["hpwl"]).detail["abs_change_pct"]
    direction = "줄었습니다" if ha <= hb else "늘었습니다"
    add("placement", f"배치 후 추정 배선 길이(HPWL)는 {_fmt(ha)} mm로, 입력 배치({_fmt(hb)} mm)보다 "
        f"{_fmt(pct)}% {direction}.", [ids["hpwl"]])
    add("placement", f"부품 겹침은 {len(after['overlaps'])}건, 보드 외곽을 벗어난 부품은 "
        f"{len(after['outside'])}건입니다.", [ids["overlap"], ids["outside"]])
    if locked:
        shown = ", ".join(f"`{r}`" for r in locked[:8]) + (" 등" if len(locked) > 8 else "")
        moved = store.get(ids["lock"]).value
        text = (f"고정한 부품 {len(locked)}개({shown})는 위치와 회전이 바뀌지 않았습니다." if moved == 0
                else f"고정한 부품 {len(locked)}개 중 {moved}개의 위치가 바뀌었습니다.")
        add("placement", text, [ids["lock"]])
    if "decap_summary" in ids:
        ev = store.get(ids["decap_summary"])
        add("placement", f"디커플링 커패시터 {ev.detail['total']}개 중 {ev.value}개가 거리 기준을 만족합니다 "
            f"(입력 배치에서는 {ev.detail['input_pass']}개).", [ids["decap_summary"]])
        worst_first = sorted(ids["decaps"], key=lambda t: (t[1]["pass"], -t[1]["distance_mm"]))
        for eid, d in worst_first[:MAX_DECAP_LINES]:
            # two decimals: one decimal could print "3.0 mm, limit 3.0 mm: fails" for 3.02 mm
            verdict = "충족" if d["pass"] else "미달"
            add("decap", f"`{d['cap']}`: `{d['ic']}`의 `{d['net']}` 핀까지 {_fmt(d['distance_mm'], 2)} mm "
                f"(기준 {_fmt(d['limit_mm'])} mm 이내) — {verdict}", [eid])
    for eid, e in ids["edges"]:
        verdict = "충족" if e["pass"] else "미달"
        add("placement", f"외부 커넥터 `{e['ref']}`: 보드 외곽까지 {_fmt(e['distance_mm'], 2)} mm "
            f"(기준 {_fmt(e['limit_mm'])} mm 이내) — {verdict}", [eid])
    if drc and drc.get("ok"):
        add("routing", f"배선 후 미배선 연결은 {drc['unconnected']}개입니다.", [ids["unrouted"]])
        if "cleanup" in ids:
            add("routing", f"배선기가 남긴 끝이 연결되지 않은 트랙·비아 조각 {store.get(ids['cleanup']).value}개를 "
                f"DRC로 찾아 제거했습니다. 연결 상태에는 영향이 없습니다.", [ids["cleanup"]])
        c = store.get(ids["drc"]).detail
        add("routing", f"DRC 결과: 전기 규칙 {c['electrical']}건, 제조 규칙 {c['manufacturing']}건, "
            f"배치(코트야드) {c['placement']}건, 실크·문자 {c['cosmetic']}건, "
            f"실행 환경(라이브러리 미설치) {c['environment']}건입니다.", [ids["drc"]])
        if "parity" in ids:
            add("routing", f"회로도와 PCB의 불일치는 {store.get(ids['parity']).value}건입니다.", [ids["parity"]])
    if route_stats:
        add("routing", f"총 배선 길이는 {_fmt(route_stats['track_length_mm'])} mm, 비아는 "
            f"{route_stats['via_count']}개입니다.", [ids["route_stats"]])
    return claims


def render_report(path: Path, *, title: str, claims: list[Claim], drc: dict | None, run_info: dict,
                  parity_checked: bool) -> None:
    verified = [c for c in claims if c.status == "verified"]
    rejected = [c for c in claims if c.status != "verified"]
    lines = [f"# 설계 리뷰 리포트 — {title}", "",
             "> 이 리포트의 모든 문장은 검사 결과(증거)를 인용합니다. 괄호 안의 `ev_` 번호는 "
             "`evidence.json`의 레코드입니다. 증거와 맞지 않는 문장은 자동으로 제외됩니다.", ""]

    def section(name, key):
        items = [c for c in verified if c.section == key]
        if not items:
            return
        lines.extend([f"## {name}", ""])
        for c in items:
            lines.append(f"- {c.text} ({', '.join(c.evidence_ids)})")
        lines.append("")

    section("배치", "placement")
    section("디커플링 커패시터 (기준 미달 우선)", "decap")
    section("배선·검증", "routing")

    if drc and drc.get("examples"):
        lines.extend(["## 확인이 필요한 DRC 항목 (최대 10건)", ""])
        for ex in drc["examples"]:
            items = "; ".join(ex["items"])
            lines.append(f"- `{ex['type']}` ({ex['severity']}): {ex['description']} — {items}")
        lines.append("")

    lines.extend(["## 검증하지 않은 항목", "",
                  "아래 항목은 이번 실행에서 검사하지 않았습니다. 제작 전 별도 검토가 필요합니다.", ""])
    for name, desc in NOT_CHECKED:
        lines.append(f"- **{name}**: {desc}")
    if not parity_checked:
        lines.append("- **회로도 일치성**: 회로도 파일이 없어 PCB와 회로도의 일치 여부를 검사하지 않았습니다.")
    lines.append("")

    if rejected:
        lines.extend(["## 제외된 문장 (증거 불일치)", ""])
        for c in rejected:
            lines.append(f"- ~~{c.text}~~ — {c.reason}")
        lines.append("")

    lines.extend(["## 실행 정보", ""])
    for k, v in run_info.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
