# 국내(한국) 학술논문·학위논문·특허·국가 R&D: AI 기반 PCB 설계 자동화

> 조사일: 2026-11-16 / 대상 기간: 2018–2026 우선
> **검증 방식에 관한 중요 제약:** 이 세션의 네트워크 정책 때문에 KCI(kci.go.kr), RISS, DBpia, ScienceON, NTIS, KIPRIS, KAIST 저장소(koasas/dspace), ee.kaist.ac.kr, alphaxiv, lgresearch.ai 페이지는 직접 열 수 없었다(WebFetch DNS 차단, curl 000). 그래서 아래 항목은 **검색엔진이 돌려준 각 원문 페이지의 메타데이터와 스니펫(제목·저자·연도·학술지·URL)으로 확인**했다. 본문 전체를 읽고 확인한 것이 아니므로 최종 보고서에 인용할 때는 링크를 다시 열어 확인하는 것을 권한다. "찾지 못함"은 "웹 검색으로 확인되지 않음"이라는 뜻이며, 해당 자료가 없다는 증거는 아니다.

---

## 1. 국내 학술지·학술대회 논문 (KCI, 대한전자공학회 등): AI/ML을 활용한 PCB 배치·배선·회로도 생성·설계 검증

### Takeaway
웹 검색 범위 안에서는 **AI/ML로 PCB 부품 배치나 배선을 다룬 KCI 등재 논문을 한 편도 확인하지 못했다.** 국내 학술지에 실린 PCB 자동 배치·배선 연구는 대부분 1995–2014년의 비AI 알고리즘(그리드, 최단경로, Shape-based) 연구다. 최근 사례는 학술대회 포스터 수준의 "생성형 AI 기반 설계 검증 도구"(2025)가 거의 전부이고, 국내 PCB AI 연구의 대다수는 결함·비전 **검사** 분야에 몰려 있다.

### Cited Findings
**(a) 국내 PCB 자동 배치·배선 논문 (비AI, 과거 계보)**
- 「Shape Based 방식에 의한 PCB 자동 배치 시스템에 관한 연구」: 대한전자공학회 전자공학회논문지-IE, 2003. KCI에 등재된 알고리즘 기반 PCB 자동 배치 연구다. — [KCI ART000904787](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART000904787)
- 「개선된 그리드 알고리즘을 이용한 PCB 자동 배선 시스템개발에 관한 연구」: 대한전자공학회 학술대회 논문이며, 검색 요약상 1995년이다. — [DBpia NODE06304638](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06304638)
- 「최단경로를 이용한 PCB 자동 배선 시스템 설계」: 우경환·이용희·임태영·이천희, 대한전자공학회 학술대회, 2001.6. — [DBpia NODE06329246](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06329246)
- 「제어된 임피던스용 다층 PCB 설계 시뮬레이터 구현」: 전자공학회논문지-SD, 2011. 다층 PCB 선로 패턴의 트랙 계산과 임피던스 자동 분석 시뮬레이터를 다루며 AI는 쓰지 않았다. — [KCI ART001612461](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001612461)
- 「회로해석 및 PCB 전자장 분석을 위한 웹 기반 자동화프로세스에 관한 연구」: 전기학회논문지 63권 12호, 2014. 회로 해석과 PCB 전자장 분석을 웹 기반으로 자동화했다. — [KCI ART001932976](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001932976)

**(b) 최근 국내 AI·설계 관련 학술대회 발표 (2018년 이후)**
- 한국산학기술학회 2025 춘계학술발표논문집 p.657 포스터. 생성형 AI로 Python 도구를 만들어 회로도(.asc) 파일을 분석한다. 회로 설계에서는 테스트 포인트 누락·중복을 검출하고, PCB 설계에서는 디커플링 커패시터 거리를 분석한다. 전장품 회로·PCB 설계 검증을 대상으로 하며, 저자와 소속은 확인하지 못했다. — [KAIS 2025 춘계 포스터 PDF](https://www.kais99.org/jkais/springNfall/spring2025/poster/2025_spring_227.pdf)
- 2023 대한전자공학회 하계학술대회 논문집은 856편 규모다. 검색 결과에서 PCB 배치·배선 AI 논문은 개별적으로 확인되지 않았다. — [DBpia VOIS00727004](https://www.dbpia.co.kr/journal/voisDetail?voisId=VOIS00727004)

**(c) 맥락: PCB 검사(AOI/비전) 연구 (설계 자동화와 다른 분야)**
- 「딥러닝 영상인식을 이용한 PCB 기판 비전 검사 시스템 개발」: 한국컴퓨터정보학회 동계학술대회 논문집, 2024. — [KoreaScience CFKO202419335083786](https://koreascience.kr/article/CFKO202419335083786.pdf)
- 「CAD 데이터를 이용한 PCB 검사에 관한 연구」: 국민대 박사학위논문, 2010. Gerber 등 CAD 데이터를 기반으로 한 시각 검사 연구다. — [ScienceON DIKO0011990865](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0011990865&dbt=DIKO)
- 국제적으로도 "PCB + 딥러닝" 검색 결과의 대부분은 YOLO 계열 결함 검출 논문이다(PCB-YOLO, YOLOv11-PCB 등). 설계 자동화 논문보다 훨씬 많다. — [PCB-YOLO (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12129336/); [YOLOv11 PCB (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12663553/)

### Inferences
- 국내 학술지 생태계에는 "AI 기반 보드 레벨 PCB 배치·배선·회로도 생성" 연구가 사실상 비어 있는 것으로 보인다. 국내 PCB 자동화 학술 계보는 2000년대 초 알고리즘 연구 이후 거의 끊겼다가, 2025년 생성형 AI 기반 설계 검증(DRC 성격) 포스터로 다시 나타나는 정도다.
- 국내 "PCB × AI" 학술 활동은 압도적으로 **검사(AOI)** 중심이다. 모디팩토리가 다루는 **설계 생성 영역은 국내 학술 선행연구가 얇다.** 학술 협력이나 논문화를 하면 선점 효과가 클 수 있다.
- 2025 KAIS 포스터는 "LLM으로 설계 검증 스크립트를 생성하는" 접근이다. 모디팩토리의 'AI 노트'나 검증 기능과 개념적으로 가장 가까운 국내 학술 사례다.

### Gaps
- KCI, DBpia, RISS, ScienceON을 직접 검색할 수 없었으므로 "강화학습 PCB", "PCB 자동 배치 딥러닝", "회로도 자동 생성 LLM" 키워드의 2018–2026 KCI 전수 조회는 하지 못했다. 한국정보처리학회·한국통신학회·한국정보통신학회·한국인공지능학회 학술대회 논문집의 개별 PCB 설계 AI 논문 존재 여부는 미확인으로 남는다.
- 2025 KAIS 포스터의 저자, 소속, 정확한 제목을 확인하지 못했다(PDF 직접 열람 불가).

---

## 2. 국내 석·박사 학위논문 (RISS, KAIST 저장소 등): PCB 자동 배선·배치, 강화학습, 딥러닝 EDA

### Takeaway
**보드 레벨 PCB 자동 배치·배선을 딥러닝이나 강화학습으로 다룬 국내 학위논문은 확인하지 못했다.** 반면 KAIST 김정호 교수 지도 아래 **패키지·인터포저·HBM 수준의 디커플링 커패시터 배치와 TSV 설계에 강화학습을 적용한 석사논문**이 2019년부터 꾸준히 나왔다. 국내 "강화학습 × 전자설계" 학위논문의 사실상 유일한 집중 지점이다.

### Cited Findings
- KAIST 전기및전자공학부 석사논문(2019.2) 「2.5차원/3차원 집적회로의 동시 스위칭 잡음 감소를 위한 심층 강화학습 기반의 최적 디커플링 캐패시터 설계 방법론」. 지도교수는 김정호다. 심층 Q-러닝(DQN)으로 디캡 설계를 자동화하며, 전력 분배망(PDN) 구조와 단위 셀당 커패시턴스만으로 설계 자동화를 구현한다. — [KAIST KOASAS 10203/266736](https://koasas.kaist.ac.kr/handle/10203/266736)
- KAIST 전기및전자공학부 석사논문(2023.2). 키워드는 심층 강화학습, 고대역폭 메모리(HBM), 신호 무결성(SI)이다. 검색 요약에는 HBM용 TSV 배열을 SI 기준으로 MDP와 DQN 에이전트로 최적화하는 연구가 언급되지만, 이 논문과 정확히 일치하는지는 확인하지 못했다. — [KAIST DSpace 10203/309847](https://dspace.kaist.ac.kr/handle/10203/309847)
- 이후 KAIST 학위논문은 하이브리드 본딩 TSV 설계에 RNN 정책망, 모델링 기반 보상 시뮬레이션, CAPG(clipping policy gradient)를 적용한 것으로 검색 요약에 나온다. 서지는 미확인이다. — [KAIST 저장소 검색결과(DSpace 10203/295947)](https://dspace.kaist.ac.kr/handle/10203/295947?mode=full)
- RISS 검색에서는 "PCB 자동 배선 + 딥러닝" 학위논문이 나오지 않았다. 관련 결과는 비AI 학술대회 논문(1995, 2001)과 국민대 2010 박사논문(CAD 데이터 기반 PCB 검사)뿐이었다. — [DBpia NODE06304638](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06304638); [ScienceON DIKO0011990865](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0011990865&dbt=DIKO)

### Inferences
- 국내 학위논문의 "AI 배치" 연구는 **SI/PI 지표(임피던스, SSN, 아이다이어그램)를 보상으로 쓰는 패키지 수준 문제**에 집중되어 있다. 일반 보드의 부품 배치나 배선(DRC, 배선 완료율, 와이어 길이)을 다룬 학위 연구는 공백으로 보인다.
- 이 공백은 모디팩토리 같은 기업이 산학과제(석사 과정 연계)를 설계할 때 차별화된 주제가 될 수 있다. 예를 들면 LLM 기반 배치, 에어와이어 특징 기반 배치 평가, 국산 부품 라이브러리 기반 회로도 생성이 있다.

### Gaps
- RISS와 KAIST 저장소 원문을 열 수 없어 2019·2023 석사논문의 저자명을 확인하지 못했다.
- 서울대·포항공대·성균관대·고려대·UNIST의 "PCB 배치·배선 강화학습" 또는 "딥러닝 EDA" 학위논문 존재 여부를 확인하지 못했다. 칩(VLSI) 배치 ML 학위논문은 여러 대학에 있을 것으로 추정되지만 검증하지 못했다.

---

## 3. 한국 대학·연구기관·기업 연구소의 국제 발표: KAIST TeraLab, LG AI연구원 등

### Takeaway
**KAIST TeraLab(김정호 교수)의 강화학습 기반 디커플링 커패시터 배치 연구는 사실로 확인된다.** EPEPS 2021, IEEE TCPMT 2020, ICML 2023(DevFormer, 박진규 교수 공동)이 있고, 2025–2026년에는 LLM 기반 HBM 설계 에이전트와 KiCad MCP 기반 패키지 설계 AI 에이전트로 확장되고 있다. 다만 **"HBM 인터포저 배선(routing)을 강화학습으로 푼 논문"은 특정 논문으로 확인하지 못했다.** 로드맵의 "HBM8 3D 배치·배선 최적화 AI 에이전트"와 2015년 비RL 인터포저 배선성 연구가 가장 가까운 항목이다. 보드 레벨 PCB 배선에서 가장 직접적인 국내 연구 주체는 **LG AI연구원**이다(PCBWorld 2026, CADET 2026).

### Cited Findings
**(a) KAIST TeraLab (김정호 교수): SI/PI 인지형 강화학습 설계**
- EPEPS 2021 「Deep Reinforcement Learning Framework for Optimal Decoupling Capacitor Placement on General PDN with an Arbitrary Probing Port」: Haeyeon Kim, Hyunwook Park, Joungho Kim 외. 포인터 네트워크 정책을 REINFORCE로 학습한다. 무작위 keep-out 영역이 있는 PDN에 디캡 20개를 배치하고, 100MHz–20GHz 구간의 434개 주파수에서 임피던스를 평가했다. 적은 샘플로도 랜덤 탐색 휴리스틱보다 우수했다. DOI 10.1109/EPEPS51341.2021.9609194. — [KAIST EE 소개 페이지](https://ee.kaist.ac.kr/ai-in-wave/deep-reinforcement-learning-framework-for-optimal-decoupling-capacitor-placement-on-general-pdn-with-an-arbitrary-probing-port-epeps-2021/); [KAIST DSpace 10203/304973](https://dspace.kaist.ac.kr/handle/10203/304973?mode=full)
- IEEE TCPMT(2020): 실리콘 인터포저 기반 2.5D/3D IC의 최적 디캡 설계에 심층 강화학습을 적용했다. Youngwoo Kim, Joungho Kim 외. 10^17–10^18 경우의 수를 다루며, 딥러닝을 쓰지 않은 기존 RL보다 10^12–10^13배 넓은 설계 공간을 탐색한다고 보고했다. — [DOI 10.1109/TCPMT.2020.2972019](https://doi.org/10.1109/TCPMT.2020.2972019)
- **DevFormer** (ICML 2023, PMLR 202:16541–16566): Haeyeon Kim, Minsu Kim, Federico Berto, Joungho Kim, Jinkyoo Park(KAIST 산업및시스템공학과 SILAB). 디캡 배치를 위한 대칭성 트랜스포머(action-permutation symmetricity, 상대 위치 임베딩)로 오프라인 데이터만으로 학습한다. 시뮬레이션과 실제 하드웨어 모두에서 SOTA보다 우수했고 **부품 수를 30% 이상 줄였다.** NeurIPS 2022 Offline RL 워크숍 논문의 확장판이며, 코드는 github.com/kaist-silab/devformer에 있다. — [PMLR](https://proceedings.mlr.press/v202/kim23h.html); [arXiv 2205.13225](https://arxiv.org/abs/2205.13225v3)
- HBM PDN 디캡 최적화를 위한 트랜스포머 네트워크 기반 강화학습(2022, 저널): Hyunwook Park, Minsu Kim, Joungho Kim 외. 여러 포트에서 보이는 자기·전달 임피던스를 최대한 줄이도록 디캡을 설계한다. — [KAIST 저장소 검색결과(KOASAS 10203/299936)](https://koasas.kaist.ac.kr/handle/10203/299936?mode=full) (게재 저널명은 검색 결과에서 확인하지 못함)
- HBM 모듈용 하이브리드 이퀄라이저를 심층 강화학습으로 빠르게 최적 설계하는 방법(IEEE 레코드 10255709). 정책망이 임의의 인터포저 채널 치수에 맞는 이퀄라이저 파라미터를 바로 설계한다. — [IEEE 레코드 (bib-bvb 색인)](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_ieee_primary_10255709)
- 신태인 박사(김정호 교수 연구실)는 HBM 패키지 전력 무결성(PI) 설계 최적화 연구로 **DesignCon 2025 Best Paper Award**를 받았다. — [KAIST EE 뉴스](https://ee.kaist.ac.kr/en/research-achieve/dr-taein-shin-from-professor-jeongho-kims-research-lab-selected-for-best-paper-award-at-designcon-2025-international-conference/); [아시아경제 영문](https://www.asiae.co.kr/en/article/2025030415183042006)
- 초기 ML 연구로는 Sung Joo Park, Bumhee Bae, Joungho Kim, Madhavan Swaminathan의 IEEE TVLSI 2017(3D IC의 ML 기반 SI/PI 설계)이 있다. KAIST EE 페이지는 "SI/PI를 고려한 최적 레이아웃 설계를 강화학습으로 수행할 수 있다"고 소개한다. — [KAIST EE AI-in-Wave](https://ee.kaist.ac.kr/ai-in-wave/16890/)
- **인터포저 배선 관련 확인 결과:** 2015 EDAPS 논문(김정호 공저)은 배선 가능성(routing feasibility)을 고려해 HBM 인터포저 top-metal 신호를 최적화했고, 3D EM 시뮬레이션과 아이 오프닝·지터를 비교했다. 강화학습 이전의 연구다. — [KAIST EE (검색 요약)](https://ee.kaist.ac.kr/?p=116890)
- 연구실 홈페이지가 소개하는 RL 프로젝트는 계층형 PDN 위 디캡 배치 문제(DPP), HBM 수동 이퀄라이저 최적화, SI/PI 설계용 "RL-X Architect"다. 연구 분야에는 SiP/PCB Design이 포함된다. — [KAIST TERA Lab](https://tera.kaist.ac.kr/); [김정호 교수 페이지](https://ee.kaist.ac.kr/en/professor/12153/)
- "HBM Roadmap Ver 1.7" 워크숍 자료(2025.6.11)에는 **LLM 기반 HBM7 설계 에이전트(디캡 배치를 위한 Interactive RL)**와 **"AI Design Agent for 3D Placement and Routing Optimization for HBM8"**이 들어 있다. HBM 패키지가 대상이며 PCB는 아니다. — [KAIST TERALAB HBM Roadmap PDF](https://aionet.tech/KAIST_HBM_Roadmap.pdf)
- 2026년 7월 3일 KAIST는 "OpenClaw AI 에이전트를 활용한 HBM 설계·연구 자동화 워크숍"을 열었다. 예정된 발표에는 **KiCad MCP를 이용한 패키지 설계·해석 AI 에이전트**, PDN 시뮬레이션, 아이다이어그램 데이터셋과 이퀄라이저 최적화, PyAEDT 기반 Ansys 전자기 시뮬레이션 자동화가 있었다(결과 보고는 미확인). — [Korea Times 2026-07-02](https://www.koreatimes.co.kr/amp/southkorea/education/20260702/kaist-workshop-to-showcase-ai-agents-for-hbm-design-automation)
- 연구실 관련 연구로 마이크로범프 패키지의 SI/PI 열화를 줄이는 핀 배정 DRL 프레임워크 "Pin-opt"가 있고, 디캡 배치에 협력 증류 메타러닝(CDML)을 적용한 연구도 있다. 둘 다 학회와 저자는 미확인이다. — [ResearchGate 김정호 프로필](https://www.researchgate.net/profile/Joungho-Kim)

**(b) LG AI연구원: 보드 레벨 PCB 배선 (국내에서 가장 직접적인 PCB AI 설계 연구)**
- **PCBWorld** (arXiv 2607.05915, 2026.7.7 제출; KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI 채택, non-archival): Hyungseok Song, Junseok Park, Won-Seok Choi, Seohui Bae, Han-Seul Jeong, Youngjoon Park, Soonyoung Lee 외(LG AI Research, 서울). KiCad 엔진 기반 오픈소스 PCB 배선 환경으로, KiCad DRC 피드백을 사용한다. 합성 인스턴스 2종과 **실제 오픈소스 보드 679개**를 담았고, 엔진이 검사하는 평가 지표 8개를 제공한다. RL 에이전트와 LLM 에이전트를 모두 지원하며, 코드는 github.com/LGAI-Research/PCBWorld에 있다. — [arXiv 2607.05915](https://arxiv.org/abs/2607.05915); [KDD 워크숍 PDF](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/assets/papers/42_PCBWorld_A_Benchmark_Enviro.pdf)
- **CADET: Construction of PCB Routing Instances with Executable Demonstrations** (arXiv 2611.16913): LG AI Research가 PCB 배선 학습용 합성 데이터셋 RouteDemos와 생성 코드를 공개했다. 행동 복제 후 강화학습으로 미세조정한 정책은 실제 테스트 보드에서 **DRV 없는 배선 완료율을 38.0%에서 67.2%로** 올렸다. 학회 게재 정보는 없고 코드는 github.com/LGAI-Research/CADET에 있다. — [arXiv 2611.16913](https://arxiv.org/html/2611.16913)
- LG AI Research 블로그 「PCB 설계 자동화를 위한 AI 배선 연구」는 RRT 기반 연속공간 배선(RRT-PCB)이 LG 계열사 실제 제품으로 검증되었다고 소개한다. 자체 휴리스틱 Pathfinder++도 언급한다. 영문 블로그 「AI-Powered PCB Design Automation」도 있다. — [LG AI Research Blog seq=509](https://www.lgresearch.ai/blog/view?seq=509); [seq=510](https://www.lgresearch.ai/blog/view?seq=510)

**(c) 기타**
- 칩(VLSI) 배치 분야의 「Parameter Optimization of VLSI Placement Through Deep Reinforcement Learning」(IEEE TCAD 2022, Georgia Tech, 성균관대 소속 저자 포함)은 상용 EDA 툴의 배치 파라미터를 DRL로 최적화한다. PCB가 아니라 칩 연구다. — [논문 PDF (gtcad.gatech.edu)](https://gtcad.gatech.edu/www/papers/anthony-tcad22.pdf)

### Inferences
- 한국의 국제 수준 "AI × 전자설계" 역량은 두 축으로 나뉜다. (1) **KAIST: SI/PI 물리 지표를 보상으로 쓰는 패키지·HBM 배치 최적화.** 강화학습과 트랜스포머 연구를 거쳐 LLM 에이전트와 KiCad MCP로 옮겨 가고 있다. (2) **LG AI연구원: 보드 레벨 PCB 배선 벤치마크와 데이터셋**(KiCad DRC 기반 RL·LLM 에이전트 평가).
- 모디팩토리 관점에서 LG AI연구원의 PCBWorld(679개 실보드, 지표 8개)는 자사 자동 배선 품질을 객관적으로 보여 줄 **국산 공개 벤치마크** 후보다. KAIST의 KiCad MCP 에이전트와 디캡 배치 RL은 SI/PI 인지형 배치 기능을 붙일 때 협력하거나 참조할 대상이다.
- 사용자 가설 중 "디캡 배치 RL"은 확인되었다. "HBM 인터포저 배선 RL"은 로드맵(HBM8 3D 배치·배선 에이전트) 수준으로만 확인되었으므로 보고서에서는 "계획·로드맵 단계"로 표현하는 것이 안전하다.

### Gaps
- KAIST 저장소, IEEE Xplore, ee.kaist.ac.kr에 직접 접근할 수 없어 트랜스포머 RL HBM 논문(2022)의 게재 저널, Pin-opt와 CDML의 학회·저자, DesignCon 2025 수상 논문의 정확한 제목을 확인하지 못했다.
- POSTECH, 서울대, UNIST, ETRI, KETI의 PCB 설계 ML 국제 논문은 검색에서 나오지 않았다. 아날로그 레이아웃이나 칩 배치 ML 연구는 존재할 것으로 추정되지만 이번 조사 범위에서는 검증하지 못했다.
- 삼성전자 등 국내 대기업의 PCB 설계 AI 공개 논문은 찾지 못했다.

---

## 4. 국내 특허 (KIPRIS): AI 기반 PCB·회로 설계 자동화 (럭스로보 포함)

### Takeaway
**럭스로보는 「부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법」 특허로 2026 대한민국 우수특허대상을 받았다.** 언론은 이 특허를 MODI Factory의 핵심 "표준화 엔진"으로 소개한다. 핵심은 에어와이어의 길이·밀집도·교차 특징으로 배치와 배선을 사전 최적화하는 것이다. 그 밖에 국내에 등록된 "AI 기반 PCB 배치·배선" 특허는 웹 검색으로 확인하지 못했다. 이름이 비슷한 KR102208989B1은 PCB와 무관한 연산 그래프 디바이스 배치 특허로 보인다.

### Cited Findings
- 럭스로보(대표 오상훈)는 **「부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법」** 특허로 2026 대한민국 우수특허대상을 받았다. 보도에 따르면 이 특허는 MODI Factory의 핵심 표준화 엔진이다. 물리 배선 전 단계의 부품 간 가상 연결선을 '에어와이어(Air Wire)'로 정의하고, 길이·밀집도·교차 같은 구조 데이터를 뽑아 부품 배치와 배선 경로를 미리 최적화한다. — [THE VC 럭스로보 기업정보](https://thevc.kr/luxrobo) (원 보도 기사 URL, 특허번호, 출원·등록일, 청구항은 미확인)
- 같은 기업정보 페이지에는 럭스로보 보유 특허가 29건으로 집계되어 있다. 집계 시점에 따라 달라질 수 있다. — [THE VC](https://thevc.kr/luxrobo)
- 럭스로보 채용공고에서 보이는 기술 구성은 PCB AI 라우터·자동 배선 알고리즘, **LLM 기반 PCB 부품 자동 배치 모델**(회로 설계 규칙과 PCB 데이터로 주요 부품의 위치와 방향 결정), 회로 시뮬레이션 엔진이다. — [원티드: PCB AI 라우터·자동 배선 개발자](https://www.wanted.co.kr/wd/382684); [원티드: ML/AI 엔지니어(LLM 기반 PCB Placement)](https://www.wanted.co.kr/wd/382685); [원티드: 회로 시뮬레이션 엔진 개발자](https://www.wanted.co.kr/wd/382675)
- MODI Factory는 2026년 3월 독일 Embedded World 'Tools(설계 자동화)' 부문 글로벌 톱3에 들었고, 최종 후보에 오른 아시아 기업은 럭스로보뿐이었다. — [뉴스토마토](https://www.newstomato.com/ReadNews.aspx?no=1294739); [서울경제](https://www.sedaily.com/article/20019757)
- **KR102208989B1 「강화 학습을 통한 디바이스 배치 최적화」**: 우선일 2017-03-24, 패밀리는 WO2018175972A1과 EP4553715A3("Device placement optimization with reinforcement learning")이다. 영문 패밀리명과 미국 대응특허(US10692003B2)로 볼 때 Google LLC의 연산 그래프→하드웨어 디바이스 배치 특허로 추정되며, **PCB 부품 배치 특허가 아니다**(출원인은 원문으로 재확인 필요). — [Google Patents KR102208989B1](https://patents.google.com/patent/KR102208989B1/enExample); [EP4553715A3](https://patents.google.com/patent/EP4553715A3/enExample)
- 검색된 국내 PCB 배치 관련 특허는 비AI 구형 특허다. 예를 들어 CAD BOM 기반 부품 자동삽입 리스트 생성(KR101217747B1)과 PCB 역설계 장치(KR20150027929A)가 있다. — [KR101217747B1](https://patents.google.com/patent/KR101217747B1/ko); [KR20150027929A](https://patents.google.com/patent/KR20150027929A/ko)
- 삼성전자의 ML 기반 PCB 레이아웃·배선 자동 설계 특허는 웹 검색으로 확인하지 못했다. — (검색 결과 없음, 출처 없음)

### Inferences
- 공개 정보 기준으로 국내 **"AI 기반 PCB 설계 자동화" 특허는 럭스로보가 사실상 선도 출원인**으로 보인다. 에어와이어 구조 특징(길이·밀집도·교차) 기반 사전 최적화는 RL·LLM 기반 해외 접근(DeepPCB, LG AI의 배선 RL)과 구분되는 **"배선 전 단계 그래프 특징 공학"** 계열로 해석할 수 있다.
- KIPRIS를 직접 조회할 수 없었으므로 "국내 특허 공백"은 확정할 수 없다. 대기업(삼성·LG)이나 해외 기업(Google, Cadence, Synopsys)의 국내 출원 패밀리가 존재할 가능성이 높다.

### Gaps
- KIPRIS 접속 불가로 럭스로보 특허의 출원·등록번호, 출원일, 청구항, 발명자를 확인하지 못했다.
- Cadence, Synopsys, Siemens, Google의 PCB·칩 배치 AI 특허의 한국 패밀리와 LG전자·LG AI연구원의 PCB 배선 특허 출원 여부를 확인하지 못했다.

---

## 5. 국가 R&D 과제 및 정부 정책 (NTIS, IITP, KEIT, 산업통상부, 과기정통부)

### Takeaway
**"AI 기반 PCB 설계 자동화"를 직접 명시한 국가 R&D 과제나 공고는 확인하지 못했다.** 정부의 "설계 AI" 정책 자원은 **AI 반도체(칩) 설계 지원**에 몰려 있다. 2024 AI-반도체 이니셔티브의 "머신러닝 적용 설계 툴", 2025 과기정통부 AI반도체 최적화 설계지원 198억 원, 2026 산업통상부 K-온디바이스 AI반도체 8,002억 원이 그 예다. 산업부의 "AI+R&DI" 전략처럼 범산업 AI 활용 R&D도 있지만, PCB나 보드 설계 EDA는 정책 문서에 독립 항목으로 등장하지 않는다.

### Cited Findings
- 「AI-반도체 이니셔티브(안)」(2024.4.25, 관계부처 합동) 지원 분야에 **"설계 툴(머신러닝 적용 → 고집적 설계 자동화 혁신) 개발"**이 포함되어 있다. 반도체(칩) 설계 중심이다. — [국가과학기술자문회의 PDF](https://www.pacst.go.kr/jsp/m/initiative/ai_initiative_intro.pdf)
- 산업부는 'AI+R&DI 추진전략'에 따라 2025년 산업·에너지 분야 AI 활용 기술개발 과제 100개 이상을 지원한다. 2030년까지 600개를 추진하고, 2032년에는 산업부 신규 R&D 과제 전체에 AI를 활용할 계획이다. — [스마트시티 종합포털(산업부 보도 인용), 2025-03-10](https://smartcity.go.kr/2025/03/10/%EC%82%B0%EC%97%85%EB%B6%80-%EC%98%AC%ED%95%B4-ai-%ED%99%9C%EC%9A%A9-%EA%B8%B0%EC%88%A0%EA%B0%9C%EB%B0%9Crd-%EA%B3%BC%EC%A0%9C-100%EA%B0%9C-%EC%9D%B4%EC%83%81-%EC%A7%80%EC%9B%90/)
- 과기정통부 2025 『AI반도체 최적화 설계지원』 사업 통합공고(제2025-0775호): 접수 기간은 2025.7.21–8.11이었다. 국산 AI반도체 팹리스의 단독 수행만 허용했고, 총 10개 과제에 과제당 최대 19.8억 원, 합계 198억 원이다. 세부 트랙은 AI 모델 맞춤형 설계지원과 설계 IP 활용지원이다. — [공고문 PDF](https://grant-documents.thevc.kr/272288_1.+2025%EB%85%84+AI%EB%B0%98%EB%8F%84%EC%B2%B4+%EC%B5%9C%EC%A0%81%ED%99%94+%EC%84%A4%EA%B3%84%EC%A7%80%EC%9B%90+%EC%82%AC%EC%97%85+%ED%86%B5%ED%95%A9+%EA%B3%B5%EA%B3%A0%EB%AC%B8.pdf); [SVA Korea 게시](https://svakorea.org/news/429)
- 과기정통부 2025 『AI 모델 맞춤형 설계지원(파운데이션 모델 트랙)』(제2025-0825호)은 1개 과제, 29.7억 원 규모다. — [공고문 PDF](https://grant-documents.thevc.kr/274437_2025%EB%85%84+AI%EB%AA%A8%EB%8D%B8+%EB%A7%9E%EC%B6%A4%ED%98%95+%EC%84%A4%EA%B3%84%EC%A7%80%EC%9B%90(%ED%8C%8C%EC%9A%B4%EB%8D%B0%EC%9D%B4%EC%85%98+%EB%AA%A8%EB%8D%B8+%ED%8A%B8%EB%9E%99)+%EC%82%AC%EC%97%85+%EA%B3%B5%EA%B3%A0%EB%AC%B8.pdf)
- 산업통상부 2026 **K-온디바이스AI반도체기술개발사업** 신규과제 공고(2026.6.11, 반도체과): 총사업비 8,002억 3천만 원(국비 5,111억 1천만 원)으로 수요기업 맞춤형 온디바이스 AI 칩 10종 개발과 완제품 실증을 지원한다. 함께 출범한 '반도체 제조지원 TF'에는 Arm, 시놉시스, 케이던스, 삼성전자 등이 참여하며, 팹리스에 대한 **IP 구매비와 EDA 라이선스 지원 방안을 마련할 계획**이다(국산 EDA 개발 사업은 아니다). — [산업통상부 공고](https://motir.go.kr/kor/article/ATCL2826a2625/71144/view?endDtD=&mno=&pageIndex=1&rowPageC=0&schClear=on&searchCondition=1&searchKeyword=&startDtD=); [머니투데이 2026-06-15](https://www.mt.co.kr/economy/2026/06/15/2026061509331190266); [이투데이](https://www.etoday.co.kr/news/view/2593500)
- 2024 지능형 반도체 개발·실증 지원사업(산업부, NTIS 공고)은 팹리스 성장 거점 지원 성격이며 PCB 설계 자동화와 직접 관련이 없다. — [NTIS 공고 1175332](https://www.ntis.go.kr/rndgate/eg/un/ra/view.do?roRndUid=1175332&flag=rndList)
- NTIS에서 "AI 기반 PCB 회로 설계 자동화" 과제명이나 KETI·ETRI 수행 과제를 웹 검색으로 찾지 못했다. — (검색 결과 없음)
- 럭스로보의 회로설계 자동화 플랫폼 개발을 다룬 2026년 7월 기사("AI·로봇 회로설계 자동화 플랫폼 개발 총력")는 있지만, 정부 과제명, 주관 부처, 예산은 검색 결과에서 확인하지 못했다. — [네이트 뉴스 2026-07-21](https://m.news.nate.com/view/20260721n00645)

### Inferences
- 정책 언어상 "설계 자동화 AI"는 주로 **칩 설계(팹리스)와 EDA 라이선스 지원** 맥락에서 쓰인다. PCB나 보드 설계 자동화는 별도 사업 범주로 잡혀 있지 않은 공백 영역이다. 모디팩토리는 (a) 산업부 AI+R&DI의 제조·전자부품 AI 활용 과제, (b) 온디바이스 AI 칩 실증(칩을 탑재할 보드 설계 수요), (c) 중기부 스타트업 R&D 같은 경로로 포지셔닝하는 것이 현실적이다.
- K-온디바이스 AI반도체 사업이 개발할 칩 10종의 "완제품 탑재·실증" 단계에는 평가보드와 제품 PCB 설계 수요가 따라온다. 모디팩토리 같은 PCB 자동 설계 서비스와 맞물릴 수 있다(추론).

### Gaps
- NTIS 과제 DB를 직접 검색할 수 없어 2018–2026 "PCB 설계 자동화", "회로 설계 AI", "EDA 국산화" 과제의 수행기관, 기간, 예산을 확인하지 못했다.
- 'K-칩스법'(조특법 반도체 세액공제)과 PCB·EDA 소프트웨어의 관련성, 2026.1.28 「산업 R&D 혁신방안」의 설계 AI 관련 내용은 확인하지 못했다.
- 럭스로보나 모디팩토리의 정부 R&D 수혜 이력(TIPS, 중기부 과제 등)을 확인하지 못했다.

---

## 6. 동향 요약, 공백, 국제 연구와의 비교

### Takeaway
국제적으로는 2025–2026년에 **LLM 기반 회로도 생성**(pcbGPT, SchGen, PCBSchemaGen), **GNN 기반 회로도 보완**, **RL 기반 PCB 배치·배선**(DeepPCB, RL_PCB, 팬아웃 RL), **PCB 배선 벤치마크**(PCBWorld, OmniRouting)가 빠르게 늘고 있다. 한국은 **KAIST(패키지·HBM SI/PI RL→LLM 에이전트)**와 **LG AI연구원(PCB 배선 벤치마크·데이터셋)**이라는 두 지점에서 국제 수준의 기여를 하고 있지만, **KCI 학술지와 학위논문 수준의 보드 레벨 PCB AI 설계 연구는 거의 없다.** 상용화 측면에서는 럭스로보 MODI Factory가 국내에서 거의 유일한 사례로 보인다.

### Cited Findings
- 국제 LLM 회로도 생성: **pcbGPT**(arXiv 2606.01188, 2026.5.31, Tobias King·Steven Kehrberg·Michael Beigl·Tobias Röddiger)는 자연어 요구사항을 KiCad 회로도 초안으로 바꾼다. 부품 환각을 막기 위해 로컬 KiCad 라이브러리와 데이터시트 검증을 쓰고, 20개 임베디드 과제로 평가했다. 저자들은 "유용한 초안이지만 전문가 검토를 대체하기엔 아직 부족하다"고 결론지었다. — [arXiv 2606.01188](https://arxiv.org/pdf/2606.01188)
- **SchGen**(arXiv 2605.30345, Microsoft Research Asia 등)은 GPT-OSS-20B를 미세조정해 자연어로부터 회로도 코드를 생성한다. — [arXiv 2605.30345](https://arxiv.org/html/2605.30345v1)
- **PCBSchemaGen**(arXiv 2602.00510)은 보상 유도 LLM 코드 합성과 구조적 검증으로 PCB 회로도를 설계한다. — [arXiv 2602.00510](https://arxiv.org/pdf/2602.00510)
- GNN 기반 회로도 보완(arXiv 2506.10577)은 PCB 회로도를 이분 그래프로 나타내고, 풀업·풀다운 저항이나 디캡 같은 최적화 부품을 추가할 위치를 예측한다. — [arXiv 2506.10577](https://arxiv.org/pdf/2506.10577)
- 생성형 AI 기반 PCB 설계·테스트 자동화 서베이(arXiv 2606.17074)는 LLM이 보드를 직접 그리지 않고 기존 EDA용 배치·배선 스크립트를 생성하는 방식이 주류라고 정리한다. 또 PCB 설계 데이터가 독점적이고 공급업체별 형식으로 파편화되어 있다는 점을 장애물로 지적한다. — [alphaXiv 2606.17074 (한글 요약)](https://www.alphaxiv.org/ko/abs/2606.17074)
- InstaDeep **DeepPCB**는 강화학습 기반 상용 PCB 배치 도구로, 최대 1,000개 부품과 2,200개 핀까지 지원한다. — [ActuIA 한국어판](https://www.actuia.com/kr/news/deeppcb-rl/)
- **RL_PCB**는 PCB 부품 배치를 위한 학습 기반 오픈소스 방법이다. — [GitHub LukeVassallo/RL_PCB](https://github.com/LukeVassallo/RL_PCB)
- RL로 PCB 배선 중 테스트포인트 배치를 다룬 보안 지향 PCB 배선 연구는 평가 대상 전체에서 배선 성공률 100%와 테스트포인트 커버리지 100%를 보고했다. — [ScienceDirect S0167926025002597](https://www.sciencedirect.com/science/article/abs/pii/S0167926025002597)
- 국내 기여의 위치: KAIST DevFormer(ICML 2023)는 최상위 ML 학회에 실린 하드웨어 배치 연구다. — [PMLR](https://proceedings.mlr.press/v202/kim23h.html) LG AI연구원 PCBWorld(KDD 2026 워크숍)와 CADET(arXiv 2026)은 PCB 배선 벤치마크·데이터셋을 공개했다. — [arXiv 2607.05915](https://arxiv.org/abs/2607.05915); [arXiv 2611.16913](https://arxiv.org/html/2611.16913)

### Inferences
- **국내외 비교:**
  - (1) *회로도 자동 생성(LLM)*: 해외는 2026년에 pcbGPT, SchGen, PCBSchemaGen이 연달아 나왔지만, 국내 학술 연구는 확인되지 않았다. 국내에서는 럭스로보가 제품으로 다루는 것이 사실상 유일해 보인다.
  - (2) *부품 배치*: 해외에는 일반 보드용 RL 배치(DeepPCB, RL_PCB)가 있다. 국내는 **SI/PI 물리 보상 기반 디캡·패키지 배치**(KAIST)에 특화되어 있다.
  - (3) *배선*: LG AI연구원이 국제 수준의 벤치마크와 데이터셋을 공개해 국내 연구가 앞선 영역이다.
  - (4) *설계 검증·DRC*: 국내는 2025 KAIS 포스터 수준이다. 해외는 KiCad DRC를 보상이나 평가에 쓰는 흐름(PCBWorld도 포함)이 표준이 되고 있다.
  - (5) *PCB 검사(AOI)*: 국내외 모두 연구가 가장 많지만 설계 자동화와는 다른 시장이다.
- **공백:** 국내 학술지, 학위논문, 국가 R&D 모두에서 "보드 레벨 엔드투엔드 AI PCB 설계(회로도→배치→배선→검증)"가 비어 있다. 모디팩토리의 "파일 업로드 → 약 90분 → AI PCB 설계안" 흐름은 국내 학술 선행연구와 겹치지 않는 영역이다. 대신 학술적 검증 근거(공개 벤치마크 성능, 논문)가 부족하다는 약점이 있으므로, PCBWorld 등 국산 벤치마크로 성능을 공개하거나 KAIST·LG AI연구원과 공동 연구를 하는 전략이 유효하다.
- **기술 수렴 신호:** KAIST(KiCad MCP 에이전트, 2026.7)와 LG AI연구원(KiCad 기반 PCBWorld)이 모두 **KiCad를 오픈 엔진**으로 채택했다. 모디팩토리의 입출력 포맷 호환과 평가 체계를 KiCad 생태계에 맞추면 국내 연구와 접점을 넓힐 수 있다.

### Gaps
- 국내 PCB 설계 AI 논문 수를 정량화(연도별 건수 등)하지 못했다. KCI와 RISS를 직접 조회할 수 없어 계량 서지 분석은 불가능했다.
- pcbGPT 저자 소속, OmniRouting 등 기타 해외 벤치마크의 상세 내용은 확인하지 못했다(이 문서 범위 밖).
- KAIST, LG AI연구원, 럭스로보 사이의 협력 관계 존재 여부는 확인하지 못했다.
