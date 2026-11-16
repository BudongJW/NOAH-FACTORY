# 모디팩토리(MODI Factory) 해외 유사 프로젝트·경쟁사 조사: AI 기반 PCB/전자설계 자동화 (2026년 11월 기준)

> 조사일: 2026-11-16. 대상: 한국 기업을 제외한 해외 상용 제품과 스타트업.
> **방법상 주의 (보고서 작성자 필독):** 이 세션에서는 WebFetch로 1차 페이지를 열 수 없었습니다(quilter.ai, protoflow.ai, trycherryblossom.com 모두 호스트 해석 실패, 네트워크 허용 목록 밖으로 추정). 그래서 아래 사실은 모두 **WebSearch 결과 요약과 그 결과가 가리키는 URL**에 근거합니다. 원문 전체를 직접 읽어 확인한 것은 아닙니다. 수치, 특히 가격은 각 벤더 공식 페이지에서 다시 확인해야 합니다.
> 출처 편향: ProtoFlow, Cherry Blossom, Quilter 블로그의 "비교" 페이지는 경쟁사가 직접 쓴 마케팅성 콘텐츠입니다. 본문에서 그런 출처는 따로 표시했습니다.
> 모디팩토리 자체 정보(파일 업로드 → 약 90분 → 설계 근거가 붙은 AI PCB 설계안, 무료 가입, 초보자 친화, 다양한 출력 포맷)는 조사 의뢰서의 설명을 그대로 옮긴 것이며, 이 문서에서 별도로 검증하지 않았습니다.

## 1. AI 자동 배치·배선(Layout/Routing) 계열: 스타트업과 기존 EDA 대기업의 현황

### Takeaway
"회로도/넷리스트를 넣으면 AI가 배치·배선까지 해 주는" 영역의 선두 스타트업은 Quilter(물리 기반 AI, 2025년 10월 Series B $25M)와 DeepPCB(InstaDeep/BioNTech 산하, 강화학습 오토라우터, 시간당 과금)입니다. 기존 EDA 대기업(Cadence, Siemens, Zuken)도 2025–2026년에 AI·에이전트 기능을 잇달아 냈지만, 대부분 숙련 설계자를 돕는 "보조형"에 머뭅니다. Altium, Autodesk, EasyEDA/JLC는 2026년 11월 현재 자체 AI 자동 배치·배선 기능이 확인되지 않습니다.

### Cited Findings

**Quilter (미국)**
- 2019년 설립. 창업자 Sergiy Nesterenko는 SpaceX에서 Falcon 9/Falcon Heavy 2단용 내방사선 전자장치를 개발했습니다. 본사는 LA(Glassdoor, Tracxn)와 Santa Clara(CB Insights)로 출처가 엇갈립니다. — [CB Insights](https://www.cbinsights.com/company/quilter); [Tracxn](https://tracxn.com/d/companies/quilter/__uE4_N1PusI7A90VMXefv11ziZd0UjL-LsLP_cGlnLmg); [Glassdoor](https://www.glassdoor.com/Overview/Working-at-Quilter-EI_IE10231577.11,18.htm)
- Series A $10M(2024년 2월): Benchmark 주도, Coatue, Root Ventures, Harrison Metal Capital 참여. — [Pulse 2.0](https://pulse2.com/quilter-25-million-series-b-raised-for-automating-pcb-design-with-physics-driven-ai/); [Dealroom](https://dealroom.co/companies/quilter/)
- Series B $25M(2025-10-08 발표): Index Ventures 주도. 자금은 국방·자동차·소비자 전자 분야 확장과 AI 모델 고도화에 쓸 계획입니다. 투자자 목록에 Lip-Bu Tan(업계 인사)도 있습니다. — [I-Connect007](https://iconnect007.com/article/147236/quilter-secures-25m-series-b-to-eliminate-manual-pcb-design-with-physicsdriven-ai/147233/design); [Quilter 블로그](https://www.quilter.ai/blog/series-b); [Justainews](https://justainews.com/companies/funding-news/index-ventures-leads-25m-round-for-quilter-ai/)
  - 주의: d2pmagazine 기사 제목의 "$25 Billion"은 오기입니다. — [D2P Magazine](https://www.d2pmagazine.com/2025/12/04/quilter-secures-25-billion-series-b-funding-to-automate-circuit-board-design-with-physics-driven-ai/)
  - 누적 투자액은 출처마다 $35M(CB Insights, Tracxn), $40M(Seedtable), $50M(CapLight)으로 다릅니다. — [Seedtable](https://seedtable.com/companies/quilter); [CapLight](https://www.caplight.com/company/quilter)
- 2026년 소식: SOC 2 Type II 인증(2026-03-10), 자동 BGA fanout 릴리스(2026-07-08). 2026년 신규 투자 라운드는 확인되지 않았습니다. — [Quilter Newsroom](https://www.quilter.ai/newsroom)
- 입력: Altium, Cadence, Siemens, KiCad 파일. 클라우드에서 물리 기반 AI로 배치와 배선을 수행합니다. — [Electronics For You](https://www.electronicsforu.com/technology-trends/quilter-ai-powered-pcb-design-tool-for-automated-pcb-layout); [Quilter docs: 입력 보드 파일 준비](https://docs.quilter.ai/prepare-your-input-board-file)
- 출력과 "설계 근거"에 가까운 기능: 여러 스택업을 동시에 평가해 레이아웃 후보 여러 개를 만들고 순위를 매깁니다. 후보마다 DRC뿐 아니라 임피던스 제어, 리턴 전류 연속성, 디커플링 효율, 결합 넷 거동 같은 물리 검토(design review)가 붙는다고 홍보합니다. — [Quilter Help: How does Quilter work](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work); [Quilter 홈](https://www.quilter.ai/)
- 제조 파일: 2026년 1월 블로그 기준 RS-274X Gerber(동박, 마스크, 실크, 외곽)와 Excellon 드릴 파일을 생성합니다. — [Quilter 블로그: Gerber/drill/fab 생성](https://www.quilter.ai/blog/from-ai-design-to-manufacturing-how-quilter-automates-gerber-drill-and-fab-file-generation)
- 독립 매체 AtlasPCB는 Quilter 출력을 "표준 DRC를 통과하는 제조 가능한 출력"으로, 벤더 주장보다 좁게 평가합니다. — [AtlasPCB](https://atlaspcb.com/blog/autonomous-pcb-layout-quilter-siemens-fuse-flux-2026)
- Project Speedrun: 부품 843개, 연결 5,141개(pins), 8층 보드 2장(SOM + 베이스보드)으로 이루어진 Linux 컴퓨터입니다. 사람 작업은 38.5시간(AI 결과 검토, 수정, 제조 파일 준비)이 들었고, 외부 레이아웃 서비스 견적은 428시간이었습니다. 다만 428시간은 견적일 뿐 실제로 수작업 비교 실험을 한 것은 아닙니다. Quilter의 레이아웃 생성 런타임은 약 27시간(자사 발표)이며, 첫 시도에 Debian 부팅에 성공했다고 합니다. 제조는 Sierra Circuits가 맡았습니다. — [VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the); [Quilter 검증 블로그](https://www.quilter.ai/blog/validating-an-ai-designed-computer-running-under-real-workloads); [Yahoo Tech](https://tech.yahoo.com/ai/articles/quilter-ai-designs-dual-pcb-223000045.html)
- 가격: 개인·학술용 무료 티어가 있으나, 자격 범위는 출처마다 다릅니다(개인·학술·탐색적 R&D 또는 10인 미만·매출 $50K 미만 소규모 팀). 무료 티어의 보드 메타데이터와 입력 파일은 학습용 퍼즐 생성에 쓰이고, 엔터프라이즈 설계는 학습에 쓰지 않습니다. 상용 가격은 핀 수 또는 프로젝트 단위로 영업 견적을 받으며, 공개 가격표는 없습니다. 모두 제3자 출처입니다. — [Futurepedia](https://www.futurepedia.io/tool/quilter); [HyperStore](https://store.hypergpt.ai/is-quilter-free); [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/free-ai-pcb-design-tools)
- 고객: 항공우주·국방·소비자 전자 분야의 Fortune 500 기업이 도입 중이라고 주장하지만 고객사 이름은 확인되지 않았습니다. 기밀 환경용 온프레미스 배포를 제공합니다. — [Seedtable](https://seedtable.com/companies/quilter); [CB Insights](https://www.cbinsights.com/company/quilter)

**DeepPCB (InstaDeep, BioNTech 자회사)**
- InstaDeep이 만든 강화학습 기반 배치·배선 엔진입니다. InstaDeep은 2023년 BioNTech에 인수되었습니다(AIDb 기준 2023년 7월부터 자회사). NeurIPS, ICML 등에 발표한 7년간의 R&D를 기반으로 한다고 밝힙니다. — [AIDb](https://theaidatabase.com/m/instadeep-deeppcb.html); [DeepPCB Help](https://deeppcb.ai/help/); [cadalts](https://cadalts.com/tools/deeppcb/)
- 입력: Altium(.PcbDoc을 웹앱에 업로드하거나 KiCad 플러그인 경유), KiCad 플러그인, EasyEDA Pro, Specctra DSN(OrCAD/Allegro/Eagle). Altium 네이티브 "Route" 버튼은 출시 예정입니다. — [DeepPCB Help](https://deeppcb.ai/help/); [DeepPCB Altium 페이지](https://deeppcb.ai/altium/)
- 가격(2026년 10–11월 제3자 출처): 무료 체험은 보드 1개, 최대 30분, 4층, airwire 150개, 부품 100개까지입니다. 선불 시간권은 1시간 $30, 10시간 $280, 30시간 $800이고 엔터프라이즈는 별도 견적입니다. 종량제 티어는 8층·2,200핀이 상한이라는 보고가 있습니다. — [cadalts](https://cadalts.com/tools/deeppcb/); [ProtoFlow 비교 (경쟁사 작성)](https://www.protoflow.ai/compare/ai-pcb-autorouter-comparison)
- 성능: 중앙값 완료율 100%, 보드의 87%가 95% 이상 완료, 중앙값 소요 수 분이라는 주장이 있습니다(벤더 인접 출처). — [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/ai-pcb-autorouter-comparison)
- JLCPCB 블로그는 EasyEDA에서 배치를 마친 보드를 AI 배선용으로 DeepPCB에 보내라고 권합니다. — [JLCPCB 블로그](https://jlcpcb.com/blog/ai-tools-for-pcb-design)

**Cadence (Allegro X AI / AuraStack AI Super Agent)**
- Allegro X AI(2023년 4월 발표): 넷리스트와 물리 제약을 입력받아 생성형 AI로 부품을 배치하고, 핵심 넷 자동 배선과 전원 플레인 생성을 수행합니다. 중소 규모 설계가 대상이며, "수일 → 수분", "10배 이상 단축"을 주장합니다. 고객 인용으로 Kioxia가 있고, 한 고객 사례에서는 수작업 3일짜리 배치를 75분에 끝냈다고 합니다. 모두 벤더 수치입니다. — [Cadence 보도자료 (2023)](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2023/cadence-introduces-allegro-x-ai-accelerating-pcb-design-with.html); [All About Circuits](https://www.allaboutcircuits.com/news/cadence-launches-cloud-ai-tool-to-shrink-pcb-placement-and-routing-times/)
- AuraStack AI Super Agent on Allegro AI Studio(2026-07-15 발표): "세계 최초 PCB·첨단 패키징용 에이전틱 AI 플랫폼"을 표방합니다. 시스템 계획, 제약 관리, IP 재사용, P&R, DFM, 멀티피직스 해석을 포괄하고 NVIDIA Blackwell/CUDA-X로 가속합니다. 출시까지 최대 2배 단축, 생산성 15배를 주장하며, 2026년 중 순차 출시 예정입니다. — [Cadence Newsroom](https://newsroom.cadence.com/press-releases/press-release-details/2026/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging/default.aspx); [Business Wire](https://www.businesswire.com/news/home/20260715175854/en/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging); [Forbes](https://www.forbes.com/sites/karlfreund/2026/07/15/cadence-automates-pcb-design-with-ai-super-agents/)
- 애널리스트 인용(SiliconANGLE): "PCB와 첨단 패키징 설계의 상당 부분은 여전히 완전 자율이 아니라 고도로 보조받는 수준이다." — [SiliconANGLE](https://siliconangle.com/2026/07/15/cadence-extends-ai-agents-beyond-chips-aurastack-circuit-boards-packaging/)

**Siemens (PADS Pro Essentials / Xpedition Standard / Xpedition 2604)**
- 중소기업·독립 엔지니어용으로 AI 기능을 넣은 PADS Pro Essentials와 Xpedition Standard를 출시했습니다(Persistence Market Research 기준 2025년 5월). Xpedition Standard는 배선 경로 예측과 반복 작업 자동화를 제공하고, PADS Pro Essentials에는 CELUS 기반 기능 블록 프런트엔드(AI 회로도·BOM 생성)가 들어갑니다. — [All About Circuits](https://www.allaboutcircuits.com/news/siemens-unveils-ai-enhanced-pcb-design-tools-for-mid-range-users/); [Engineering.com](https://www.engineering.com/siemens-brings-ai-driven-pcb-design-to-small-and-medium-electronics-teams/); [Persistence Market Research](https://www.persistencemarketresearch.com/market-research/pcb-design-software-market.asp)
- Xpedition 2604(2026년 4월)에는 AI 지원 어시스턴스, 다중 보드 검증, 3D 검사 개선이 들어갔습니다(제3자 보도). — [ElectronicsForU](https://www.electronicsforu.com/technology-trends/siemens-xpedition-a-professional-pcb-design-tool-for-complex-electronics)
- Siemens–CELUS 협력 발표(2024-10-30, 텍사스 Austin): 중소기업·독립 엔지니어 대상 AI 지원 PCB 설계입니다. — [Siemens News](https://news.siemens.com/en-gb/siemens-celus/); [CELUS News](https://www.celus.io/news/celus-siemens-collaboration)
- 2026년 1월 ASTER Technologies(DFT)를 인수했습니다. — [Straits Research](https://straitsresearch.com/report/pcb-design-software-market)
- 상충: 한 제3자 비교는 "PADS Essentials에는 AI copilot이 없다"고 써서 위 CELUS 통합 설명과 충돌합니다. — [GSAS India](https://gsasindia.com/blog/pcb-design-tool-comparison-india-2026)

**Zuken (CR-8000 2026)**
- 2026년 10월 20–22일 무렵 출시되었습니다. Design Gateway의 회로도 자동 배선, Design Force의 Main Path View, AI 기반 Smart Design Reuse(과거 프로젝트의 배치 구성을 검색해 적용), 로컬 AI-PR 서버로 배치 지식을 공유하는 "Dynamic Brain", AIPR(Autonomous Intelligent Place and Route)이 포함됩니다. — [Zuken](https://www.zuken.com/en/resource/cr-8000-2026-pcb-design-automation/); [EEJournal](https://www.eejournal.com/industry_news/cr-8000-2026-streamlines-pcb-development-with-new-automation-and-reuse-capabilities/)
- Zuken 스스로 AI 기능은 "실제적이지만 제한적"이며 엔지니어가 통제권을 유지한다고 설명합니다. 설계 시간이 몇 % 줄었는지 검증된 수치는 공개하지 않았습니다. — [Zuken US 블로그](https://www.zuken.com/us/blog/ai-pcb-place-and-route-what-can-ai-actually-do-today/); [ENGtechnica](https://engtechnica.com/zuken-cr-8000-2026-automates-schematic-routing-layout-reuse/)

**Altium (Renesas 그룹)**
- 2025년에 구독형 Altium Discover, Develop, Agile을 도입했고, Altium Designer는 더 이상 단독 판매하지 않습니다. — [Wikipedia: Altium Designer](https://en.wikipedia.org/wiki/Altium_Designer)
- "Renesas 365, Powered by Altium"이 2026년 3월 GA되었습니다. 컨텍스트 인식 시스템이 자원·설계 제약을 짚고 해결책을 제안한다고 설명합니다. — [Edge AI and Vision Alliance](https://www.edge-ai-vision.com/2026/03/renesas-announces-general-availability-of-renesas-365/); [Engineering.com](https://www.engineering.com/renesas-365-powered-by-altium-unveiled-for-software-defined-products/)
- Altium의 배선 자동화(ActiveRoute, Situs 오토라우터)는 AI로 소개되지 않습니다. 2026-10-26 Altium 제품 페이지에서 AI 회로도 작성이나 AI 배선을 찾지 못했다는 확인이 있습니다(경쟁사 작성 페이지). Altium이 공식 문서화한 AI 기능은 Requirements Portal의 Engineering Assistant이고, "MCP Server for Altium Designer/Altium 365"는 2026-11-02 기준 Coming Soon입니다. — [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/best-ai-pcb-design-software-2026); [JLCPCB 블로그](https://jlcpcb.com/blog/ai-tools-for-pcb-design); [GitHub altium-copilot (커뮤니티, 읽기 전용)](https://github.com/ee-in-a-box/altium-copilot)

**Autodesk Fusion Electronics**
- 2026년 9월 업데이트에서 "NETROUTE"(회로도 자동 배선 명령, 스크립트·자동화·AI 생성 회로도용)가 추가되었고, 2026년 5월에는 Electronics Python API가 처음 지원되었습니다. 기존 PCB 오토라우터는 DRC 기반의 전통 방식입니다. AI 자동 배치 기능은 확인되지 않았습니다. — [Autodesk Fusion 2026년 9월 업데이트](https://www.autodesk.com/products/fusion-360/blog/september-2026-major-product-update-whats-new/); [Fusion 2026 Release Notes](https://help.autodesk.com/cloudhelp/ENU/Fusion-ReleaseNotes/files/FIC-REL-NOTES-INC.htm); [Autodesk 블로그](https://www.autodesk.com/products/fusion-360/blog/18-things-need-to-know-fusion-360-electronics/)

**EasyEDA / JLCPCB**
- 2026년 8월 기준 공식 1st-party AI 어시스턴트는 없습니다(경쟁사 작성 비교). JLCPCB 블로그는 EasyEDA Pro API Gateway와 오픈소스 API Skill, 로컬 브리지로 Claude Code나 Codex 같은 코딩 에이전트를 연결하는 워크플로를 소개합니다. Adafruit 요약(2026-09-19)에 따르면 headless CLI와 MCP는 "진행 중"이며 2026년 공개 베타 예정이고, 자율 설계는 "미래 비전"으로 분류됩니다. — [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/easyeda-ai-copilot); [JLCPCB 블로그](https://jlcpcb.com/blog/ai-tools-for-pcb-design); [Adafruit](https://blog.adafruit.com/2026/09/19/jlc-puts-ai-assisted-board-design-in-files-you-can-read-review-and-edit/)

### Inferences
- "완전 자동 레이아웃"을 실제 서비스로 파는 곳은 Quilter와 DeepPCB(배선 중심) 정도입니다. 대형 EDA 3사(Cadence, Siemens, Zuken)는 기존 고가 툴 안의 보조 기능이나 에이전트로 접근합니다. 모디팩토리가 "업로드 → 설계안"이라는 서비스형 UX를 내세운다면, 가장 가까운 해외 비교 대상은 Quilter입니다.
- Quilter는 대형 보드에서 레이아웃 생성에 약 27시간(Speedrun)이 걸렸고, DeepPCB는 소형 보드 배선을 수 분 안에 끝낸다고 주장합니다. 따라서 "90분"이라는 수치 자체보다는 어떤 복잡도의 보드를 어디까지(회로도인지, 배치·배선인지, 제조 파일까지인지) 90분에 해 주는지가 비교의 핵심이 됩니다.

### Gaps
- Quilter, Flux, DeepPCB 공식 가격 페이지를 직접 열람하지 못했습니다(WebFetch 차단). 가격은 모두 제3자 집계입니다.
- DeepPCB의 정식 출시 연도, 누적 사용자 수, 배선한 보드 수는 확인하지 못했습니다.
- Renesas의 Altium 인수(금액, 완료 시점)는 이번 세션에서 1차 출처로 검증하지 못했습니다. Renesas 365 "Powered by Altium" GA(2026년 3월)만 확인했습니다.
- Siemens PADS Pro Essentials와 Xpedition Standard의 정확한 출시일은 출처마다 시기가 엇갈립니다.
- Quilter의 고객사 이름과 매출 지표는 공개 자료에서 찾지 못했습니다.

## 2. AI 회로도·BOM 생성, 코드 기반, 프롬프트→보드 계열 (Celus, Circuit Mind, Flux, JITX, Diode, atopile, tscircuit, 신생사)

### Takeaway
"요구사항이나 블록도 → 회로도/BOM" 영역에서는 Circuit Mind(2026년 10월 $25M, 검증 에이전트 AVE 출시)와 CELUS(Siemens와 제휴, 엔지니어 1.5만 명)가 대표적입니다. 브라우저형 "AI 하드웨어 엔지니어" Flux는 2026년 2월 $37M을 유치하고 가입자 100만 명을 넘겼습니다. 코드 기반(JITX, Diode/Zener, atopile, tscircuit)과 프롬프트→보드형 신생사(Cherry Blossom, ProtoFlow, Resin)도 늘고 있습니다.

### Cited Findings

**Flux (Flux.ai, 미국 샌프란시스코)**
- 2026-02-27 발표로 총 $37M을 유치했습니다. 8VC가 주도한 $27M Series B에 Bain Capital Ventures, Liquid 2 Ventures, Outsiders Fund가 참여했고, 그동안 공개하지 않았던 $10M Series A(Outsiders Fund 주도, BCV 공동 주도)도 함께 밝혔습니다. CEO는 Matthias Wagner입니다. — [Yahoo Finance (GlobeNewswire)](https://finance.yahoo.com/news/flux-ai-hardware-engineer-announces-131400703.html); [SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)
- 2019년 설립(Matthias Wagner, Christian Blank, Lance Cassidy)이라는 정보는 단일 출처입니다. 누적 투자액 약 $49M은 집계 사이트 추정치입니다. 2026-06-25에 "$5M 추가 유치"가 있었다는 Dealroom 항목은 검증하지 못했습니다. — [yespress](https://yespress.io/flux); [Tracxn](https://tracxn.com/d/companies/flux-ai/__DgsqcxsjLsm7cUHAQiGcPjtiZwIU_vAHmJznT8TYkS8); [Dealroom](https://app.dealroom.co/companies/flux_ai)
- 가입자 100만 명 돌파(활성 사용자 수는 불명). — [SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)
- 기능: 텍스트 프롬프트로 회로 기판을 설계하는 "AI 하드웨어 엔지니어"(2025-10-07 보도자료)입니다. 리서치, 자동 레이아웃, 실시간 부품 데이터를 처리하는 "투명한 AI 에이전트"를 내세우며, Spring 2026 업데이트에서 AI 자동 레이아웃의 후처리 부담을 줄였다고 밝혔습니다. — [GlobeNewswire](https://www.globenewswire.com/news-release/2025/10/07/3162463/0/en/AI-hardware-engineer-Flux-turns-text-prompts-into-circuit-board-designs.html); [Flux 블로그](https://www.flux.ai/p/blog/flux-public-launch-announcement)
- 가격(2026년 10월 제3자 확인): Pro는 월 $250(연간 결제 시 월 $200)이고 AI Compute Unit(ACU) 400개가 포함됩니다. 개인 플랜은 14일 체험이며, 체험 후에는 비공개 프로젝트 편집, 내보내기, AI 사용에 유료 플랜이 필요합니다. 추가 ACU는 개당 $2입니다. 과거 출처에는 Pro $15나 $39 같은 저가 플랜이 있어 가격 구조가 바뀐 것으로 보입니다. — [AnyGen Flux 리뷰](https://www.anygen.io/showcase/fluxai-review/index.html); [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/free-ai-pcb-design-tools); [Electronics-Lab](https://www.electronics-lab.com/news/flux-ai-an-ai-powered-browser-based-pcb-design-tool-review/)

**Circuit Mind (영국 런던)**
- 2018년 설립, 런던 소재. — [CB Insights](https://www.cbinsights.com/company/circuit-mind)
- 2026-10-28에 $25M 유치를 발표했습니다. Norwest가 주도한 $18.5M Series A와 미공개였던 Seed(Third Prime 주도)를 합한 금액이며, 누적 $33.4M입니다. 기존 투자자 Third Prime, Differential, Blackhorn과 신규 투자자 Lightscape VC가 참여했고, Norwest의 Dave Zilberman이 이사회에 합류했습니다. 미국 본사 개설, 영업·엔지니어링 채용, 설계 프로세스 커버리지 확대에 자금을 쓸 계획입니다. — [SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/); [New Electronics](https://www.newelectronics.co.uk/content/news/circuit-mind-secures-25m-funding-to-expand-ai-driven-electronics-design-platform); [The Next Web](https://thenextweb.com/news/circuit-mind-25m-funding-ai-circuit-board-design)
- AVE(Agentic Verification Engine, 2026년 10월 출시): AI 에이전트 무리가 회로도(사람이 그린 것 포함)를 부품 데이터시트, 앱노트, 조직별 설계 리뷰 체크리스트와 대조해 검증합니다. 특허 받은 물리 기반 엔진 위에 AI 에이전트를 얹은 구조입니다. — [SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/)
- ACE: 블록도를 입력하면 완성된 회로도, BOM, 전력·디레이팅 분석, FMEA를 출력합니다. 소요 시간은 자사 주장 약 60초, ipXchange 기준 10분 미만입니다. — [Circuit Mind ACE 발표](https://www.circuitmind.io/resource-center/unveiling-ace-architecture-to-pcb-schematic-in-60-seconds); [ipXchange](https://ipxchange.tech/product-news/go-from-block-diagram-to-bom-in-minutes-meet-circuit-minds-ace-tool/)
- 고객 사례: Los Alamos National Laboratory는 수 주 걸리던 작업이 4시간 13분(자동화 후 수작업 3.5시간 포함)으로 줄었다고 합니다(자사 발표). Emerson의 하드웨어 엔지니어링 디렉터 추천사도 있습니다. — [Circuit Mind 리소스](https://www.circuitmind.io/resource-center/evidence-that-ai-is-breaking-the-engineering-triangle-in-electronics-design); [Electromaker](https://www.electromaker.io/blog/article/circuit-mind-turns-block-diagrams-into-schematics-fast)

**CELUS (독일 뮌헨)**
- 2017년 또는 2018년 설립(출처마다 다름). Seed €1.7M(Speedinvest 주도) 이후 2022년 7월 Series A €25M(Earlybird 주도, DI Capital, Speedinvest, Plug and Play 참여)을 유치했습니다. 이후 신규 라운드는 이번 검색에서 찾지 못했습니다. — [Tech.eu](https://tech.eu/2022/07/06/disrupting-fragmented-electronics-supply-chain-with-design-automation-celus-rakes-in-eur25-million/); [CELUS seed 발표](https://www.celus.io/news/celus-raises-seed-round-of-eu1-7m); [EU-Startups](https://www.eu-startups.com/2022/07/munich-based-celus-secures-e25-million-to-supercharge-its-mission-to-automate-electronics-design/)
- 클라우드 플랫폼으로 기능 블록에서 회로도, PCB 레이아웃, BOM을 생성합니다. 사용 엔지니어는 2022년 1,800명 이상에서 2024년 10월 15,000명 이상으로 늘었습니다. — [Yahoo Finance (TechCrunch)](https://finance.yahoo.com/news/celus-uses-ai-automate-circuit-120028757.html); [ChannelLife](https://channellife.com.au/story/siemens-celus-team-up-to-revolutionise-pcb-design)
- Siemens EDA의 프런트엔드로 들어가 AI 회로도·BOM 생성과 기능 블록 수준 설계를 제공합니다(2024-10-30 발표). 음성→설계, 이미지→설계 기능을 개발 중이라는 미확인 단일 출처도 있습니다. — [Siemens](https://www.siemens.com/en-us/products/pcb/ai-pcb-design-intersection/celus-collaboration/); [Power Electronics News](https://www.powerelectronicsnews.com/celus-design-platform-revolutionizes-electronics-design-with-ai/)

**JITX (미국)**
- 2022-09-18에 Series A $12M(Sequoia 주도, YC, FundersClub, Liquid 2 참여)을 유치하며 정식 출시(GA)했습니다. 2025–2026년 신규 라운드는 찾지 못했습니다. — [JITX 블로그](https://www.jitx.com/blog/series-a-announcement); [SiliconANGLE](https://siliconangle.com/2022/09/20/jitx-raises-12m-programmatic-circuit-board-design-platform/); [Tracxn](https://tracxn.com/d/companies/jitx/__jUTcWraTa5nR56YOnxXEEaiw6oGovUPkYsPD_tauVow)
- 엔지니어가 보드 요구사항을 코드로 기술하면 JITX가 부품 선정, 배치, 배선, 검증을 수행합니다. — [IEEE Spectrum](https://spectrum.ieee.org/startup-jitx-uses-ai-to-automate-complex-circuit-board-design); [Altium Resources](https://resources.altium.com/p/jitx-way-hardware-engineers-write-codes)

**Diode Computers (미국 뉴욕, YC S24)**
- 2025년 7월 Series A $11.4M(a16z 주도, YC, Caffeinated Capital, BoxGroup 참여). 창업자는 Davide Asnaghi와 Lenny Khazan입니다. — [Dealroom](https://app.dealroom.co/news/feed/diode-computers-raises-11-4m-for-ai-pcb-design); [Benzatine](https://benzatine.com/news-room/diode-computers-secures-114-million-to-revolutionize-pcb-design-with-ai)
- Starlark 기반 PCB 기술 언어 "Zener"와 `pcb` 툴체인(MIT 라이선스 오픈소스)을 제공합니다. KiCad, Altium, Cadence로 내보낼 수 있고, KiCad 레이아웃 생성에는 KiCad 10.x가 필요합니다. — [GitHub diodeinc/pcb](https://github.com/diodeinc/pcb); [Zener 언어 문서](https://docs.pcb.new/pages/spec)
- Anthropic과 협업(2025년 12월 공개)해 Claude가 데이터시트를 읽고 Zener 레퍼런스 회로를 만들도록 했습니다. 블라인드 평가에서 Sonnet 4.5 결과가 10회 중 8회 선호되었다는 수치는 2차 출처입니다. — [Diode 블로그](https://blog.diode.computer/anthropic-partnership); [gend.co (2차)](https://www.gend.co/blog/enhancing-claude-pcb-design-skills); [X @diodeinc](https://x.com/diodeinc?lang=en)
- 사업 모델은 셀프서브(즉시 제조·조립 견적)와 엔터프라이즈(Diode 엔지니어가 설계)입니다. 로보틱스, 의료기기, 항공우주가 타깃이고 "Fortune 100 고객"을 주장합니다. — [yespress](https://yespress.io/diode-computers-inc); [Benzatine](https://benzatine.com/news-room/diode-computers-secures-114-million-to-revolutionize-pcb-design-with-ai)

**atopile / tscircuit (오픈소스 코드 기반)**
- atopile: YC W24, MIT 오픈소스. 펀딩은 출처마다 $500K YC seed, $0, 비공개로 엇갈립니다. 전기공학 에이전트 벤치마크 "EEBench"를 만든 팀입니다. — [Latka](https://getlatka.com/companies/atopile.io); [Extruct](https://www.extruct.ai/hub/atopile-io/); [Silixon](https://silixon.io/blog/best-ai-pcb-design-tools)
- tscircuit: React/TypeScript 코드를 회로도와 PCB로 컴파일하며 AI 에이전트가 코드를 작성하는 방식에 적합합니다. MIT 오픈소스. Seed 단계(43 Fund, Konvoy 또는 Boost VC로 출처 상충). — [f4.fund](https://f4.fund/startups/tscircuit); [Silixon](https://silixon.io/blog/best-ai-pcb-design-tools)

**신생 프롬프트→보드형 도구 (2025–2026)**
- Cherry Blossom: 2026년 출시된 브라우저 기반 도구입니다. 평문 프롬프트로 회로도, 레이아웃, BOM, 제조 파일을 만듭니다. 무료 플랜은 AI 없이 에디터만 제공하고, AI는 Pro 월 $20부터입니다(가격은 경쟁사 ProtoFlow 페이지 기준). 외부 AI 제공자로 데이터를 보냅니다. — [Product Hunt](https://www.producthunt.com/products/cherry-blossom); [Cherry Blossom 블로그](https://www.trycherryblossom.com/blog/protoflow-alternative)
- ProtoFlow: 데스크톱 앱 형태의 AI 보조 회로도 도구로 KiCad와 Altium으로 내보냅니다. 무료로 하루 AI 메시지 15개를 쓸 수 있고 레이아웃, SPICE, Gerber도 지원합니다. 옵트아웃하지 않으면 사용자 설계를 학습에 쓴다는 보고가 있습니다. — [Product Hunt](https://www.producthunt.com/products/protoflow-2); [Cherry Blossom 블로그 (경쟁사 작성)](https://www.trycherryblossom.com/blog/protoflow-alternative)
- Resin Technologies(YC 등재): "AI-native PCB 설계 도구"를 표방하며 부품 조사, 회로도 생성, 보드 배선 기능을 내세웁니다. 배치(batch), 펀딩, 출시일은 미확인입니다. — [YC](https://www.ycombinator.com/companies/resin-technologies)
- Cirkit Designer: 브라우저 기반 초보자·Arduino용 도구입니다. 자연어 설명으로 부품을 제안하고 코드를 생성하며 시뮬레이션을 제공합니다. 무료로 시작해 유료 멤버십으로 확장하는 구조이고 부품 라이브러리는 1,000개 이상입니다. PCB 제조 파일 출력 여부는 확인하지 못했습니다. — [Cirkit Designer](https://www.cirkitdesigner.com); [Instructables (창업자 작성)](https://instructables.com/Designing-Arduino-Projects-With-ChatGPT-Cirkit-Des)

**확인 결과 범위 밖이거나 확인 불가**
- Vinci: 칩 열 시뮬레이션용 물리 AI(Palo Alto). Series A $36M(2025년 12월, Xora 주도, 누적 $46M)이며 PCB 설계 도구는 아닙니다. $250M 유치·기업가치 $1.5B 보도는 단일 출처라 미확인입니다. — [SiliconANGLE](https://siliconangle.com/2025/12/03/vinci-nabs-46m-speed-chip-simulations-ai/); [Yahoo/Reuters](https://finance.yahoo.com/news/software-firm-vinci-speeds-hardware-130649208.html); [Byteiota (미확인)](https://byteiota.com/vinci-raises-250m-to-simulate-chips-1000x-faster/)
- Silimate: YC S23, 칩(RTL) 설계 디버깅 AI로 PCB 설계와는 무관합니다. — [Stanford Daily](https://stanforddaily.com/2026/03/11/silimate-ceo-pioneers-ai-debugger/)
- "Cady": PCB 리뷰 AI 스타트업으로 검색했으나 결과가 없었습니다(Gaps 참조).

### Inferences
- 해외 시장은 두 갈래로 나뉩니다. (a) 프런트엔드 쪽 요구사항→회로도/BOM은 Circuit Mind, CELUS, Flux, Diode, (b) 백엔드 쪽 배치·배선은 Quilter, DeepPCB, Cadence입니다. 한 서비스에서 "파일 업로드 → 회로도 검토 + 레이아웃 제안 + 근거"를 모두 주는 곳은 드뭅니다. Flux, Cherry Blossom, CELUS가 엔드투엔드를 표방하지만, 실제 레이아웃 품질은 독립적으로 검증된 바가 없습니다.
- 코드 기반 접근(JITX, Diode, atopile, tscircuit)은 LLM 에이전트와 잘 맞지만 진입 장벽이 높아 초보자용이라고 보기 어렵습니다.

### Gaps
- Circuit Mind와 CELUS의 공개 가격, 무료 티어 존재 여부를 찾지 못했습니다(엔터프라이즈 영업 모델로 추정되나 미확인).
- CELUS의 2023–2026 신규 펀딩과 현재 상태(2026년 뉴스)를 찾지 못했습니다.
- Flux의 2026년 6월 $5M 추가 유치 여부를 검증하지 못했습니다.
- Resin Technologies, Cherry Blossom, ProtoFlow의 설립 연도, 본사, 펀딩은 미확인입니다.
- "Cady"라는 AI PCB 스타트업은 존재를 확인하지 못했습니다.

## 3. 제품별 상세 비교표 (설립, 본사, 펀딩, 입력, 출력, 소요 시간, 설명 기능, 가격, 대상, 고객)

### Takeaway
펀딩 규모 상위는 Flux(2026년 2월 $37M), Quilter(2025년 10월 $25M, 누적 $35–50M), Circuit Mind(2026년 10월 $25M, 누적 $33.4M), CELUS(2022년 €25M) 순입니다. 무료 사용 경로는 Quilter(비상업 무료), Cherry Blossom(AI 없는 무료), ProtoFlow(일 15회), 오픈소스(Diode, atopile, tscircuit)에 있습니다. 초보자를 명시적으로 겨냥한 곳은 Flux, Cirkit Designer, Cherry Blossom 정도입니다.

### Cited Findings

| 제품/회사 | 설립·본사 | 펀딩 (날짜) | 입력 | 출력 | 소요 시간 주장 | 설계 근거·설명 기능 | 가격/무료 | 주 타깃 | 근거 출처 |
|---|---|---|---|---|---|---|---|---|---|
| **Quilter** | 2019 / LA 또는 Santa Clara(상충) | A $10M(2024-02, Benchmark), B $25M(2025-10-08, Index), 누적 $35–50M(상충) | Altium, Cadence, Siemens, KiCad 파일 | 다수 레이아웃 후보(순위) + Gerber RS-274X/Excellon | Speedrun 생성 약 27h, 사람 38.5h(외부 견적 428h 대비) | 후보별 물리 기반 design review(임피던스, 리턴 전류, 디커플링) | 개인·학술 무료(학습 데이터 활용), 상용은 핀/프로젝트 견적 | 전문가, 기업(항공우주, 국방) | [Series B](https://www.quilter.ai/blog/series-b), [Help](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work), [VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the), [Futurepedia](https://www.futurepedia.io/tool/quilter) |
| **DeepPCB** (InstaDeep/BioNTech) | InstaDeep(2023년 BioNTech 인수) | 모회사 소속(별도 펀딩 없음) | Altium .PcbDoc, KiCad 플러그인, EasyEDA Pro, Specctra DSN | 배선된 보드 | 중앙값 수 분(벤더 인접) | 확인 안 됨 | 체험 1보드 30분, $30/h, $280/10h, $800/30h | 전문가, 팀 | [Help](https://deeppcb.ai/help/), [cadalts](https://cadalts.com/tools/deeppcb/) |
| **Cadence Allegro X AI / AuraStack** | Cadence(상장 대기업) | 해당 없음 | 넷리스트 + 물리 제약 | 배치, 핵심 넷 배선, 전원 플레인 | 수일 → 수분, 10배 이상(벤더), AuraStack 생산성 15배 | 에이전트 기반 제약 관리 | 기업용 라이선스(가격 비공개) | 대기업 전문가 | [Cadence 2023](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2023/cadence-introduces-allegro-x-ai-accelerating-pcb-design-with.html), [Cadence 2026](https://newsroom.cadence.com/press-releases/press-release-details/2026/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging/default.aspx) |
| **Siemens PADS Pro Essentials / Xpedition Standard** | Siemens | 해당 없음 | 자사 툴(+ CELUS 블록 프런트엔드) | 회로도, BOM, 레이아웃 + Valor DFM | 미공개 | AI 경로 예측, 클라우드 DFM | Xpedition Standard 30일 체험(제3자) | 중소기업, 독립 엔지니어 | [All About Circuits](https://www.allaboutcircuits.com/news/siemens-unveils-ai-enhanced-pcb-design-tools-for-mid-range-users/), [GSAS India](https://gsasindia.com/blog/pcb-design-tool-comparison-india-2026) |
| **Zuken CR-8000 2026** | Zuken(일본) | 해당 없음 | 자사 툴 | 회로도 자동 배선, AIPR, 설계 재사용 | 검증된 단축률 없음 | 과거 배치 지식 재사용(Dynamic Brain) | 기업용 | 대기업 전문가 | [Zuken](https://www.zuken.com/en/resource/cr-8000-2026-pcb-design-automation/) |
| **Flux** | 2019(단일 출처) / 샌프란시스코 | $37M(2026-02-27: B $27M 8VC + A $10M) | 텍스트 프롬프트, 브라우저 에디터 | 회로도, 자동 레이아웃, 내보내기 | 미공개 | "투명한 AI 에이전트", Copilot | Pro $250/월(연간 $200), 400 ACU, 14일 체험(2026년 10월 제3자) | 초보자부터 전문가, 가입 100만+ | [SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/), [AnyGen](https://www.anygen.io/showcase/fluxai-review/index.html) |
| **Circuit Mind** | 2018 / 런던 | $25M(2026-10-28: A $18.5M Norwest + Seed), 누적 $33.4M | 블록도, 기존 회로도(AVE) | 회로도, BOM, 전력·디레이팅, FMEA, 검증 리포트 | ACE 약 60초(자사) 또는 10분 미만(ipXchange) | 데이터시트, 앱노트, 체크리스트 대조 검증(AVE) | 미공개 | 기업(LANL, Emerson) | [SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/), [ipXchange](https://ipxchange.tech/product-news/go-from-block-diagram-to-bom-in-minutes-meet-circuit-minds-ace-tool/) |
| **CELUS** | 2017/2018 / 뮌헨 | Seed €1.7M, A €25M(2022-07, Earlybird) | 기능 블록(요구사항) | 회로도, BOM(, 레이아웃) | 미확인 | 미확인 | 미확인 | 중소기업, 독립 엔지니어(1.5만 명, 2024) | [Tech.eu](https://tech.eu/2022/07/06/disrupting-fragmented-electronics-supply-chain-with-design-automation-celus-rakes-in-eur25-million/), [ChannelLife](https://channellife.com.au/story/siemens-celus-team-up-to-revolutionise-pcb-design) |
| **JITX** | 미국(YC) | A $12M(2022-09, Sequoia) | 코드 | 부품 선정, 배치, 배선, 검증 | 미확인 | 코드 자체가 근거 | 미확인 | 전문가 | [JITX](https://www.jitx.com/blog/series-a-announcement) |
| **Diode Computers** | 뉴욕(YC S24) | A $11.4M(2025-07, a16z) | Zener 코드, KiCad 임포트 | KiCad 레이아웃, Altium/Cadence 내보내기, 제조 견적 | 미확인 | 코드 기반 리뷰(버그 22개 발견 사례) | 오픈소스 툴체인 + 엔터프라이즈 설계 서비스 | 전문가(로보틱스, 의료, 항공) | [GitHub](https://github.com/diodeinc/pcb), [Dealroom](https://app.dealroom.co/news/feed/diode-computers-raises-11-4m-for-ai-pcb-design), [Diode 블로그](https://blog.diode.computer/hardware-review) |
| **atopile / tscircuit** | YC W24 / 미확인 | 소규모·상충 | 코드 | 회로도, PCB | — | — | MIT 오픈소스 무료 | 개발자 | [Silixon](https://silixon.io/blog/best-ai-pcb-design-tools), [f4.fund](https://f4.fund/startups/tscircuit) |
| **Cherry Blossom** | 2026 출시 / 미확인 | 미확인 | 평문 프롬프트 | 회로도, 레이아웃, BOM, 제조 파일 | 미확인 | 미확인 | 무료(AI 없음), AI Pro $20/월 | 초보자부터 메이커 | [Product Hunt](https://www.producthunt.com/products/cherry-blossom) |
| **ProtoFlow** | 미확인 | 미확인 | 프롬프트(데스크톱) | 회로도 → KiCad/Altium, 레이아웃, SPICE, Gerber | 미확인 | 미확인 | 무료 일 15 AI 메시지 | 메이커, 엔지니어 | [Product Hunt](https://www.producthunt.com/products/protoflow-2) |
| **Cirkit Designer** | 미확인 | 미확인 | 자연어 설명 | 배선도, Arduino 코드, 시뮬레이션 | 미확인 | AI가 배선 질문에 답변 | 무료 시작 + 유료 멤버십 | 초보자(Arduino) | [Cirkit Designer](https://www.cirkitdesigner.com) |
| **EasyEDA/JLC** | 중국 | 해당 없음 | EasyEDA Pro + 외부 AI 에이전트(브리지) | 수동 설계 + DeepPCB 연계 | — | 1st-party AI 없음 | EasyEDA 무료 | 메이커, 초보자 | [JLCPCB](https://jlcpcb.com/blog/ai-tools-for-pcb-design), [Adafruit](https://blog.adafruit.com/2026/09/19/jlc-puts-ai-assisted-board-design-in-files-you-can-read-review-and-edit/) |
| **Altium (Renesas)** | 호주 기원 / Renesas 그룹 | 해당 없음 | 자사 툴 | 수동 설계 + 비AI 라우터 | — | Requirements용 Engineering Assistant | 구독(Discover/Develop/Agile) | 전문가 | [Wikipedia](https://en.wikipedia.org/wiki/Altium_Designer) |
| **Autodesk Fusion Electronics** | Autodesk | 해당 없음 | 자사 툴 + Python API | 전통 오토라우터, NETROUTE(회로도) | — | 없음 | Fusion 구독 | 메이커부터 기계·전자 통합 팀 | [Autodesk](https://www.autodesk.com/products/fusion-360/blog/september-2026-major-product-update-whats-new/) |

### Inferences
- "파일을 올리면 사람이 리뷰할 수 있는 설계안과 근거 리포트를 받는" 서비스형 모델과 가장 닮은 해외 사례는 Quilter(레이아웃 후보 + 물리 리뷰)와 Circuit Mind(회로도 + BOM + FMEA + 검증 리포트)입니다. 둘 다 기업과 전문가를 겨냥합니다.
- 초보자 타깃 해외 제품(Flux, Cirkit Designer, Cherry Blossom)은 대화형 에디터 UX입니다. "업로드 후 기다리면 완성안이 오는" 비동기 서비스형과는 UX가 다릅니다.

### Gaps
- 표의 "미확인" 칸은 이번 검색으로 1차 근거를 찾지 못한 항목입니다. 추측으로 채우지 않았습니다.
- 각사 출력의 ODB++, IPC-2581 지원 여부는 확인하지 못했습니다(Quilter의 Gerber/Excellon만 확인).

## 4. 시장 맥락: PCB 설계 소프트웨어·AI-EDA 시장 규모와 추세

### Takeaway
2026년 PCB 설계 소프트웨어 시장은 조사기관에 따라 약 $3.8B–6.2B로 추정되고, 연평균 성장률(CAGR)은 대략 8–15%입니다. 2025–2026년에는 Cadence, Siemens, Zuken이 AI·에이전트 기능을 내놓는 한편 Quilter, Flux, Circuit Mind, Diode 같은 스타트업에 VC 자금이 몰렸습니다.

### Cited Findings
- Straits Research: 2026년 $4.38B → 2034년 $11.08B(CAGR 약 12.3%). 2025년 북미 점유율 38.2%. — [Straits Research](https://straitsresearch.com/report/pcb-design-software-market)
- Precedence Research: 2026년 약 $4.7B → 2035년 약 $16.02B. — [Precedence Research](https://www.precedenceresearch.com/pcb-design-software-market)
- Grand View Research: 2025년 $5.4B, 2026년 약 $6.1B. — [Grand View Research](https://www.grandviewresearch.com/industry-analysis/pcb-design-software-market-report)
- Future Market Insights: 2026년 $6.16B → 2036년 $25.13B. — [FMI](https://www.futuremarketinsights.com/reports/pcb-design-software-market)
- MarkWide Research: 2026년 $3.8B → 2035년 $7.85B. 별도 집계한 PCB CAD 시장은 2026년 $2.4B. — [MarkWide](https://markwideresearch.com/pcb-design-software-market); [MarkWide PCB CAD](https://markwideresearch.com/pcb-cad-software-market)
- 신뢰하기 어려운 수치: DEV Community 글의 "AI EDA 분기 매출 $4.2B(2026년 1분기)"는 출처가 불명확하고 다른 추정치와도 맞지 않아 쓰지 않는 것이 좋습니다. — [DEV Community](https://dev.to/abc_8b09c7009ee0029b85665/ai-powered-eda-tools-see-20th-consecutive-quarter-of-growth-42b-market-in-q1-2026-35kc)
- 업계 이벤트: Siemens AI PCB 툴(2025년 5월), Siemens의 ASTER 인수(2026년 1월), Cadence AuraStack(2026년 7월). — [Persistence](https://www.persistencemarketresearch.com/market-research/pcb-design-software-market.asp); [Straits](https://straitsresearch.com/report/pcb-design-software-market); [Cadence](https://newsroom.cadence.com/press-releases/press-release-details/2026/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging/default.aspx)
- VC 투자 흐름(2025–2026): Diode $11.4M(2025년 7월), Quilter $25M(2025년 10월), Vinci $36M(2025년 12월, 칩 시뮬레이션), Flux $37M(2026년 2월), Circuit Mind $25M(2026년 10월). — [Dealroom](https://app.dealroom.co/news/feed/diode-computers-raises-11-4m-for-ai-pcb-design); [I-Connect007](https://iconnect007.com/article/147236/quilter-secures-25m-series-b-to-eliminate-manual-pcb-design-with-physicsdriven-ai/147233/design); [SiliconANGLE (Vinci)](https://siliconangle.com/2025/12/03/vinci-nabs-46m-speed-chip-simulations-ai/); [SiliconANGLE (Flux)](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/); [SiliconANGLE (Circuit Mind)](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/)
- LLM 연계 추세: JLC(EasyEDA)는 Claude Code/Codex 연동 워크플로를, Altium은 MCP 서버(Coming Soon)를 준비 중이며, Diode는 Anthropic과 협업했습니다. — [JLCPCB](https://jlcpcb.com/blog/ai-tools-for-pcb-design); [Diode 블로그](https://blog.diode.computer/anthropic-partnership)

### Inferences
- 시장 규모 추정치가 기관마다 2배 가까이 차이 나므로, 보고서에서는 범위($4–6B, 2026)로 제시하는 편이 안전합니다.
- 2025–2026 펀딩 라운드들은 "AI PCB 설계" 범주가 VC의 독립 투자 테마로 자리 잡았음을 보여 줍니다. 국내 서비스 입장에서는 시장 검증 신호이자, 해외 선발 주자가 이미 존재한다는 위협 신호이기도 합니다.

### Gaps
- AI-EDA(AI PCB 설계)만 따로 떼어 낸 시장 규모는 신뢰할 만한 출처에서 찾지 못했습니다.
- 위 시장조사 보고서들은 요약 페이지만 확인했고, 방법론과 범위(PCB CAD 단독인지 시뮬레이션 포함인지)는 검증하지 못했습니다.

## 5. 모디팩토리의 가치 제안(90분, 설계 근거, 무료 온보딩, 초보자, 다중 포맷) 차별성 평가

### Takeaway
개별 기능(빠른 처리, 근거·리뷰 리포트, 무료 진입, 다중 포맷 내보내기)은 해외에 이미 하나 이상 존재합니다. 다만 "초보자 대상 + 파일 업로드형 비동기 서비스 + 레이아웃 제안 + 이해하기 쉬운 설계 근거"를 한데 묶은 해외 제품은 이번 조사에서 확인되지 않았습니다. 차별화의 핵심은 기능 하나하나가 아니라 이 조합과 타깃 세그먼트에 있습니다.

### Cited Findings
- **빠른 처리:** Circuit Mind ACE는 회로도·BOM 생성에 약 60초에서 10분 미만, DeepPCB는 배선 중앙값 수 분, Cadence Allegro X AI는 "수일 → 수분"을 주장합니다. 반면 Quilter의 복잡 보드(843부품) 생성 런타임은 약 27시간이었습니다. — [ipXchange](https://ipxchange.tech/product-news/go-from-block-diagram-to-bom-in-minutes-meet-circuit-minds-ace-tool/); [ProtoFlow (경쟁사 작성)](https://www.protoflow.ai/compare/ai-pcb-autorouter-comparison); [Cadence](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2023/cadence-introduces-allegro-x-ai-accelerating-pcb-design-with.html); [VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the)
- **설계 근거·리뷰:** Quilter는 레이아웃 후보마다 물리 기반 design review를 붙이고 후보에 순위를 매깁니다. Circuit Mind는 FMEA, 디레이팅 분석, 데이터시트 대조 검증(AVE)을 제공합니다. Flux는 "투명한 AI 에이전트"를 표방합니다. — [Quilter Help](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work); [SiliconANGLE (Circuit Mind)](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/); [SiliconANGLE (Flux)](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)
- **무료 진입:** Quilter는 개인·학술 무료(대신 입력 파일을 학습에 활용), DeepPCB는 1보드 체험만, Flux는 14일 체험 후 유료, Cherry Blossom은 AI 없는 무료, ProtoFlow는 일 15 AI 메시지 무료, Diode, atopile, tscircuit은 오픈소스입니다. — [Futurepedia](https://www.futurepedia.io/tool/quilter); [cadalts](https://cadalts.com/tools/deeppcb/); [AnyGen](https://www.anygen.io/showcase/fluxai-review/index.html); [Product Hunt (Cherry Blossom)](https://www.producthunt.com/products/cherry-blossom); [Product Hunt (ProtoFlow)](https://www.producthunt.com/products/protoflow-2); [GitHub diodeinc/pcb](https://github.com/diodeinc/pcb)
- **초보자 타깃:** 자금력이 큰 해외 업체는 대부분 기업과 전문가가 대상입니다. Quilter는 항공우주·국방, Circuit Mind는 LANL·Emerson, Diode는 로보틱스·의료·항공우주, Cadence와 Zuken은 대기업입니다. 초보자·메이커 친화 제품은 Flux(가입 100만+), Cirkit Designer(Arduino), Cherry Blossom, EasyEDA 정도입니다. — [Seedtable](https://seedtable.com/companies/quilter); [Electromaker](https://www.electromaker.io/blog/article/circuit-mind-turns-block-diagrams-into-schematics-fast); [yespress (Diode)](https://yespress.io/diode-computers-inc); [Cirkit Designer](https://www.cirkitdesigner.com)
- **다중 포맷 출력:** Quilter는 Gerber/Excellon과 원본 EDA 포맷, Diode는 KiCad, Altium, Cadence 내보내기, ProtoFlow는 KiCad와 Altium 내보내기, Cherry Blossom은 제조 파일을 출력합니다. — [Quilter 블로그](https://www.quilter.ai/blog/from-ai-design-to-manufacturing-how-quilter-automates-gerber-drill-and-fab-file-generation); [GitHub diodeinc/pcb](https://github.com/diodeinc/pcb); [Product Hunt (ProtoFlow)](https://www.producthunt.com/products/protoflow-2)
- **데이터 정책도 비교 포인트입니다:** Quilter 무료 티어는 입력 파일을 학습에 쓰고, ProtoFlow는 기본적으로 학습에 쓰며(옵트아웃 가능), Cherry Blossom은 외부 AI 제공자로 데이터를 보냅니다. — [Futurepedia](https://www.futurepedia.io/tool/quilter); [Cherry Blossom 블로그](https://www.trycherryblossom.com/blog/protoflow-alternative)

### Inferences
- **이미 흔한 요소(차별성 낮음):** 다중 포맷 출력과 무료 진입은 해외에서 흔합니다. "AI가 빠르게 설계안을 낸다"는 점도 Circuit Mind, DeepPCB, Cadence가 분 단위를 주장하므로 90분이 압도적으로 빠르다고 보기는 어렵습니다. 다만 비교 대상의 범위(회로도만인지, 배선만인지, 엔드투엔드인지)가 서로 달라 직접 비교는 불가능합니다.
- **상대적으로 차별 가능한 요소:** (1) 해외의 "근거·리뷰" 기능은 전문가용 물리 검토(임피던스, FMEA 등)입니다. 초보자가 읽을 수 있는 서술형 설계 근거(왜 이 부품, 왜 이 배치인지)를 기본 제공한다면 차별화 여지가 있습니다. (2) 해외 초보자용 도구는 대화형 에디터(Flux, Cherry Blossom)이거나 회로도·브레드보드 수준(Cirkit)입니다. "파일만 올리면 일정 시간 안에 PCB 설계안을 돌려주는 서비스형 UX"를 초보자에게 무료로 제공하는 해외 사례는 이번 조사 범위에서 찾지 못했습니다. (3) 한국어 지원과 국내 제조·조달 연계는 해외 제품에서 확인되지 않아 현지화 우위가 될 수 있습니다(직접 검색으로 확인한 것은 아니며 추론입니다).
- **위협 요인:** Flux(100만 가입, $37M)가 초보자 시장을 이미 선점하고 있고, Quilter는 무료 티어로 비상업 사용자를 흡수할 수 있습니다. JLC/EasyEDA도 LLM 에이전트 연동(2026년 베타 예정)을 추진 중이어서, 저가 PCB 제조사와 묶인 AI 설계라는 형태로 모디팩토리와 직접 경쟁할 가능성이 있습니다.
- **검증 필요 포인트:** 모디팩토리의 "90분"이 어떤 입력(회로도, 넷리스트, 요구사항 문서 중 무엇인지)에서 어떤 산출물(배치, 배선, Gerber 중 어디까지)까지인지 명확해야 Quilter, Circuit Mind와 동일한 기준으로 비교할 수 있습니다.

### Gaps
- 모디팩토리의 실제 입력 포맷, 출력 포맷, 처리 범위를 이 조사에서 검증하지 않았으므로 기능 대 기능의 정밀 비교에는 한계가 있습니다(국내 조사 담당 자료와 대조 필요).
- 해외 제품의 실제 사용자 만족도, 첫 시도 성공률(first-pass yield)에 관한 독립 벤치마크는 찾지 못했습니다(Quilter Speedrun은 자사 사례).
- Hacker News 등 커뮤니티 평판은 이번에 조사하지 못했습니다(도구 호출 한도).
