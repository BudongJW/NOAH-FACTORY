# 보완 조사: 경쟁사 사실 재검증 + AI PCB 설계 도구 실사용자 평판 (2026-11-16 기준)

> **검증 표시 규칙**
> - **[원문 확인]**: 이 세션에서 Bash `curl`(프록시 경유)로 해당 페이지 원문을 직접 받아 읽은 항목입니다(2026-11-16).
> - **[GitHub-verified]**: raw.githubusercontent.com에서 README 원문을 직접 읽은 항목입니다.
> - **[search-snippet]**: WebSearch 요약/스니펫만 본 항목입니다(원문 미열람).
> - **[unverified]**: 단일 출처이거나 서로 충돌해 확인하지 못한 항목입니다.
> - **[벤더 작성]**: 해당 회사나 경쟁사가 직접 쓴 비교·홍보 콘텐츠입니다. 독립 근거가 아닙니다.
>
> **접근성 관련 중요 정정:** 이전 노트는 "quilter.ai, flux.ai, deeppcb.ai 등이 차단"이라고 적었습니다. 그러나 이번 세션에서는 Bash `curl`로 quilter.ai, flux.ai, deeppcb.ai, zuken.com, eebench.org, news.ycombinator.com, hn.algolia.com(API), eevblog.com, forum.kicad.info, newstap.co.kr에 **정상 접근**했습니다. 차단을 확인한 곳은 reddit.com(curl 403, WebSearch도 도메인 거부), adafruit.com(CloudFront 403), newsroom.cadence.com(403), wowtale.net(403), api.github.com(세션 권한 없음)입니다. aimatters.co.kr은 빈 응답이었습니다. WebFetch 도구 자체는 이번에 시험하지 않았습니다.
> 이 문서에 나오는 모델명(GPT-6 Astra, Claude Opus 5, Fable 5, Grok 4.6 등)은 2026년 하반기 원문에 적힌 그대로 옮긴 것입니다.

## 1. 가격·플랜 상세 (Quilter, Flux, DeepPCB, Circuit Mind, CELUS, Cadence, Siemens, Zuken, Altium/Renesas)

### Takeaway
공개 단가가 있는 곳은 DeepPCB 하나뿐입니다(시간당 $30부터, 원문 확인). Quilter는 "좌석이 아니라 프로젝트(미배선 핀 수) 단위 과금"이라는 구조만 공개하고 금액은 영업 견적입니다. 무료 티어는 10인 미만·매출 $50K 미만이 조건이고, 보드 메타데이터를 학습 퍼즐 생성에 씁니다(원문 확인). Flux는 플랜 이름(Explore/Build/Pro/Teams/Enterprise)과 약관은 원문으로 확인했습니다. 하지만 금액은 페이지에서 클라이언트 측으로 렌더링되어 확인하지 못했고, 체험 기간이 14일에서 7일로 줄었습니다. Circuit Mind, CELUS, Cadence, Siemens, Zuken은 공개 가격이 없습니다.

### Cited Findings

**Quilter: 가격 구조 (원문 확인으로 승격)**
- [원문 확인] 표어는 "Pay per Project. Not per Seat."입니다. 연간 라이선스가 없고, 프로젝트가 있을 때만 용량을 구매합니다. 보드 비용은 **업로드 시점의 미배선 핀 수**로 정해지며, RF 넷·팬아웃·고전압부처럼 미리 배선해 둔 핀은 과금하지 않습니다. 달러 금액은 공개하지 않고 "Talk to Sales"로 안내합니다. — [Quilter Pricing](https://www.quilter.ai/pricing)
- [원문 확인] 프로젝트마다 포함되는 것은 다음과 같습니다. 무제한 반복(대부분 팀이 프로젝트당 2–5회 반복한다고 기재), 병렬 작업(예: 6층과 4층 동시 실행), 첫 보드에 대한 가이드 온보딩(Quilter 엔지니어가 1.5시간 동안 업로드, "circuit comprehension report" 검토, 플로어플랜 설정을 함께 진행), 네이티브 ECAD 출력(Altium, Cadence Allegro, Siemens Xpedition, KiCad), BOM 10% 유연성입니다. BOM이 10% 넘게 바뀌면 새 프로젝트로 봅니다. 출력물 소유권은 사용자에게 있습니다. — [Quilter Pricing](https://www.quilter.ai/pricing)
- [원문 확인] 배포 방식은 두 가지입니다. Cloud는 AWS 위에서 운영하고 SOC 2 Type 2를 갖췄습니다. Self-hosted는 고객 쿠버네티스에 Helm 차트로 배포하며, NVIDIA GPU가 필요하고 기본 서비스만 수십 GB RAM을 씁니다. 에어갭(완전 폐쇄망) 운용도 가능합니다. Self-hosted는 "더 높은 비용과 추가 요금이 있을 수 있다"고 적혀 있습니다. — [Quilter Pricing](https://www.quilter.ai/pricing)
- [원문 확인] **무료 티어**("Always Free")는 무제한 반복과 전체 기능을 제공합니다. 허용 용도는 학술, 개인, "적격 전문가용(exploratory R&D)"이고, 자격 조건은 **10인 미만이면서 매출 $50K 미만**입니다. 배포 방식은 "Private data on public cloud"입니다. 이로써 이전 노트에 있던 자격 조건 충돌이 해소됩니다. — [Quilter Free](https://www.quilter.ai/free-ai-pcb-design)
- [원문 확인] **학습 데이터 조항:** 무료 티어 문구는 "Quilter uses your board's metadata (outline, component footprints, constraints) and/or input files to generate training puzzles that improve our design engine"입니다. Enterprise 문구는 "Designs are fully confidential and are never used for direct or indirect training purposes"입니다. — [Quilter Free](https://www.quilter.ai/free-ai-pcb-design)
- [원문 확인] Quilter는 스스로 범위를 이렇게 한정합니다. "Quilter is not an AI schematic generator, and it is limited in advanced simulation or circuit analysis functionality." 마케팅 문구로는 "Schematic to fab-ready in under 4 hours", "first candidates often appear within the first hour"를 씁니다. — [Quilter Free](https://www.quilter.ai/free-ai-pcb-design); [Quilter Pricing](https://www.quilter.ai/pricing)

**Flux: 플랜과 약관 (일부만 원문 확인)**
- [원문 확인] 플랜은 개인용 Explore, Build("BEST FOR MOST"), Pro와 조직용 Teams(편집자당 과금), Enterprise(맞춤 견적)입니다. Pro에는 "Hands-on guidance from EEs"가 붙습니다. Enterprise에는 숨김 워크스페이스, 강화된 보안, SLA(응답 2시간, 해소 24시간), 전담 매니저, 인보이스 결제가 들어갑니다. **금액 칸은 HTML에서 "—"로 나오고 JS로 채워지기 때문에 금액은 확인하지 못했습니다.** — [Flux Pricing](https://www.flux.ai/pricing)
- [원문 확인] FAQ 기준 약관은 다음과 같습니다. **신규 개인 플랜 체험은 7일**입니다(이전 노트의 "14일"은 과거 정보). Pro 체험을 시작하면 선택한 플랜·기간의 구독 전액만큼 카드에 승인 보류(authorization hold)를 겁니다. Teams는 체험 없이 바로 유료로 시작합니다. 체험이 끝나면 비공개 프로젝트 편집, 내보내기, AI 사용에 유료 플랜이 필요합니다. ACU(Agent Compute Unit)는 Agent 모드만 소모하고 Chat 모드는 소모하지 않으며, 매월 다시 채워집니다. — [Flux Pricing](https://www.flux.ai/pricing)
- [search-snippet, 상충] 2026년 8월 제3자 집계는 Teams를 편집자당 월 $158(연간 결제 시 $120), 편집자당 ACU 100개, 추가 ACU 개당 $2로 적습니다. Pro는 월 $200(연간 $142)로, 진입 플랜은 Explore 월 $20(연간 $16) 또는 "Starter $20"으로 엇갈립니다. 이전 노트의 "Pro $250/월, ACU 400개"와도 충돌합니다. 플랜 이름에 Build가 있다는 점은 원문과 맞지만 금액은 미확정입니다. — [ProtoFlow 블로그 (경쟁사 작성)](https://www.protoflow.ai/blog/flux-ai-pricing); [AnyGen](https://www.anygen.io/showcase/fluxai-review/index.html); [TrustRadius](https://www.trustradius.com/products/flux-ai/pricing)
- [원문 확인] Flux 사이트 내비게이션에 "Mechanical Design (MCAD)"와 "Enclosure design"이 있어, 제품 범위가 PCB에서 외함·기구까지 넓어졌습니다. [search-snippet] 2026년 9월 "PCB에서 프로토타입까지" AI 기능 출시 보도도 있습니다. — [Flux Pricing](https://www.flux.ai/pricing); [I-Connect007](https://iconnect007.com/article/151825/flux-launches-new-ai-capabilities-to-take-hardware-designs-from-pcb-to-prototype/151822/pcb)

**DeepPCB: 시간제 과금 (원문 확인으로 승격)**
- [원문 확인] 선불 시간권은 1시간 $30("For hobbyists"), 10시간 $280(약 5% 할인), 30시간 $800(약 10% 할인)이고 Enterprise는 별도 문의입니다. — [DeepPCB Pricing](https://deeppcb.ai/pricing/)
- [원문 확인] 한도는 다음과 같습니다.

  | 항목 | 무료 체험 | 종량제(PAYG) |
  |---|---|---|
  | 시간 | 최대 30분 | 필요한 만큼 |
  | 보드 수 | 1개 | 무제한 |
  | 층수 | 최대 4층 | 최대 8층 |
  | airwire | 최대 150개 | **최대 1,200개** |
  | 부품 | 최대 100개 | 최대 1,000개 |
  | 핀 | 최대 2,200개 | 최대 2,200개 |
  | Stop & Resume | 미포함 | 포함 |

  airwire 1,200개나 8층을 넘는 보드는 Enterprise(DeepPCB Pro)로 넘어갑니다. 페이지에는 "qualified professional의 검토가 필요하다"는 면책 문구가 있습니다. — [DeepPCB Pricing](https://deeppcb.ai/pricing/)
- [GitHub-verified] KiCad 플러그인은 Apache-2.0 오픈소스이고 KiCad 6.0 이상에서 동작합니다. 크레딧 기반이며 API 키가 필요하고, 중단된 작업을 이어서 할 수 있습니다(session restore). — [GitHub instadeepai/deeppcb-kicad-plugin](https://github.com/instadeepai/deeppcb-kicad-plugin)

**Circuit Mind / CELUS**
- [원문 확인] circuitmind.io/pricing은 404이고, 사이트에는 "Book a demo"만 있어 공개 가격이 없습니다. celus.io/pricing도 404입니다. — [Circuit Mind](https://www.circuitmind.io/); [CELUS](https://www.celus.io/)
- [search-snippet, unverified] 비교 사이트들은 Circuit Mind에 Individual/Professional/Enterprise 티어가 있다거나 프로젝트 복잡도에 따른 크레딧 구독이라고 적지만, 금액은 없고 벤더 원문으로 확인되지도 않습니다. CELUS는 "영업 견적"입니다. 주의: celus.net 가격 페이지는 동명의 다른 회사(출판 플랫폼)입니다. — [Agentaya](https://agentaya.com/ai-review/circuitmind/); [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/celus-alternative)

**Cadence (Allegro X AI / AuraStack)**
- [search-snippet] AuraStack AI Super Agent는 7월 발표 당시 "2026년 중 출시"로 소개되었습니다. 이후 Embedded 보도에 따르면 얼리 액세스 단계이고, 정식 공급은 2026년 8월 말에서 9월 초 무렵입니다. 가격과 라이선스는 미발표입니다. 고객 인용으로 FORVIA HELLA는 "부품 300개 배치가 최대 4일에서 4분으로" 줄었다고 했습니다(벤더 보도자료 인용). newsroom.cadence.com은 이번에 403이었습니다. — [Embedded](https://www.embedded.com/cadence-develops-agentic-ai-platform-for-pcb-design/); [Fierce Sensors](https://www.fiercesensors.com/ai/cadence-aurastack-debuts-boost-pcb-and-packaging-designers); [Nasdaq (보도자료)](https://www.nasdaq.com/press-release/cadence-introduces-aurastack-ai-super-agent-worlds-first-agentic-ai-platform-pcb-and)

**Siemens (신규 정보)**
- [search-snippet] **Fuse EDA AI Agent**가 2026-03-16에 출시되었습니다. Siemens EDA 전 포트폴리오에서 멀티 에이전트 워크플로를 조율하고, PCB 쪽에서는 Xpedition과 HyperLynx의 레이아웃·신호무결성(SI) 작업을 지원합니다. Fuse EDA AI 시스템은 RAG, MCP, Agent Skills를 지원하고 NVIDIA Nemotron 및 Agent Toolkit과 연동됩니다. "1000배, 생산성 50배" 같은 수치는 검증되지 않았습니다. 가격은 비공개입니다. — [Siemens 보도자료](https://news.siemens.com/en-us/siemens-fuse-eda-ai-agent/); [I-Connect007](https://iconnect007.com/article/149238/siemens-launches-fuse-eda-ai-agent-for-chip-and-pcb-workflows/149235/ein); [Fierce Sensors](https://www.fiercesensors.com/ai/siemens-boosts-its-eda-nvidia-ai-tools-and-hardware-agentic-engineering-pcbssemis)

**Zuken CR-8000 2026 (원문 확인으로 승격)**
- [원문 확인] 보도자료는 2026-10-20(Westford, Munich)에 나왔고 "available now"입니다. 주요 기능은 다음과 같습니다.
  - Design Gateway의 회로도 자동 배선
  - Design Force의 Main Path View: 주요 디바이스 간 연결만 강조하고 디스크리트 연결은 숨기며, 연결 거리 제약과 전원 연결만 따로 보여 줄 수 있습니다.
  - AI-PR 기반 Smart Design Reuse: 과거 프로젝트의 배치를 검색·비교해 적용합니다.
  - **Dynamic Brain**: 배치 지식을 로컬 AI-PR 서버로 공유하며 "데이터는 클라우드가 아닌 고객 네트워크 안에" 둡니다.
  - 고핀수 디바이스용 팬아웃 기능

  가격과 정량적 단축률은 공개하지 않았습니다. — [Zuken 보도자료](https://www.zuken.com/en/resource/cr-8000-2026-pcb-design-automation/)

**Altium / Renesas**
- [search-snippet] **Renesas의 Altium 인수는 2024-08-01에 완료**되었습니다. 주당 AUD 68.50, 지분가치 약 AUD 9.1B(약 US$5.9B)이며 Altium은 Renesas의 완전자회사가 되었습니다. — [Altium 보도자료](https://www.altium.com/company/newsroom/press-releases/renesas-completes-acquisition-altium); [TechPowerUp](https://www.techpowerup.com/325134/renesas-completes-acquisition-of-altium-for-usd-5-9bn); [EE Times](https://www.eetimes.com/reneses-completes-altium-acquisition/)
- [search-snippet] 2026년 Altium의 AI 기능은 **Agentic Requirements Engineering**(2026-10-14 출시)입니다. Requirements Portal 안에서 AI 에이전트가 변경을 제안하고 엔지니어가 승인하는 방식이며, Engineering Assistant와 재사용 가능한 "AI Skills"로 구성됩니다. Altium Develop과 Agile Teams 구독에 포함됩니다. **레이아웃이나 배선 AI는 아닙니다.** 공식 MCP 서버(Altium Designer용, Altium 365용)는 2026-11-02 기준 "Coming Soon"이라는 제3자 확인만 있습니다. — [Altium 문서](https://www.altium.com/documentation/altium-365/requirements-portal/agentic-requirements-engineering); [Altium Resources](https://resources.altium.com/p/introducing-agentic-requirements-engineering); [JLCPCB 블로그](https://jlcpcb.com/blog/altium-mcp-how-to-design-a-real-pcb-with-gpt-6-and-codex)
- [search-snippet, 상충] Renesas 365 "Powered by Altium"의 출시 시점은 이전 노트에서 2026년 3월 GA로 적었습니다. 그런데 Renesas 블로그 스니펫은 2026-04-28로 표기합니다. — [Renesas 블로그](https://www.renesas.com/en/blogs/renesas-365-powered-altium-first-implementation-renesas-digitalization-vision)

### Inferences
- 과금 모델은 네 가지로 갈립니다. (a) 프로젝트·핀 단위(Quilter), (b) 연산 시간 크레딧(DeepPCB), (c) 좌석 + 에이전트 크레딧(Flux), (d) 엔터프라이즈 견적(Circuit Mind, CELUS, Cadence, Siemens, Zuken)입니다. 모디팩토리가 "무료 → 구독"으로 갈 때 Quilter식 "프로젝트당 무제한 반복"은 초보자에게 이해하기 쉬운 비교 기준이 됩니다.
- Quilter 무료 티어는 학습에 데이터를 쓰고, Zuken은 "데이터를 고객 네트워크 안에" 두며, Konnect-EDA는 "아무것도 전송하지 않음"(4장)을 내세웁니다. 이처럼 **데이터 정책이 마케팅 포인트가 되었습니다.** 모디팩토리도 무료 사용자 데이터를 학습에 쓰는지 명시해야 신뢰를 얻을 수 있습니다.

### Gaps
- Flux 플랜별 실제 금액은 원문(JS 렌더링)에서 확인하지 못했고 제3자 수치끼리도 충돌합니다.
- Quilter 핀당 단가, DeepPCB Enterprise 가격, Cadence·Siemens·Zuken AI 옵션 가격은 공개 자료가 없습니다.
- Circuit Mind의 티어 구조는 벤더 원문으로 확인하지 못했습니다.

## 2. 첫 시도 성공률·품질 증거 (독립 벤치마크, 제3자 평가)

### Takeaway
**독립적이고 통제된 레이아웃 벤치마크는 2026년 11월 현재도 찾지 못했습니다.** 숫자가 있는 비교는 모두 벤더가 썼습니다. DeepPCB가 Quilter와 Freerouting을 비교했고, Quilter는 내부 벤치마크를 썼으며, Cadence는 고객 인용을 씁니다. 다만 DeepPCB의 Quilter 비교는 공개 보드 3종으로 재현할 수 있게 설계되어 있습니다. 회로(비레이아웃) 쪽에는 EEBench(atopile 팀)라는 결정론적 SPICE 기반 공개 벤치마크가 생겼지만 레이아웃은 다루지 않습니다.

### Cited Findings
- [원문 확인, 벤더 작성: DeepPCB] **DeepPCB vs Quilter**(2026-04-20): 공개된 오픈소스 KiCad 보드 3종을 두 툴의 공개 버전으로 "수동 개입 없이" 배선한 결과입니다.

  | 보드 | airwire | 완료율 DeepPCB / Quilter | via DeepPCB / Quilter |
  |---|---|---|---|
  | STRF | 98 | 99% / 94% | 29 / 58 |
  | PocketBeagle | 290 | 96% / 82% | 135 / 163 |
  | BeagleConnect Freedom | 414 | 97% / 87% | 191 / 235 |

  평균 완료율은 97.3% 대 87.7%입니다. 첫 결과까지 1–2분 대 15–20분이고, 제약 추출은 "자동 대 수동", 출력 포맷 수는 "6 대 2"라고 주장합니다. 이 글은 Quilter의 2026년 3월 비교글이 방법론과 보드를 공개하지 않은 "internal benchmarks"라고 비판합니다. — [DeepPCB 블로그](https://deeppcb.ai/deeppcb-vs-quilter-open-source-routing-compared-2026/); [Quilter 블로그 (벤더 작성)](https://www.quilter.ai/blog/the-2026-guide-to-autonomous-pcb-design-quilter-vs-deeppcb-vs-flux-ai)
  - 주의: 이 비교는 Quilter의 강점인 자동 배치와 물리 검토는 평가하지 않고 "배선 완료율"만 봅니다. [search-snippet] 같은 수치를 쓴 제3자 글(idostudio)도 데이터를 재사용했을 뿐 독립적으로 재현한 것으로 보이지 않습니다. — [idostudio](https://idostudio.ai/insight/2026-09-11-deeppcb-vs-quilter-what-ai-autorouters-do-to-your-ground-plane); [StationX](https://app.stationx.net/articles/ai-pcb-design)
- [원문 확인, 벤더 작성: DeepPCB] **Freerouting vs DeepPCB**(2026-10-14): DeepPCB는 "KiCad 보드 중앙값 완료율 96.9%, KiCad 보드의 95.6%가 95% 이상 완료"를 주장하고, Freerouting은 "복잡 보드에서 60–75%"라고 씁니다. 100-airwire 4층 보드 기준 작업 시간을 Freerouting 3–5시간, DeepPCB 30–45분으로 제시합니다. 데이터셋과 방법론은 공개하지 않았습니다. — [DeepPCB 블로그](https://deeppcb.ai/freerouting-vs-deeppcb/)
- [원문 확인, 벤더 작성: DeepPCB] **GPT-6 Astra 결과물 재배선**(2026-09-06): Astra가 "원샷"으로 만든 Microduck 보드(70×60mm, 4층, 27넷)를 DeepPCB가 분석했습니다.
  - Astra 결과에는 트랙 폭이 5종(0.2–1.5mm) 쓰였는데 넷클래스는 기본값 1개뿐이고 비어 있어, 폭 4종은 DRC로 검증할 수 없습니다.
  - via 32개 중 9개가 패드 안에 있습니다(via-in-pad라서 충전·캡핑 공정이 필요).
  - DeepPCB로 다시 배선한 결과는 연결 132/132, 층 전환 via 14개, 트랙 길이 1,104mm(Astra 1,282mm)이고 15분이 걸렸습니다.

  글은 "추론 실패가 아니라 라우팅 숙련의 문제"라고 결론짓습니다. — [DeepPCB 블로그](https://deeppcb.ai/gpt-6-astra-pcb-routing-deeppcb/)
- [원문 확인, 코드 기반 경쟁사 작성: atopile 팀] **EEBench V1**(2026-09-04 블로그): 13개 과제를 결정론적 SPICE 시뮬레이션과 설계 체크로 채점하고, 공차 코너와 실제 부품 사양, BOM 비용 효율까지 반영합니다.
  - 9월 1일 리더보드: Claude Opus 5 61.6%, Grok 4.6 57.1%, Claude Fable 5.1 56.4%, Claude Fable 5 54.3%, Claude Opus 4.8 Max 51.4%
  - xAI는 Grok 4.6 모델 카드에 EEBench 60.0%(xhigh)를 실었습니다.
  - 실패 사례: 공칭 22µF 커패시터가 4.7V 바이어스에서 실효 11.4µF로 떨어졌고, 요구치는 545µF였습니다. 빌드는 성공했지만 회로는 실패한 경우입니다.
  - **레이아웃, 제조, 브링업은 평가하지 않는다**고 명시합니다.

  — [EEBench 블로그](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)
- [search-snippet, 벤더 보도자료] Cadence AuraStack 고객 인용: FORVIA HELLA는 부품 300개 배치가 최대 4일에서 4분으로 줄었다고 했습니다. — [Fierce Sensors](https://www.fiercesensors.com/ai/cadence-aurastack-debuts-boost-pcb-and-packaging-designers)
- [search-snippet] 과거 독립 평가: EEVblog 1535(2023)에서 Dave Jones는 DeepPCB를 테스트하고 "TLDR; It sucks. Humans for the win."이라고 평했습니다(24시간 안에 배선 미완료). 3년 전 결과라 현재 제품에 그대로 적용할 수는 없습니다. — [EEVblog 1535](https://www.eevblog.com/2023/04/06/eevblog-1535-deeppcb-ai-autorouting-fail/); [EEVblog 포럼](https://www.eevblog.com/forum/blog/eevblog-1535-deeppcb-ai-autorouting-tested!/)
- [GitHub-verified] MCP 도구의 신뢰성을 보여 주는 단서: mixelpixx/KiCAD-MCP-Server v2.9.0 변경 기록에 "실제 333-pad 보드에서 304개 패드가 잘못된 넷을 갖고 있었다(sync_schematic_to_board 수정 전)"는 버그 수정이 있습니다. "KiCad가 저장할 때 via를 다른 넷으로 옮길 수 있는데 DRC가 이를 잡지 못한다"는 이유로 `audit_via_nets`도 추가했습니다. — [GitHub mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)

### Inferences
- "완료율"만으로는 품질을 비교할 수 없습니다. DeepPCB도 Astra 비판에서 넷클래스 미선언과 via-in-pad 같은 **설계 의도의 규칙화 여부**를 품질 기준으로 씁니다. 모디팩토리의 "AI 노트(설계 근거)"를 서술형 설명에 그치지 않고 넷클래스, 폭, 클리어런스 같은 검증 가능한 규칙으로 함께 출력하면, 업계 비판 포인트에 정면으로 대응할 수 있습니다.
- 공개 보드 3종(STRF, PocketBeagle, BeagleConnect Freedom)으로 이미 재현 가능한 비교 틀이 존재합니다. 모디팩토리가 같은 보드로 완료율, via 수, 소요 시간을 공개하면 저비용으로 신뢰를 얻을 수 있는 선택지가 됩니다.

### Gaps
- Quilter, DeepPCB, Flux 자동 레이아웃, Cadence AI 배치를 같은 조건에서 비교한 **독립(비벤더) 벤치마크**는 찾지 못했습니다.
- Quilter의 2026년 3월 "internal benchmarks" 수치 자체는 원문으로 확인하지 않았습니다.
- 학회 발표(DesignCon, PCB West 등)의 제3자 평가 자료는 이번에 찾지 못했습니다.

## 3. 실사용자 평판 (Hacker News, Reddit, EEVblog, KiCad 포럼)

### Takeaway
실무 엔지니어들은 AI를 **라이브러리 정리, BOM, 풋프린트 확인, 설계 리뷰** 용도로는 쓸모 있다고 보지만, **레이아웃, 특히 부품 배치는 아직 신뢰하지 않는다**는 쪽이 지배적입니다. 단순한 취미 보드(RP2040, ESP32급)는 범용 LLM과 KiCad MCP 조합으로 실제 제작과 동작까지 성공한 사례가 늘었습니다. Flux는 HN에서 "토큰만 태우고 결과가 없다"는 비용 불만이 반복되고, 2026년 6월 Adafruit와의 법적 분쟁으로 평판 리스크가 생겼습니다. Reddit은 이번 세션에서 접근하지 못했습니다.

### Cited Findings

**Hacker News: "Can AI design circuit boards yet?"** (2026-09-04, 422점, EEBench 글) [원문 확인, HN Algolia API]
- "Routing is the easiest part of layout... the difficult task is in placing components, and adjusting those placements." (nickff) — [HN](https://news.ycombinator.com/item?id=49569550)
- "AI is great for sorting out your libraries, drawing and helping double check footprints managing your BOM. I still draw my schematics and layout my boards... There are too many stupid errors it makes. I do get it to review my work though and often it catches things I have missed." (dubbie99) — [HN](https://news.ycombinator.com/item?id=49569601)
- 단순 회로의 회로도는 대체로 괜찮지만 디커플링 커패시터를 과하게 넣는 경향이 있고, "PCB layout has basically been terrible every time I've tried it". (rpcope1) — [HN](https://news.ycombinator.com/item?id=49569618)
- "it's consistently been a spectacular fail each time in actually designing the board". (cmiles8) — [HN](https://news.ycombinator.com/item?id=49569652)
- 긍정 사례: KiCAD MCP Server와 Codex로 만든 플렉스 PCB가 JLC와 PCBWay DRC를 통과했습니다(itomato). JLCPCB 설정으로 DRC 통과, 주문, 제작, 사용까지 성공했지만 "ridiculously simple" 취미 보드였다는 사례도 있습니다(thearn4). — [HN](https://news.ycombinator.com/item?id=49569752); [HN](https://news.ycombinator.com/item?id=49569871)
- LLM은 텍스트(넷리스트) 기반인 회로도 캡처에는 강하지만 PCB 배선에서 무너지며, 6층 이상 보드에서는 성공하지 못했다는 의견(akiselev)이 있습니다. 반면 단순한 RP2040 보드를 LLM이 Python으로 배선해 첫 시도에 동작했다는 반론(mapontosevenths)도 있습니다. — [HN](https://news.ycombinator.com/item?id=49571739); [HN](https://news.ycombinator.com/item?id=49571840)

**Hacker News: "This PCB is brought to you by Fable 5"** (2026-09-14, 160점) [원문 확인]
- 정밀 아날로그 설계자의 평: 모델이 특수 전자회로에 대한 통찰은 주지만 "they can hardly put that knowledge to work if instructed to generate a schematic or lay out a PCB." (XRG) — [HN](https://news.ycombinator.com/item?id=49698275)
- "AI is indeed raising the floor"라고 하면서도, 경험이 없으면 "단순 회로"의 경계를 모르고 넘기 쉽다는 경고(Cyan488)가 있습니다. — [HN](https://news.ycombinator.com/item?id=49696205)
- 비용 데이터: 조립 완제품 5장에 €130(디스플레이 별도), JLCPCB 5장 조립 $175에 배송·관세·세금 약 $100 추가. — [HN](https://news.ycombinator.com/item?id=49695833); [HN](https://news.ycombinator.com/item?id=49698808)

**Hacker News: Flux 관련** [원문 확인] (2026-06-02, Adafruit–Flux 분쟁 스레드 안의 댓글이라 선택 편향 가능성 있음)
- "After about 50-100$ in tokens a couple of times, I couldn't get more than a couple of simple components on the schematic... The product just grinds tokens for little return... I had far better luck wiring together KiCad MCP, SKIDL... Placement is probably the big issue." (karmicthreat) — [HN](https://news.ycombinator.com/item?id=48368721)
- "they got $140 out of me before I realized what it was (not) capable of. Their support was nonexistent." (StephenSmith) — [HN](https://news.ycombinator.com/item?id=48368798)
- "i gave them a $100~ bucks and i got like nothing" (taf2) — [HN](https://news.ycombinator.com/item?id=48370685)
- [search-snippet, 벤더 작성: Quilter] Quilter 블로그는 Flux에 대해 Reddit에 결제·해지 관련 강한 부정 경험담이 있다고 씁니다(경쟁사 주장). — [Quilter 블로그](https://www.quilter.ai/blog/the-ai-pcb-tool-landscape-in-2026-from-hobbyist-co-pilots-to-professional-automation)

**Adafruit–Flux.ai 법적 분쟁 (신뢰·보안 이슈)**
- [search-snippet] Adafruit는 Flux.ai(법인명 Defy Gravity, Inc.)를 대리한 Fenwick & West로부터 2026-05-22자 demand letter를 받았고, 블로그 게시를 중단했습니다. 여러 보도는 이를 Adafruit가 Flux 서버 설정 오류를 책임 있게 공개(responsible disclosure)하려던 건으로 설명합니다. 서한은 CFAA 위반과 명예훼손을 주장한 것으로 보도되었습니다. 해결 여부는 확인하지 못했습니다. — [Slashdot](https://yro.slashdot.org/story/26/06/02/1647209/adafruit-pauses-blog-after-demand-letter-from-fluxais-lawyers); [ascii.co.uk](https://ascii.co.uk/news/article/news-20260603-6eac5d5f/adafruit-halts-publication-after-legal-threat-over-flux-secu); [Threads @adafruit](https://www.threads.com/@adafruit/post/DZFAAjtlq3W/adafruit-receives-demand-letter-from-fenwick-legal-counsel-on-behalf-of-defy/)
- [원문 확인] HN 스레드 "Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai"는 2026-06-02에 684점을 받았습니다. 이후 2026-06-10 "Adafruit vs. Flux [pdf]" 스레드에서 Adafruit가 소장(complaint) 링크를 공개했다는 댓글이 있습니다(소장 원문은 adafruit.com 403으로 미확인). — [HN 48368121](https://news.ycombinator.com/item?id=48368121); [HN 댓글](https://news.ycombinator.com/item?id=48475147)

**Hacker News: Copperhead와 시장 인식** [원문 확인]
- "The space is definitely heating up. Flux.ai being the incumbent, Silixon based out of the UK have been showing demos, Quilter and DeepPCB for layout, The recent OpenAI demo... my experience of hardware engineers is very gatekeepy." (mikeayles) — [HN](https://news.ycombinator.com/item?id=49610503)
- "Autorouters with auto layout have been around in many forms for years. Their output never compares to a skilled EE doing it manually." (Aurornis) — [HN](https://news.ycombinator.com/item?id=49611479)
- "I used claude and gemini to edit/debug kicad schematics. And it was pretty good. What is the point of this agent?" (tadasv). 범용 LLM이 전용 도구를 대체할 수 있다는 인식입니다. — [HN](https://news.ycombinator.com/item?id=49610368)
- [search-snippet] Quilter Speedrun 보도(Slashdot, HN 미러)에 대해 "기존 회로도로부터 배선한 것이지 컴퓨터를 '설계'한 것은 아니다"라는 반론 댓글이 있었습니다. — [Slashdot](https://hardware.slashdot.org/story/25/12/16/229209/dual-pcb-linux-computer-with-843-components-designed-by-ai-boots-on-first-attempt)

**EEVblog 포럼 "AI PCB layout"** (2026년 1–6월, 조회 7,786) [원문 확인]
- "so far i haven't really seen anything that was properly good. Seen some online platforms that claim they can do electronics design work with AI... It was mostly just feeding netlists trough a general purpose LLM" (Berni) — [EEVblog](https://www.eevblog.com/forum/chat/ai-pcb-layout/)
- "So... autorouter? ... utilizing neural networks is exactly the right direction to go into to make already quite decent autorouters even better" (Siwastaja) — [EEVblog](https://www.eevblog.com/forum/chat/ai-pcb-layout/)
- "LLMs (or anything else we have now) won't get us anywhere close to full AI Layout... 'here's a schematic, let me know when the layout is done' is still fantasy." 설계 의도 전달, 기구 엔지니어와의 커넥터·마운팅 협업이 핵심이라는 지적입니다. (Smokey) — [EEVblog](https://www.eevblog.com/forum/chat/ai-pcb-layout/)
- Flux 공개 프로젝트(10층 BGA 팬아웃)를 비꼬는 댓글(hans)이 있습니다. ProtoFlow를 칭찬한 글은 게시물 1개짜리 신규 계정이라 홍보성일 가능성이 있습니다(xplanate). — [EEVblog](https://www.eevblog.com/forum/chat/ai-pcb-layout/)

**KiCad 포럼 "Open AI claims GPT 6 - ASTRA can make pcb boards"** (2026-09-04~, 게시물 37개) [원문 확인, Discourse JSON]
- "Moderately good at PCB design but its still very bad with high frequency signals" (Bezalelohim) — [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/3)
- 학습 데이터가 주로 오픈 하드웨어라 취미용으로 편향되어 있고, 고품질 전문 PCB는 사유 자산이라는 지적(jrbloom), "무엇이 틀렸는지"를 보여 주는 예시가 거의 없다는 지적(Naib)이 있습니다. — [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/8); [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/9)
- "PCB component placement is the hard problem and for that you have to understand the circuit." (davidsrsb), "AI operating a 60 year old technology is mostly entertainment." (Heath_Raftery) — [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/15); [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/16)

**Reddit**
- 접근하지 못했습니다. WebSearch는 reddit.com 도메인 필터를 거부했고, curl은 403이었습니다. r/PrintedCircuitBoard, r/KiCad, r/AskElectronics, r/ECE의 직접 인용은 확보하지 못했습니다.

### Inferences
- 반복되는 불만은 다섯 가지입니다. (1) 배치를 신뢰할 수 없음, (2) 고속·RF·BGA·HDI 취약, (3) 토큰·크레딧 과금 대비 결과 부족(Flux), (4) "AI가 설계했다"는 과장 마케팅(Speedrun, Astra), (5) 학습 데이터 편향과 데이터 정책 불신입니다. 반대로 칭찬받는 지점은 리뷰·검증 보조와 단순 보드의 빠른 시제품화입니다.
- 모디팩토리의 초보자 타깃 관점에서 보면, 초보자가 만드는 단순 보드는 이미 범용 LLM(Claude, GPT, Codex)과 KiCad MCP 조합으로도 일부 가능해졌습니다. 따라서 차별점은 "되는 것" 자체보다 **결과 신뢰성(DRC/규칙 명시), 예측 가능한 비용(Flux식 토큰 소모 불만의 반대), 투명한 데이터 정책**에서 나와야 할 가능성이 큽니다(추론).
- 전문가 커뮤니티(EEVblog, KiCad 포럼)는 "AI 레이아웃"이라는 표현 자체에 회의적입니다. 모디팩토리가 해외 전문가층에 진입하려면 마케팅 용어를 과장하지 않는 것이 중요합니다(추론).

### Gaps
- Reddit 직접 인용을 확보하지 못했습니다(접근 차단).
- Quilter와 Circuit Mind 실사용자의 1인칭 후기는 공개 포럼에서 거의 찾지 못했습니다. 기업 고객 위주라 공개 후기가 적은 것으로 보입니다.
- Adafruit–Flux 분쟁의 결말(소송 제기, 합의)과 소장 내용은 확인하지 못했습니다.

## 4. GitHub로 검증한 오픈소스·코드 기반 경쟁자 상세

### Takeaway
오픈소스 쪽에서 실사용에 가장 가까운 조합은 **KiCad + KiCAD-MCP-Server(257개 도구, Freerouting·JLCPCB 연동) + Freerouting(공개 API, MCP)**입니다. 다만 Freerouting은 메인테이너가 주 4시간만 투입하는 체제이고, tscircuit의 자동 배치는 아직 "개발 중"입니다. atopile과 Diode는 배치·배선을 KiCad에 맡깁니다. 오픈소스 MCP 진영에서는 폐쇄형 상용판(Konnect-EDA)으로 넘어가는 흐름이 나타났습니다.

### Cited Findings
- **Freerouting** [GitHub-verified]
  - 메인테이너는 2020년 1월부터 유지보수를 맡아 왔고, 이제 프로젝트에 **주 4시간 정도**만 쓰겠다고 밝혔습니다.
  - Silver/Gold 후원자의 이슈를 우선 처리하고, 신규 API 키는 주 1회 수동 검토 후 승인하며, 정식 릴리스는 2–3개월에 한 번 정도입니다.
  - API 루트는 `https://api.freerouting.app/v1`(베타, 변경될 수 있음)이고 공식 Python SDK는 `pip install freerouting-client`입니다. Docker(ghcr.io, `latest`/`nightly` 태그)나 JRE로 셀프호스팅할 수 있습니다.
  - MCP는 `npx -y @freerouting/freerouting-mcp-server`로 쓸 수 있고 Cursor, Cline, Claude Desktop용입니다. Java JRE 25가 권장되며, 배선에는 "수 분에서 수 시간"이 걸립니다.

  — [GitHub freerouting/freerouting](https://github.com/freerouting/freerouting)
- **mixelpixx/KiCAD-MCP-Server (v2.9.0)** [GitHub-verified]
  - MIT 라이선스이고 활발히 유지보수됩니다. 20개 카테고리에 **도구 257개**가 있고, 회로도용 도구 65개, 심볼 약 1만 개, 동적 리소스 23개를 제공합니다.
  - 툴박스 모드로 핵심 37개 도구만 먼저 불러올 수 있습니다. VS Code Copilot이 도구를 128개까지만 받기 때문입니다.
  - Freerouting 연동(Java, Docker, Podman)을 지원합니다. JLCPCB 부품 카탈로그 250만 개 이상의 가격·재고를 조회하고, LCSC 데이터시트로 정보를 보강합니다.
  - MCP 2025-06-18 사양을 따르며 KiCad 9/10을 지원합니다. IPC 백엔드는 실험 단계입니다.
  - v2.9.0 신규 기능: `readonly`/`manufacturing` 운영 모드(리뷰 에이전트용), 층·넷 단위 오토라우팅, `get_stackup`, `audit_via_nets`, `set_voltage_clearance_rules`
  - 세션 로그에 전체 도구 호출 이력이 남는다는 프라이버시 경고가 있습니다.

  — [GitHub mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)
- **Konnect-EDA (Orchis.ai, 위 프로젝트의 후속 상용판)** [GitHub-verified, README 기재 내용]: 폐쇄 소스이고 KiCad 10 네이티브 플러그인(단일 Rust 바이너리)입니다. IPC API와 kicad-cli를 쓰며, 21개 툴셋에 도구 228개를 담고 Claude와 Codex용 스킬을 번들로 제공합니다. 학생, 취미, 개인 개발자는 1.0 이후에도 무료이고 기업은 1.0부터 상용 라이선스가 필요합니다. "Orchis.ai로 아무것도 보내지 않는다"고 명시합니다. — [GitHub mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server); [GitHub Orchis-ai-LLC/Konnect-EDA](https://github.com/Orchis-ai-LLC/Konnect-EDA)
- **tscircuit** [GitHub-verified]
  - TypeScript/React로 회로도, PCB, 3D, 제조 파일을 만듭니다.
  - 자동 배치는 README에 "PCB용 'flex'·'CSS Grid' 오토레이아웃 알고리즘을 만드는 중"이라고 되어 있어 **아직 개발 중**입니다.
  - 오토라우터는 내장 `@tscircuit/capacity-autorouter`(MIT)입니다. 수백 개 알고리즘을 파이프라인으로 묶고 순차 배선 대신 연속 근사와 하이퍼그래프 방식을 씁니다. 온라인 플레이그라운드와 버그 리포트 워크플로를 갖췄습니다.
  - 텍스트→풋프린트 AI 도구와 llms.txt를 제공합니다.

  — [GitHub tscircuit/tscircuit](https://github.com/tscircuit/tscircuit); [GitHub tscircuit/capacity-autorouter](https://github.com/tscircuit/capacity-autorouter)
- **atopile** [GitHub-verified]
  - MIT 라이선스이고 VS Code/Cursor 확장으로 설치합니다.
  - `.ato` 선언형 언어로 단위, 공차, assertion을 표현하고, 컴파일러가 제약을 풀어 부품을 고르고 체크를 돌린 뒤 KiCad 레이아웃을 갱신합니다.
  - 워크플로에서 레이아웃은 "place and route in KiCad"로, **자동 배치·배선은 없습니다.**
  - 예제로 NONOS(스마트 스피커), DSP, "AI-Pin — Vibe-coded Humane Pin"이 있습니다.
  - [search-snippet, unverified] HN 댓글에 "6개월 전 공개 오픈소스 작업이 멈추고 브라우저 IDE로 피벗했다"는 주장이 있으나 README는 활성 상태처럼 보입니다. API 차단으로 최근 커밋 날짜는 확인하지 못했습니다. 2026-09 EEBench 글이 "ato v2"와 atopile 내부 제약 솔버를 쓰고 있어 개발은 이어지는 것으로 보입니다.

  — [GitHub atopile/atopile](https://github.com/atopile/atopile); [HN Show HN: Atopile (검색 결과로 나온 스레드이며 해당 댓글 위치는 미확인)](https://news.ycombinator.com/item?id=39263854); [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)
- **Diode `pcb` (Zener)** [GitHub-verified]: Starlark 기반 Zener 언어를 쓰고 `pcb build`, `pcb layout`으로 KiCad 레이아웃 파일을 생성합니다. 레이아웃에는 KiCad 10.x가 필요하고, 네이티브 Windows는 실험 단계라 WSL2를 권장합니다. Rust로 구현되었고 MIT 라이선스입니다. README는 atopile과 tscircuit에서 영감을 받았다고 밝힙니다. — [GitHub diodeinc/pcb](https://github.com/diodeinc/pcb)
- **DeepPCB KiCad 플러그인** [GitHub-verified]: Apache-2.0, KiCad 6.0 이상, 크레딧 기반입니다. [원문 확인, 벤더] 2026년 5월 첫 출시 후 2026-10-13 v1.2.0에서 설정 보조 에이전트 "Cooper"가 KiCad 패널로 들어왔습니다. Cooper는 넷클래스, 차동쌍, 플레인, 스택업을 읽고 설정 변경을 제안하며, 사용자가 변경마다 승인하거나 거절합니다. 배선 결과는 KiCad undo 스택에 한 항목으로 들어옵니다. — [GitHub instadeepai/deeppcb-kicad-plugin](https://github.com/instadeepai/deeppcb-kicad-plugin); [DeepPCB 블로그](https://deeppcb.ai/cooper-kicad-plugin/)

### Inferences
- 오픈소스 MCP 도구는 이미 수백 개 수준이라 "AI가 KiCad를 조작한다"는 기능 자체는 범용화(commodity)되었습니다. 모디팩토리의 방어선은 도구 개수가 아니라 자동 배치 품질과 검증 가능한 근거입니다.
- Freerouting은 운영 인력이 매우 적고 API 키도 수동 승인이므로, 상용 서비스가 백엔드로 의존하기에는 공급 리스크가 있습니다(셀프호스팅으로 완화할 수 있음).
- DeepPCB Cooper는 "AI가 설정을 읽고 제안하면 사람이 승인하는" UX를 내세웁니다. 모디팩토리의 "AI 노트"와 가장 가까운 해외 기능이므로 직접 비교할 대상입니다(추론).

### Gaps
- api.github.com이 이 세션에서 막혀 스타 수, 최신 릴리스, 마지막 커밋 날짜를 갱신하지 못했습니다(이전 노트 수치 유지).
- JITX의 공개 저장소(있다면)와 Diode의 추가 오픈 저장소는 확인하지 못했습니다.

## 5. 한국: 세카(SECA) 검증과 2026년 신규 국내 진입자

### Takeaway
세카의 핵심 사실(LG전자 사내벤처 출신, 2026년 6월 독립법인, LG전자·블루포인트 시드, 블루포인트 추천으로 TIPS 선정, PoC 공수 66% 절감, 매출 7억원)은 뉴스 원문으로 확인했습니다. 다만 **세카의 제품은 PCB 레이아웃 도구가 아니라** 설계 문서 연결·검증과 부품 선정 자동화이며, 다음 단계로 아날로그 회로와 넷리스트·배치·배선을 이해하는 파운데이션 모델을 개발합니다. 2026년 국내에서 AI PCB 레이아웃에 새로 진입한 다른 기업은 찾지 못했습니다.

### Cited Findings
- [원문 확인] 뉴스탭 2026-11-16 기사의 확인 사항은 다음과 같습니다.
  - **출신과 투자:** LG전자 사내벤처에서 출발해 2026년 6월 독립법인으로 출범했고, LG전자와 블루포인트파트너스에서 시드투자를 받았습니다. 블루포인트 추천으로 TIPS에 선정되었습니다(16일 발표).
  - **대상 산업:** 자동차, 반도체, 로보틱스
  - **제품 범위:** 고객 요구사항, BOM, 데이터시트, 회로도에 흩어진 설계 정보를 AI로 연결하고, 부품 선정부터 회로 검증까지 반복 업무를 자동화합니다.
  - **PoC 성과(회사 발표):** 국내 대형 제조기업 PoC에서 엔지니어링 공수를 66% 줄였습니다. 같은 업무에서 경쟁 솔루션은 25%였고, 엔지니어 만족 비율은 80%였습니다.
  - **매출:** 독립 후 7억원이며, 국내외 제조기업과 반도체 설계기업 대상 유료 프로젝트를 진행 중입니다.
  - **다음 단계:** 아날로그 회로 설계 자동화. 넷리스트와 실제 배치·배선 정보를 함께 이해하는 설계 특화 파운데이션 모델을 개발합니다. 글로벌 EDA 기업과 국내 반도체 대기업 출신 인력을 확보했고, UT Austin과 공동연구 중입니다.
  - **해외:** 2026년 7월 상하이 WAIC 한국 혁신관(KIC중국)에 참가했고, 중국 완성차·팹리스와 기회를 모색 중입니다. 미국에서는 글로벌 반도체 기업과 과제를 하고 있고, 유럽 완성차와 PoC를 논의 중입니다.
  - **사업 모델:** 연간 소프트웨어 라이선스 기반 반복 매출로 전환할 계획입니다.
  - **대표:** 김준형. 2030년 매출 1000억원이 목표입니다.

  — [뉴스탭](https://www.newstap.co.kr/news/articleView.html?idxno=337854)
- [원문 확인, 메타 설명만] 유니콘팩토리 기사(2026-11-16)도 "AI 기반 설계 자동화 스타트업 세카가 TIPS에 선정"되었다고 확인합니다. — [유니콘팩토리](https://www.unicornfactory.co.kr/article/2026111610165217978)
- [search-snippet] 다른 보도에서는 "설계 문서 검토 시간이 건당 약 6시간에서 약 24분으로 92% 단축"되었다고 합니다. 66%와는 측정 대상이 다른 수치로 보입니다. 검색 요약이 어느 기사인지 특정하지 않았으며, 이전 노트에 적힌 서플·네이트뉴스 보도로 추정됩니다. 스튜디오341은 팀당 최대 4억원 초기 투자를 계획했습니다. — [서플](https://supple.kr/news/cmwizgtsng6uz10eg6f9w6s71); [네이트뉴스](https://m.news.nate.com/view/20261105n25257); [elec4](https://elec4.co.kr/contents/article_detail?article_idx=36615); [스타트업타임즈](https://www.startuptimes.kr/article/%EC%84%B8%EC%B9%B4-LG%EC%A0%84%EC%9E%90%EB%B8%94%EB%A3%A8%ED%8F%AC%EC%9D%B8%ED%8A%B8-%EC%8B%9C%EB%93%9C%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98%EB%8F%85%EB%A6%BD%EB%B2%95%EC%9D%B8-%EC%B6%9C%EB%B2%94)
- [search-snippet] 국내 신규 진입자 검색에서는 럭스로보(MODI Factory)와 세카 외에 2026년 AI PCB·회로 설계 스타트업이 새로 확인되지 않았습니다. 국내 매체는 OpenAI GPT-6 Astra의 KiCad 시연("회로도에서 배선까지 2분 54초")을 보도했으나, 단일 매체이고 원문은 빈 응답이라 열람하지 못했습니다. — [AI매터스 (검색 요약)](https://aimatters.co.kr/news-report/51077/); [다음/럭스로보](https://v.daum.net/v/20260316101424706)

### Inferences
- 세카는 B2B 대형 제조사의 **설계 검증·문서 정합성** 영역에서 실제 매출을 내고 있지만, 모디팩토리의 **비전문가 + 자동 배치·배선** 영역과는 현재 겹치지 않습니다. 넷리스트와 배치·배선을 학습하는 파운데이션 모델이 현실화하면 B2B 레이아웃 시장에서 충돌할 수 있습니다. 시기는 미정입니다.
- 국내 직접 경쟁자는 여전히 확인되지 않습니다. 국내 사용자에게 실질적인 경쟁 압력은 해외 서비스(Quilter 무료 티어, Flux)와 범용 LLM(Astra, Claude) + KiCad MCP 조합에서 올 가능성이 큽니다(추론).

### Gaps
- 세카의 정확한 제품 UI/입력 포맷, 가격(연간 라이선스 금액), 시드투자 금액은 비공개이거나 미확인입니다.
- 머니투데이, 와우테일 등 다른 원문(와우테일 403)은 열람하지 못했습니다.
- 대학·출연연의 AI PCB 스핀오프 같은 국내 신규 진입자는 검색되지 않았습니다. 존재하지 않는다고 단정할 수는 없습니다.

## 6. 2026년 하반기 신규 진입자와 주요 업데이트 (해외)

### Takeaway
2026년 하반기 최대 변수는 **범용 프런티어 모델의 PCB 진입**입니다. OpenAI GPT-6 Astra는 2026년 9월 초 발표 페이지 첫 데모로 KiCad 레이아웃을 시연했습니다. 스타트업 쪽에서는 Copperhead("Cursor for circuit boards", 2026-09 Show HN), Schematik(네덜란드), siliXon(영국, $1.5M), CopperPilot($390K)이 등장했습니다. 기존 업체도 에이전트를 붙였습니다(DeepPCB Cooper, Altium Agentic Requirements, Siemens Fuse, Cadence AuraStack, Zuken CR-8000 2026, Flux MCAD/외함).

### Cited Findings
- **OpenAI GPT-6 Astra (2026년 9월 초)** [원문 확인]
  - EEBench 블로그(2026-09-04)에 따르면 OpenAI가 출시 글 첫 화면에 GPT-6 Astra가 KiCad에서 PCB 작업을 하는 데모를 올렸습니다.
  - KiCad 포럼 첫 글은 OpenAI 블로그를 이렇게 인용합니다. "15-second condensed playback of GPT‑6 Astra performing PCB layout in KiCad, turning an electronic schematic into a manufacturable PCB by placing components and routing copper connections."
  - [원문 확인, 벤더 작성: DeepPCB] 한 사용자는 "Astra just ONE-SHOTTED my PCB"라고 썼습니다. 4층 27넷 보드였고, 품질 이슈는 2장에 정리했습니다.

  — [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/); [KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487); [DeepPCB](https://deeppcb.ai/gpt-6-astra-pcb-routing-deeppcb/)
- **Copperhead (copperhead.sh)** [원문 확인, HN]: "Show HN: Copperhead – Cursor for circuit boards"(2026-09-08, 250점)입니다. 창업자 측 설명은 "Claude나 GPT의 래퍼가 아니라 자체 하드웨어 IR, 결정론적 엔진, 지속 검증을 결합한다"는 것이고, 시뮬레이션 연동은 "준비 중"입니다. 반응 중에는 "범용 LLM으로도 되는데 왜 필요한가"라는 회의가 있었습니다. — [HN](https://news.ycombinator.com/item?id=49610059); [HN 창업자 답변](https://news.ycombinator.com/item?id=49610492)
- **Schematik (schematik.io, 네덜란드)** [원문 확인, HN 댓글]: 현재는 BOM, 회로도, 펌웨어에 집중하고 회로 기판으로 점차 확장할 예정입니다. "Astra로 한 초기 실험이 유망하다"고 했습니다. 펀딩은 미확인입니다. — [HN](https://news.ycombinator.com/item?id=49570026); [HN](https://news.ycombinator.com/item?id=49569555)
- **siliXon (영국)** [search-snippet]: TechFundingNews 2026-05-21 보도로 $1.5M을 유치했습니다. 텍스트 프롬프트로 PCB 설계를 생성하며, 기존 PCB 설계, 데이터시트, 제조 규칙으로 학습했다고 합니다. HN에서도 "UK 기반 Silixon 데모"가 언급되었습니다. — [AtlasPCB](https://www.atlaspcb.com/news/news-silixon-ai-text-to-pcb-funding-2026/); [HN](https://news.ycombinator.com/item?id=49610503)
- **CopperPilot** [search-snippet, 날짜 미확인]: Neon Fund가 주도한 프리시드로 $390K를 유치했습니다. 요구사항 조사, 부품 선정, 회로도, 배치·배선, 자체 검증을 수행하는 에이전트이며, "기본 LLM 18.6% 대 Epsilon 결합 시 78%"라는 수치를 자체 발표했습니다. — [Indian Startup News](https://indianstartupnews.com/funding/copperpilot-an-ai-design-agent-startup-for-electronics-hardware-raises-390000-in-funding-12771225)
- **DeepPCB Cooper** [원문 확인, 벤더]: 2026년 6월 웹앱에 탑재되었고 10월 KiCad 플러그인으로 들어왔습니다. 플러그인 자체는 5월에 나왔습니다. — [DeepPCB](https://deeppcb.ai/cooper-kicad-plugin/); [DeepPCB](https://deeppcb.ai/gpt-6-astra-pcb-routing-deeppcb/)
- **EEBench / atopile** [원문 확인]: 벤치마크를 넘어 "프런티어 랩과 직접 협업해 시뮬레이션 기반 학습 환경을 제공한다"고 밝혀, 사업 방향이 RL 환경 공급으로 확장되고 있습니다. — [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)
- **기존 업체 업데이트(재확인):** Siemens Fuse EDA AI Agent(2026-03-16, search-snippet), Cadence AuraStack(2026-07, 얼리 액세스, search-snippet), Altium Agentic Requirements(2026-10-14, search-snippet), Zuken CR-8000 2026(2026-10-20, 원문 확인), Flux MCAD/외함 확장(원문 확인 + 2026-09 보도). 각 출처는 1장에 있습니다.
- [unverified] Flux 사이트 비교 페이지 목록에 "Flux vs Trace"가 있어 "Trace"라는 경쟁 제품이 존재하는 것으로 보이나, 정체는 확인하지 못했습니다. 같은 목록에 "Flux vs Claude Code/Codex/Cursor/ChatGPT"도 있어, **Flux가 범용 AI 코딩 에이전트를 직접 경쟁자로 본다**는 점은 원문으로 확인됩니다. — [Flux Pricing (푸터)](https://www.flux.ai/pricing)

### Inferences
- 2026년 하반기에는 "범용 LLM + KiCad(MCP/Python) + 전용 라우터(DeepPCB, Freerouting)" 조합이 실제 워크플로로 자리 잡는 중입니다. DeepPCB도 "모델이 라우터를 구동하는 구조가 맞다"며 이를 수용합니다. 모디팩토리 같은 엔드투엔드 서비스는 프런티어 모델 사용자에게 **구동 대상 엔진(API/MCP)**으로도 자신을 노출할지 검토할 가치가 있습니다(추론).
- 초보자용 "프롬프트→보드" 시장은 Flux, Copperhead, siliXon, CopperPilot, Schematik에 범용 모델까지 들어와 빠르게 붐비고 있습니다. "파일 업로드 → 근거 있는 레이아웃"이라는 모디팩토리 포지션은 이들과 입력 방식이 달라 여전히 구분됩니다(추론).

### Gaps
**종합 미해결 목록**
1. Flux 플랜별 실제 금액(원문이 JS 렌더링이고 제3자 수치가 상충)
2. Quilter 핀당 단가, 각 대형 EDA AI 옵션 가격
3. 독립(비벤더) 레이아웃 벤치마크. 공개 보드 3종 비교도 벤더 작성
4. Reddit 실사용자 인용(접근 차단)
5. Adafruit–Flux 분쟁 결말과 소장 내용(adafruit.com 403)
6. OpenAI Astra PCB 데모의 공식 원문(openai.com 미시도), "2분 54초" 수치의 교차 확인
7. Copperhead, Schematik, CopperPilot의 펀딩, 설립일, 가격, 실제 출력 품질
8. "Trace"(Flux 비교 대상)의 정체
9. GitHub 저장소 스타 수와 최신 릴리스 갱신(api.github.com 차단), JITX 공개 저장소 여부
10. 세카 가격·시드 금액, 국내 신규 진입자 추가 여부
11. Renesas 365 출시일 상충(2026년 3월 GA 대 2026-04-28)
