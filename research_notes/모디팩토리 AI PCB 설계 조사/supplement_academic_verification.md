# 보충 조사: GitHub와 원문으로 AI 기반 PCB 설계 학술 주장 검증, 누락 문헌 보완

> **검증 방법과 라벨 (보고서 작성자 필독)**
>
> 조사일은 2026-11-16이다. 앞선 노트(`international_academic.md`, `korean_academic.md`)는 대부분 검색 스니펫에 기댔다. 이번 보충은 두 단계로 진행했다.
> 1. GitHub 공식 저장소의 README와 저장소에 들어 있는 논문 PDF를 직접 읽었다.
> 2. 조사 도중 네트워크 제한이 풀렸다. 그래서 arXiv API와 arXiv HTML, NeurIPS·ICML 학회 페이지, 대학 기관저장소(UM OAR), RISS 상세 레코드, 학회 포스터 PDF도 직접 열어 대조했다.
>
> **라벨**
> - **[원문 확인]**: 1차 원문을 직접 읽고 확인했다. arXiv 초록·본문, 학회 공식 페이지 초록, 기관저장소 초록, 논문 PDF, RISS 서지·초록 레코드가 여기에 해당한다.
> - **[GitHub-verified]**: 공식 저장소 README나 github.io 페이지로 확인했다.
> - **[GitHub-verified·참고문헌]**: GitHub에 올라온 1차 논문 PDF의 참고문헌 목록에 해당 서지가 실린 것까지만 확인했다.
> - **[search-snippet]**: 웹 검색 스니펫만으로 확인했다.
> - **[unverified]**: 제3자 큐레이션 목록에만 등재되어 있거나, 확인할 수단이 없었다.
>
> **여전히 막힌 곳**
> - OpenReview API는 챌린지 검증(403)을 요구해서 열 수 없었다.
> - OpenAlex는 이 IP의 무료 일일 한도를 다 써서 막혔다. 사용자 이메일로 키를 발급받는 방식은 개인정보 원칙에 따라 쓰지 않았다.
> - KAIST KOASAS·DSpace는 연결이 리셋되거나 502 오류가 났다.
> - github.com HTML 페이지는 403을 돌려줬다.
> - api.github.com의 저장소·조직 단위 엔드포인트는 세션 제한으로 막혔다. 검색 API와 raw 파일은 쓸 수 있었다.

---

## Q1. 핵심 논문의 공식 저장소와 원문으로 제목·저자·학회·핵심 수치 확인

### Takeaway
요청받은 핵심 논문 가운데 **pcbGPT, SchGen, HWE-Bench, EDA Bench, PCB Gym, PCBInnoBench, PCB-QA, DRCY, RL_PCB, DevFormer, PCBWorld, CADET, PCBSchemaGen v1·v2, Cypress, OmniLayout**의 헤드라인 수치를 원문(arXiv 초록·본문, 학회 페이지, 기관저장소, 저장소 PDF)으로 확인했다.

PCBSchemaGen의 과제 수 충돌은 판본 차이로 풀렸다.

| 출처 | 과제 수 | 헤드라인 수치 |
|---|---|---|
| v1 | 23개 | 초록에 수치 없음 |
| v2(NeurIPS 2026) | 2개 벤치마크, 227개(PCBBench 62 + OSE 165) | PCBBench 평균 통과율 81.3%(Gemma-4-31B) |
| DOE 슬라이드 | 65개 | 77.5% |

DOE 슬라이드의 수치는 어느 원문 판본과도 맞지 않는다. 65는 PCBBench 과제 ID 범위(1–65)와 일치한다.

새로 확인한 사실은 세 가지다.
- PCB-QA는 UNSW 서베이와 **같은 저자 그룹**이 같은 날 제출했다. 공저자로 Benjamin Tan이 추가됐다.
- 앞선 노트에서 인용한 DRCY의 성과 수치(리뷰 11건, DDR5 오류 100% 검출)는 **arXiv 논문에는 없다**. 벤더 블로그에서만 나온다.
- PCBWorld 체크포인트, CADET 체크포인트, PCBSchemaGen v2 코드는 **비상업 라이선스**다.

### Cited Findings

**[1] RL_PCB: Vassallo & Bajada, DATE 2024 [원문 확인 + GitHub-verified]**
- 서지: "Learning Circuit Placement Techniques Through Reinforcement Learning with Adaptive Rewards," 2024 DATE, pp. 1–6, IEEE 문서 10546526. 코드는 MIT 라이선스다 — [GitHub LukeVassallo/RL_PCB](https://github.com/LukeVassallo/RL_PCB)
- 기관저장소 초록에서 확인한 내용 — [UM OAR 초록](https://www.um.edu.mt/library/oar/handle/123456789/131782)
  - PCB 배치를 MDP로 정식화하고, 적응형 보상으로 일반 정책을 학습한다.
  - 미학습 회로에서 TD3 정책은 SA 대비 post-routing 배선길이를 평균 **17%**, SAC 정책은 **21%** 줄였다.
  - 협력·경쟁의 창발 행동이 관찰됐다.
  - 배치 수렴이 빨라졌고, 때로는 한 자릿수 배 이상 빨랐다.

**[2] Cypress: NVlabs, ISPD 2025 [원문 확인 + GitHub-verified]**
- 서지: Niansong Zhang, Anthony Agnesina, Noor Shbat, Yuval Leader, Zhiru Zhang, Haoxing Ren(Cornell, NVIDIA), ISPD 2025 — [GitHub NVlabs/Cypress](https://github.com/NVlabs/Cypress)
- 원문 초록의 핵심 수치 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
  - routability 1–5.9배 향상
  - 완전 배선 설계의 routed track length 1–19.7배 단축
  - GPU 가속으로 런타임 최대 492.3배 단축
- 비교 기준선 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
  - NS-Place와 NS-Place+, OpenROAD SA-PCB, 상용 Quilter(2024-04-04 버전, 클라우드 제출)
  - routability는 FreeRouting v1.9.0으로 측정했다.
- 원문의 경쟁 맥락 서술 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
  - "Quilter는 부품 176개 설계에 2.6시간이 걸린다."
  - Quilter의 지원 범위는 핀 1,000개 미만, 부품 100개, 밀도 10%, 500 MHz, 2 A다.
  - Cadence Allegro X AI는 MCTS를 쓰며 대형 설계에는 제약이 있다.

**[3] PCBWorld: LG AI Research [원문 확인 + GitHub-verified]**
- arXiv:2607.05915, 2026-07-07 제출, v4는 2026-09-11 갱신. 코멘트는 "Accepted to the KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI (non-archival)"다. 저자는 Hyungseok Song, Junseok Park, Won-Seok Choi, Seohui Bae, Han-Seul Jeong, Youngjoon Park, Soonyoung Lee다 — [arXiv](https://arxiv.org/abs/2607.05915)
- 초록 내용 — [arXiv](https://arxiv.org/abs/2607.05915)
  - 문제 인식: "learning-based methods still lag behind rule-based routers"
  - 구성: 합성 생성기 2종과 **실보드 679개**, 엔진이 검사하는 지표 8개
  - 결과: 합성 보드로만 학습한 RL 정책이 실보드로 zero-shot 전이했고, 규칙 기반 라우터에 "근접"했다.
- 본문 표(D3-A 99개 소형 보드, @5) — [README](https://github.com/LGAI-Research/PCBWorld); [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)

  | 방법 | CP | Pot. |
  |---|---|---|
  | Freerouting | 0.80 | 22.71 |
  | KRT | 0.74 | – |
  | GPT-5.4 에이전트 | 0.65 | – |
  | PPO | **0.86** | 21.46 |

  - 본문의 결론은 "PPO가 소형 보드에서는 모든 기준선을 능가했지만, 대형 보드에서는 가장 강한 규칙 기반 라우터에 뒤처졌다"이다.
  - D3 세트는 PCBench 코퍼스에서 파생했다. D3-B는 287개, D3-C는 292개다.
- 라이선스: 환경 코드는 BSD-3, 엔진(LGAI-Research/PCBWorld-Engine)은 GPLv3다. 체크포인트는 **EXAONE AI Model License 1.2-NC**로, 체크포인트와 그 출력 모두 상업적 사용이 금지된다 — [README](https://github.com/LGAI-Research/PCBWorld)

**[4] CADET: LG AI Research [원문 확인 + GitHub-verified]**
- arXiv:2611.16913, 2026-11-12 제출. 28쪽, 그림 10개, 표 15개로 구성된 프리프린트다. 저자는 PCBWorld와 같은 7인이다 — [arXiv](https://arxiv.org/abs/2611.16913)
- 초록 내용 — [arXiv](https://arxiv.org/abs/2611.16913)
  - RouteDemos는 DRV 0인 합성 보드 100,000개와 엔진 행동 시연으로 구성된다. 17개 통계에서 실보드 142개 분포와 유사하다.
  - BC를 거친 뒤 RL로 미세조정한 정책은 실제 테스트 보드의 완전 무위반 배선률을 **RL-only 기준선 대비 38.0%에서 67.2%로** 올렸다.
  - 이 수치는 FreeRouting과 비슷하고, GPT-6 Astra 등 나머지 기준선보다 높다.
- 본문 표(D3-B test 141개) — [README](https://github.com/LGAI-Research/CADET); [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)

  | 방법 | 배선률 | 시간 |
  |---|---|---|
  | FreeRouting @1 | 65.6% | 45.6초/보드 |
  | CADET @1 | 67.2% | 15.5초 |
  | CADET @3 | 79.8% | – |

  - D3-A에서는 FreeRouting @1이 82.1%, CADET @1이 89.5%, CADET @3이 96.3%였다.
  - 38.0%는 "PPO (RouteDemos)" 행이며, 편차는 ±6.2다.

**[5] PCB-Bench: ICLR 2026 [GitHub-verified / OpenReview 접근 실패]**
- 저자는 Jindong Li, Lianrong Chen, Bin Yang, Jiadong Zhu, Ying Wang, Yuzhe Ma, Menglin Yang이다. 소속은 HKUST(Guangzhou)다 — [프로젝트 페이지](https://digailab.github.io/PCB-Bench/); [GitHub](https://github.com/digailab/PCB-Bench)
- 규모 — [프로젝트 페이지](https://digailab.github.io/PCB-Bench/)
  - 텍스트 QA·객관식 약 3,700개
  - 멀티모달 문제 약 500개
  - **실제 PCB 프로젝트 174개**(OSHWHub 출처). 앞선 노트의 "170개 이상"을 174개로 정정한다.
- OpenReview(id Q5QLu7XTWx) API는 챌린지 검증 요구(403)로 열지 못했다. 모델별 점수는 확인하지 못했다.

**[6] PCBSchemaGen: 판본 충돌 정리 [원문 확인 + GitHub-verified]**
- **v1**(arXiv:2602.00510v1, 2026-01-31) — [arXiv v1](https://arxiv.org/abs/2602.00510v1); [GitHub Sthyao/PCBSchemaGen](https://github.com/Sthyao/PCBSchemaGen)
  - 제목: "PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards (PCB)"
  - 저자: Huanghaohe Zou, Peng Han, Emad Nazerian, Alex Q. Huang
  - 초록: "training-free", 데이터시트에서 만든 지식그래프와 부분그래프 동형 검증, "**23개** PCB 회로도 과제(디지털·아날로그·전원)"
  - 초록에 통과율 수치는 없다.
- **v2**(arXiv:2602.00510v2, 2026-06-17 갱신, NeurIPS 2026) — [arXiv v2](https://arxiv.org/abs/2602.00510v2); [GitHub HZou9/PCBSchemaGen_v2](https://github.com/HZou9/PCBSchemaGen_v2)
  - 제목: "Reward-Guided LLM Code Synthesis for Printed Circuit Boards (PCB) Schematic Design with Structured Verification"
  - 저자: v1의 4인에 Mafu Zhang, Zhicheng Guo가 추가됐다.
  - 초록: 결정론적 5층 연속보상 검증기(핀 단위 오류 위치 지정)와 Thompson Sampling 밴딧을 쓴다. "2개 벤치마크, **227개** 실제 IC 과제, **22개** 도메인"이며, Open-Schematics 기반 세트는 완전 hold-out 일반화 테스트다.
  - 핵심 수치: "Gemma-4-31B가 PCBBench 과제의 **81.3%**를 평균 통과"
  - 같은 백본의 Circuitron식 프롬프팅 기준선은 어려운 시스템 레벨 설계에서 "붕괴"했다.
- 저장소 실물 — [benchmark.tsv](https://github.com/HZou9/PCBSchemaGen_v2/blob/main/benchmarks/pcbbench/benchmark.tsv)
  - PCBBench TSV는 **62행**(Easy 17, Medium 28, Hard 17)이고, OSE는 165개다.
  - 과제 ID 범위는 **1–65**이며, 48·53·63번이 비어 있다.
- **77.5% / 65개 과제**: DOE 리뷰 슬라이드(2026-07-27)에만 나온다. 검색 요약에 따르면 같은 슬라이드에 63.6%라는 다른 수치도 있다. 원문 v2의 81.3%와 다르다. 측정 대상(과제 세트·모델·지표)이 다른지는 확인하지 못했다 [search-snippet] — [DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf)
- 라이선스: 코드는 **PolyForm Noncommercial 1.0.0**이고, 벤치마크와 지식그래프는 MIT다 — [README v2](https://github.com/HZou9/PCBSchemaGen_v2)

**[7] SchGen: Microsoft 외 [원문 확인 + GitHub-verified]**
- arXiv:2605.30345(2026-05-28), 19쪽. 저자는 Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu다 — [arXiv](https://arxiv.org/abs/2605.30345); [GitHub microsoft/SchGen](https://github.com/microsoft/SchGen)
- 본문 수치 — [arXiv HTML](https://arxiv.org/html/2605.30345v1)
  - Code-L1 표현으로 **유효 회로율 82%**, **전문가가 검증한 기능 정확도 60.5%**를 얻었다.
  - 원시 KiCad 파일 기준선은 유효 회로율이 **32%**에 그쳤다.
  - 표에서 Vanilla GPT-oss-20b의 기능 정확도는 17.0%, GPT-5.2-L1은 50.0%였다.
  - 20B 모델로 GPT-5.2 등 프런티어 LLM보다 높았다.
- 앞선 노트의 원시 KiCad 기준선 "32.45%, 3.0%" 가운데 3.0%는 이번에 본문에서 다시 찾지 못했다. 32%는 확인했다.
- 학습 방식: GPT-oss-20b의 전문가 레이어 7, 15, 23에 LoRA를 적용했다. 데이터는 SparkFun CC BY-SA 기반이고, 코드는 MIT다 — [README](https://github.com/microsoft/SchGen)

**[8] pcbGPT [원문 확인 + GitHub-verified]**
- 서지: arXiv:2606.01188(2026-05-31). 저자는 Tobias King, Steven Kehrberg, Michael Beigl, Tobias Röddiger다 — [arXiv](https://arxiv.org/abs/2606.01188)
- 초록 — [arXiv](https://arxiv.org/abs/2606.01188)
  - Python DSL, 부품 라이브러리 검색, 데이터시트 기반 지식, 실행 기반 검사, 구조·의미 검증을 쓴다.
  - 임베디드 과제 20개에서 최고 모델이 pass@1 **0.90**, pass@5 **1.00**을 기록했다.
  - 난이도별 pass@1은 basic·easy 1.00, medium 0.91, hard 0.72다.
  - 결론: "검토 가능한 초안으로는 유용하지만 전문가 리뷰를 대체할 만큼 신뢰할 수는 없다."
- 코드 저장소는 tk-king/pcbGPT이며 웹·데스크톱 앱을 포함한다 — [GitHub](https://github.com/tk-king/pcbGPT)

**[9] HWE-Bench: 보드 레벨 회로도 [원문 확인 + GitHub-verified]**
- 서지: arXiv:2603.18102(2026-03-18). 저자는 **Weibo Qiu, Yinhao Xiao, Runyu Pan**이다(새로 확인) — [arXiv](https://arxiv.org/abs/2603.18102)
- 초록 — [arXiv](https://arxiv.org/abs/2603.18102)
  - GitHub와 OSHWLab에서 가져온 **300개** 과제, 응용 도메인 8개, 실제 IC 데이터시트 **2,914개**
  - 정적 전기규칙 검사 뒤 회로 시뮬레이터로 동작을 검증한다.
  - 최고 모델의 전체 통과율은 **8.15%**다.
  - 진단: 모델이 "물리적 직관이 부족하다."
- 저장소는 EDI-Systems/HWE-Bench다. 파이프라인은 MinerU 데이터시트 파싱, 4단계 생성, 정적 규칙 검사, LTspice 검증으로 이어진다 — [GitHub](https://github.com/EDI-Systems/HWE-Bench)
- 이름이 같은 다른 벤치마크와 혼동하지 말 것. pku-liang/hwe-bench는 RTL 버그 수리 417건을 다룬다(arXiv:2604.14709) — [GitHub](https://github.com/pku-liang/hwe-bench)

**[10] EDA Bench: ICML 2026 [원문 확인 + GitHub-verified]**
- ICML 페이지 초록 — [ICML 2026](https://icml.cc/virtual/2026/77908)
  - 공개 오픈하드웨어에서 뽑은 KiCad PCB 재구성 과제 **35개**
  - 오라클이 구리 추출, 외부 포트, 트레이스 기생성분·단락, ngspice, ERC·DRC를 검사한다.
  - 참조 설계 35개는 모두 1.0점을, 구조 실패 카나리 35개는 모두 0.15점 이하를 받았다.
  - 가장 강한 웹 접근 하네스의 종합 점수는 **4.58%**였다. 35개 중 **21개 프로젝트를 빌드**했지만 기능 검사 대부분에 실패했다.
- 저장소 EDA-bench/eda-bench는 Harbor 기반이며 난이도 가중치를 1.0부터 5.0까지 둔다. DATA_CARD는 "에이전트 단계에서 네트워크가 허용되므로 closed-book 시험이 아니다"라고 밝힌다 — [DATA_CARD](https://github.com/EDA-bench/eda-bench/blob/master/DATA_CARD.md)

**[11] PCB Gym과 PCBInnoBench: NeurIPS 2026 [원문 확인]**
- **PCB Gym** — [NeurIPS](https://neurips.cc/virtual/2026/161602)
  - 배치와 라우팅을 함께 다루는 에이전트 환경이다. 설계 의도는 Zener(schematic-as-code HDL)로 준다.
  - 데이터는 오픈하드웨어 2–12층 보드다. 결정론적 게이트와 루브릭 기반 에이전트 채점기로 평가한다.
  - 프런티어 LLM이 DRC 유효이면서 완전 배선된 보드를 만든 비율은 **32.1%**다. 전원 레일을 일반 신호처럼 배선하는 실수가 잦았다.
  - GitHub 저장소는 찾지 못했다.
- **PCBInnoBench** — [NeurIPS](https://neurips.cc/virtual/2026/poster/139034)
  - 실제 프로젝트 기반의 전문가 설계 KiCad 과제 **372개**
  - 최고 에이전트의 Pass@1은 가이드가 있을 때 **22.0%**, 없을 때 **7.3%**다.
  - 데이터와 코드는 anonymous.4open.science/r/pcbinnobench-C841에 있다.
  - GitHub의 speder-eda/pcbinnobench 저장소는 존재하지만(2026-11-05 push), README는 404였다.

**[12] PCB-QA [원문 확인, 새 사실]**
- 서지: arXiv:2606.23704(2026-06-10). 저자는 **Sahana Srinivasan, Benjamin Tan, Benjamin Turnbull, Hammond Pearce**다. UNSW 서베이 그룹과 같고, 같은 날 제출됐다 — [arXiv](https://arxiv.org/abs/2606.23704)
- 초록 — [arXiv](https://arxiv.org/abs/2606.23704)
  - 오픈소스 하드웨어 프로젝트 **8개**에서 직접 만든 QA **480쌍**. 부품 연결, 데이터시트 검토, SPICE 데이터를 다룬다.
  - LLM 4종을 비교했다. Gemini 3 Flash Preview가 제안된 **JSON 텍스트 형식**에서 **93%** 정확도를 기록했다.
  - 연구 질문은 LLM이 PDF나 KiCad 원본 같은 "네이티브 형식"과 텍스트 형식 가운데 무엇을 더 잘 이해하느냐다.

**[13] DRCY: AllSpice [원문 확인 / 성과 수치는 벤더 블로그]**
- 서지: arXiv:2603.15672(2026-03-13). 저자는 **Kyle Dumont, Nicholas Herbert, Hayder Tirmazi, Shrikanth Upadhayaya**다 — [arXiv](https://arxiv.org/abs/2603.15672)
- 초록 — [arXiv](https://arxiv.org/abs/2603.15672)
  - "최초의 production-ready 멀티에이전트 LLM 회로도 연결 리뷰"라고 자칭한다.
  - 데이터시트를 자동으로 가져와 핀 단위로 분석하고, 리뷰에 인라인 코멘트를 단다.
  - AllSpice Hub에서 CI/CD 액션으로 운영된다.
  - 5-에이전트 파이프라인을 쓰고, 다회 실행 합의(multi-run consensus)로 안전 필수 분석의 신뢰도를 높인다.
- 본문의 Critic 에이전트는 데이터시트 추출을 10점 척도로 채점한다. 가중치는 기능 완전성 25%, 핀 기능 커버리지 40%, 응용 정보 20%, 전형 응용회로 15%다 — [arXiv HTML](https://arxiv.org/html/2603.15672v1)
- **정정**: 앞선 노트의 "리뷰 11건에서 실제 이슈 4건, DDR5 주입 오류 100% 검출"은 arXiv 본문에서 찾지 못했다. AllSpice 블로그(벤더 자체 보고)에만 있는 수치로 다뤄야 한다 — [AllSpice 블로그](https://www.allspice.io/post/how-hardware-engineering-teams-evaluate-drcy) [search-snippet]

**[14] OmniLayout과 OmniRouting [원문 확인 + GitHub-verified]**
- **OmniLayout**: arXiv:2607.03261(v3는 2026-09-27 갱신). 저자는 Taiting Lu 외 15인이며 교신저자는 Mahanth Gowda다 — [arXiv](https://arxiv.org/abs/2607.03261)
  - 회로도와 결합된 산업급 PCB 레이아웃 **1,681개**, IC 배치 인스턴스 **77.24K**개, 과제 4종으로 구성된다.
  - **새 사실**: 저장소에서 데이터셋 다운로드가 "출처별 라이선스 검토를 위해 일시 철회"되었다. 코드만 MIT로 남아 있다 — [GitHub AAAAAiden/OmniLayout-Benchmark](https://github.com/AAAAAiden/OmniLayout-Benchmark)
- **OmniRouting**: arXiv:2608.04434(2026-08-05). 같은 그룹이 만든 PCB **라우팅** 추론 벤치마크다 — [arXiv](https://arxiv.org/abs/2608.04434)
  - 회로도와 결합된 산업급 설계 1,681개에 스택업과 라우팅 제약을 담았다.
  - 과제 4종에서 LMM의 경로 계획 능력이 약하고, 설계 규칙 준수가 부족하고, 전기 기능 보존이 일관되지 않다고 보고했다.

**[15] DevFormer: KAIST, ICML 2023 [원문 확인 + GitHub-verified]**
- arXiv:2205.13225v3의 코멘트는 "ICML 2023. NeurIPS 2022 Offline RL Workshop 논문의 확장판"이다. 초록은 시뮬레이션과 실제 하드웨어에서 SOTA를 능가하면서 "부품 수를 **30% 이상**" 줄였다고 밝힌다 — [arXiv](https://arxiv.org/abs/2205.13225)
- 저장소는 ai4co/devformer로 이전했다. DPP(디캡 배치 문제)는 RL4CO에 들어갔고, ReEvo(NeurIPS 2024)에서도 쓰였다 — [GitHub kaist-silab/devformer](https://github.com/kaist-silab/devformer)

**[16] AlphaChip(circuit_training)과 비판 측 [원문 확인 + GitHub-verified]**
- arXiv 2302.11014는 v3(2026-03-10)에서 제목이 "**An Updated Assessment of Reinforcement Learning for Macro Placement**"로 바뀌었다. 코멘트는 "accepted and published in IEEE Transactions on CAD"다 — [arXiv](https://arxiv.org/abs/2302.11014)
  - 초록: go-with-the-winners 기법과 멀티스레딩으로 강화한 SA를 썼다. 7nm 공개 벤치마크를 만들었다. AlphaChip 최신판을 처음부터 학습하는 경우와 미세조정하는 경우를 모두 평가했다. 상용 P&R로 "true reward"를 측정했다.
  - 초록은 CT의 확장성과 사전학습 방법론이 "여전히 확인되지 않았다"고 지적한다.
- MacroPlacement README에 따르면 TCAD 채택일은 2025-12-16(IEEE Xplore 11300304)이다. 결론은 "SA가 사전학습된 CT보다 여전히 우수"하다. 이 결과를 익명 심사위원과 GT/USC S.-K. Lim 그룹이 재현했다 — [GitHub MacroPlacement](https://github.com/TILOS-AI-Institute/MacroPlacement)
- Google circuit_training README는 "Nature 2021 방법론을 재현한다"고 하고, "Alphabet 안팎의 칩 레이아웃 설계에 쓰인다"고 주장한다(Google 측 주장) — [GitHub circuit_training](https://github.com/google-research/circuit_training)

**[17] 기타 정정**
- **Unet-Astar**(IEEE Access 2023): 저장소 README에 "코드는 논문 채택 후 제공"이라고만 적혀 있다. **코드는 공개되지 않았다** — [GitHub](https://github.com/Firesuiry/Unet-Astar-For-PCB-Routing)
- **Component Centric Placement**(Kart Leong Lim, arXiv:2602.23540): 초록에서 DQN, Actor-Critic, SA를 비교했고, "실제 PCB 9개 이상"에서 "사람에 가까운 배치"를 냈다는 서술을 확인했다 [원문 확인] — [arXiv](https://arxiv.org/abs/2602.23540)
- **FanoutNet**: 서지는 Haiyun Li, Jixin Zhang, Ning Xu, Mingyu Liu, *AAAI* 37(7):8554–8561, 2023, DOI 10.1609/aaai.v37i7.26030이다. 공식 코드는 찾지 못했다 [GitHub-verified·참고문헌] — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)

### Inferences
- 보고서 본문의 정량 주장에는 원문으로 확인한 수치만 쓰면 된다. 아래 표가 그 목록이다. "DRC는 통과해도 기능은 실패한다"(EDA Bench 21/35 빌드, 4.58%)와 "실보드 수준 회로도는 8.15%"(HWE-Bench)는 모두 원문으로 확인됐다.

  | 논문 | 원문 확인 수치 |
  |---|---|
  | PCBWorld | 679 보드, D3-A 표 |
  | CADET | 38.0%→67.2%, FreeRouting 65.6% |
  | Cypress | 1–5.9배, 1–19.7배, 492.3배 |
  | RL_PCB | 17%/21% |
  | pcbGPT | 0.90 |
  | SchGen | 82%/60.5% |
  | HWE-Bench | 8.15% |
  | EDA Bench | 4.58% |
  | PCB Gym | 32.1% |
  | PCBInnoBench | 22.0/7.3% |
  | PCB-QA | 93% |
  | PCBSchemaGen v2 | 81.3% |

- PCBSchemaGen은 v2 원문의 "81.3%(PCBBench 평균, Gemma-4-31B)"를 인용해야 한다. DOE 슬라이드의 77.5%와 65개 과제는 쓰지 않는 편이 안전하다.
- 상용 서비스 관점에서 PCBWorld와 CADET 체크포인트(EXAONE NC), PCBSchemaGen v2 코드(PolyForm NC), OmniLayout 데이터(배포 철회)는 모디팩토리가 그대로 쓸 수 없다. 반면 RL_PCB(MIT), SchGen(MIT), PCBWorld 환경 코드(BSD-3)는 상대적으로 자유롭다. 다만 PCBWorld 엔진은 GPLv3이므로 연동 방식을 따로 검토해야 한다.

### Gaps
- PCB-Bench의 모델별 점수: OpenReview가 챌린지로 막혔고, README 표는 이미지 형태다.
- SchGen 원시 KiCad 기준선의 "3.0%" 기능 정확도는 본문에서 다시 찾지 못했다.
- DOE 슬라이드의 77.5%·65개 과제가 무엇을 측정한 값인지 확인하지 못했다.
- PCB Gym 저자와 코드 공개 여부, PCBInnoBench 저자를 확인하지 못했다. 학회 페이지 초록에는 저자 정보가 없다.

---

## Q2. GitHub 큐레이션 목록과 원문 참고문헌으로 찾은 누락 논문(2023–2026)

### Takeaway
주류 AI4EDA 목록 세 개(thu-nics/awesome_ai4eda, ai4eda/awesome-AI4EDA, Thinklab-SJTU/Awesome-LLM4EDA)에는 PCB, KiCad, schematic, datasheet 항목이 **한 건도 없었다.** 대신 PCB 전용 목록(tikyttqq/Awesome-PCB-Routing)과 엔지니어링 에이전트 목록(whut09/Awesome-AI-Engineering-Agents), LG AI 논문 참고문헌에서 누락 논문 약 25편을 찾았다.

원문으로 확인한 핵심 신규 문헌은 다섯 가지다.
- **PCBRouteAgent**(2026-11): PCBWorld 위에서 LLM 라우팅을 수행하고, D3-A 클린패스 94.9%를 냈다.
- **CircuitLM**: IEEE ICLAD 2026에 채택됐다.
- **GPCB Routing**: IEEE TCAD 2025
- **월드모델 RL과 Freerouting 결합**: ESWA 2026, 코드 공개
- **ModuPlace**: LLM 기반 모듈형 배치

앞선 노트에서 "존재 미확인"이던 CircuitLM과 PCBAgent는 실재하는 논문이다.

### Cited Findings

**(a) 원문으로 확인 [원문 확인]**
- **PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?** — [arXiv](https://arxiv.org/abs/2611.08175); [GitHub chip-ai-agent/PCBRouteAgent](https://github.com/chip-ai-agent/PCBRouteAgent)
  - 서지: Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang, arXiv:2611.08175(2026-11-05, v2 11-09)
  - 방법: Global Routing Planner가 보드 이미지와 전기·기하 정보로 연결 토폴로지, 순서, 통로, 레이어 전환을 정한다. Detailed Routing Executor가 KiCad 네이티브 엔진으로 실행하고, 실패 피드백으로 가이드를 수정한다.
  - 평가: PCBWorld-Bench 4개 분할의 **247개** 보드
  - 클린패스율: D2 100%, D3-A 94.9%, D3-B 100%, D3-C 40%
  - 실보드 3개 분할에서 최고 기준선 대비 각각 13.9, 36, 10%p 높았다.
- **CircuitLM** — [arXiv](https://arxiv.org/abs/2601.04505); [GitHub](https://github.com/Khandakar227/circuitlm)
  - 서지: Khandakar Shakib Al Hasan, Syed Rifat Raiyan, Hasin Mahtab Alvee, Wahid Sadik, arXiv:2601.04505. 코멘트는 "**2026 IEEE ICLAD 채택**"이다.
  - 방법: 임베딩 기반 부품 지식베이스와 5단계 파이프라인(부품 식별, 핀아웃 검색, CoT, JSON 회로도 합성, 시각화)
  - 평가: 프롬프트 100개를 LLM 5종으로 실행했다. 결정론적 ERC 엔진(심각도 4단계)과 LLM-as-a-judge로 이중 평가했다.
- **ModuPlace: LLM-Assisted Modular PCB Placement via Preference-Optimized Constraint Graph Generation** — [저자 PDF](https://yhhan.com/PDFs/ModuPlace_paper.pdf)
  - 저자: Yaohui Han, Beichen Li, Mingyang Zhao, Rongliang Fu, Qunsong Ye, Tinghuan Chen, Bei Yu, Tsung-Yi Ho(CUHK 외)
  - 방법: 모듈 단위 계층 배치, LLM 미세조정과 선호 최적화로 제약 그래프 생성
  - DAC 2026 게재는 목록 기준이라 [unverified]다.
- **PCB-QA**와 **OmniRouting**은 Q1의 [12]와 [14]를 참고하라.

**(b) 1차 PDF 참고문헌으로 확인 [GitHub-verified·참고문헌]**
- **GPCB Routing: Generative Pretrained Transformers-Based Printed Circuit Board Routing Method**: Jienan Chen 외 8인, *IEEE TCAD* 44(4):1420–1433, 2025, DOI 10.1109/TCAD.2024.3486241 — [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)
- **Automation of PCB Autorouting via World-Model Reinforcement Learning and Freerouting Integration**: Yin-Chi Liao, Sheng-Xin Pan, Po-Jui Chiang, *Expert Systems with Applications* 311:131424, 2026 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - 코드: JPype로 freerouting.jar를 Gymnasium 환경으로 감싸 DreamerV3로 학습한다 [GitHub-verified] — [GitHub yinqimakeitfun/dreamer-Autorouting](https://github.com/yinqimakeitfun/dreamer-Autorouting)
- **PCBench**: Youbiao He 외, DAC 2024 WIP 포스터 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - 저장소 README는 PCB **164개**, PCB-RDL, RL 환경을 소개한다 — [GitHub PCBench/PCBench](https://github.com/PCBench/PCBench)
  - **상충 사항**: PCBWorld는 "PCBench 코퍼스에서 파생한 679개"라고 쓴다. 두 수치가 왜 다른지 확인하지 못했다.
- 같은 그룹의 관련 연구: Youbiao He, Iowa State 박사논문 "Towards Automated PCB Routing"(2024), MCTS와 DRL을 결합한 회로 라우팅(VLSI-DAT 2022) — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
- 차동 페어를 다룬 비ML PCB 라우팅: Lin 외, "A Unified PCB Routing Algorithm With Complicated Constraints and Differential Pairs," ASP-DAC 2021 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
- **NS-Place**: Cheng, Ho, Holtz, ASP-DAC 2022 — [Cypress PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)

**(c) 큐레이션 목록에만 등재 [unverified]**

라우팅 — [tikyttqq/Awesome-PCB-Routing](https://github.com/tikyttqq/Awesome-PCB-Routing)
- **PCBAgent**: An Agent-based Framework for High-Density PCB Placement, ASP-DAC 2025, DOI 10.1145/3658617.3697736
- **TRouter**: IEEE TCAD 2023, DOI 10.1109/tcad.2023.3243544. 앞선 노트의 "학회·연도 미확인"을 해소한다.
- Security-oriented PCB routing with DRL, *Integration* 2026, DOI 10.1016/j.vlsi.2025.102602
- Multi-agent minimal-layer via routing, *Integration* 2026
- ST-GAT, 멀티에이전트 RL PCB 라우팅, ECIE 2026
- Intelligent Ordered Escape Routing via DRL, CEI 2025
- Applying Existing LLMs for PCB Routing, *Eng. Proc.* 2025
- Routing GPT for PCB, ISEDA 2024
- SER-NET, ICICM 2024
- DDDQN PCB Routing, ICICM 2024
- Hierarchy MCTS, ICCA 2020
- PCB-Migrator, DATE 2026

배치·회로도·라이브러리 — [whut09/Awesome-AI-Engineering-Agents](https://github.com/whut09/Awesome-AI-Engineering-Agents)
- AI-Optimized Placement and Routing for PCB Design, IEEE 2024
- RL-Based Placement Method for PCB, ICCCAS 2024
- **ML-aided Schematic Symbol Generation in PCB EDA Tools**, MLCAD 2024, DOI 10.1145/3670474.3685944
- Goal Driven PCB Synthesis Using ML and CloudScale Compute, ISPD 2023
- From Natural Language to Real Schematics(전력전자), arXiv:2610.38201
- RAC(계약 기반 PCB 배치·배선·수리), arXiv:2610.20935
- OmniSch(회로도 멀티모달 벤치마크), arXiv:2604.00270

**(d) LLM으로 KiCad·Altium을 조작하는 오픈소스 도구 [GitHub 목록 등재]**
- eda-agent(salitronic): Altium, KiCad, EasyEDA Pro를 MCP로 편집·리뷰·배치한다.
- KiCad MCP, KiCad Copilot, Backplane
- 상용 쪽에는 Cadence AuraStack AI Super Agent와 Siemens Fuse EDA AI Agent가 실려 있다.
- 출처: [whut09 목록](https://github.com/whut09/Awesome-AI-Engineering-Agents)
- **DeepPCB KiCad 플러그인**(크레딧 기반 클라우드 라우팅)은 저장소에서 직접 확인했다 [GitHub-verified] — [GitHub](https://github.com/instadeepai/deeppcb-kicad-plugin)

**(e) 산업계 오토라우터 벤치마크 [GitHub-verified]**
- Koppar-AI/autorouter-bench: 오픈하드웨어 실보드 8개(2층과 4층, RP2040, CM5 IO, OLIMEX SoM 등)를 KiCad로 채점한다. 2026-10 Zap!(Mutual Solutions)의 공개 보드 25개 비교 세트도 포함한다 — [GitHub](https://github.com/Koppar-AI/autorouter-bench)

### Inferences
- PCBRouteAgent는 PCBWorld-Bench 4개 분할에서 높은 클린패스율을 보고했다. LG AI의 국산 벤치마크가 외부 연구의 표준 평가 환경으로 쓰이기 시작했다는 원문 증거다.
- 다만 대형 보드(D3-C)는 40%에 그친다. LLM 에이전트 라우팅이 실서비스 수준에 오르기 전에 남은 핵심 과제는 대형 보드다.
- KiCad 엔진을 심판으로 쓰는 공개 비교가 업계 관행으로 굳어지고 있다. PCBWorld, Koppar, Zap!이 그 예다.

### Gaps
- (c)에 나열한 목록 등재 논문 약 20편의 저자와 수치는 확인하지 못했다.
- 보드 레벨 열·SI·PI ML 논문, 설계 근거나 설명가능성을 다룬 PCB 전용 논문은 TRouter 외에 새로 찾지 못했다.

---

## Q3. 한국 저자 연구: LG AI, KAIST, 국내 학위논문과 학술지 (RISS 원문 레코드로 검증)

### Takeaway
RISS 상세 레코드(서지·초록·주제어)로 검증한 결과, 앞선 노트의 결론("보드 레벨 AI PCB 학위논문은 국내에 사실상 없음")은 **부분 수정이 필요하다.**
- **보드 레벨 PCB 디캡 선택·최적화에 RL을 쓴 2025년 학위논문**이 있다. 성균관대 석사(DDQN)와 KAIST 박사(주제어에 PCB와 Reinforcement learning)다.
- **LLM과 RL을 결합한 PCB 부품 자동 배치 시스템** 학술대회 논문이 있다. 연세대, 대한전자공학회 2024.11.
- 비ML이지만 2025–2026년에 나온 PCB 자동 배치·라우팅 연구도 있다. 아주대 ILP 이스케이프 라우팅(박사논문과 학술지)과 ㈜티에스이의 GPU 휴리스틱 배치(2026)다.

그래도 **ML이나 LLM으로 일반 보드의 배치·배선을 다룬 학술지(KCI급) 논문은 여전히 찾지 못했다.** 2025 KAIS 포스터는 원문 PDF로 저자와 소속을 확인했다.

### Cited Findings

**(a) LG AI연구원 [원문 확인]**
- PCBWorld(arXiv 2607.05915)와 CADET(arXiv 2611.16913)의 저자 7인은 모두 LG AI Research(서울) 소속이다. PCBWorld는 KDD 2026 워크숍(2026-08-09~13, 제주, non-archival)에서 발표됐다 — [arXiv PCBWorld](https://arxiv.org/abs/2607.05915); [arXiv CADET](https://arxiv.org/abs/2611.16913); [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)

**(b) KAIST [원문 확인: RISS·arXiv / search-snippet: KOASAS 항목]**
- DevFormer(ICML 2023)의 저자 5인에는 김정호(전기및전자공학부)와 박진규(산업및시스템공학과)가 포함된다. 부품 수를 30% 이상 줄였다 — [arXiv](https://arxiv.org/abs/2205.13225)
- 강형민, 「노이즈 커플링 및 EMI 억제를 위한 고전력 공급 및 스위칭 PCB의 모델링, 시뮬레이션 및 최적화」, KAIST 전기및전자공학부 박사, 2025. 주제어는 Decoupling capacitor, Design optimization, Noise coupling, **PCB**, **Reinforcement learning**이다. RISS 화면에서 초록 본문은 보이지 않았다 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=240b9d5e4445a07cffe0bdc3ef48d419)
- 김경묵, 「강화학습 기반 최적화 방법을 통한 DDR5 메모리 VDDQ 전력 분배 네트워크 설계 및 분석」, KAIST 석사, 2025. 주제어는 DRL, PDN, Decap, SSN, DDR5 Memory다 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=17d971b24de8ec09ffe0bdc3ef48d419)
- 신태인, 「이산-연속 공간 강화학습을 이용한 전력 공급 노이즈 유발 지터 기반의 고대역폭 메모리의 입출력 인터페이스 최적화 방법론」, KAIST 박사, 2024. 앞선 노트의 DesignCon 2025 수상자와 같은 인물이다 — [RISS 검색](https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EA%B3%A0%EB%8C%80%EC%97%AD%ED%8F%AD%20%EB%A9%94%EB%AA%A8%EB%A6%AC%20%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5&colName=bib_t)
- 이성희, 김현웅, 류승훈, 이상욱, 안승영, 「강화학습 기반 3차원-집적회로의 다중 전력망 전원 잡음을 고려한 디커플링 커패시터 최적화 방법」, 대한전자공학회 학술대회, 2023.6 — [RISS 검색](https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EB%94%94%EC%BB%A4%ED%94%8C%EB%A7%81%20%EC%BB%A4%ED%8C%A8%EC%8B%9C%ED%84%B0%20%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5&colName=re_a_kor)
- 앞선 노트의 2019 석사논문(DQN 디캡)과 2023 석사논문(HBM SI)은 KOASAS·DSpace 접속 실패(연결 리셋, 502)로 다시 확인하지 못했다. RISS 키워드 검색에서도 나오지 않았다. 여전히 [search-snippet]이다.

**(c) 다른 대학과 기업 [원문 확인: RISS 레코드]**
- **최성우(Seongwoo Choi), 이충용(Chungyong Lee), 「전자 회로 설계를 위한 PCB 부품 자동 배치 시스템」**, 대한전자공학회 학술대회 2024.11, pp. 57–60 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=1bbed88c8b28d298d18150b21a227875)
  - 초록: 센서와 IC 같은 주요 부품은 **LLM 기반 모듈**로, 저항과 커패시터 같은 수동소자는 **RL 기반 모듈**로 배치한다. 전기적 특성과 배선 효율을 기준으로 최적화한다.
  - 대상은 코딩 교육과 메이커 사용자, 비전문가다.
  - **이번 조사에서 확인한 국내 최초의 LLM·RL 기반 보드 레벨 부품 배치 학술 발표**다. 다만 학술대회 4쪽 논문이다.
- **Choi, SeongWoo, "An Automated Method for Passive Component Placement Ensuring Stable Communication and Routability"**, 연세대 전기전자공학과 석사, 2025.8 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=6656cc9e3edaf0faffe0bdc3ef48d419)
  - 방법: 회로도에서 연결된 부품의 상대 배치를 유지한다. 추정 배선길이, 레이어 전환 페널티, 지역 혼잡도로 후보 위치에 점수를 매긴다. 후보는 격자 표현(BoardMatrix)으로 필터링한다.
  - 실험: IoT 제품 PCB 7종에서 **KiCad 대비 총 배선길이를 평균 16% 줄였고**, 배선 성공률은 대부분 100%에 가까웠다. 설계당 배치는 **10초 이내**에 끝났다.
  - 초록상 이 학위논문은 ML이 아닌 규칙·점수 기반 방법이다.
- **Ok, Kihun, "A deep reinforcement learning-based decoupling capacitor selection algorithm"**, 성균관대 전자전기컴퓨터공학과 석사, 2025.2 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=c7a362e1fb76b395ffe0bdc3ef48d419)
  - 방법: **Double DQN과 Prioritized Experience Replay**로 디캡의 종류와 포트를 선택한다. 대상은 **여러 부하를 포함한 PCB 전력전달망**이다.
  - 보상함수를 바꿔 비용 효율을 고려하게 하자, 최소 개수의 디캡으로 목표 임피던스를 만족했다.
- **조범근(아주대), 「최적화 기법을 활용한 PCB 자동 설계 방법 연구」**, 박사, 2025.2. 주제어는 PCB, Escape routing, Integer Programming이다 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=ef3a59ff65a9a9c6ffe0bdc3ef48d419)
  - 내용: 혼합 신호와 **차동 페어**의 이스케이프 라우팅을 다층에서 동시에 최적화한다. 그래프 결과를 설계 규칙을 만족하는 PCB 레이아웃 좌표로 변환한다.
  - 결과: 수작업 라우팅보다 더 많은 신호를 더 짧은 배선으로 연결했다.
  - 학술지판은 조범근, 구형일, 「최적화 기법을 사용한 멀티레이어 이스케이프 라우팅 알고리즘」, 전자공학회논문지 62(1), 2025다. 레이아웃 변환을 ILP로 정식화했다. 비ML 연구다 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=25244f2f4a38ac1eb7998d826d417196)
- **하영서, 김형진(㈜티에스이), 심재창(국립경국대), 「잔여 배치 수용량 기반 적응적 순서와 다중 기준 후보 평가를 이용한 PCB 소자 자동 배치 기법」**, 멀티미디어학회논문지 29(8), 2026 — [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=2fc2e7a24ce235f07ecd42904f0c5d65)
  - 방법: 부품마다 남은 배치 수용량을 추정해 공간이 부족한 부품을 먼저 배치한다. 후보 위치는 연결 거리, 근접성, keep-out, 정렬, 밀집도로 평가한다. 충돌 검사와 평가는 **GPU로 병렬 처리**한다.
  - 결과: 부품 4,356개 중 4,305개를 배치해 **배치율 98.83%**를 달성했다. 비ML 휴리스틱이다.
- PCB 관련 설계에 RL을 쓴 학술지 논문: 김민승, 이은수, 「강화학습 기반 DAB 컨버터용 PCB 평면 변압기 최적 설계 연구」, 전력전자학회 논문지 30(4), 2025. 김광호, 홍영기, 박은병, 나완수, 「DDPG 방법을 이용한 4포트 EMI 필터의 설계 방법에 대한 연구」, 한국전자파학회 논문지 33(2), 2022. 둘 다 배치·배선이 아니라 부품·필터 설계다 — [RISS 검색](https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=PCB%20%EA%B0%95%ED%99%94%ED%95%99%EC%8A%B5&colName=re_a_kor)
- **2025 KAIS 춘계 포스터** — [KAIS 포스터 PDF](https://www.kais99.org/jkais/springNfall/spring2025/poster/2025_spring_227.pdf)
  - 제목: 「생성형 AI 기반 파이썬을 이용한 하드웨어 설계 오류 자동 검출 및 개선 사례」(A Case Study on Automated Detection and Improvement of Hardware Design Errors Using Generative AI and Python)
  - 저자: 김범진, 홍성율, 한기영, 방극희(**피에이치에이 H/W설계팀**)
  - 내용: 전장품 회로와 PCB 설계에서 테스트 포인트 누락·중복을 검출하고 디커플링 캐패시터 거리를 분석한다. 결과는 엑셀 보고서로 자동 생성한다.
  - 앞선 노트의 "저자·소속 미확인"을 해소한다.
- 기존 국내 계보 확인(비AI): 김현기, 우경환, 「인쇄회로기판 자동배치/배선 시스템 개발에 관한 연구」, 정보처리학회논문지 A 11(4), 2004. 한웅석, 김종찬, 「PCB CAD에서의 최적 배선을 위한 진화 프로그래밍을 이용한 자동 부품 배치」, 한국지능시스템학회논문지 6(3), 1996 — [RISS 검색](https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=PCB%20%EC%9E%90%EB%8F%99%20%EB%B0%B0%EC%B9%98&colName=re_a_kor)
- **검색 범위와 결과**: RISS 학위논문과 국내 학술논문에서 "PCB 강화학습", "PCB 배치 딥러닝", "PCB 배선 인공지능", "PCB 자동 배치", "PCB 설계 자동화", "회로도 생성 LLM", "PCB 설계 대규모 언어모델", "부품 배치 강화학습"을 검색했다. **LLM 회로도 생성 관련 국내 논문은 0건**이었다. ML이나 LLM 기반 보드 배치·배선 학술지 논문도 0건이었다 — [RISS 검색 예시](https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%ED%9A%8C%EB%A1%9C%EB%8F%84%20%EC%83%9D%EC%84%B1%20LLM&colName=bib_t)

**(d) GitHub 신규 발견 [GitHub-verified, 비동료심사]**
- **MoTT: Modal-Token Transformer for Generalizable Decoupling Capacitor Placement** — [GitHub jeehoo0507/MoTT](https://github.com/jeehoo0507/MoTT)
  - 저장소: 한국어 README, 2026-11-13 push, 결과는 보고서 PDF로 공개했다.
  - 방법: 판을 좌표 대신 공진 모드, 칸, 디캡 토큰으로 표현해 PCB, 패키지, 인터포저에 일반화하려 한다.
  - 처음 보는 판 종류에서의 성공률: PCB형 0.89, 인터포저형 0.99(좌표 입력 모델은 0.64, 0.65)
  - 재구현 비교(하네스 적용, PCB형): MoTT 0.99, B-DevFormer 0.79, B-Park 0.04
  - 저자 실명과 소속은 확인하지 못했다.

### Inferences
- 국내 "AI × 보드 레벨 PCB" 학술 연구는 2024–2025년에 본격적으로 나타났다. 축은 둘이다.
  - **PDN·디캡 RL**: KAIST 강형민·김경묵, 성균관대 옥기훈. 보드 레벨 PCB를 명시적으로 다룬다.
  - **LLM·RL 부품 배치**: 연세대 최성우·이충용 2024 학술대회
- 다만 둘 다 학위논문이나 학술대회 수준이다. 학술지(KCI급) 논문과 회로도 생성 LLM 연구는 비어 있다. 모디팩토리의 "LLM 기반 PCB 부품 자동 배치 모델"(채용공고 기준)과 가장 가까운 국내 선행연구는 **연세대 2024 학술대회 논문**이다. 산학 협력이나 선행기술 검토 대상으로 우선 고려할 만하다.
- 연세대 석사논문의 "KiCad 대비 배선길이 16% 감소, 10초 이내 배치"와 ㈜티에스이의 "부품 4,356개 중 98.83% 배치(GPU)"는 비ML 기준선으로 쓰기 좋다. 모디팩토리의 90분 SLA 안에서 쓸 수 있는 빠른 휴리스틱 배치 근거가 된다.

### Gaps
- KAIST KOASAS·DSpace에 접속하지 못해 2019·2023 석사논문 저자와 강형민 박사논문 초록 본문을 확인하지 못했다.
- 최성우·이충용(2024)의 LLM·RL 모듈 상세와 정량 결과를 확인하지 못했다. 원문은 DBpia에서 제공한다.
- 멀티미디어학회논문지, 전자공학회논문지, 전력전자학회 논문지의 KCI 등재 여부는 KCI에서 직접 확인하지 못했다. kci.go.kr 루트가 400을 반환했다.
- MoTT 저자 신원을 확인하지 못했다.

---

## Q4. 2026년 PCB용 GenAI 서베이(Srinivasan, Turnbull, Pearce) 확인

### Takeaway
arXiv API 원문 메타데이터로 확인한 서지는 다음과 같다. 제목은 "Surveying GenAI-based Automation in Printed Circuit Board Design and Test", 저자는 Sahana Srinivasan, Benjamin Turnbull, Hammond Pearce, arXiv:2606.17074, 2026-06-10 제출이다. 코멘트는 "33 pages, 5 figures, 11 tables. Under review"다.

같은 그룹이 같은 날 PCB-QA(480 QA 쌍)도 제출했다.

### Cited Findings
- 초록 — [arXiv](https://arxiv.org/abs/2606.17074) [원문 확인]
  - 범위: 공급망, 시스템 사양, 회로 설계, 레이아웃·최적화, 검증·테스트, 조립·유통까지 PCB 생애주기 전체를 다룬다.
  - 문헌을 의도와 기여 기준으로 분류하는 체계를 제시한다.
  - 핵심 과제로 도메인 특화 데이터 부족과 기존 PCB 도구와의 통합 지원 부족을 꼽는다.
- 같은 그룹의 실증 연구인 PCB-QA(Benjamin Tan 추가, 8쪽)는 텍스트 기반 PCB 형식(JSON)을 쓰면 LLM 평가가 가능하다는 것을 보였다 — [arXiv](https://arxiv.org/abs/2606.23704) [원문 확인]
- GitHub 목록 tikyttqq/Awesome-PCB-Routing의 Surveys 섹션에도 실려 있다 — [GitHub](https://github.com/tikyttqq/Awesome-PCB-Routing)

### Inferences
- 보고서에서 PCB GenAI 1차 서베이로 인용해도 된다. "under review" 상태라는 점은 명시해야 한다.

### Gaps
- 분류 체계의 세부 항목, 인용 논문 목록, 저자 소속(UNSW)을 확인하지 못했다. arXiv 메타데이터에는 소속이 없고, 본문 PDF는 이번에 읽지 않았다.

---

## Q5. 검증 상태 요약과 남은 미검증 항목

### Takeaway
요청받은 핵심 논문 전부와 UNSW 서베이를 [원문 확인] 또는 [GitHub-verified]로 올렸다. 다만 PCB-Bench의 모델별 점수는 OpenReview 차단으로 확인하지 못했다. 국내 항목은 RISS 원문 레코드로 학위논문 4건, 학술대회 논문 2건, 학술지 논문 4건을 새로 확인했다.

### Cited Findings
| 항목 | 판정 | 근거 |
|---|---|---|
| RL_PCB 17%/21% | 원문 확인 | [UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782) |
| Cypress 1–5.9배, 1–19.7배, 492.3배 | 원문 확인 | [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf) |
| PCBWorld 679 보드, 8 지표, D3-A 표 | 원문 확인 | [arXiv](https://arxiv.org/abs/2607.05915) |
| CADET 38.0→67.2%, FreeRouting 65.6% | 원문 확인 | [arXiv](https://arxiv.org/abs/2611.16913) |
| PCB-Bench 약 3,700/약 500/174 | GitHub-verified (OpenReview 차단) | [github.io](https://digailab.github.io/PCB-Bench/) |
| PCBInnoBench 372, 22.0%/7.3% | 원문 확인 | [NeurIPS](https://neurips.cc/virtual/2026/poster/139034) |
| PCB Gym 32.1% | 원문 확인 | [NeurIPS](https://neurips.cc/virtual/2026/161602) |
| EDA Bench 35, 4.58%, 21/35 | 원문 확인 | [ICML](https://icml.cc/virtual/2026/77908) |
| SchGen 82%, 60.5%, 기준선 32% | 원문 확인 | [arXiv HTML](https://arxiv.org/html/2605.30345v1) |
| pcbGPT 0.90/1.00, hard 0.72 | 원문 확인 | [arXiv](https://arxiv.org/abs/2606.01188) |
| PCBSchemaGen v1 23개 / v2 227개, 81.3% | 원문 확인 | [v1](https://arxiv.org/abs/2602.00510v1); [v2](https://arxiv.org/abs/2602.00510v2) |
| PCBSchemaGen 77.5%, 65개 | search-snippet (원문과 불일치) | [DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf) |
| DRCY 서지, 5-에이전트 구조 | 원문 확인 | [arXiv](https://arxiv.org/abs/2603.15672) |
| DRCY 리뷰 11건, DDR5 100% | search-snippet (벤더 블로그, 논문에 없음) | [AllSpice](https://www.allspice.io/post/how-hardware-engineering-teams-evaluate-drcy) |
| HWE-Bench 300/2,914/8.15%, 저자 | 원문 확인 | [arXiv](https://arxiv.org/abs/2603.18102) |
| PCB-QA 480쌍, 93% | 원문 확인 | [arXiv](https://arxiv.org/abs/2606.23704) |
| OmniLayout 1,681/77.24K, 데이터 철회 | 원문 확인 + GitHub-verified | [arXiv](https://arxiv.org/abs/2607.03261); [GitHub](https://github.com/AAAAAiden/OmniLayout-Benchmark) |
| DevFormer 30% 이상 감소 | 원문 확인 | [arXiv](https://arxiv.org/abs/2205.13225) |
| AlphaChip 비판 TCAD 게재 | 원문 확인 | [arXiv](https://arxiv.org/abs/2302.11014) |
| UNSW 서베이 서지 | 원문 확인 | [arXiv](https://arxiv.org/abs/2606.17074) |
| KAIS 2025 포스터 저자·소속 | 원문 확인 | [PDF](https://www.kais99.org/jkais/springNfall/spring2025/poster/2025_spring_227.pdf) |
| 국내 LLM·RL PCB 배치(연세대 2024) | 원문 확인 (RISS 초록) | [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=1bbed88c8b28d298d18150b21a227875) |
| KAIST 2019·2023 석사논문 | search-snippet (KOASAS 접속 실패) | [KOASAS](https://koasas.kaist.ac.kr/handle/10203/266736) |

### Inferences
- 앞선 노트에서 고쳐야 할 사항은 아래와 같다.
  1. PCB-Bench 실제 프로젝트 수를 174개로 고친다.
  2. Unet-Astar의 코드는 공개되지 않았다.
  3. PCBWorld 결과는 "소형 보드에서는 PPO가 규칙 기반을 능가, 대형 보드에서는 뒤처짐"으로 고친다.
  4. CADET의 비교 기준이 RL-only라는 점을 명시한다.
  5. AlphaChip 비판 논문은 TCAD 판으로 바꾼다.
  6. DRCY 성과 수치는 벤더 블로그 출처로 강등한다.
  7. HWE-Bench와 DRCY 저자를 추가한다.
  8. PCBSchemaGen 헤드라인을 v2의 81.3%로 바꾼다.
  9. 국내 학위논문 공백 결론을 "PDN·디캡 RL 학위논문과 LLM·RL 배치 학술대회 논문은 있음, 학술지와 회로도 생성 LLM은 공백"으로 수정한다.

### Gaps (남은 미검증 목록)
1. PCB-Bench의 모델별 점수: OpenReview 챌린지로 막혔다.
2. PCBSchemaGen 77.5%와 65개 과제의 측정 대상
3. PCBench 데이터셋 규모 상충: 164개 대 679개 파생
4. 큐레이션 목록에만 실린 약 20편의 저자와 결과: PCBAgent, TRouter, GPT 라우팅 계열, Integration 2026 논문 등
5. PCB Gym과 PCBInnoBench의 저자, 공식 코드 공개 상태
6. KAIST KOASAS 학위논문(2019, 2023)의 저자와 초록, 강형민 박사논문 초록 본문
7. 최성우·이충용(2024) LLM·RL 배치 시스템의 정량 결과(DBpia 원문)
8. 국내 학술지의 KCI 등재 여부
9. UNSW 서베이의 분류 체계 세부와 저자 소속
