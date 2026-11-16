# 보충 조사: GitHub 1차 자료로 AI 기반 PCB 설계 학술 주장 검증하고 누락 문헌 보완하기

> **검증 방법과 라벨 (보고서 작성자 필독)**
> - 조사일: 2026-11-16. 앞선 노트(`international_academic.md`, `korean_academic.md`)는 대부분 검색 스니펫으로만 확인했다. 이번에는 GitHub에 올라온 공식 저장소의 README와 저장소 안의 논문 PDF를 직접 내려받아 읽었다. 경로는 raw.githubusercontent.com, github.io, api.github.com의 검색 엔드포인트다.
> - 저장소 안에 논문 PDF가 있는 경우(LG AI Research의 CADET.pdf, PCBWorld.pdf)는 `pdftotext`로 본문, 표, 참고문헌까지 확인했다.
> - **라벨 정의**
>   - **[GitHub-verified]**: 공식 저장소의 README, 저장소 내 PDF, 또는 github.io 프로젝트 페이지에서 직접 확인했다.
>   - **[GitHub-verified·참고문헌]**: GitHub에 올라온 1차 논문 PDF의 참고문헌 목록에 해당 서지가 실려 있는 것까지만 확인했다. 그 논문 자체를 읽지는 않았다.
>   - **[원문-verified]**: GitHub가 아닌 저자 서버의 논문 PDF를 직접 읽었다. Cornell 서버의 Cypress, 저자 홈페이지의 ModuPlace가 여기에 해당한다.
>   - **[search-snippet]**: 웹 검색 스니펫으로만 확인했다.
>   - **[unverified]**: 제3자 큐레이션 목록에만 실려 있거나, 확인 수단이 없었다.
> - **차단·제약 사항**
>   - github.com HTML 페이지는 프록시가 403을 반환했다. api.github.com의 저장소·조직 단위 엔드포인트(`/repos/...`, `/orgs/...`)는 "세션에 연결된 저장소만 허용"이라는 메시지와 함께 막혔다. 그래서 저장소 파일 목록과 조직의 저장소 목록은 볼 수 없었다.
>   - 저장소 검색 API, raw 파일, github.io는 정상적으로 열렸다.

---

## Q1. 핵심 논문의 공식 저장소에서 제목, 저자, 학회, 핵심 수치 확인하기

### Takeaway
LG AI Research의 PCBWorld와 CADET는 저장소에 논문 PDF가 함께 올라와 있어 저자, 학회, 수치를 모두 1차 자료로 확인했다. CADET의 "38.0% → 67.2%"는 RL 단독 기준선(PPO on RouteDemos)과 비교한 수치이고, FreeRouting @1(65.6%)과는 비슷한 수준이다.

PCBSchemaGen의 과제 수가 23, 65, 227로 서로 다른 문제는 판본 차이로 설명된다.
- v1 저장소에는 23개 과제가 있다.
- v2(NeurIPS 2026) 저장소에는 PCBBench 62개와 Open-Schematics 165개, 합계 227개가 있다.
- PCBBench 과제 ID는 1–65 범위이고, 그중 3개가 비어 있다.

"77.5%"는 어느 GitHub 저장소에서도 확인되지 않아 미해결로 남는다.

주의할 정정이 두 가지 있다.
- Unet-Astar 저장소에는 코드가 없다.
- PCBWorld, CADET 체크포인트와 PCBSchemaGen v2 코드는 **비상업 라이선스**다. 상용 서비스(모디팩토리)에 그대로 쓸 수 없다.

### Cited Findings

**[1] RL_PCB: Vassallo & Bajada, DATE 2024 [GitHub-verified: 서지 / search-snippet: 수치]**
- README의 BibTeX에 실린 서지는 다음과 같다. Luke Vassallo, Josef Bajada, "Learning Circuit Placement Techniques Through Reinforcement Learning with Adaptive Rewards," 2024 DATE, pp. 1–6. IEEE 문서 번호는 10546526이고, MIT 라이선스(© 2023 Luke Vassallo)다 — [GitHub LukeVassallo/RL_PCB](https://github.com/LukeVassallo/RL_PCB)
- README가 직접 밝힌 내용은 다섯 가지다 — [GitHub RL_PCB](https://github.com/LukeVassallo/RL_PCB)
  - 셀룰러 오토마타에서 착안한 방법으로, 각 부품이 에이전트가 되어 국소·전역 정보로 자기 위치를 갱신한다.
  - "post-routing wirelength 기준으로 확률적 방법(stochastic methods)을 능가"한다.
  - 평가 시 SA 기준선과 함께 A* 기반 라우터로 배선한 뒤 HPWL과 routed wirelength를 표로 정리한다.
  - KiCad `.kicad_pcb` 파서를 포함한다.
  - 석사논문은 AlphaChip(Mirhoseini et al.)의 한계를 분석하고, 그에 대한 대안으로 이 방법을 제안했다.
- "미학습 회로에서 SA 대비 TD3 17%, SAC 21% 감소"라는 수치는 README에 없다. 여전히 [search-snippet]이다.

**[2] Cypress: NVlabs, ISPD 2025 [GitHub-verified: 서지 / 원문-verified: 수치]**
- README BibTeX: "Cypress: VLSI-Inspired PCB Placement with GPU Acceleration," Niansong Zhang, Anthony Agnesina, Noor Shbat, Yuval Leader, Zhiru Zhang, Haoxing Ren, *Proceedings of the 2025 International Symposium on Physical Design*. DREAMPlace를 확장했고, 하이퍼파라미터 튜너는 AutoDMP에서 착안했다 — [GitHub NVlabs/Cypress](https://github.com/NVlabs/Cypress)
- 원문 초록에서 확인한 수치 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
  - 제안 벤치마크에서 routability가 1–5.9배 높았다.
  - 완전 배선된 설계의 routed track length가 **1–19.7배 짧았다**(새로 확인한 수치).
  - GPU 가속으로 런타임이 최대 492.3배 빨라졌다.
  - 본문은 이 속도 향상을 "current state-of-the-art solutions" 대비라고 표현한다. 표의 평균은 SA-PCB 기준으로 정규화되어 있다.
- 비교 기준선은 NS-Place(+ 개선판 NS-Place+), OpenROAD SA-PCB, **상용 Quilter**(2024-04-04 버전, 클라우드 제출)였다. routability는 FreeRouting v1.9.0으로 2층 기준으로 측정했다. Cypress는 V100 GPU에서, 비교 도구는 Xeon CPU에서 실행했다 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
- 경쟁 맥락에서 쓸 만한 원문 서술 — [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
  - "Quilter는 부품 176개 설계 레이아웃에 2.6시간이 걸린다."
  - Quilter가 지원하는 범위는 핀 1,000개 미만, 부품 100개, 밀도 10%, 500 MHz, 2 A다.
  - Cadence Allegro X AI는 MCTS 기반이며 대형 설계에는 제약이 있다.

**[3] PCBWorld: LG AI Research, KDD 2026 Workshop [GitHub-verified, PDF 포함]**
- 서지: Hyungseok Song*, Junseok Park*, Won-Seok Choi*, Seohui Bae, Han-Seul Jeong, Youngjoon Park†, Soonyoung Lee†(LG AI Research, 서울). *KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI*(2026-08-09~13, 제주), arXiv:2607.05915 — [README](https://github.com/LGAI-Research/PCBWorld); [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
- 환경 구성 — [README](https://github.com/LGAI-Research/PCBWorld)
  - 버전 v1.2.2이며, KiCad 9.0.8의 push-and-shove 라우터를 Gymnasium 환경으로 감쌌다.
  - 모든 스텝을 KiCad DRC로 채점한다.
  - 기준선은 세 계열이다. decoder-only PPO/GRPO 트랜스포머, LLM 도구 호출 에이전트, 규칙 기반 Freerouting과 KRT(KiCadRoutingTools)다.
- 데이터셋 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - "679개 실보드"(D3)를 원문으로 확인했다. 이 보드들은 PCBench 오픈소스 코퍼스에서 파생했고, KiCad 9로 변환한 뒤 완전 연결·DRV 0인 보드만 남겼다.
  - 패드 수 기준으로 D3-A/B/C로 나눈다. D3-B(Medium)는 287개, D3-C(Large)는 292개다.
  - 평가 지표는 8개다.
- README 표(논문 Table 3, D3-A 99개 소형 보드, @5 프로토콜)의 CP(clean pass) 값 — [README](https://github.com/LGAI-Research/PCBWorld)

  | 방법 | CP |
  |---|---|
  | Freerouting | 0.80 |
  | KRT | 0.74 |
  | LLM 에이전트 GPT-5.4 | 0.65 (231초/보드) |
  | GPT-5.4-mini | 0.28 |
  | Qwen3.5-397B | 0.34 |
  | **PPO(합성 보드로만 학습, zero-shot)** | **0.86** (1.83초) |

  - Pot.(potential) 지표는 Freerouting이 22.71로 PPO(21.46)보다 높았다.
- **기존 노트 수정이 필요하다.** 초록의 "learning-based methods still lag behind rule-based routers"는 기존 연구 전반에 대한 진단이다. PCBWorld 자체 결과는 "PPO가 소형 보드에서 모든 기준선을 능가했지만, 대형 보드에서는 가장 강한 규칙 기반 라우터에 뒤처졌다"이다. 저자들은 대형 보드 라우팅을 RL과 LLM 모두에게 미해결 과제로 남겼다 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
- 라이선스 — [README](https://github.com/LGAI-Research/PCBWorld)
  - 환경 코드는 BSD-3-Clause다.
  - 엔진(LGAI-Research/PCBWorld-Engine, KiCad 수정본)은 **GPLv3**다.
  - 학습된 체크포인트는 **EXAONE AI Model License 1.2 – NC**(연구·교육용, 체크포인트와 그 출력의 상업적 사용 금지)다.

**[4] CADET: LG AI Research, 프리프린트 [GitHub-verified, PDF 포함]**
- 제목은 "CADET: Construction of PCB Routing Instances with Executable Demonstrations"이고, 저자는 PCBWorld와 같은 7명이다. PDF 표지는 "Preprint"이며 학회 표기는 없다. 코드는 BSD-3, 체크포인트는 EXAONE NC 라이선스다 — [GitHub LGAI-Research/CADET](https://github.com/LGAI-Research/CADET); [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)
- 초록 원문에서 확인한 내용 — [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)
  - 합성 데이터셋 RouteDemos는 DRV 0으로 배선된 합성 보드 100,000개와 그 엔진 행동 시연으로 구성된다.
  - 17개 통계에서 실제 참조 보드 142개의 분포와 유사하다.
  - 행동 복제(BC) 후 RL로 미세조정한 결과, 실제 테스트 보드의 "complete DRV-free routing" 비율이 **RL-only 기준선 대비 38.0% → 67.2%**로 올랐다.
  - 이 수치는 FreeRouting과 비슷하고 GPT-6 Astra 등 나머지 기준선보다 높았다.
  - 38.0%는 "PPO (RouteDemos)" 행으로, 시드 간 ±6.2다.
- README 결과표(D3-B test 141개 보드) — [README](https://github.com/LGAI-Research/CADET)

  | 방법 | CP | Rout. | 시간 |
  |---|---|---|---|
  | FreeRouting @1 | 65.6% | 96.8% | 45.6초/보드 |
  | GPT-6 Astra @1 | 56.0% | – | 491.7초 |
  | GPT-6 Luna @1 | 5.0% | – | – |
  | CADET @1 | 67.2% | 91.7% | **15.5초** |
  | CADET @3 | **79.8%** | 95.9% | 47.6초 |

- D3-A(99개 보드)에서는 FreeRouting @1이 82.1%, CADET @1이 89.5%, CADET @3이 96.3%였다 — [README](https://github.com/LGAI-Research/CADET)
- 저자들의 문제 인식: 공개 보드 컬렉션은 각각 약 1천 개 수준이고, 대부분 완성된 보드만 있을 뿐 EDA 엔진 조작 시연은 없다 — [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)

**[5] PCB-Bench: ICLR 2026 [GitHub-verified]**
- 저자는 Jindong Li, Lianrong Chen, Bin Yang, Jiadong Zhu(공동 1저자), Ying Wang, Yuzhe Ma, Menglin Yang(교신)이다. 소속은 **The Hong Kong University of Science and Technology (Guangzhou)**이고, OpenReview id는 Q5QLu7XTWx다 — [github.io 프로젝트 페이지](https://digailab.github.io/PCB-Bench/); [GitHub digailab/PCB-Bench](https://github.com/digailab/PCB-Bench)
- 규모 — [README](https://github.com/digailab/PCB-Bench)
  - 전문가가 작성한 자유형 QA 약 1,800개와 각각의 객관식 버전, 합계 약 3,700문항
  - 멀티모달 문제 약 500개
  - **실제 PCB 프로젝트 174개**(OSHWHub/JLCPCB 출처). 앞선 노트의 "170개 이상"을 174개로 정정한다.
  - 평가는 제로샷이며, Qwen2.5-7B-Instruct 기반 도메인 특화 변형도 평가했다.

**[6] PCBSchemaGen: 23 / 65 / 227 과제 수 상충 해소 [GitHub-verified] / 77.5% [search-snippet, 미해결]**
- **v1**(arXiv:2602.00510v1) — [GitHub Sthyao/PCBSchemaGen](https://github.com/Sthyao/PCBSchemaGen)
  - 제목: "PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards (PCB)"
  - 저자: Huanghaohe Zou, Peng Han, Emad Nazerian, Alex Q. Huang
  - `benchmark.tsv`는 **23개 과제**다. Easy는 P1–P6, Medium은 P7–P16, Hard는 P17–P23(동기 벅, DAB, LLC, 3상)이다.
- **v2/NeurIPS 2026** — [GitHub HZou9/PCBSchemaGen_v2](https://github.com/HZou9/PCBSchemaGen_v2)
  - 제목: "PCBSchemaGen: Reward-Guided LLM Code Synthesis for Printed Circuit Boards (PCB) Schematic Design with Structured Verification"
  - 저자: v1 4인에 Mafu Zhang, Zhicheng Guo가 추가됐다.
  - 벤치마크는 `pcbbench/benchmark.tsv` **62개**(Easy 17, Medium 28, Hard 17)와 Open-Schematics-Eval **165개**(Easy 40, Medium 48, Hard 77)다. 합계 **227개**이며, 도메인은 22개다.
- **65의 출처(추정)**: 직접 내려받은 PCBBench TSV의 ID는 1–65이고, **48, 53, 63번이 비어 있다**. README의 실행 예시도 `--task-range 1-65`이고 "suite에 없는 ID는 건너뜀"이라고 적혀 있다. DOE 슬라이드의 "65개 과제"는 ID 범위 또는 정리 전 개수일 가능성이 높다. 다만 이것은 추정이다 — [benchmark.tsv](https://github.com/HZou9/PCBSchemaGen_v2/blob/main/benchmarks/pcbbench/benchmark.tsv)
- **77.5%**: GitHub 어디에도 없다. DOE 리뷰 슬라이드(2026-07)에만 나온다. 검색 요약에 따르면 같은 슬라이드에 63.6%라는 두 번째 수치도 있다. 제3자 요약은 v2 기준 86–88% Pass@1을 언급하지만 2차 출처라 확인하지 못했다 — [DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf) [search-snippet]
- 검증기 구조(README에 명시) — [README v2](https://github.com/HZou9/PCBSchemaGen_v2)
  - 문법 검사와 샌드박스 SKiDL 실행에 KiCad ERC를 더한 뒤 단계별 검사를 한다. L1 전기 불변식, L4 전력전자 불변식, L1b 핀 역할 호환성, L2 하위범주 템플릿, L3 토폴로지 시그니처, 동기 벅 스위치 노드 검사 순이다.
  - 보상은 처음 실패한 단계에 따라 0.0–1.0 계단식으로 정해진다.
  - 기본 정제 정책은 Thompson Sampling이고, 예시 모델은 `google/gemma-4-31b-it`다.
- **라이선스**: 코드는 **PolyForm Noncommercial 1.0.0**이고, 상업 라이선스는 hzou@utexas.edu로 문의해야 한다. 벤치마크와 KG는 MIT다 — [README v2](https://github.com/HZou9/PCBSchemaGen_v2)

**[7] SchGen: Microsoft [GitHub-verified: 서지·방법 / search-snippet: 수치]**
- 저자: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu, arXiv:2605.30345 — [GitHub microsoft/SchGen](https://github.com/microsoft/SchGen)
- 방법 — [README](https://github.com/microsoft/SchGen)
  - GPT-oss-20b의 전문가 레이어 7, 15, 23에 LoRA를 적용해 2 epoch 학습한다.
  - 학습 데이터는 SparkFun(CC BY-SA 4.0) 기반이다. 각 샘플에 KiCad 회로도, 코드 표현(L1/L2/L3), 합성 요청, CoT 추론 과정이 들어 있다.
  - KiCad 8.0.9를 쓰며, 코드는 MIT 라이선스다.
- README의 면책 문구: "전기적 정확성이나 제조 가능성을 보장하지 않으며, 제작 전 사람 검토가 필요하다."
- 유효 회로율 82%와 기능 정확도 60.5%는 README에 없다. 여전히 [search-snippet]이다.

**[8] pcbGPT [GitHub-verified: 저장소 / search-snippet: 수치]**
- 저장소는 tk-king/pcbGPT다. 기능은 KiCad 라이브러리 기반 부품 검색, 데이터시트 분석(참조 회로·핀 구성 추출), LLM 검증 루프, KiCad와 SPICE 넷리스트 내보내기다. 웹 UI와 데스크톱 앱(Windows/macOS)도 배포한다 — [GitHub tk-king/pcbGPT](https://github.com/tk-king/pcbGPT)
- README는 "제작 전 자격 있는 엔지니어 검토 필수"라고 명시한다. pass@1 0.90 등 수치는 README에 없다.

**[9] HWE-Bench: 보드 레벨 회로도 [GitHub-verified: 저장소·파이프라인 / search-snippet: 수치]**
- 저장소는 EDI-Systems/HWE-Bench다. README에는 "[Conference 2026]"과 arXiv "xxxx.xxxxx" 같은 자리표시자가 남아 있어 학회명을 확인할 수 없다 — [GitHub EDI-Systems/HWE-Bench](https://github.com/EDI-Systems/HWE-Bench)
- 파이프라인은 세 단계다 — [README](https://github.com/EDI-Systems/HWE-Bench)
  - MinerU로 PDF 데이터시트를 파싱해 JSON 부품 라이브러리를 만든다.
  - 4단계 생성: 모듈 분할 → 부품 선정 → 모듈 연결 → 시스템 넷리스트
  - 정적 규칙(MCU 핀 충돌, 버스 정합)과 LTspice 다단계 과도 시뮬레이션으로 이중 검증한다.
- 과제 300개, 데이터시트 2,914개, 최고 통과율 8.15%는 README에 없다. 여전히 [search-snippet]이다.
- **동명 혼동 주의**: pku-liang/hwe-bench는 RTL 버그 수리 벤치마크다(오픈 하드웨어 6개 프로젝트의 실제 버그 수정 사례 417개, arXiv:2604.14709). 2026-11-10에 v1.1이 공개됐다 — [GitHub pku-liang/hwe-bench](https://github.com/pku-liang/hwe-bench)

**[10] EDA Bench [GitHub-verified: 과제 수·채점 / search-snippet: 4.58%, ICML]**
- 저장소 EDA-bench/eda-bench의 내용 — [README](https://github.com/EDA-bench/eda-bench); [DATA_CARD](https://github.com/EDA-bench/eda-bench/blob/master/DATA_CARD.md)
  - Harbor 프레임워크 기반 과제 **35개**로, "실제 PCB 설계 기반"이다.
  - 에이전트는 KiCad 9와 ngspice 환경에서 `.kicad_pro/.kicad_sch/.kicad_pcb` 전체를 만들어야 한다.
  - 검증기는 네트워크가 차단된 컨테이너에서 연결성, 외부 I/O, ngspice 시뮬레이션, 전원·단락 안전, ERC/DRC, 회로도·PCB 일관성을 검사한다.
  - 난이도별 가중 평균을 쓴다(very easy 1.0부터 extreme 5.0까지).
- DATA_CARD가 밝힌 한계: 에이전트 단계에서 공개 네트워크 접근이 허용되므로 closed-book 시험이 아니다. 자동 검사는 "제조 인증이 아닌 공학적 프록시"다 — [DATA_CARD](https://github.com/EDA-bench/eda-bench/blob/master/DATA_CARD.md)
- 4.58% 수치와 ICML 2026 게재는 README에 없다.

**[11] OmniLayout [GitHub-verified, 중요한 새 사실 있음]**
- 저장소 AAAAAiden/OmniLayout-Benchmark에서 확인한 내용 — [GitHub](https://github.com/AAAAAiden/OmniLayout-Benchmark)
  - EAGLE 보드에서 파생한 **그래프 JSON 1,681개**와 위치 레코드 **77,236개**를 확인했다. 앞선 노트의 "77.24K"와 일치한다.
  - 넷은 55,830개, SMD 패드 레코드는 168,815개다.
- **새 사실**: 데이터셋 다운로드가 "출처별 라이선스·저작자 표시 검토를 위해 일시 철회"되었다. v0.1.0 릴리스는 비공개 초안으로 돌려졌다. 코드만 MIT로 공개되어 있다 — [GitHub](https://github.com/AAAAAiden/OmniLayout-Benchmark)
- 초기 릴리스에는 회로도 이미지, 회로도–보드 짝 테이블, 공식 train/val/test 분할이 없다 — [GitHub](https://github.com/AAAAAiden/OmniLayout-Benchmark)

**[12] FanoutNet: AAAI 2023 [GitHub-verified·참고문헌]**
- 공식 코드 저장소는 찾지 못했다. LG AI의 PCBWorld.pdf와 CADET.pdf 참고문헌에서 정확한 서지를 확인했다. Haiyun Li, Jixin Zhang, Ning Xu, Mingyu Liu, *AAAI* 37(7):8554–8561, 2023, DOI 10.1609/aaai.v37i7.26030 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf); [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)

**[13] DevFormer: KAIST, ICML 2023 [GitHub-verified]**
- 제목은 "DevFormer: A Symmetric Transformer for Context-Aware Device Placement"이고, 저자는 Haeyeon Kim, Minsu Kim, Federico Berto, Joungho Kim, Jinkyoo Park다. ICML 2023(2023-05 채택)에 실렸다 — [GitHub kaist-silab/devformer](https://github.com/kaist-silab/devformer)
- 저장소 이력 — [README](https://github.com/kaist-silab/devformer)
  - 설치 안내는 `ai4co/devformer`로 이전했다.
  - 디캡 배치 문제(DPP)와 다중 포트 변형은 2023-09부터 RL4CO 환경에 포함됐다.
  - 2024-09에는 NeurIPS 2024 논문 ReEvo에서 LLM이 DPP의 새 SOTA 휴리스틱을 찾았다.
- "부품 수 30% 이상 감소"는 README에 없다. PMLR 초록 기준의 [search-snippet]이다.

**[14] Google circuit_training(AlphaChip)과 비판 저장소 [GitHub-verified]**
- circuit_training README가 밝힌 내용 — [GitHub google-research/circuit_training](https://github.com/google-research/circuit_training)
  - 프레임워크 이름을 "AlphaChip"으로 쓰고, "Nature 2021 논문의 방법론을 재현한다"고 명시한다.
  - "Alphabet 안팎에서 칩 레이아웃 설계에 쓰인다"고 주장한다(Google 측 주장).
  - 사전학습 체크포인트를 공개했고, 사전학습이 속도, 신뢰성, 품질을 높인다고 ISPD 2022 후속연구(Yue et al.)를 인용한다.
- TILOS MacroPlacement의 최신 상황 — [GitHub TILOS-AI-Institute/MacroPlacement](https://github.com/TILOS-AI-Institute/MacroPlacement)
  - **2025-12-16**에 저널 논문 "An Updated Assessment of Reinforcement Learning for Macro Placement"가 **IEEE TCAD에 채택**되어 조기 공개됐다(IEEE Xplore 11300304).
  - 이 논문은 ISPD23 논문에 제기된 네 가지 비판에 답한다. 사전학습 미사용, 수렴 문제, 45/12nm 대 7nm 공정 차이, 계산 자원 규모다. 결론은 ISPD23과 같다. **"강화한 SA가 사전학습된 CT(AlphaChip)보다 여전히 우수하다."**
  - 이 SA 결과는 익명 심사위원 1인과 Georgia Tech/USC의 S.-K. Lim 교수 그룹 학생들이 재현했다.
  - 2026-01-05에는 TCAD 심사 중 CT+DREAMPlace(CT-AC-DP) 추가 평가 결과를 공개했다.
  - FAQ: Google 엔지니어에게서 CT 실행이 올바르다는 확인을 두 차례 받았다(2022-08-10, 10-03). 사전학습 데이터인 TPU 블록 20개와 Nature 당시의 사전학습 코드는 공개되지 않았다.
  - 2025-03 갱신에서는 2024-08에 공개된 사전학습 체크포인트로 미세조정까지 평가했다.
- 앞선 노트는 "arXiv v3(2026-03)"를 인용했는데, 동료심사를 거친 TCAD 판으로 갱신해야 한다.

**[15] 기타 저장소 확인 결과**
- **Unet-Astar**(IEEE Access 2023): 저장소 README 전문은 "The code is still modifing, and it will be provided after the papaer is accepted."다. **코드가 공개되지 않았다.** 앞선 노트의 "코드는 GitHub" 표현을 정정해야 한다 — [GitHub Firesuiry/Unet-Astar-For-PCB-Routing](https://github.com/Firesuiry/Unet-Astar-For-PCB-Routing)
- **PCBInnoBench**(NeurIPS 2026): GitHub에 speder-eda/pcbinnobench 저장소가 있다(설명 없음, 2026-11-05 push). README는 main과 master 브랜치 모두 404였다. 검색 스니펫상 데이터와 코드는 익명 저장소(anonymous.4open.science/r/pcbinnobench-C841)에 있다 — [GitHub 검색 결과](https://github.com/speder-eda/pcbinnobench) [unverified: 내용]
- **PCB Gym**(NeurIPS 2026): GitHub 저장소를 찾지 못했다. 설계 의도 기술 언어인 Zener는 Diode Computers의 diodeinc/pcb로 보인다(검색 스니펫) — [NeurIPS](https://neurips.cc/virtual/2026/161602) [search-snippet]
- **PCB-QA, DRCY**: 공개 저장소를 찾지 못했다. DRCY는 AllSpice 상용 제품이다.
- **pasplett/pcb-node-pair-gnn**(GNN 회로도 부품 추가, arXiv 2506.10577): README가 main과 master 모두 404였다. 저장소가 비공개이거나 README가 없을 수 있다 [unverified].

### Inferences
- PCBWorld와 CADET는 저자, 수치, 라이선스까지 1차 자료로 확인한 **이 분야에서 가장 검증 수준이 높은 문헌**이다. 보고서에서 "학습형 라우터가 FreeRouting 수준에 도달했다"는 근거로 쓸 수 있다. 소형 보드에서는 CADET @1 89.5% 대 FreeRouting 82.1%, D3-B에서는 67.2% 대 65.6%다. 다만 "대형 보드는 미해결"이라는 단서를 반드시 함께 달아야 한다.
- 상용화 관점에서 PCBWorld와 CADET 체크포인트(EXAONE NC), PCBSchemaGen v2 코드(PolyForm NC), OmniLayout 데이터(배포 철회)는 **모디팩토리가 그대로 쓰거나 재배포할 수 없다.** 사내 평가 목적이라도 라이선스를 검토해야 한다. 반면 RL_PCB(MIT), SchGen 코드(MIT), Cypress 저장소, PCBWorld 환경 코드(BSD-3)는 상대적으로 자유롭다. 다만 PCBWorld 엔진은 GPLv3이고, Cypress의 라이선스 파일은 이번에 확인하지 못했다.
- Cypress 원문의 Quilter 수치(2.6시간/176부품, 2024-04 버전)는 "업로드 후 90분" SLA의 경쟁 비교 근거로 쓸 수 있다. 다만 2024년 시점 수치라 현재 Quilter 성능과는 다를 수 있다.

### Gaps
- RL_PCB의 17/21%, SchGen의 82/60.5%, pcbGPT의 0.90, HWE-Bench의 8.15%, EDA Bench의 4.58%, DevFormer의 30% 감소는 모두 GitHub 1차 자료에 없어 [search-snippet]으로 남았다. 각 논문 PDF가 저장소에 없고 arXiv는 차단되어 있다.
- PCBSchemaGen의 77.5%와 "65개 과제"가 어느 판의 어떤 표에서 나왔는지 확정하지 못했다.
- Cypress 저장소의 LICENSE 파일과 벤치마크 세부(설계 수)는 확인하지 못했다. GitHub API가 차단되어 파일 목록을 볼 수 없었다.

---

## Q2. GitHub 큐레이션 목록에서 찾은, 앞선 노트에 없던 보드 레벨 PCB 논문(2023–2026)

### Takeaway
주류 AI4EDA 목록 세 개(thu-nics/awesome_ai4eda, ai4eda/awesome-AI4EDA, Thinklab-SJTU/Awesome-LLM4EDA)에는 "PCB", "KiCad", "schematic", "datasheet"가 **한 건도 없었다.** 칩 중심 큐레이션에서는 PCB가 사실상 빠져 있다.

반면 PCB 전용·엔지니어링 에이전트 목록(tikyttqq/Awesome-PCB-Routing, whut09/Awesome-AI-Engineering-Agents)과 LG AI 논문의 참고문헌에서 **누락 논문 약 25편**을 찾았다. 특히 중요한 것은 다섯 가지다.
- 라우팅: GPCB Routing(IEEE TCAD 2025), 월드모델 RL과 Freerouting 결합(ESWA 2026, 코드 공개), PCBRouteAgent(2026-11, PCBWorld 기반 LLM 라우팅 에이전트)
- 배치: PCBAgent(ASP-DAC 2025), ModuPlace(DAC 2026, LLM 모듈 배치)
- 앞선 노트에서 "존재 미확인"이던 **CircuitLM**과 **PCBAgent**는 실재하는 논문으로 확인됐다.

### Cited Findings

**(a) 1차 PDF 참고문헌으로 확인 [GitHub-verified·참고문헌]**
- **GPCB Routing: Generative Pretrained Transformers-Based Printed Circuit Board Routing Method**: Jienan Chen, Jun Tu, Hao Wang, Jie Zheng, Hao Liu, Shenglong Bai, Xiantuo He, Weikang Qian, *IEEE TCAD* 44(4):1420–1433, 2025, DOI 10.1109/TCAD.2024.3486241 — [CADET.pdf 참고문헌](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)
- **Automation of PCB Autorouting via World-Model Reinforcement Learning and Freerouting Integration**: Yin-Chi Liao, Sheng-Xin Pan, Po-Jui Chiang, *Expert Systems with Applications* 311:131424, 2026 — [PCBWorld.pdf 참고문헌](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - 코드 저장소 yinqimakeitfun/dreamer-Autorouting은 JPype로 `freerouting.jar`를 Gymnasium 환경으로 감싸 DreamerV3로 학습한다 [GitHub-verified] — [GitHub](https://github.com/yinqimakeitfun/dreamer-Autorouting). 저장소와 논문의 연결은 Awesome-PCB-Routing 목록 기준이다.
- **PCBench: A Dataset for Printed Circuit Board Routing**: Youbiao He, Jacob Frieden, Hebi Li, Roba Abbajabal, Ge Luo, Forrest Sheng Bao, DAC 2024 Work-in-Progress Poster — [PCBWorld.pdf 참고문헌](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - 저장소 README는 PCB **164개** 데이터셋, PCB-RDL(JSON 라우팅 기술 언어), 데이터 증강 스크립트, RL 환경을 소개한다 [GitHub-verified] — [GitHub PCBench/PCBench](https://github.com/PCBench/PCBench)
  - **상충 사항**: PCBWorld는 "PCBench 코퍼스에서 파생한 679개"라고 쓴다. README의 164개는 초기 공개분이거나 다른 집계일 수 있으며, 확인하지 못했다.
- 같은 그룹의 관련 연구 — [PCBWorld.pdf 참고문헌](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
  - Youbiao He, "Towards Automated PCB Routing: Leveraging Machine Learning and Heuristic Techniques," Iowa State University 박사논문, 2024, DOI 10.31274/td-20240617-74
  - He, Li, Tian, Bao, "Circuit Routing Using Monte Carlo Tree Search and Deep Reinforcement Learning," VLSI-DAT 2022
- **OmniRouting: A Semantic-Coupled Multimodal Benchmark for Constraint-Aware Spatial Reasoning in PCB Routing**: Taiting Lu 외(OmniLayout과 같은 그룹, Mahanth Gowda 교신 추정), arXiv:2608.04434, 2026 — [CADET.pdf 참고문헌](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf)
- 차동 페어 갭과 관련한 비ML 선행연구: Ting-Chou Lin, Devon Merrill, Yen-Yi Wu, Chester Holtz, Chung-Kuan Cheng, "A Unified Printed Circuit Board Routing Algorithm With Complicated Constraints and Differential Pairs," ASP-DAC 2021, DOI 10.1145/3394885.3431568 — [PCBWorld.pdf 참고문헌](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf)
- **NS-Place**: Chung-Kuan Cheng, Chia-Tung Ho, Chester Holtz, "Net Separation-Oriented Printed Circuit Board Placement via Margin Maximization," ASP-DAC 2022, pp. 288–293 [원문-verified·참고문헌] — [Cypress PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)

**(b) 저장소나 원문 PDF로 직접 확인**
- **PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?** [GitHub-verified: 서지·방법 / unverified: 수치]
  - 저자: Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang, arXiv:2611.08175. 코드는 BSD-3이다 — [GitHub chip-ai-agent/PCBRouteAgent](https://github.com/chip-ai-agent/PCBRouteAgent)
  - 방법: 두 구성요소로 된 멀티모달 에이전트다. Global Routing Planner가 연결 계획, 우선순위, 레이어 계획을 맡고, Detailed Routing Executor가 KiCad 네이티브 PNS 라우터로 배선한다. 실패 피드백을 받으면 전략을 수정한다 — [README](https://github.com/chip-ai-agent/PCBRouteAgent)
  - **PCBWorld를 서브모듈로 쓰고**, PCBWorld-Bench의 D2와 D3-A/B/C 분할에서 공식 평가기로 채점한다. 예시 모델은 claude-opus-5-5다.
  - LG AI 벤치마크가 외부 연구의 표준 평가 환경으로 채택된 사례다. 결과 수치는 README에 없다.
- **CircuitLM: A Multi-Agent LLM-Aided Design Framework for Generating Circuit Schematics from Natural Language Prompts** [GitHub-verified]
  - 저자: Khandakar Shakib Al Hasan, Syed Rifat Raiyan, Hasin Mahtab Alvee, Wahid Sadik, arXiv:2601.04505, MIT 라이선스 — [GitHub Khandakar227/circuitlm](https://github.com/Khandakar227/circuitlm)
  - 구성: 다중 에이전트, ChromaDB 벡터 검색과 퍼지 매칭 기반 부품 선택, **결정론적 ERC 엔진**, 웹 시각화 도구
  - TODO 항목에는 "Human-in-the-loop 리뷰"와 "넷리스트 내보내기"가 미구현으로 남아 있다. 앞선 노트의 "CircuitLM 존재 미확인"을 해소한다.
- **ModuPlace: LLM-Assisted Modular PCB Placement via Preference-Optimized Constraint Graph Generation** [원문-verified: 제목·저자·초록 / unverified: 학회]
  - 저자: Yaohui Han, Beichen Li, Mingyang Zhao, Rongliang Fu, Qunsong Ye, Tinghuan Chen, Bei Yu, Tsung-Yi Ho(CUHK, CUHK-Shenzhen, Central South Univ., Index)
  - 방법: 부품을 여러 단위의 모듈로 나눠 계층적으로 배치하고, LLM 미세조정과 선호 최적화로 제약 그래프를 생성해 결과를 인간 전문가 배치에 맞춘다. "모든 지표에서 모든 기준선을 능가"했다고 저자가 주장한다 — [저자 PDF](https://yhhan.com/PDFs/ModuPlace_paper.pdf)
  - DAC 2026 게재는 Awesome-PCB-Routing 목록 기준이다. 같은 저자의 **PCB-Migrator**(DATE 2026, PCB PnR 이식)는 PDF가 404였다 [unverified].
- **DeepPCB KiCad 플러그인** [GitHub-verified]: InstaDeep의 공식 플러그인이다. KiCad 6.0 이상의 PCM에서 설치하고, DeepPCB 클라우드 엔진으로 배선한다. 크레딧 기반 과금이며 세션 복구를 지원한다 — [GitHub instadeepai/deeppcb-kicad-plugin](https://github.com/instadeepai/deeppcb-kicad-plugin)

**(c) GitHub 큐레이션 목록에만 등재 [unverified, 목록 출처]**

라우팅 — [tikyttqq/Awesome-PCB-Routing](https://github.com/tikyttqq/Awesome-PCB-Routing)
- PCBAgent: An Agent-based Framework for High-Density Printed Circuit Board Placement, ASP-DAC 2025, DOI 10.1145/3658617.3697736. 앞선 노트의 "PCBAgent 미확인"을 해소한다. ResearchGate 레코드도 검색에서 확인됐다 — [ResearchGate](https://www.researchgate.net/publication/389577277_PCBAgent_An_Agent-based_Framework_for_High-Density_Printed_Circuit_Board_Placement)
- TRouter: Thermal-Driven PCB Routing via Nonlocal Crisscross Attention Networks, **IEEE TCAD 2023**, DOI 10.1109/tcad.2023.3243544. 앞선 노트의 "학회·연도 미확인"을 해소한다.
- Security-oriented printed-circuit-board routing with deep reinforcement learning, *Integration* 2026, DOI 10.1016/j.vlsi.2025.102602. 앞선 노트의 ScienceDirect S0167926025002597, ISQED 2026 항목과 같은 계열로 보인다.
- Multi-agent based minimal-layer via routing algorithm for PCB design, *Integration* 2026, DOI 10.1016/j.vlsi.2025.102533
- ST-GAT: Spatial-Temporal Graph Attention Network for Multi-Agent RL-Based PCB Routing, ECIE 2026
- Intelligent Ordered Escape Routing via Deep Reinforcement Learning and Hybrid Heuristics, CEI 2025
- Applying Existing Large Language Models for Print Circuit Board Routing, *Engineering Proceedings* 2025 (ICSEE 2024)
- A Pad-Focused PCB Routing Algorithm Using Polygon-Based Dynamic Partitioning, IEEE Access (DOI 10.1109/access.2024.3386921)
- Routing Generative Pre-Trained Transformers for Printed Circuit Board, ISEDA 2024
- SER-NET: PCB Simultaneous Escape Routing via DRL, ICICM 2024
- Reinforcement Learning Based PCB Routing Using Dueling Double DQN, ICICM 2024
- A Hierarchy MCTS Algorithm for The Automated PCB Routing, ICCA 2020

배치, 회로도, 라이브러리 — [whut09/Awesome-AI-Engineering-Agents](https://github.com/whut09/Awesome-AI-Engineering-Agents)
- AI-Optimized Placement and Routing for PCB Design, IEEE 2024 (Xplore 10568665)
- Reinforcement Learning-Based Placement Method for Printed Circuit Board, ICCCAS 2024, DOI 10.1109/ICCCAS62034.2024.10652635
- **An ML-aided Approach to Automatically Generate Schematic Symbols in PCB EDA Tools**, MLCAD 2024, DOI 10.1145/3670474.3685944. 데이터시트에서 라이브러리를 만드는 갭에 해당한다.
- Goal Driven PCB Synthesis Using Machine Learning and CloudScale Compute, ISPD 2023, DOI 10.1145/3569052.3578907
- From Natural Language to Real Schematics: An Automated Workflow for Power Electronics Schematic Synthesis, arXiv:2610.38201
- RAC: A Relational Agent Contract for Constraint-Governed Engineering Tasks, arXiv:2610.20935. 계약 기반 PCB 배치, 배선, 수리를 다룬다.
- OmniSch: A Multimodal PCB Schematic Benchmark for Structured Diagram Visual Reasoning, arXiv:2604.00270
- 아날로그 인접 연구: EEschematic(arXiv:2510.17002), Schemato(넷리스트→회로도, arXiv:2411.13899), AmpAgent(arXiv:2409.14739)

서베이 — [tikyttqq/Awesome-PCB-Routing](https://github.com/tikyttqq/Awesome-PCB-Routing)
- Consumer Electronics Product Manufacturing Time Reduction and Optimization Using AI-Based PCB and VLSI Circuit Designing, *IEEE TCE* 2023, DOI 10.1109/tce.2023.3240249

**(d) LLM의 KiCad·Altium 조작 도구 (오픈소스) [GitHub 목록 등재]**
- eda-agent(salitronic): MCP와 EDA API로 **Altium, KiCad, EasyEDA Pro**의 회로도·PCB를 편집하고 리뷰, 감사, 배치, 패널화까지 한다. Apache-2.0이다.
- KiCad MCP(lamaalrajih/kicad-mcp), KiCad Copilot(biosshot), Backplane(KiCad IPC API 기반 에이전트 작업공간)
- 상용 쪽에는 Cadence AuraStack AI Super Agent("Announced"), Siemens Fuse EDA AI Agent("Production")가 실려 있다.
- 출처: [whut09 목록](https://github.com/whut09/Awesome-AI-Engineering-Agents)

**(e) 산업계 오토라우터 벤치마크 [GitHub-verified]**
- Koppar-AI/autorouter-bench: 전문가가 배선한 오픈하드웨어 보드 8개를 쓴다(2층과 4층, RP2040, Raspberry Pi CM5 IO, OLIMEX SoM 등). 배선을 지운 뒤 각 라우터에 같은 배치, 규칙, 시간 제한을 주고 **KiCad가 채점**한다(완성률, DRC 증가분, 비아, 길이, 시간). 추가로 Zap!(Mutual Solutions)이 2026-10-12~13에 비교에 쓴 공개 보드 25개 세트(zap25)도 포함한다 — [GitHub](https://github.com/Koppar-AI/autorouter-bench)
- calligraphysystems/open-pcb-routing-benchmark: "복잡한 다층·고밀도 2층 KiCad 보드 13개를 100% 완성, KiCad DRC 0으로 배선"했다는 저장소 설명만 확인했다 [unverified: 내용] — [GitHub](https://github.com/calligraphysystems/open-pcb-routing-benchmark)

### Inferences
- 2024–2026년 PCB 라우팅 ML 문헌은 앞선 노트보다 훨씬 두껍다. 특히 GPT형 생성 라우팅(GPCB Routing TCAD 2025, ISEDA 2024)과 RL+Freerouting 결합이 그렇다. 중국 학계(EDA 학회와 IEEE TCAD)의 비중이 크다.
- "LLM 에이전트가 PCBWorld 환경에서 라우팅"(PCBRouteAgent)하고 "KiCad 채점 오토라우터 벤치마크"(Koppar, Zap!)가 등장하면서, **KiCad 엔진을 심판으로 쓰는 공개 비교**가 업계 표준으로 굳어지고 있다. 모디팩토리도 같은 형식으로 성능을 공개하면 국제 비교가 가능하다.
- MLCAD 2024의 회로도 심볼 자동 생성 연구와 SFgen(앞선 노트)은 업로드 파일에서 빠진 라이브러리를 보완하는 기능의 학술 근거가 된다.

### Gaps
- (c)의 목록 등재 논문 약 20편은 저자, 수치, 학회를 1차 자료로 확인하지 못했다. 큐레이션 목록은 제3자가 관리하므로 오류 가능성이 있다.
- 열·SI/PI 보드 레벨 ML 신규 논문은 TRouter(열 인지 라우팅) 외에 목록에서 찾지 못했다. 설계 근거·설명가능성 전용 PCB 논문도 목록에 없었다.
- 데이터시트 파싱 기반 부품 선정 논문은 HWE-Bench 파이프라인(MinerU)과 pcbGPT 외에 새로 찾지 못했다.

---

## Q3. 한국 저자 연구: KAIST, LG AI연구원, 기타 저장소와 KCI·RISS 스니펫 검증

### Takeaway
한국 저자 연구 가운데 GitHub로 1차 검증한 것은 세 가지다.
- **LG AI연구원 PCBWorld와 CADET**: 저자 7인, 서울 소속, 제주 KDD 워크숍을 원문 PDF로 확인했다.
- **KAIST DevFormer**: ICML 2023이며, 저장소는 ai4co로 이전했다.
- **MoTT**: 신규 발견이다. 한국어로 쓰인 디캡 배치 트랜스포머 저장소(2026-11)지만 동료심사 논문은 아니다.

KAIST TeraLab의 다른 저장소(CDML, HBM RL 등)는 찾지 못했다. GitHub 조직 목록 API가 막혔고, 저장소 검색 결과도 0건이었다. KCI와 RISS 쪽에서는 AI 기반 PCB 배치·배선 학위논문을 이번에도 찾지 못했다.

### Cited Findings
- **LG AI연구원 PCBWorld** [GitHub-verified]: 저자 전원의 소속이 "LG AI Research, Seoul, Republic of Korea"로 표기되어 있다. Song, J. Park, Choi가 공동 1저자이고, Y. Park와 Lee가 교신저자다. 워크숍은 "KDD Workshop on Agentic AI '26, August 9–13, 2026, Jeju, Republic of Korea"다. 연락처는 yj.park@lgresearch.ai다 — [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf); [README](https://github.com/LGAI-Research/PCBWorld)
- **LG AI연구원 CADET** [GitHub-verified]: 같은 7인이 쓴 프리프린트다. 연락처는 yj.park@lgresearch.ai와 7590sok@gmail.com이다. 학습된 정책 6개가 Hugging Face(LG-AI-Research/CADET)에 EXAONE NC 라이선스로 공개됐다 — [README](https://github.com/LGAI-Research/CADET)
- **엔진 저장소** [GitHub-verified]: KiCad 수정본, RL 라우터, 엔진 서버는 별도 저장소 LGAI-Research/PCBWorld-Engine(GPLv3)에 있다 — [README](https://github.com/LGAI-Research/PCBWorld)
- **KAIST DevFormer** [GitHub-verified]: 저자 5인 가운데 Joungho Kim(전기및전자공학부 TeraLab)과 Jinkyoo Park(산업및시스템공학과)가 있다. DPP 벤치마크와 시뮬레이터(`decap_sim`)를 공개했고, RL4CO와 ReEvo(NeurIPS 2024)로 이어졌다 — [GitHub kaist-silab/devformer](https://github.com/kaist-silab/devformer)
- **MoTT: Modal-Token Transformer for Generalizable Decoupling Capacitor Placement** [GitHub-verified, 비동료심사]
  - 저장소 jeehoo0507/MoTT의 README는 한국어로 쓰였고 영문판도 있다. 2026-11-13에 push했다. 결과는 보고서 PDF(`paper/MoTT_report.pdf`)로 공개했다 — [GitHub jeehoo0507/MoTT](https://github.com/jeehoo0507/MoTT)
  - 방법: 판을 좌표 대신 공진 모드, 칸, 디캡 종류 토큰으로 표현해 PCB, 패키지, 인터포저 종류에 걸쳐 일반화하는 것이 목표다. 모방학습 0.75시간 뒤 RL 1.25시간을 학습한다.
  - 처음 보는 판 종류에서의 성공률 — [README](https://github.com/jeehoo0507/MoTT)

    | 판 종류 | MoTT | 좌표 입력 모델 |
    |---|---|---|
    | PCB형 | 0.89 | 0.64 |
    | 인터포저형 | 0.99 | 0.65 |
    | 패키지형(검증 하네스 적용) | 0.99 | 0.92 |

  - 선행연구 재구현(B-Park, B-DevFormer, B-Manoharan)과도 비교했다. 같은 조건에서 PCB형 성공률은 B-DevFormer 0.79, B-Park 0.04였고, MoTT는 0.99였다(하네스 적용) — [README](https://github.com/jeehoo0507/MoTT)
  - 저자 실명과 소속은 README에 없다. KAIST TeraLab과의 관련성도 확인하지 못했다.
- **KAIST TeraLab, CDML, Pin-opt 저장소**: GitHub 저장소 검색("teralab kaist", "hbm decap", "kaist pcb routing")이 모두 0건이었다. kaist-silab/CDML과 ai4co/cdml 같은 추정 경로도 404였다 [unverified].
- **KCI·RISS 스니펫(새 항목)** [search-snippet]
  - 「딥러닝 기반의 PCB 부품 문자인식을 위한 코어 셋 구성」(KCI ART002699042, 멀티미디어학회논문지, 2021)은 검사·인식 분야이며 설계 자동화가 아니다 — [KCI](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002699042)
  - 「초고속 신호 전송 최적화를 위한 PCB 설계 연구」(숭실대 학위논문, 2019, 김창균)는 SI 설계 연구이며 AI가 아니다 — [ScienceON DIKO0015305385](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0015305385&dbt=DIKO)
  - 「강화학습을 이용한 인공지능 기반 공간배치 시뮬레이터 개발」(KCI ART002777625)은 제목만 확인했다. PCB 대상인지는 확인하지 못했다(공간·건축 배치일 가능성) — [KCI](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002777625)
  - "PCB 부품 배치 강화학습" 학위논문은 이번 검색에서도 나오지 않았다. 앞선 노트의 결론(보드 레벨 AI 배치·배선 국내 학위논문 공백)이 유지된다.

### Inferences
- LG AI연구원의 PCBWorld는 외부 연구(PCBRouteAgent)가 서브모듈로 채택했고, 한국에서 열린 KDD 워크숍에 발표됐다. **국산 PCB 벤치마크가 국제 평가 표준으로 쓰이기 시작했다는 1차 증거**다.
- 체크포인트가 비상업(NC) 라이선스라 모디팩토리는 LG 모델을 직접 쓸 수 없다. 대신 BSD-3 환경 코드와 공개 벤치마크로 자사 엔진을 평가하고 공개하는 방식은 가능하다. GPLv3 엔진을 연동할 때는 배포 형태를 검토해야 한다.
- MoTT는 한국어 문서를 갖춘 최신 디캡 배치 저장소로, "PCB·패키지·인터포저 범용 디캡 배치"를 표방한다. 다만 동료심사를 거치지 않았으므로 보고서에서는 "공개 연구 코드" 수준으로만 언급해야 한다.

### Gaps
- KAIST TeraLab의 HBM·인터포저 RL 저장소, 트랜스포머 RL HBM 논문(2022)의 학술지명, Pin-opt와 CDML 저장소를 확인하지 못했다. GitHub 조직 목록 API가 막혔고 검색 결과도 없었다.
- MoTT 저자의 실명, 소속, 보고서의 성격(수업 과제인지, 학위 연구인지 등)을 확인하지 못했다.
- KCI, RISS, DBpia는 여전히 직접 조회할 수 없다. 2025–2026 국내 학술대회(대한전자공학회 등)의 PCB 설계 AI 발표 여부는 미확인으로 남는다.

---

## Q4. 2026년 PCB용 ML·LLM 서베이(Srinivasan, Turnbull, Pearce) 확인

### Takeaway
"Surveying GenAI-based Automation in Printed Circuit Board Design and Test"(arXiv:2606.17074)의 존재, 저자 3인, 제출일(2026-06-10)을 검색 결과로 다시 확인했다. PCB 라우팅 전용 GitHub 큐레이션 목록에도 대표 서베이로 실려 있다. 다만 원문(arXiv)은 차단되어 세부 분류 체계는 확인하지 못했다.

### Cited Findings
- 서지: Sahana Srinivasan, Benjamin Turnbull, Hammond Pearce, arXiv:2606.17074, 2026-06-10 제출, "under review", 33쪽, 그림 5개, 표 11개, 분류 cs.AR/cs.AI [search-snippet] — [arXiv](https://arxiv.org/abs/2606.17074); [arXiv HTML](https://arxiv.org/html/2606.17074v1); [X 게시](https://x.com/WWVY/status/2067147627838214619)
- 범위: 공급망, 시스템 사양, 회로 설계, 레이아웃, 검증·테스트, 조립까지 PCB 생애주기 전체를 다룬다. 핵심 장애물로 도메인 데이터 부족과 기존 PCB 도구와의 통합 부족을 꼽는다. "GenAI만으로는 아직 모든 단계를 자동화할 수 없다"고 결론짓는다 [search-snippet] — [arXiv](https://arxiv.org/abs/2606.17074)
- GitHub 큐레이션 목록 tikyttqq/Awesome-PCB-Routing의 "Surveys" 섹션 첫 항목으로 실려 있다 [GitHub 목록 등재] — [GitHub](https://github.com/tikyttqq/Awesome-PCB-Routing)

### Inferences
- 앞선 노트처럼 이 서베이를 "PCB GenAI 1차 서베이"로 인용해도 된다. 함께 쓸 보조 서베이로는 IEEE TCE 2023 「Consumer Electronics Product Manufacturing Time Reduction ... AI-Based PCB and VLSI Circuit Designing」이 있다. 다만 이 논문은 목록 등재로만 확인했다.

### Gaps
- 서베이의 분류 체계, 인용 논문 목록, 저자 소속(UNSW)은 이번 패스에서도 원문으로 확인하지 못했다. 소속은 앞선 노트의 스니펫 기준이다.
- 동반 GitHub 저장소는 검색으로 찾지 못했다("PCB survey GenAI" 0건).

---

## Q5. 검증 상태 요약과 남은 미검증 항목

### Takeaway
이번 보충으로 다음 항목을 [GitHub-verified] 또는 [원문-verified]로 올렸다.
- 핵심 문헌 12건의 서지: RL_PCB, Cypress, PCBWorld, CADET, PCB-Bench, PCBSchemaGen v1·v2, SchGen, pcbGPT, HWE-Bench, EDA Bench, OmniLayout, DevFormer
- 일부 핵심 수치: PCBWorld와 CADET 전 결과표, Cypress 초록 수치, PCB-Bench 규모, OmniLayout 규모, EDA Bench 과제 수
- AlphaChip 논쟁의 최신 상태: TCAD 2025-12 채택

남은 미검증 항목은 대부분 "수치는 arXiv 원문에만 있는" 경우다.

### Cited Findings
| 항목 | 이번 판정 | 근거 |
|---|---|---|
| PCBWorld 679 보드, 8개 지표, Table 3 | GitHub-verified | [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf) |
| CADET 38.0→67.2%(RL-only 대비), FreeRouting 65.6% | GitHub-verified | [CADET.pdf](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf) |
| Cypress 1–5.9배, 1–19.7배, 492.3배 | 원문-verified | [Cornell PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf) |
| PCB-Bench 약 3,700, 약 500, 174 프로젝트, HKUST(GZ) | GitHub-verified | [github.io](https://digailab.github.io/PCB-Bench/) |
| PCBSchemaGen 23(v1) / 62+165=227(v2) | GitHub-verified | [v1](https://github.com/Sthyao/PCBSchemaGen); [v2](https://github.com/HZou9/PCBSchemaGen_v2) |
| PCBSchemaGen 65개 과제 / 77.5% | search-snippet (65는 ID 범위 1–65로 추정) | [DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf) |
| EDA Bench 35 과제 | GitHub-verified | [DATA_CARD](https://github.com/EDA-bench/eda-bench/blob/master/DATA_CARD.md) |
| EDA Bench 4.58%, ICML 2026 | search-snippet | [ICML](https://icml.cc/virtual/2026/77908) |
| OmniLayout 1,681 / 77,236, 데이터 배포 철회 | GitHub-verified | [GitHub](https://github.com/AAAAAiden/OmniLayout-Benchmark) |
| HWE-Bench 파이프라인 | GitHub-verified | [GitHub](https://github.com/EDI-Systems/HWE-Bench) |
| HWE-Bench 300 과제, 8.15% | search-snippet | [emergentmind](https://www.emergentmind.com/papers/2603.18102) |
| RL_PCB 17%/21% | search-snippet | [UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782) |
| SchGen 82%/60.5%, pcbGPT 0.90 | search-snippet | [alphaxiv](https://www.alphaxiv.org/abs/2605.30345.md); [arXiv](https://arxiv.org/pdf/2606.01188) |
| PCB Gym 32.1%, PCBInnoBench 22.0%/7.3% | search-snippet (저장소 없음 또는 README 없음) | [NeurIPS PCB Gym](https://neurips.cc/virtual/2026/161602); [NeurIPS PCBInnoBench](https://neurips.cc/virtual/2026/poster/139034) |
| PCB-QA 480쌍, DRCY 결과 | search-snippet (저장소 없음) | [arXiv PCB-QA](https://arxiv.org/pdf/2606.23704); [arXiv DRCY](https://arxiv.org/abs/2603.15672) |
| FanoutNet 서지(저자 4인, pp. 8554–8561) | GitHub-verified·참고문헌 | [PCBWorld.pdf](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf) |
| DevFormer 서지 / 30% 감소 | GitHub-verified / search-snippet | [GitHub](https://github.com/kaist-silab/devformer) |
| AlphaChip 비판 TCAD 채택(2025-12-16) | GitHub-verified | [MacroPlacement](https://github.com/TILOS-AI-Institute/MacroPlacement) |
| Unet-Astar 코드 미공개 | GitHub-verified (정정) | [GitHub](https://github.com/Firesuiry/Unet-Astar-For-PCB-Routing) |
| UNSW 서베이 서지 | search-snippet | [arXiv](https://arxiv.org/abs/2606.17074) |

### Inferences
- 보고서 본문의 정량 주장은 **PCBWorld, CADET, Cypress, PCB-Bench 규모** 위주로 구성하는 것이 가장 안전하다. pcbGPT, SchGen, HWE-Bench, EDA Bench, PCB Gym 수치는 "프리프린트·학회 초록 기준"이라는 단서를 붙여야 한다.
- 앞선 노트에서 정정할 사항은 다섯 가지다.
  - Unet-Astar의 코드는 미공개다.
  - PCB-Bench의 실제 프로젝트 수는 174개다.
  - PCBWorld 결과는 "소형 보드에서 PPO가 규칙 기반을 능가, 대형에서는 뒤처짐"으로 서술을 고친다.
  - AlphaChip 비판은 TCAD 판으로 갱신한다.
  - CADET의 비교 기준은 "RL-only 기준선"임을 명시한다.

### Gaps (남은 미검증 목록)
1. RL_PCB(17/21%), SchGen(82/60.5%), pcbGPT(0.90), HWE-Bench(300, 2,914, 8.15%), EDA Bench(4.58%), PCB Gym(32.1%), PCBInnoBench(22.0/7.3%), PCB-QA(480), DevFormer(30%)의 수치. 원문은 arXiv, 학회 사이트, IEEE에 있고 모두 차단되어 있다.
2. PCBSchemaGen의 77.5%와 "65개 과제"가 어느 판, 어느 표에서 나왔는지.
3. PCBench 데이터셋 규모 상충. README는 164개, PCBWorld는 679개를 "PCBench 코퍼스에서 파생"했다고 쓴다.
4. 큐레이션 목록에만 실린 약 20편(PCBAgent, TRouter, ModuPlace 학회, GPT 라우팅 계열, Integration 2026 2편 등)의 저자와 결과.
5. KAIST TeraLab의 HBM·디캡 후속 저장소(CDML, Pin-opt), MoTT 저자 신원.
6. PCB Gym, PCBInnoBench, PCB-QA의 공식 코드 공개 상태. PCBInnoBench는 GitHub 저장소가 있으나 README를 열지 못했다.
7. UNSW 서베이의 세부 분류 체계와 저자 소속.
8. Cypress와 SchGen 저장소의 LICENSE 원문. README 기준으로 SchGen은 MIT이고, Cypress는 미확인이다.
