# 모디팩토리(MODI Factory) 유사 프로젝트 조사: (A) 국내 기업·서비스, (B) AI/자동 PCB 설계 오픈소스

> 조사일: 2026-11-16. GitHub 수치(스타·포크)는 모두 2026-11-16에 github.com 저장소 페이지에서 직접 확인한 값.
> **방법상 한계(중요):** 이 세션의 네트워크 정책 때문에 한국 언론·기업 사이트(sedaily.com, modifactory.com, news.nate.com, lgresearch.ai, forum.kicad.info 등)를 직접 열람하지 못했다. GitHub API(api.github.com)도 막혀 있었다. 따라서 (A) 국내 부분의 사실은 대부분 **검색엔진 결과 스니펫/요약 기준(원문 미열람)**이며, 아래에 그렇게 표시했다. (B) GitHub 수치는 저장소 페이지를 직접 열어 확인했다.
> 참고: 모디팩토리 자체는 **럭스로보(LUXROBO)**가 만든 서비스로 확인됨(아래 A-1). 모디팩토리 자체 상세는 다른 조사 범위이므로 비교에 필요한 정도만 적음.

## (A-1) 국내 AI 기반 PCB·회로·하드웨어 설계 자동화 기업/서비스

### Takeaway
국내에서 "파일 업로드 → AI가 PCB 배치·배선까지 자동 생성"하는 **일반 사용자 대상 웹 서비스는 모디팩토리(럭스로보)가 사실상 유일하게 확인됨**. 그 밖의 국내 플레이어는 (1) 하드웨어 설계 문서 검증 AI(세카, LG전자 분사), (2) 대기업 내부 연구(LG AI연구원 PCB 자동배선), (3) 제조 공정 최적화(마키나락스 SMT), (4) 반도체(칩) 단 AI EDA(알세미 등)로, 직접 경쟁보다는 인접 영역이다.

### Cited Findings
**럭스로보 / MODI Factory (비교 기준점)**
- 모디팩토리는 럭스로보가 만든 AI 기반 PCB 설계 자동화 플랫폼이며, 럭스로보는 교육용 IoT 모듈 기업에서 AI PCB 설계 자동화 플랫폼 기업으로 사업모델을 전환 중이라고 보도됨. 보도 시점 기준 "정식 출시 전 베타버전" — [서울경제(검색 스니펫, 원문 미열람)](https://www.sedaily.com/article/20019757)
- Embedded World 2026(독일 뉘른베르크)에서 '설계 자동화(Tools)' 부문 글로벌 톱3에 최종 지명, "아시아 기업 중 유일" — [서울경제(스니펫)](https://www.sedaily.com/article/20019757); [더빅데이터 2026-03-16(스니펫)](https://www.thebigdata.co.kr/view.php?ud=2026031615220030386cf2d78c68_23)
- 회사 사이트 설명: 회로도·레이아웃 파일 업로드 시 물리 기반 검증→배치→배선을 90분 이내 처리(자체 주장, PCB 밀도·서버 환경에 따라 달라질 수 있다고 명시) — [MODI Factory 블로그(스니펫)](https://www.modifactory.com/blog/ko/insights-001); [MODI Factory](https://www.modifactory.com/ko)
- 부품 배치·배선 자동 수행, 판단 근거를 'AI 노트'로 제시, 무료 요금제로 사용자 확대 후 구독형 도입 계획 — [네이트뉴스 '2026 하반기 혁신 IT 대상' 2026-09-11(스니펫)](https://news.nate.com/view/20260911n18067)
- 자사 블로그에서 결과물로 JLCPCB 발주용 거버(Gerber) 추출 방법 안내 — [MODI Factory 블로그(스니펫)](https://www.modifactory.com/blog/ko/jlcpcb-order-guide)
- 한국·미국·인도 중심 글로벌 베타 준비, "모디 팩토리 단일 프로젝트로 유료 매출 5억원, 유저 1만명 목표"(2025년 보도) — [뉴스토마토(스니펫)](http://www.newstomato.com/readnews.aspx?no=1287248)
- 투자: 2025년 10월 Pre-IPO 투자 유치(THE VC 기재), 과거 카카오인베스트먼트·카카오브레인 40억원(2017), 시리즈B 90억원(KDB산업은행 등) — [THE VC](https://thevc.kr/luxrobo); [파이낸셜뉴스 2017-06-07](https://www.fnnews.com/news/201706071046598737); [벤처스퀘어](https://www.venturesquare.net/802751)

**세카(SECA) — LG전자 사내벤처 분사, 하드웨어 설계 자동화(가장 가까운 국내 'AI for 하드웨어 설계' 스타트업)**
- LG전자·블루포인트파트너스 공동 사내벤처 프로그램 '스튜디오341'에서 분사, 2026년 6월 독립법인 출범, LG전자·블루포인트 시드투자(금액 비공개) — [머니투데이 2026-08-19(스니펫)](https://www.mt.co.kr/future/2026/08/19/2026081908314619012); [WOWTALE EN 2026-08-19(스니펫)](https://en.wowtale.net/2026/08/19/234790/)
- 제품 'SECA Design Intelligence Platform': 데이터시트·회로도·BOM·넷리스트를 지식그래프로 연결하고 AI 에이전트가 문서 간 불일치 탐지, 기존 EDA·PLM과 연계 — [네이트뉴스 2026-11-05(스니펫)](https://m.news.nate.com/view/20261105n25257); [ZDNet Korea 2026-10-08(스니펫)](https://zdnet.co.kr/view/?no=20261008135433)
- 2026-11-16 중기부 팁스(TIPS) 선정 발표. 대형 제조기업 PoC에서 설계 공수 66% 절감(경쟁 솔루션 25%), 법인 출범 후 매출 7억원, 2030년 매출 1000억원 목표 — [와우테일 2026-11-16(스니펫)](https://wowtale.net/2026/11/16/268099/); [유니콘팩토리 2026-11-16(스니펫)](https://www.unicornfactory.co.kr/article/2026111610165217978); [중기이코노미(스니펫)](https://www.junggi.co.kr/news/articleView.html?idxno=38510)
- 다음 단계: 넷리스트+부품 배치·배선 정보를 함께 학습하는 설계 특화 AI 파운데이션 모델, 아날로그 회로 설계 자동화로 확장 계획 — [와우테일(스니펫)](https://wowtale.net/2026/11/16/268099/)
- 주의: 기사마다 절감 수치(66%, 92%, 480→160시간 등)의 맥락 표현이 다름 — [서플(스니펫)](https://supple.kr/news/cmwizgtsng6uz10eg6f9w6s71); [네이트뉴스(스니펫)](https://m.news.nate.com/view/20261105n25257)

**LG AI연구원 — PCB 자동배선 연구(사내/계열사용)**
- LG전자·LG디스플레이·LG이노텍 등 계열사의 PCB 자동배선 문제를 연구, 격자 기반+연속 공간 기반 방식 병행, 계열사 실제 제품으로 검증, 엔지니어 배선 데이터를 학습해 실제 설계와 유사한 결과 목표 — [LG AI Research 블로그(스니펫, 원문 미열람)](https://www.lgresearch.ai/blog/view?seq=509)

**마키나락스(MakinaRocks) — PCB '설계'가 아니라 SMT '조립 공정' 최적화**
- 강화학습으로 PCB 위 부품 장착 순서(SMT mount sequence) 최적화, 8주 만에 기존 알고리즘 수준 달성. 33개 PCB 샘플 실험, IPC 샘플에서 이동거리 354.6mm→332.8mm — [마키나락스 유스케이스](https://www.makinarocks.ai/use-case/reinforcement-learning-based-smt-sequence-optimization/); [마키나락스 블로그](https://makinarocks.ai/optimizing-chip-mount-planning-smt-reinforcement-learning)
- 별도로 구글 방법론 기반 강화학습으로 ASIC 플로어플랜(매크로 배치) 자동화 연구 — [마키나락스 블로그](https://www.makinarocks.ai/blog/application-specific-integrated-circuit-asic-floorplan-automation-part-i/)

**알세미(Alsemy) — 반도체 소자 모델링 AI EDA(PCB 아님)**
- 2019년 SK하이닉스 사내벤처에서 분사, AI 기반 반도체 설계 자동화 SW(컴팩트 모델 자동 생성). 2026년 5월 브릿지 75억원 유치, 누적 168억원 보도 — [다음/VC 요람 2026-05-25(스니펫)](https://v.daum.net/v/20260525122307460); [혁신의숲](https://www.innoforest.co.kr/company/CP00001930/%EC%95%8C%EC%84%B8%EB%AF%B8)

**학계(참고)** — UNIST·경북대 연구팀: LC-VCO 회로도→물리 레이아웃 자동설계 AI, 기존 약 119시간→28.5시간(칩 RF 회로, PCB 아님) — [전기신문(스니펫)](https://www.electimes.com/news/articleView.html?idxno=367646)

**PCB 제조사(대덕전자·이수페타시스)**
- 두 회사가 AI PCB 설계 서비스를 운영한다는 자료는 검색되지 않음. 이수페타시스는 리벨리온·퓨리오사AI와 AI 가속기용 PCB 양산 협력(2025-07) 등 '제조' 측 AI 수요 대응 — [파이낸셜뉴스 영문(스니펫)](https://en.fnnews.com/news/202507111319504309); [다음 2024-03-27](https://v.daum.net/v/20240327101549462)

**해외 맥락(비교용, 간략)** — Quilter(미국) 2025-10 시리즈B 2,500만 달러(Index Ventures 주도), Flux 누적 3,700만 달러(2026-02 보도) 등 해외 AI PCB 스타트업은 대규모 투자 단계 — [Pulse 2.0](https://pulse2.com/quilter-25-million-series-b-raised-for-automating-pcb-design-with-physics-driven-ai); [SiliconANGLE 2026-02-27](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)

### Inferences
- 국내에서 "비전문가용 + AI 자동 배치·배선 + 설계 근거 설명" 조합을 내건 상용 웹 서비스는 모디팩토리 외에 확인되지 않았다. 국내 경쟁 구도는 '같은 제품'보다 '인접 영역(설계 검증 AI·대기업 내부 연구·칩 EDA)'이 중심이다.
- 세카는 타깃(대기업 전장/가전 설계팀)과 기능(문서 정합성 검증·설계 초안 공수 절감)이 다르지만, '넷리스트+배치·배선 학습 파운데이션 모델' 계획이 실현되면 B2B 영역에서 모디팩토리와 겹칠 가능성이 있다.
- LG AI연구원 사례는 대기업이 자체 데이터로 PCB 자동배선을 내재화하려는 흐름을 보여주며, 이는 B2B 확장 시 대기업이 외부 SaaS보다 내부 솔루션을 선호할 수 있다는 신호로 해석된다(추론).

### Gaps
- 과제 지시문에 있던 후보 — 베이리스(Bayless), 서플라이웨이, 위즈네트 관련 서비스, 이노피아, 세미파이브 설계 플랫폼, 보스반도체 — 는 이번 조사에서 PCB/회로 설계 자동화 서비스로 **확인되지 않음**(관련 검색 결과 없음 또는 미검색). 존재 여부를 단정하지 않음.
- 'PCB 바로', '피씨비웨이 한국' 같은 명칭의 국내 온라인 PCB 플랫폼은 확인되지 않음(아래 A-2의 PCBGOGO 한국어 사이트 등만 확인).
- 모디팩토리의 정식 출시일, 실제 가입자 수, 가격은 검색 결과에서 확인 불가.
- 국내 언론 원문을 직접 열람하지 못해(네트워크 차단) 수치는 검색 스니펫 기준이다. 정확한 인용이 필요하면 원문 재확인 필요.

## (A-2) 국내 PCB 설계 외주·제조 중개·온라인 주문 플랫폼 (AI가 아닌 대안 경로)

### Takeaway
초보자가 모디팩토리 대신 택할 수 있는 국내 경로는 (1) 크몽 등 재능마켓의 개인/소규모 업체 PCB 설계 외주(수십만 원~, 수일), (2) 캐파(CAPA) 같은 제조 파트너 중개, (3) 한국어 온라인 견적 PCB 제조(대부분 중국 공장 기반)다. AI 자동설계 기능을 내세운 국내 외주·중개 플랫폼은 확인되지 않았다.

### Cited Findings
- 크몽: 회로·PCB·펌웨어 설계 및 보드 제작 판매자 다수. 한 판매자는 "330,000원부터, 3일 이내 완료" 패키지 — [크몽 412145](https://kmong.com/gig/412145); [크몽 614520](https://kmong.com/gig/614520); [크몽 109900](https://kmong.com/gig/109900)
- (주)제이: 스타트업·취미 개발자 대상 2층 이하 단순 회로 PCB 설계 옵션 100,000원 — [(주)제이](https://j-iot.co.kr/product/10)
- 대전 소재 업체: 회로설계·PCB 아트웍 외주, 펌웨어, 검사 지그 제작, 설계 툴로 EasyEDA Pro·PADS 사용 명시 — [gspls.kr](https://gspls.kr/work)
- 하드웨어 외주 전 준비 자료(회로도, BoM, PCB 파일 등) 안내 콘텐츠 — [비트버스](https://www.bitbus.co.kr/insights/hardware-outsourcing-preparation)
- 캐파(CAPA): 제조 파트너 검색에 '전자회로(PCB)' 분야 파트너 7,626개 등록(검색 시점 스니펫), 견적 요청 가능 — [캐파 PCB 파트너](https://capa.ai/partners?keyword=%EC%A0%84%EC%9E%90%ED%9A%8C%EB%A1%9C%28PCB%29)
- 한국어 온라인 견적 PCB 제조: PCBGOGO 한국어(실시간 견적, 1~14층, 중국 공장), 와이즈피시비(파일 업로드→기술검토→견적→생산), MPGATE(회로설계·부품조달·SMT 원스톱) — [PCBGOGO KR](https://www.pcbgogo.co.kr/); [WISE PCB](https://www.wisepcb.com/); [MPGATE](https://www.mpgate.co.kr/)
- KoFab은 국내 제조업체 연결 플랫폼이나 3D프린팅·CNC 중심 — [KoFab](https://www.kofab.org/)
- 국내 PCB 업체 KMTEK은 'AI로 설계한 PCB 제조 전 확인사항' 콘텐츠를 게시(AI 설계 결과물을 제조로 넘기는 수요를 겨냥) — [Korea Master Technology](https://kmtek.co.kr/pcb-ai/)

### Inferences
- 국내 PCB 설계 외주 가격대(약 10만~33만원~, 수일 소요)는 모디팩토리의 '무료 가입 + 90분' 포지셔닝과 직접 비교되는 기준선이 된다. 모디팩토리의 결과물(거버)을 PCBGOGO·JLCPCB·국내 제조사로 넘기는 흐름이 자연스럽다.
- 제조 중개(캐파)·온라인 주문 플랫폼에 AI 설계 기능이 붙은 사례는 없으므로, 모디팩토리↔제조 플랫폼 간 제휴/연동이 국내 공백 영역으로 보인다(추론).

### Gaps
- 크몽 등 외주 시장 규모·거래량, 캐파의 PCB 설계(제조 아님) 중개 실적은 확인 불가.
- 국내 대형 EDA 리셀러(Altium·Cadence·Siemens 국내 총판)가 AI 기능을 별도 서비스로 판매하는지 확인하지 못함.

## (A-3) 국내 초보자용 하드웨어·메이커 교육 생태계 (간략)

### Takeaway
모디팩토리의 모회사 럭스로보는 원래 모듈형 코딩 교육 키트 'MODI'로 알려진 교육용 IoT/로봇 모듈 기업이다. 즉 '초보자 친화' 포지셔닝은 MODI 교육 사업의 연장선에 있다.

### Cited Findings
- 럭스로보는 '로봇 모듈 플랫폼 기업'으로 카카오인베스트먼트·카카오브레인이 2017년 40억원 공동 투자 — [카카오 보도자료](https://www.kakaocorp.com/page/detail/8317?lang=ENG); [파이낸셜뉴스 2017-06-07](https://www.fnnews.com/news/201706071046598737)
- 코딩 비전공자도 MODI 모듈로 로봇을 만들 수 있다는 체험기 — [벤처스퀘어](https://www.venturesquare.net/751030)
- 럭스로보가 교육용 IoT 모듈 기업에서 AI PCB 설계 플랫폼 기업으로 전환 중 — [서울경제(스니펫)](https://www.sedaily.com/article/20019757); [더빅데이터 2026-03-16(스니펫)](https://www.thebigdata.co.kr/view.php?ud=2026031615220030386cf2d78c68_23)

### Inferences
- MODI 교육 사용자층(학교·메이커)이 모디팩토리의 초기 비전문가 사용자 유입 경로가 될 수 있다(추론, 근거 자료 없음).

### Gaps
- 국내 메이커스페이스(중기부 메이커 스페이스 사업 등), 한국 전자 DIY 커뮤니티(예: 네이버 카페)에 대한 자료는 이번 조사에서 수집하지 못함.

## (B-1) 오픈소스 EDA·오토라우터·코드 기반 설계 도구 (서비스 구성요소 후보)

### Takeaway
모디팩토리 같은 서비스를 오픈소스로 구성할 때 핵심 빌딩블록은 **KiCad(파일 포맷·DRC·거버 출력) + Freerouting(오토라우팅, 공개 API·MCP 제공)** 이고, 회로를 코드로 표현하는 계층으로 **atopile, tscircuit, SKiDL, circuit-synth**가 있다. 단, **자동 '배치(placement)'를 실사용 수준으로 제공하는 성숙한 오픈소스는 없음** — 대부분 배치는 수동이거나 연구 코드 수준.

### Cited Findings
| 프로젝트 | URL | 스타(2026-11-16) | 라이선스 | 핵심 기능 | 성숙도/비고 |
|---|---|---|---|---|---|
| Freerouting | [github](https://github.com/freerouting/freerouting) | 약 2.2k (포크 363) | GPL-3.0 | Specctra/Electra DSN 기반 PCB 오토라우터 | 공개 API `api.freerouting.app/v1` 베타(키 신청제), Docker/JRE 셀프호스팅 가능, MCP 연동(Cursor·Cline·Claude Desktop), 메인테이너 주 4시간 수준 |
| KiCad (GitHub 미러) | [github](https://github.com/KiCad/kicad-source-mirror) | 약 3.2k (포크 786) | GPL-3.0 외 | 오픈소스 회로도·PCB EDA 표준 | 본 개발은 GitLab, GitHub는 미러 |
| atopile | [github](https://github.com/atopile/atopile) | 약 4.1k (포크 262) | MIT | `.ato` 선언형 언어로 회로를 코드화, 파라메트릭 부품 자동 선정, KiCad 레이아웃 연동, BOM·제조 데이터 출력 | 2,843 커밋, PyPI 배포, 상용 지원; 저장소에 AGENTS.md/CLAUDE.md 있음(내장 AI 기능은 README상 미기재) |
| tscircuit | [github](https://github.com/tscircuit/tscircuit) | 약 3.0k (포크 357) | MIT | TypeScript/React로 회로 작성→회로도·PCB·3D·제조파일 | 문서상 개발 중, 자동 배치 미지원(좌표 수동), 오토라우터 개발 중; 텍스트→풋프린트 AI 도구, llms.txt 제공 |
| SKiDL | [github](https://github.com/devbisme/skidl) | 약 1.7k (포크 186) | MIT | Python으로 회로(넷리스트) 설계 | KiCad 5~10 지원, PyPI, 2,283 커밋; AI 기능 없음 |
| circuit-synth | [github](https://github.com/circuit-synth/circuit-synth) | 295 (포크 36) | MIT | Python→KiCad 프로젝트(.kicad_sch/.kicad_pcb) 생성, Claude Code 에이전트(circuit-architect, simulation-expert, FMEA 등) | 자동 배치·배선 없음(KiCad에서 수동), Python 3.12+/KiCad 8+ |

- tscircuit core에 단층/다층 fanout 오토라우터 추가 PR이 2026-07-28 병합 — [tscircuit/core PR #2889 (검색 스니펫)](https://github.com/tscircuit/core/pull/2889)
- tscircuit 문서에 'Claude 등 AI 어시스턴트로 회로 생성' 섹션 존재 — [tscircuit docs](https://docs.tscircuit.com/category/circuit-generation)
- 2026-09 KiCad 포럼 사용자 보고: AI+tscircuit로 약 15개 설계 발주, RP2040/RP2350/ESP32 기반 보드는 AI가 잘 하지만 복잡한 설계는 한계 — [검색 스니펫 기반, 원문 미열람](https://forum.kicad.info/t/two-months-of-testing-llms-on-pcb-autorouting-what-worked-what-didnt-and-whats-left-to-try-open-archive/72250)

### Inferences
- MODI Factory의 '업로드→배치·배선→거버' 파이프라인을 오픈소스로 재현한다면, 배선은 Freerouting(GPL-3.0이므로 SaaS 내부 사용은 가능하나 배포 시 GPL 의무 주의), 파일 처리·DRC·출력은 KiCad CLI로 가능하나, **자동 배치와 '설계 근거' 생성이 오픈소스 공백**이며 바로 이 부분이 모디팩토리의 차별 요소로 보인다(추론).
- atopile·tscircuit·circuit-synth는 '회로를 코드로' 접근이어서 LLM이 생성하기 쉬운 중간표현을 제공한다. 비전문가용 서비스의 프론트엔드(자연어→회로) 계층 후보다.

### Gaps
- GitHub API 차단으로 각 저장소의 최신 릴리스 버전·날짜와 마지막 커밋 일자를 확인하지 못함(페이지에 미표시).
- KiCad 본가(GitLab)의 스타·IPC API 상세는 미확인.

## (B-2) LLM·MCP 기반 KiCad/EDA 연동 프로젝트 (2025–2026)

### Takeaway
2025–2026년 사이 KiCad를 LLM(Claude 등)이 조작하도록 하는 MCP 서버가 급증했다. 가장 큰 것은 mixelpixx/KiCAD-MCP-Server(약 3.4k 스타)로 Freerouting·JLCPCB 부품 연동까지 포함한다. 다만 이들은 "AI가 사람 대신 KiCad를 조작"하는 보조 도구이며, 품질 보장형 자동설계 서비스는 아니다.

### Cited Findings
| 프로젝트 | URL | 스타(2026-11-16) | 라이선스 | 내용 |
|---|---|---|---|---|
| mixelpixx/KiCAD-MCP-Server | [github](https://github.com/mixelpixx/KiCAD-MCP-Server) | 약 3.4k (포크 449) | MIT | 프로젝트 생성·회로도 편집·부품 배치·라우팅·DRC/ERC·출력, 커스텀 심볼/풋프린트, JLCPCB 부품·가격·재고, Freerouting 연동; KiCad 9/10; 1,255 커밋; README에 "AI 생성 설계는 자격 있는 엔지니어 검토 필요" 고지; 후속 폐쇄형 'Konnect-EDA' 홍보 |
| lamaalrajih/kicad-mcp | [github](https://github.com/lamaalrajih/kicad-mcp) | 536 (포크 83) | MIT | 프로젝트 관리, PCB 분석, 넷리스트 추출, BOM, DRC, 회로 패턴 인식(벅/부스트 등); KiCad 9+; 초기 단계 |
| ProductOfAmerica/mcp-server-kicad | [github](https://github.com/ProductOfAmerica/mcp-server-kicad) | 미확인 | 미확인 | 100+ 도구(회로도·PCB·ERC/DRC·오토라우팅·거버/BOM/3D 출력), 현재 유지보수 모드(보안·호환성 수정만) — 검색 스니펫 기준 |
| Finerestaurant/kicad-mcp-python | [github](https://github.com/Finerestaurant/kicad-mcp-python) | 미확인 | 미확인 | KiCad 공식 IPC API 사용 — 검색 스니펫 기준 |
| ANamelessDrake/kicad-mcp | [github](https://github.com/ANamelessDrake/kicad-mcp) | 미확인 | 미확인 | KiCad 8 .kicad_sch/.kicad_pcb 파일 수준 편집 — 검색 스니펫 기준 |
| paul356/KiCad-AI-Assistant | [github](https://github.com/paul356/KiCad-AI-Assistant) | 미확인 | 미확인 | KiCad 10용 LLM 채팅 플러그인 — 검색 스니펫 기준 |

- Freerouting 자체도 MCP 섹션을 두고 공개 API를 통해 `npx`로 Java 설치 없이 MCP 사용 가능 — [Freerouting GitHub](https://github.com/freerouting/freerouting)
- KiCad 포럼에 MCP 서버 공개 글이 다수 게시(예: oaslananka/kicad-mcp-pro 등) — [KiCad 포럼 글 1(스니펫)](https://forum.kicad.info/t/i-built-an-mcp-server-that-lets-ai-assistants-help-with-kicad-pcb-design/66451); [KiCad 포럼 글 2(스니펫)](https://forum.kicad.info/t/i-built-an-open-source-mcp-server-for-ai-assisted-kicad-workflows/68678)
- 커뮤니티 실험 보고: LLM이 배선 실패를 구조화 텍스트(레이어 점유+넷 인접+제약)로 읽을 때 recall 0.82, SVG 이미지로 읽을 때 0.03 (비공식 포럼 글, 일화적 자료) — [KiCad 포럼(스니펫, 원문 미열람)](https://forum.kicad.info/t/two-months-of-testing-llms-on-pcb-autorouting-what-worked-what-didnt-and-whats-left-to-try-open-archive/72250)

### Inferences
- 모디팩토리의 '설계 근거(AI 노트)'와 유사한 기능은 MCP+LLM 조합으로 오픈소스에서도 흉내낼 수 있으나, 대부분 개발자용(Claude Desktop/Cursor 설치 필요)이라 '웹 업로드 한 번'의 비전문가 UX와는 거리가 있다.
- 구조화 텍스트 입력이 이미지보다 LLM 성능에 훨씬 유리하다는 커뮤니티 관찰은, 설계 근거 생성 시 넷리스트·제약을 텍스트로 LLM에 넘기는 설계가 유리함을 시사한다(추론, 일화적 근거).

### Gaps
- ProductOfAmerica, Finerestaurant, ANamelessDrake, paul356 저장소의 스타·라이선스는 직접 확인하지 못함(시간 제약).
- MCP 서버들의 실제 설계 품질(DRC 통과율 등) 정량 평가는 찾지 못함.

## (B-3) ML/RL 기반 배치 연구 코드·데이터셋·벤치마크

### Takeaway
PCB 자동 배치는 연구 단계 오픈소스(RL_PCB, NVIDIA Cypress, learned-pcb-placement)가 있으나 스타 수 수십 규모의 연구 코드다. 칩 레벨(구글 circuit_training/AlphaChip, OpenROAD)은 성숙하지만 PCB에 바로 쓰기 어렵다. LLM 평가용 벤치마크(PCB-Bench, ICLR 2026)가 등장했다.

### Cited Findings
| 프로젝트 | URL | 스타(2026-11-16) | 라이선스 | 내용 / 성숙도 |
|---|---|---|---|---|
| RL_PCB (Luke Vassallo) | [github](https://github.com/LukeVassallo/RL_PCB) | 76 (포크 26) | MIT | 강화학습(TD3/SAC로 추정, 그림 파일명 기준)으로 PCB 부품 배치 반복 개선; DATE 2024 논문 "Learning Circuit Placement Techniques Through RL with Adaptive Rewards"; 학습 회로 6개, Python 3.8/PyTorch 1.13 고정 — 연구 코드 |
| NVlabs/Cypress | [github](https://github.com/NVlabs/Cypress) | 56 (포크 20) | Apache-2.0 | VLSI(DREAMPlace/AutoDMP) 기법을 응용한 GPU 가속 PCB 배치, ISPD 2025 논문; 벤치마크 포함 — 연구 코드 |
| elcruzo/learned-pcb-placement | [github](https://github.com/elcruzo/learned-pcb-placement) | 미확인 | 미확인 | GNN(GAT)+시뮬레이티드 어닐링, 오픈소스 KiCad 보드 12개(5~94부품)로 평가 — 검색 스니펫 기준 |
| google-research/circuit_training (AlphaChip) | [github](https://github.com/google-research/circuit_training) | 약 1.7k (포크 274) | Apache-2.0 | 분산 심층강화학습 칩 플로어플랜(매크로 배치), 2021 Nature 방법론 재현; README상 "연구 프로젝트", Linux 전용, 최신 체크포인트 2024-08 |
| OpenROAD | [github](https://github.com/The-OpenROAD-Project/OpenROAD) | 약 3.3k (포크 1.1k) | BSD-3-Clause | RTL→GDS 칩 설계 플로우(칩 레벨, PCB 아님) |
| digailab/PCB-Bench | [github](https://github.com/digailab/PCB-Bench) | 미확인 | 미확인 | (멀티모달) LLM의 PCB 배치·배선 추론 능력 평가 벤치마크, ICLR 2026 — 검색 스니펫 기준 |
| tangsanli5201/DeepPCB | [github](https://github.com/tangsanli5201/DeepPCB) | 미확인 | 미확인 | PCB **결함** 검출 데이터셋(설계용 아님) — 검색 스니펫 기준 |

- Cypress 벤치마크: 41~476 부품의 소규모 공개 설계 세트와 5,118~6,628 부품 대규모 세트 — [Cypress 논문(ISPD 2025)](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
- 2026년 arXiv에 PCB 설계 자동화 관련 벤치마크/데이터셋이 다수 등장: PCBWorld(엔진 기반 PCB 설계 자동화 벤치마크), PCB-QA(PCB 설계 QA 데이터셋), SchGen(회로도 생성), pcbGPT(자연어 요구사항→회로도 합성) — [PCBWorld](https://arxiv.org/pdf/2607.05915); [PCB-QA](https://arxiv.org/pdf/2606.23704); [SchGen](https://arxiv.org/pdf/2605.30345); [pcbGPT](https://arxiv.org/pdf/2606.01188)
- 'DeepPCB'라는 이름은 InstaDeep의 상용 AI PCB 배치·배선 클라우드 서비스(백서 공개)와 위 결함 데이터셋 두 가지가 있어 혼동 주의; InstaDeep DeepPCB는 오픈소스가 아님 — [DeepPCB 백서](https://deeppcb.ai/white-paper/)

### Inferences
- 오픈소스만으로 '실무 수준 자동 배치'를 구현하기는 어렵고, RL_PCB·Cypress는 알고리즘 참조/벤치마크용으로 적합하다. 모디팩토리급 서비스는 자체 데이터·휴리스틱·물리 검증을 결합한 독자 엔진이 필요할 것으로 보인다(추론).
- 2026년 학계 벤치마크(PCB-Bench, PCBWorld, PCB-QA)는 모디팩토리 같은 서비스의 성능을 외부적으로 비교·검증하는 기준으로 활용 가능하다(추론).

### Gaps
- learned-pcb-placement, PCB-Bench, DeepPCB(데이터셋)의 스타·라이선스는 직접 확인하지 못함.
- "pcb-rl" 등 지시문에 언급된 기타 저장소명은 이번 검색에서 특정 저장소로 확인되지 않음.
- 오픈소스 자동 배치 도구의 실제 상용 보드 대비 품질 비교 자료는 찾지 못함.
