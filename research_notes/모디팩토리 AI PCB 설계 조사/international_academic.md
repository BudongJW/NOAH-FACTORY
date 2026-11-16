# 해외(비한국) 학술 문헌 조사: AI/ML 기반 PCB 자동 설계

> **검증 방법 및 한계 (보고서 작성자 필독)**
> - 이 세션의 네트워크 정책 때문에 arxiv.org, dspace.mit.edu, um.edu.mt, ojs.aaai.org를 WebFetch로 직접 열 수 없었다(호스트 미허용, `ENOTFOUND`). arXiv/Semantic Scholar API도 curl로 403이 나서 막혔다. 원문 전체를 확인하려면 세션 네트워크 설정에서 이 호스트들을 허용해야 한다.
> - 그래서 모든 논문은 웹 검색 결과로 검증했다. 확인한 것은 제목·저자·arXiv ID/DOI·학회 페이지 URL·초록 스니펫이고, 학회 공식 페이지(neurips.cc, iclr.cc, icml.cc, date-conference.com, isqed.org)나 arXiv 색인 페이지가 함께 나온 경우로 한정했다. 원문 표나 수치를 직접 보지는 못했으므로 아래 정량 결과는 모두 "초록·스니펫 기준"이다. 제3자 요약에서만 나온 수치는 따로 표시했다.
> - 칩(VLSI) 수준 연구에는 **[칩-레벨]** 태그를 붙였다. PCB에 직접 옮겨 쓸 수 있거나 영향력이 큰 연구만 넣었다.
> - "서비스 관련성"은 업로드 → 약 90분 안에 AI PCB 설계안과 설계 근거를 제공하는 서비스 기준으로 평가했다.

---

## Q1. ML 기반 PCB 부품 배치(Placement): RL, GNN, SA 하이브리드, DeepPCB, AlphaChip의 PCB 전이 가능성과 논란

### Takeaway
보드 레벨 배치에서는 두 계열이 가장 성숙했다. 하나는 RL 정책을 오프라인으로 학습한 뒤 새 회로에 일반화하는 방식(Vassallo & Bajada, DATE 2024: 미학습 회로에서 SA 대비 라우팅 후 배선길이 17~21% 감소)이고, 다른 하나는 VLSI의 해석적(analytical) 배치를 GPU로 가속해 PCB에 이식한 방식(Cypress, ISPD 2025 최우수논문: SA-PCB 대비 최대 492.3배 빠르고 routability 1~5.9배)이다. 칩 레벨의 AlphaChip(Nature 2021)은 영향력은 크지만 SA나 상용 도구보다 낫다는 주장이 재현 논쟁에 걸려 있다. 그래서 PCB 서비스의 핵심 엔진으로 그대로 가져오기에는 위험하다.

### Cited Findings

**[P1] Learning Circuit Placement Techniques through Reinforcement Learning with Adaptive Rewards**
- 저자/연도/학회: Luke Vassallo, Josef Bajada (University of Malta), DATE 2024 (Valencia), IEEE 2024년 3월 출간 — [UM OAR 저장소](https://www.um.edu.mt/library/oar/handle/123456789/131782)
- 방법: PCB 배치 문제를 MDP로 정식화하고 RL로 일반적인 배치 기법을 학습한다. TD3와 SAC 정책을 쓴다 — [UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)
- 결과: 미학습(unseen) 회로에서 TD3·SAC 정책의 라우팅 후 배선길이가 최신 simulated annealing 대비 각각 17%, 21% 감소했다. 정성 분석에서는 정책이 "기본적인 배치 기법"을 학습한 것으로 나타났다 — [UM OAR 초록(검색 스니펫)](https://www.um.edu.mt/library/oar/handle/123456789/131782)
- 코드: RL_PCB 저장소(MIT 라이선스, KiCad 파일 파싱 포함, SA 기준선 비교). Vassallo의 석사논문 프로젝트로, 지도교수는 Josef Bajada — [GitHub LukeVassallo/RL_PCB](https://github.com/LukeVassallo/RL_PCB)
- 참고: 과업 지시문의 "Vassallo et al."은 이 논문이다. 공저자 "Bowyer"는 검색 결과 어디에도 없었다.
- 서비스 관련성: **높음.** 학습된 정책은 추론 속도가 빨라 90분 안에 처리하기에 유리하다. KiCad 입력을 지원하고 오픈소스라 프로토타입 기준선으로 쓰기 좋다.

**[P2] Physically Constrained PCB Placement Using Deep Reinforcement Learning (MIT 석사논문)**
- 저자/연도: Peter Crocker, MIT, 2021 — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/139247); 제목 확인: [libmast 레코드](https://libmast.utm.my/Record/mit-1721.1%2F139247)
- 방법: 시뮬레이션된 PCB 캔버스에서 RL 에이전트가 부품을 배치하도록 학습한다. 목표는 제조 시 부품 겹침과 배선 교차가 없는 "물리적으로 검증된" 레이아웃이다 — [검색 요약(MIT DSpace)](https://dspace.mit.edu/handle/1721.1/139247)
- 한계: 학위논문이라 동료심사를 거치지 않았다. SA 기준선 비교 여부는 확인하지 못했다.
- 서비스 관련성: 중간. 겹침·교차 같은 물리 제약을 보상에 넣는 방식을 참고할 수 있다.

**[P3] Component Centric Placement Using Deep Reinforcement Learning**
- 저자/연도: Kart Leong Lim (A*STAR Institute of Microelectronics), arXiv:2602.23540, 2026-02-26 — [arXiv](https://arxiv.org/abs/2602.23540)
- 방법: 주(main) 부품을 보드 중앙에 고정하고 주변 빈 공간을 이산화한 뒤 수동소자를 배치해 탐색 공간을 크게 줄인다. DQN, A2C, SA를 같은 틀에서 비교한다 — [arXiv](https://arxiv.org/abs/2602.23540); [deeppaper 요약](https://arxiv.deeppaper.ai/papers/2602.23540v1)
- 결과: 실제 PCB 9개 이상에서 평가했다. 최고 방법이 배선길이와 실현 가능성 면에서 "사람 수준에 가까운" 배치를 냈다고 저자가 주장한다. 수동소자를 전원 핀 근처에 두어 배선을 줄이고 겹침을 피한다는 설계 논리를 명시했다 — [arXiv HTML](https://arxiv.org/html/2602.23540v1)
- 한계: 프리프린트이고 독립 재현은 없다.
- 서비스 관련성: **높음(설계 근거 측면).** "디커플링 캡은 전원 핀 근처" 같은 규칙형 근거가 정책 구조에 녹아 있어 설명문으로 바꾸기 쉽다.

**[P4] Cypress: VLSI-Inspired PCB Placement with GPU Acceleration**
- 저자/연도/학회: Niansong Zhang, Anthony Agnesina, Noor Shbat, Yuval Leader, Zhiru Zhang, Haoxing Ren (Cornell, NVIDIA), ISPD 2025 (Austin), **ISPD 2025 Best Paper Award** — [논문 PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf); [수상 공지](https://zhang.ece.cornell.edu/news/cypress_ispd_bpa.html)
- 방법: VLSI의 해석적 배치 기법(DREAMPlace 기반)을 PCB용 비용함수와 제약 처리로 바꾸고 GPU로 가속한다. 실제 상용 설계에서 합성한 PCB 벤치마크 세트도 공개했다 — [논문 PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf); [GitHub NVlabs/Cypress](https://github.com/NVlabs/Cypress)
- 결과: 제안 벤치마크에서 routability가 1~5.9배 높고, GPU 가속으로 런타임이 최대 492.3배 빨라졌다(저자 슬라이드상 SA-PCB 대비) — [논문 PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
- 문제 인식: 저자들은 PCB 배치가 수작업에 크게 의존해 "수 주"가 걸리고, 기존 자동 배치 도구는 품질과 확장성에서 성과가 제한적이었다고 지적한다 — [논문 PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)
- 서비스 관련성: **매우 높음.** 90분 SLA에서는 GPU 가속 해석적 배치가 가장 현실적인 1차 엔진이다. 오픈소스이고 벤치마크도 있다.

**[P5] Placement in Integrated Circuits using Cyclic Reinforcement Learning and Simulated Annealing [칩-레벨]**
- 저자/연도/학회: Dhruv Vashisht, Devika Shanbhag, Levent Burak Kara 외 (공저자 7명), arXiv:2011.07577, NeurIPS 2020 Workshop — [arXiv](https://arxiv.org/abs/2011.07577v1); [NeurIPS](https://neurips.cc/virtual/2020/20493)
- 방법/결과: RL로 거친 초기 배치를 빠르게 만들고 SA로 탐욕적으로 개선하기를 순환 반복한다. RL이 SA에 좋은 초기해를 주어 비용이 "상당한 차이로" 낮아졌다. 문제는 sequence pair로 인코딩했다 — [arXiv](https://arxiv.org/abs/2011.07577v1)
- 서비스 관련성: 중간. RL+SA 하이브리드라는 설계 패턴을 PCB로 옮길 수 있다. 대상은 IC다.

**[P6] A graph placement methodology for fast chip design (AlphaChip) [칩-레벨, 영향력 큼]**
- 저자/연도/학회: Azalia Mirhoseini, Anna Goldie 외, *Nature* 594, 207–212 (2021), DOI 10.1038/s41586-021-03544-w — [RePEc](https://ideas.repec.org/a/nat/nature/v594y2021i7862d10.1038_s41586-021-03544-w.html)
- 방법: 칩 플로어플래닝을 RL로 풀고, 전이 가능한 표현을 배우는 edge-based GCN을 쓴다 — [RePEc 초록](https://ideas.repec.org/a/nat/nature/v594y2021i7862d10.1038_s41586-021-03544-w.html)
- 주장: Nature News & Views는 "수 시간 만에" 우수한 플로어플랜을 만든다고 소개했다 — [Nature N&V](https://www.nature.com/articles/d41586-021-01515-9.pdf). Google은 이 방법이 차세대 TPU 설계에 실제로 쓰였다고 밝혔다 — [Google Research 블로그](https://research.google/blog/chip-design-with-deep-reinforcement-learning/?m=1). "6시간"이라는 구체 수치는 이번 검색에서 확인하지 못했다.

**[P7] Assessment of Reinforcement Learning for Macro Placement [칩-레벨, AlphaChip 비판]**
- 저자/연도/학회: Chung-Kuan Cheng, Andrew B. Kahng, Sayak Kundu, Yucheng Wang, Zhiang Wang (UCSD), ISPD 2023 초청논문, ACM DOI 10.1145/3569052.3578926 — [arXiv 2302.11014](https://arxiv.org/abs/2302.11014v3); [UCSD PDF](https://vlsicad.ucsd.edu/Publications/Conferences/396/c396.pdf)
- 내용: Nature 결과를 완전히 재현하지 못했다. 핵심 세부가 Circuit Training 코드의 plc_client API 뒤에 숨어 있다고 지적했고, 초기 배치에 대한 의존성이 크다고 보고했다. 2026년 3월 arXiv v3에서는 SA를 멀티스레딩과 go-with-the-winners로 강화했고, SA와 인간 기준선이 최신 AlphaChip보다 여전히 우수하면서 자원은 훨씬 적게 든다고 보고했다 — [arXiv v3](https://arxiv.org/abs/2302.11014v3)

**[P8] The False Dawn: Reevaluating Google's Reinforcement Learning for Chip Macro Placement [칩-레벨, 비판]**
- 저자/연도: Igor L. Markov, arXiv:2306.09633 (2023, 이후 개정) — [deeppaper 요약](https://arxiv.deeppaper.ai/papers/2306.09633v10?locale=en)
- 주장: Google RL이 인간 설계자, Simulated Annealing, 상용 소프트웨어 모두에 뒤처진다. 새 AlphaChip 버전에서도 Nature 논문의 결함이 남아 있다고 본다 — [deeppaper 요약](https://arxiv.deeppaper.ai/papers/2306.09633v10?locale=en); [AlphaChip 논쟁 정리](https://wiki.krisyotam.com/content/wikipedia_en_all_nopic_2026-03/AlphaChip_(controversy))

**[P9] That Chip Has Sailed: A Critique of Unfounded Skepticism Around AI for Chip Design [칩-레벨, 저자 측 반박]**
- 저자/연도: Anna Goldie, Azalia Mirhoseini, Jeff Dean, arXiv:2411.10053 (2024-11) — [arXiv](https://arxiv.org/abs/2411.10053v1)
- 주장: Cheng 등은 Nature의 방법론(사전학습 등)을 적용하지 않았고, Markov의 메타분석은 편향됐으며, 조사 결과 부정행위 증거는 없었다(저자 측 주장으로, 비판자들이 다투고 있음) — [arXiv HTML](https://arxiv.org/html/2411.10053v1)
- 학계 반응: CACM은 Nature 부록과 갱신이 비판을 다시 불붙였고, Google이 벤치마크 공유를 거부했다고 보도했다 — [CACM "Updates Spark Uproar"](https://cacm.acm.org/news/updates-spark-uproar). Nature는 성능 주장에 대한 독립 조사를 알리는 편집자 노트를 붙였고, 2024년에 조사를 거쳐 부록(addendum)을 게재했다. 일부 출처는 이 부록에서 상용 설계 소프트웨어의 좌표 데이터를 썼다는 점이 공개됐다고 전한다 — [AlphaChip 논쟁 정리](https://wiki.krisyotam.com/content/wikipedia_en_all_nopic_2026-03/AlphaChip_(controversy)); [CACM](https://cacm.acm.org/news/updates-spark-uproar) (2차 출처라 Nature 원문은 확인하지 못함)

**[P10] Graph Neural Networks for Automatic Addition of Optimizing Components in Printed Circuit Board Schematics**
- 저자/연도: Plettenberg, Alcalde, Sick, Thomas, arXiv:2506.10577 (2025-06) — [arXiv HTML](https://arxiv.org/html/2506.10577v1)
- 방법: 회로도를 이분 그래프로 모델링한다(심볼과 넷은 노드, 핀은 엣지). 2단자 부품 추가를 노드 쌍 예측 문제로 정식화하고, 풀업·풀다운 저항, 디커플링 캡, RC 필터 자동 추가를 다룬다. 코드는 github.com/pasplett/pcb-node-pair-gnn에 공개됐다 — [arXiv](https://arxiv.org/pdf/2506.10577)
- 서비스 관련성: **높음.** 업로드된 회로도에서 "빠진 디커플링 캡이나 풀업"을 찾아 제안하는 기능의 학술 근거가 된다.

**[P11] Novel Graph-Based Reinforcement Learning Approach for Multi-Power-Domain PCB PDN Shape and Stackup Synthesis**
- 저자: Chulsoon Hwang, Xu Gao, Jianmin Zhang, Haran Manoharan, Jingnan Pan (Google Research 및 Missouri S&T), 2025 — [Google Research 페이지](https://research.google/pubs/novel-graph-based-reinforcement-learning-approach-for-multi-power-domain-pcb-pdn-shape-and-stackup-synthesis/)
- 방법: 전원 도메인별 스택업 레이어를 할당하고, DC 저항 제약을 만족하면서 서로 겹치지 않도록 전원 플레인 형상을 반복 정제한다. 멀티에이전트 RL 버전은 IEEE EMC 학회에 발표됐다 — [Google Research](https://research.google/pubs/novel-graph-based-reinforcement-learning-approach-for-multi-power-domain-pcb-pdn-shape-and-stackup-synthesis/); [IBIS Summit 2025 슬라이드](https://ibis.org/summits/aug25/manoharan.pdf)
- 서비스 관련성: 중간~높음. 다층 보드의 PDN과 스택업 자동 제안에 쓸 수 있다.

**DeepPCB (InstaDeep): 산업 맥락**
- 2019년 11월 RL 기반 라우팅 플랫폼으로 출시됐다. 당시에는 최대 150쌍·2층 보드, .dsn 업로드, 24시간 내 결과 제공이었다 — [PCD&F 보도](https://www.pcdandf.com/pcdesign/index.php/editorial/menu-new-indust-prod/17292-instadeep-releases-deeppcb-ai-pcb-routing-platform); [InstaDeep](https://instadeep.com/?p=1000)
- Cloud TPU 도입 후 처리량이 235배 늘고 학습 비용은 약 90% 줄었다고 밝혔다(자사 주장) — [InstaDeep 블로그](https://instadeep.com/?p=3475)

### Inferences
- 90분 SLA에서는 "GPU 해석적 배치(Cypress 계열)로 전역 배치 → 학습된 RL 정책이나 규칙 기반 미세조정(Vassallo, Lim 계열) → 짧은 SA 정제"로 이어지는 하이브리드 파이프라인이 학술적으로 가장 근거가 탄탄하다. RL을 서비스 시점에 처음부터 학습시키는 방식(초기 DeepPCB처럼 24시간 단위)은 SLA와 맞지 않는다.
- AlphaChip 논쟁에서 얻을 실무 교훈은 세 가지다. ① 강한 SA나 상용 기준선과 반드시 비교해야 하고, ② 재현 가능한 벤치마크를 공개해야 하며, ③ "AI라서 더 좋다"는 주장을 마케팅에 쓰기 전에 검증해야 한다.
- GNN 기반 부품 추가 제안(P10)과 PDN RL(P11)은 배치 자체보다는 "설계 보완 제안"이라는 차별화 기능의 근거로 쓸 수 있다.

### Gaps
- DeepPCB 팀이 팟캐스트에서 언급한 "NeurIPS spotlight 논문"의 제목과 링크는 찾지 못했다 — [팟캐스트 요약](https://www.globalplayer.com/podcasts/episodes/7Drb7cS/). DeepPCB 배치(placement) 기술의 학술 논문도 확인하지 못했다.
- Vassallo 논문의 IEEE DOI와 원문 수치표는 원문 접근이 막혀(제한 공개, 네트워크 차단) 확인하지 못했다.
- AlphaChip의 PCB 직접 적용 사례(동료심사 논문)는 찾지 못했다. PCB 전이성은 추론에 그친다.
- Crocker 외의 "Crocker et al." 공저 논문(학회판)이 있는지는 확인하지 못했다.

---

## Q2. ML 기반 PCB 라우팅: RL 라우터, A*·학습 하이브리드, 고속·차동 페어, freerouting 비교, 벤치마크

### Takeaway
PCB 라우팅용 학습 기반 연구는 주로 부분 문제에 집중돼 있다. 팬아웃(FanoutNet, AAAI 2023), 이스케이프 라우팅(DQN, SPIE 2025), A* 탐색 영역 추천(Unet-Astar, IEEE Access 2023)이 그 예다. 2026년 PCBWorld 벤치마크 저자들은 학습 기반 라우터가 여전히 규칙 기반 라우터에 뒤처진다고 명시했다. 고속·차동 페어 PCB 라우팅을 ML로 다룬 동료심사 논문은 찾지 못했다.

### Cited Findings

**[R1] FanoutNet: A Neuralized PCB Fanout Automation Method Using Deep Reinforcement Learning**
- 학회/연도: AAAI 2023 (Li et al.) — [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26030); [mlanthology](https://mlanthology.org/aaai/2023/li2023aaai-fanoutnet)
- 방법: 라우팅 전 단계인 팬아웃을 심층 RL로 자동화한다. CNN과 어텐션 기반 정책·가치망을 PPO로 학습하고, 다중제약 라우터가 보상 피드백을 준다. 이 팬아웃 방법을 PCB 라우터에 적용해 라우팅 품질을 높였다 — [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26030); [liner 리뷰](https://liner.com/review/fanoutnet-neuralized-pcb-fanout-automation-method-using-deep-reinforcement-learning)
- 서비스 관련성: 중간~높음. BGA 팬아웃은 상용 자동화가 약한 영역이다.

**[R2] Unet-Astar: A Deep Learning-Based Fast Routing Algorithm for Unified PCB Routing**
- 저자/연도/학회: Shiyuan Yin, Min Jin, Gang Chen, Guoliang Gong, Wenyu Mao, Huaxiang Lu, *IEEE Access* 11:113712–113725 (2023), DOI 10.1109/access.2023.3323589 — [DOAJ](https://doaj.org/article/be16200414264fe48da8f179bd034013); [Bohrium](https://www.bohrium.com/paper-details/unet-astar-a-deep-learning-based-fast-routing-algorithm-for-unified-pcb-routing/922310827124458078-2649)
- 방법: "Deeper Unet"이 A* 라우터에 추천 영역을 생성해 탐색을 가속한다. 이스케이프 라우팅, 영역 라우팅, BGA를 다룬다. 코드는 GitHub Firesuiry/Unet-Astar-For-PCB-Routing — [Bohrium](https://www.bohrium.com/paper-details/unet-astar-a-deep-learning-based-fast-routing-algorithm-for-unified-pcb-routing/922310827124458078-2649)
- 서비스 관련성: **높음.** 검증된 탐색 알고리즘(A*)에 학습을 "가이드"로만 더하는 구조라 정확성 보장과 속도를 함께 얻는다. 90분 SLA에 적합하다.

**[R3] Escape routing using deep reinforcement learning**
- 학회/연도: SPIE Proc. Vol. 13510 (2025-02) — [SPIE](https://remotesensing.spiedigitallibrary.org/conference-proceedings-of-spie/13510/135101B/Escape-routing-using-deep-reinforcement-learning/10.1117/12.3058004.full)
- 방법/결과: 이스케이프 라우팅을 MDP로 정식화하고 DQN으로 푼다. 25×26 시뮬레이션 격자에서 핀 30/60/90개로 실험했다 — [SPIE](https://remotesensing.spiedigitallibrary.org/conference-proceedings-of-spie/13510/135101B/Escape-routing-using-deep-reinforcement-learning/10.1117/12.3058004.full)
- 한계: 장난감 규모의 격자다.

**[R4] Security-Aware Printed-Circuit-Board Routing Based on Deep Reinforcement Learning**
- 학회/연도: ISQED 2026 — [ISQED 2026 세션](https://isqed.org/English/Archives/2026/Technical_Sessions/131.html)
- 방법/결과: 다층 라우팅은 A* 탐색이 맡고, RL 에이전트는 테스트 포인트 삽입 위치를 고른다. 트레이스를 생성하기 전에 넷 우선순위(라우팅 순서)를 정한다. 평가한 보드에서 라우팅 100% 성공과 테스트 포인트 완전 커버리지를 보고했다 — [ISQED](https://isqed.org/English/Archives/2026/Technical_Sessions/131.html)
- 서비스 관련성: 중간. DFT(테스트 포인트) 자동 삽입이라는 제조 친화 기능의 근거가 된다.

**[R5] PCBWorld: A Benchmark Environment for Engine-Grounded PCB Design Automation**
- 저자/연도: Hyungseok Song 외 6명(LG AI Research 소속 포함), arXiv:2607.05915 (2026-07) — [arXiv](https://arxiv.org/abs/2607.05915)
- 내용: KiCad EDA 엔진 위에 만든 오픈소스 라우팅 환경이다. 에이전트가 엔진의 기본 연산으로 보드를 대화형으로 라우팅하고 DRC 피드백을 받는다. RL 정책과 도구 사용형 LLM 에이전트를 모두 지원한다. PCBWorld-Bench는 합성 인스턴스 2종과 실제 오픈소스 보드 679개(.kicad_pcb)로 구성되며, 라우팅을 지운 보드를 완성하게 한 뒤 KiCad 엔진으로 8개 지표를 채점한다. 방법론과 무관한 평가라 외부 라우터와 학습형 에이전트를 같은 기준으로 비교한다 — [arXiv](https://arxiv.org/abs/2607.05915); [HF 미러 요약](https://djaym7-arxivmedia.hf.space/post/256186)
- 핵심 진단: 초록은 학습 기반 PCB 라우팅이 여전히 규칙 기반 라우터에 뒤처진다고 명시한다 — [검색 요약](https://djaym7-arxivmedia.hf.space/post/256186)
- freerouting 비교: OrthoRoute 저장소에 따르면 PCBWorld 저자들이 OrthoRoute를 Freerouting, KiCadRoutingTools, 여러 학습형 라우팅 에이전트와 함께 벤치마크했다 — [GitHub OrthoRoute](https://github.com/bbenchoff/OrthoRoute)
- 서비스 관련성: **매우 높음.** 자사 라우팅 엔진을 freerouting 등과 공정하게 비교하는 사내 평가 프레임으로 바로 쓸 수 있다.

### Inferences
- 90분 SLA에서는 Freerouting이나 상용 오토라우터 같은 검증된 결정론적 라우터를 기본 엔진으로 두고, ML은 팬아웃, 넷 순서, 탐색 영역 추천 같은 가이드에 쓰는 하이브리드가 학술 근거와 맞는다(R1, R2, R4, R5).
- 고속 신호(임피던스 제어, 길이 매칭, 차동 페어)는 학습 기반 연구가 사실상 비어 있다. 서비스는 규칙·제약 기반으로 처리하고, 설계 근거에 "적용한 제약"을 명시하는 편이 안전하다.

### Gaps
- PCB 차동 페어·길이 매칭·임피던스 제어 라우팅을 ML로 다룬 동료심사 논문을 찾지 못했다. 검색 요약에서 차동 넷 쌍 제약을 다룬 커스텀 IC 상세 라우팅 심층 RL 논문(2023, ACM DOI 10.1145/3569052.3571874로 표기)이 언급됐지만, 학회명(ICCAD인지 ISPD인지)과 서지를 확인하지 못해 인용 목록에서 뺐다. 칩-레벨 연구라 PCB용도 아니다.
- PCBWorld 논문의 구체 수치(완성률, 라우터별 점수)는 원문 접근 차단으로 확인하지 못했다.
- "TRouter: Thermal-driven PCB Routing via Non-Local Crisscross Attention Networks"는 Bohrium 목록에서 제목만 확인됐고, 학회·연도·결과는 확인하지 못했다 — [Bohrium](https://www.bohrium.com/paper-details/trouter-thermal-driven-pcb-routing-via-non-local-crisscross-attention-networks/865002220448382999-2522)
- DeepPCB 라우팅 기술을 다룬 학술 논문(동료심사)을 확인하지 못했다.

---

## Q3. LLM 기반 하드웨어·전자 설계: 회로도·넷리스트 생성, 부품 선정, 데이터시트 파싱, 설계 규칙·리뷰

### Takeaway
2026년에 보드 레벨 LLM 연구가 급증했다. 자연어에서 KiCad 회로도를 생성하는 연구가 여럿 나왔고(pcbGPT, SchGen, PCBSchemaGen), 데이터시트를 근거로 회로도를 리뷰하는 연구(DRCY)도 나왔다. 공통 결론은 "LLM 단독"이 아니라 결정론적 검증기(ERC, 그래프 검증, DSL 체크)와 루프를 도는 구조여야 실용적이라는 것이다. 회로도 초안 수준에서는 단순 과제 성공률이 높지만, 실보드 수준 회로도 생성(HWE-Bench 8.15%)과 레이아웃 생성(Q4 참조)에서는 여전히 매우 낮다.

### Cited Findings

**[L1] pcbGPT: Automatic PCB Schematic Synthesis from Natural Language Requirements**
- 저자/연도: Karlsruhe Institute of Technology, Bosch Sensortec, arXiv:2606.01188 (2026-05-31) — [arXiv HTML](https://arxiv.org/html/2606.01188v1)
- 방법: 대화형 요구사항을 편집 가능한 KiCad 호환 회로도 초안으로 바꾼다. 부품 그라운딩(라이브러리 검색), 회로 DSL, 결정론적 체크, 의미 검증으로 구성된다 — [arXiv](https://arxiv.org/pdf/2606.01188)
- 결과: 임베디드 과제 20개에서 최고 모델이 pass@1 0.90, pass@5 1.00을 기록했다. 난이도별 pass@1은 basic·easy 1.00, medium 0.91, hard 0.72다. 저자들은 결과물이 초기 프로토타이핑용 초안으로는 유용하지만 아직 전문가 리뷰를 대체할 만큼 신뢰할 수는 없다고 결론지었다 — [arXiv](https://arxiv.org/pdf/2606.01188) (검색 스니펫 기준)
- 서비스 관련성: **높음.** "초안과 전문가 리뷰"라는 포지셔닝이 이 서비스의 "설계 제안" 개념과 같다.

**[L2] SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations**
- 저자/연도: UC San Diego, Microsoft Research Asia, arXiv:2605.30345 (2026-05-28) — [arXiv](https://arxiv.org/abs/2605.30345); [GitHub microsoft/SchGen](https://github.com/microsoft/SchGen)
- 방법: GPT-oss-20B를 파인튜닝(LoRA)해, 편집 가능한 KiCad 회로도를 생성하는 Python 코드를 출력하게 한다. 오픈소스 하드웨어(SparkFun, 1,390종 회로도 유형)를 코드 표현으로 변환해 데이터를 구축했다 — [alphaxiv](https://www.alphaxiv.org/abs/2605.30345.md)
- 데이터셋: 자연어 요청과 회로도 생성 코드 쌍 8,420개(GPT 초안 → 사람 교정·주석 → LLM으로 요청 생성) — [HF 데이터셋](https://huggingface.co/datasets/microsoft/SchGen_dataset)
- 결과: 유효 회로율 82%, 전문가 검증 기능 정확도 60.5%. 원시 KiCad 파일을 직접 생성하는 기준선은 각각 32.45%, 3.0%였다 — [검색 요약(alphaxiv)](https://www.alphaxiv.org/abs/2605.30345.md)
- 서비스 관련성: **높음.** "KiCad 원시 포맷을 직접 생성하지 말고 코드나 DSL 중간표현을 쓰라"는 설계 교훈을 준다.

**[L3] PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards**
- 저자/연도: arXiv:2602.00510 (2026-01), 이후 NeurIPS 2026 포스터로 개정 — [arXiv HTML](https://arxiv.org/html/2602.00510v1); [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/149018)
- 방법(v1): 학습 없이 LLM이 SKiDL 코드를 생성하고, 지식그래프 기반 검증기가 피드백한다. v1 벤치마크는 디지털, 아날로그, 전원 도메인의 실제 IC를 쓰는 23개 회로다 — [arXiv](https://arxiv.org/html/2602.00510v1)
- 방법(NeurIPS 판): IC 데이터시트에서 유도한 도메인 스키마, 연속 보상과 **핀 단위 오류 위치 지정**을 주는 결정론적 5층 검증기, Thompson Sampling 밴딧 정제를 쓴다. 벤치마크 2개, 22개 도메인, 총 227개 과제(pcbbench 62개, open_schematics 165개, 후자는 일반화 테스트)로 평가했다. 같은 Gemma-4-31B 백본이라도 어려운 시스템 레벨 설계에서는 성능이 떨어진다 — [NeurIPS](https://neurips.cc/virtual/2026/poster/149018); [HF 벤치마크](https://huggingface.co/datasets/Hzou9/PCBSchemaGen-Benchmarks)
- 수치 상충: DOE 리뷰 슬라이드(2026-07)는 65개 과제, 22개 도메인, IC 44종에서 Pass@1 77.5%, 전문가 대비 37배 빠르고 570배 저렴하며, 5kW AC/DC 전원을 실제 제작 보드로 검증했다고 주장한다. 이는 다른 판의 벤치마크 규모와 맞지 않으므로 예비 수치로 다뤄야 한다 — [DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf)
- 서비스 관련성: **매우 높음.** "핀 단위 오류 위치 지정"은 그대로 설계 근거와 검증 리포트로 노출할 수 있는 형식이다.

**[L4] HWE-Bench: Can Language Models Perform Board-level Schematic Designs?**
- 연도: arXiv:2603.18102 (2026-03) — [arXiv HTML](https://arxiv.org/html/2603.18102v1)
- 내용: GitHub와 OSHWLab에서 수집한 보드 레벨 과제 300개(응용 도메인 8개)와 실제 IC 데이터시트 2,914개 지식베이스로 구성된다. 기능 요구사항과 데이터시트를 입력으로 받아 회로도를 처음부터 생성하게 하고, 정적 전기규칙 검사와 회로 시뮬레이션으로 동적 동작을 검증한다 — [arXiv](https://arxiv.org/pdf/2603.18102)
- 결과: 최고 모델의 전체 통과율이 8.15%다(제3자 요약 수치로, 원문 표에서는 확인하지 못함) — [emergentmind](https://www.emergentmind.com/papers/2603.18102)
- 참고: 하드웨어 버그 수리용의 동명 벤치마크(HWE-Bench, 417개 과제)와 혼동하지 말 것.

**[L5] DRCY: Agentic Hardware Design Reviews**
- 저자/연도: AllSpice Inc., arXiv:2603.15672 (2026-03-13), CAIS 2026 데모 — [arXiv](https://arxiv.org/abs/2603.15672); [CAIS 2026](https://caisconf.org/program/2026/demos/drcy-hardware-review/)
- 방법: 회로도 연결을 부품 데이터시트와 대조해 1차 자동 리뷰를 한다. 부품 그룹화(선택 단계) → 데이터시트 검색 → 추출 에이전트 → 비평(critic) 에이전트 순으로 돌며, 비평 에이전트는 기능 완전성, 핀 기능 커버리지, 응용 정보, 전형 응용회로를 기준으로 추출 품질을 점수화한다. AllSpice Hub에서 CI/CD 액션으로 운영 중이다 — [arXiv PDF](https://arxiv.org/pdf/2603.15672); [AllSpice 기술 블로그](https://www.allspice.io/post/under-the-hood-how-drcy-reviews-your-schematics)
- 결과(벤더 자체 보고): 설계 리뷰 11건(최대 150페이지 회로도)에서 사람 리뷰를 이미 통과한 실제 이슈 4건을 찾았고, 의도적으로 주입한 DDR5 오류는 100% 검출했다. 오탐률은 공개하지 않았다 — [AllSpice](https://www.allspice.io/post/how-hardware-engineering-teams-evaluate-drcy)
- 서비스 관련성: **매우 높음.** 데이터시트를 근거로 한 설계 리뷰는 이 서비스의 "설계 근거" 기능에 가장 가까운 학술 레퍼런스다.

**[L6] 데이터시트 파싱·부품 라이브러리 생성**
- **DocEDA** (arXiv:2412.05301, 2024-11): 문서와 데이터시트에서 연쇄 사고(CoT) 프롬프트로 전기 파라미터를 추출하고, 레이아웃 분석 모델로 회로 관련 영역을 분류한다 — [arXiv](https://arxiv.org/abs/2412.05301?context=cs)
- **D2S-FLOW** (arXiv:2502.16540, 2025): 데이터시트 파라미터를 추출해 PySpice 모델을 생성한다 — [arXiv](https://arxiv.org/pdf/2502.16540)
- **SFgen: Symbol and Footprint Database for Electronic Components by Agentic Recognition and Generation** (arXiv:2607.19767, 2026): 멀티모달 LLM으로 데이터시트에서 심볼과 풋프린트를 생성한다. 심볼 정확도 86%, 풋프린트 80%, 부품 1,000개 DB를 구축했다 — [arXiv](https://arxiv.org/pdf/2607.19767)
- **RAG 기반 부품 선정** (MDPI *Electronics* 15(11):2301, 2026): LLM이 만든 데이터시트 요약으로 유사 부품을 검색한다 — [MDPI](https://www.mdpi.com/2079-9292/15/11/2301)
- 서비스 관련성: 풋프린트 80% 정확도는 사람 검증이 필수라는 뜻이다. 업로드 파일에 라이브러리가 빠졌을 때 보완하는 용도로 쓸 수 있다.

**[L7] LLM과 KiCad 및 EDA 에이전트(초기·인접 연구)**
- **SmartonAI** — "New Interaction Paradigm for Complex EDA Software Leveraging GPT" (arXiv:2307.14740, 2023): LLM 비서가 KiCad 같은 복잡한 EDA 소프트웨어 조작을 돕는다 — [arXiv HTML](https://arxiv.org/html/2307.14740v2)
- **ChatEDA** [칩-레벨]: Zhuolun He, Haoyuan Wu 외, arXiv:2308.10204, *IEEE TCAD* 43(10):3184–3197 (2024-10). 파인튜닝한 LLM(AutoMage)이 RTL→GDSII 흐름의 과업 분해, 스크립트 생성, 실행을 맡는 자율 에이전트다. 저자 실험에서 GPT-4보다 우수했다 — [HF Papers](https://huggingface.co/papers/2308.10204); [arXiv](https://arxiv.org/abs/2308.10204v1)
- **AnalogCoder** [회로 레벨]: Yao Lai 외, AAAI 2025 (arXiv:2405.14918). 학습 없이 Python 코드 생성으로 아날로그 회로를 설계하는 최초의 LLM 에이전트라고 주장한다. 회로 20개 설계에 성공해 GPT-4o보다 5개 많았다. 코드는 GitHub에 공개 — [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/32016); [arXiv](https://arxiv.org/abs/2405.14918v1); [GitHub](https://github.com/laiyao1/AnalogCoder)
- **EDASYTH** (Preprints.org 202609.0945, 비동료심사): LTspice 아날로그 설계와 KiCad 레이아웃을 6단계 워크플로로 묶고 ERC 체크를 루프에 넣는다 — [Preprints.org](https://www.preprints.org/manuscript/202609.0945)

**[L8] LLM과 최적화로 하는 열 인지 PCB 레이아웃**
- "PCB Thermal Layout Optimization for Power Electronics: Integrating Large Language Models with NSGA-II for Enhanced Energy Efficiency," IEEE ECCE 2025, DOI 10.1109/ECCE58356.2025.11259777 (Chalmers, KU Leuven). LLM이 설계 지식으로 개체군 생성과 후보 선택을 돕는 다목적 유전 알고리즘이다 — [Chalmers research](https://research.chalmers.se/en/publication/550860)

### Inferences
- 업로드 → 90분 → 설계 제안 서비스에서 LLM은 ① 요구사항과 회로도 해석, ② 부품 및 데이터시트 근거 수집, ③ 설계 근거 서술과 리뷰를 맡는 것이 문헌상 가장 근거가 강하다. 배치와 라우팅 자체는 Q1·Q2의 최적화 엔진에 맡기는 분업 구조가 맞다.
- 성공한 시스템들(pcbGPT, SchGen, PCBSchemaGen)의 공통 설계 원칙은 "중간표현(DSL, SKiDL, Python 코드)과 결정론적 검증기 루프"다. 원시 KiCad 포맷을 직접 생성하면 성능이 급락한다(SchGen 기준선 3.0%).
- 단순·중간 난이도 과제(pcbGPT의 20개 과제)와 실제 보드 수준 과제(HWE-Bench 300개) 사이 성능 격차가 매우 크다(0.90 대 0.08). 따라서 서비스는 "전문가 검토용 초안"으로 포지셔닝해야 한다.

### Gaps
- 과업 지시문에 예시로 나온 "CircuitLM", "LLM4PCB", "PCBAgent", "AutoPCB"라는 이름의 학술 논문은 이번 검색에서 확인하지 못했다. 존재 여부가 불확실하므로 보고서에 인용하지 말 것.
- ChipGPT는 AnalogCoder 논문의 비교표에서 "디지털 설계" 연구로 언급된 것만 확인했고, 상세 서지는 확인하지 못했다 — [검색 결과](https://ojs.aaai.org/index.php/AAAI/article/view/32016)
- LLM이 직접 PCB DRC를 수행하는 연구(레이아웃 DRC)는 찾지 못했다. 확인된 것은 회로도·데이터시트 수준 리뷰(DRCY)와 KiCad DRC를 피드백으로 쓰는 환경(PCBWorld, EDA Bench)뿐이다.
- AnalogCoder-Pro의 "GPT-5 Pass@5 98.6%" 수치는 2차 요약 사이트 출처라 신뢰도가 낮다.

---

## Q4. PCB AI용 데이터셋과 벤치마크

### Takeaway
2026년에 PCB 전용 벤치마크가 한꺼번에 나왔다. ICLR, NeurIPS, ICML 2026에 PCB-Bench, PCBInnoBench, PCB Gym, EDA Bench가 발표됐고, arXiv에도 PCBWorld, OmniLayout, PCB-QA, HWE-Bench가 올라왔다. 결과는 일관되게 비관적이다. LLM 에이전트의 실보드 레이아웃과 기능 완성률은 4.6~32% 수준이다. 학습용 대규모 PCB 레이아웃 코퍼스는 여전히 부족하고, 칩 쪽의 CircuitNet 같은 표준 데이터셋에 해당하는 PCB 데이터셋은 아직 없다.

### Cited Findings

| 이름 | 학회·연도 | 규모·구성 | 핵심 결과 | 출처 |
|---|---|---|---|---|
| **PCB-Bench** | ICLR 2026 (Jindong Li, Lianrong Chen, Bin Yang, Jiadong Zhu, Ying Wang, Yuzhe Ma, Menglin Yang) | 텍스트 약 3,700건(QA 1,800쌍 이상과 객관식 버전), 이미지·텍스트 멀티모달, 실제 PCB 프로젝트 170개 이상(회로도, 배치 파일, 문서) | 제로샷 평가에서 공간 배치 추론, 도메인 제약 준수, 엔지니어링 산출물 해석에 큰 격차가 있었다 | [ICLR](https://iclr.cc/virtual/2026/poster/10009621); [프로젝트](https://digailab.github.io/PCB-Bench) |
| **PCBInnoBench** | NeurIPS 2026 | 실제 프로젝트 기반 KiCad 과제 372개. 에이전트가 기존 ECAD를 수정하고 구조, 과제, 교차 산출물 검사를 통과해야 한다 | 최고 에이전트 Pass@1이 전문가 가이드 있을 때 22.0%, 없을 때 7.3% | [NeurIPS](https://neurips.cc/virtual/2026/poster/139034) |
| **PCB Gym** | NeurIPS 2026 | 오픈 하드웨어 기반 2~12층 보드. 배치와 라우팅을 함께 다루며, 설계 의도는 Zener(schematic-as-code HDL)로 제공. 결정론적 검사와 루브릭 기반 에이전트 채점 | 프런티어 LLM이 DRC를 통과하고 완전 라우팅된 보드를 낸 비율은 약 32.1%. 흔한 실패는 전원 레일을 일반 신호 넷처럼 다룬 것 | [NeurIPS](https://neurips.cc/virtual/2026/161602) |
| **EDA Bench** | ICML 2026 | 공개 오픈하드웨어에서 뽑은 KiCad 재구성 과제 35개. 오라클이 구리 라우팅, 포트, 트레이스 기생성분, 단락, ngspice 시뮬레이션, ERC·DRC를 검사 | 최강 하네스의 종합 점수 4.58%. 35개 중 21개는 빌드했지만 기능 검사는 대부분 실패했다. 그럴듯해 보여도 전기적으로 동작하지 않는다는 결론 | [ICML](https://icml.cc/virtual/2026/77908) |
| **PCBWorld-Bench** | arXiv 2607.05915 (2026-07) | 합성 2종과 실제 보드 679개, 8개 지표, 방법론 무관 평가 | 학습형 라우터는 규칙 기반에 뒤처짐 | [arXiv](https://arxiv.org/abs/2607.05915) |
| **OmniLayout** | arXiv 2607.03261 (2026-07, Taiting Lu 외 14명) | 회로도와 결합된 산업급 PCB 레이아웃 1,681개, IC 배치 인스턴스 77.24K개. 과제 4종(기하 추론, routability 인지 배치, 전기 기능 보존, 도구 증강 에이전트) | LLM의 기하 추론이 약하고 routability 최적화가 부족하며 전기 기능 보존이 일관되지 않음 | [arXiv](https://arxiv.org/abs/2607.03261); [deeplearn.org](https://deeplearn.org/arxiv/787921/omnilayout:-a-schematic-coupled-multimodal-benchmark-for-constraint-aware-geometric-reasoning-in-pcb-layout) |
| **HWE-Bench** | arXiv 2603.18102 (2026-03) | 보드 레벨 회로도 과제 300개, 데이터시트 2,914개 | 최고 통과율 8.15%(제3자 요약) | [arXiv](https://arxiv.org/html/2603.18102v1) |
| **PCB-QA** | arXiv 2606.23704 (2026) | 초기 KiCad 설계 파일 기반 QA 480쌍. KiCad 원본, 넷리스트 JSON, SPICE 넷리스트 등 여러 표현 | 오픈·클로즈드 LLM 비교(구체 수치는 확인 못함) | [arXiv](https://arxiv.org/pdf/2606.23704) |
| **PCBnet** | arXiv 2608.27923 (2026) | 회로도 이미지와 SPICE 넷리스트 쌍 300개 이상, 자동 변환 파이프라인 | 부품 검출 mAP 94.54%, 텍스트 인식 98.57%, 종단 연결 정확도 84.47% | [takara 요약](https://tldr.takara.ai/p/2608.27923) |
| **PCBSchemaGen 벤치마크** | NeurIPS 2026 | pcbbench 62개와 open_schematics 165개 | Q3 참조 | [HF](https://huggingface.co/datasets/Hzou9/PCBSchemaGen-Benchmarks) |
| **Cypress PCB 벤치마크** | ISPD 2025 | 상용 설계에서 합성한 배치 벤치마크 | Q1 참조 | [GitHub](https://github.com/NVlabs/Cypress) |
| **UniPCB** | arXiv 2601.19222 (2026) | 이미지 6천 장과 멀티모달 QA 2.3만 쌍(PCB 품질 검사). PCB-GPT 모델 포함 | 설계가 아닌 검사(inspection) 분야 | [arXiv](https://arxiv.org/html/2601.19222) |

- **학습용 코퍼스**: Open Schematics(Hugging Face)는 공개 하드웨어 저장소에서 모은 회로도 샘플 약 84,470개로, 원본, 렌더 이미지, 메타데이터, 같은 프로젝트의 PCB 파일을 포함한다. 레코드별 라이선스 확인이 필요하다 — [HF open-schematics-v4](https://huggingface.co/datasets/bshada/open-schematics-v4)
- **SchGen 데이터셋**: 자연어와 회로도 코드 쌍 8,420개 — [HF](https://huggingface.co/datasets/microsoft/SchGen_dataset)
- **PCBBenchmarks**: ASP-DAC 투고용 KiCad 라우팅 벤치마크 bm1~bm11(라우팅 전·후 파일) — [Gitee openpcb](https://gitee.com/openpcb/PCBBenchmarks)
- **데이터 부족 신호**: KiCad 포럼에서 연구자들이 비상업 연구용으로 공개 KiCad 회로도·PCB 쌍을 구하고 있다 — [KiCad 포럼](https://forum.kicad.info/t/seeking-a-samples-of-kicad-projects-schematics-pcbs-for-a-non-commercial-research-dataset/61531)
- **CircuitNet [칩-레벨 참조 표준]**: Peking University가 만든 데이터셋으로, 오픈소스 RISC-V 설계 6종에서 상용 도구로 생성한 샘플 1만 개 이상(유효 레이아웃 10,242개)을 담고 있다. 혼잡도(routability), DRC 위반, IR drop을 예측 과제로 다룬다. *Science China Information Sciences*(2022)와 *IEEE TCAD*(2023)에 실렸다. 데이터 불균형과 모델 전이성을 핵심 난제로 지목했고, 지식증류 전이로 ISPD 2015 설계에서 혼잡도 예측 정확도를 최대 20% 높였다 — [arXiv 2208.01040](https://arxiv.org/pdf/2208.01040); [프로젝트](https://circuitnet.github.io/intro/overview.html)

### Inferences
- 벤치마크가 공통으로 보여주는 것은 "DRC 통과 ≠ 기능 동작"이다. EDA Bench에서는 21개를 빌드했지만 점수는 4.58%였고, PCB Gym에서는 전원 레일을 신호처럼 다루는 실패가 흔했다. 서비스 품질 지표는 DRC 통과율만이 아니라 ERC, 전원 무결성, 시뮬레이션 기반 기능 검사를 포함해야 한다.
- 사내 평가는 PCBWorld-Bench(라우팅), Cypress 벤치마크(배치), PCB Gym 또는 PCBInnoBench(에이전트 종합)를 조합하면 국제적으로 비교 가능한 수치를 낼 수 있다.
- 칩 분야에서 CircuitNet이 했던 역할을 PCB에서 맡을 대규모 레이아웃 데이터셋은 아직 없다. 자체 수집 데이터(고객 업로드는 동의를 받은 경우에만)가 경쟁 우위가 될 수 있다.

### Gaps
- PCB-Bench, PCB-QA, OmniLayout의 모델별 정량 결과표는 원문 접근 차단으로 확인하지 못했다.
- PCB Gym과 PCBInnoBench의 코드·리더보드 공개 상태(PCBInnoBench는 익명 저장소로 공개)는 확인하지 못했다.
- Open Schematics 중 실제 PCB 레이아웃 파일이 들어 있는 레코드의 비율은 확인하지 못했다.

---

## Q5. AI-EDA의 설명가능성과 설계 근거(설계 근거)

### Takeaway
EDA 분야의 XAI 연구는 아주 적다. 가장 직접적인 선례는 SHAP으로 DRC 핫스팟 예측을 설명한 연구(Zeng 외, DATE 2020)이고, PCB 배치·라우팅 결정을 설명하는 전용 연구는 찾지 못했다. 실무적으로는 LLM 서술 자체가 아니라 데이터시트, 결정론적 검증기, 규칙 같은 "검증 가능한 근거"에 기반한 설명이 최근 연구의 흐름이다(DRCY, PCBSchemaGen의 핀 단위 오류 위치 지정).

### Cited Findings
- **Explainable DRC Hotspot Prediction with Random Forest and SHAP Tree Explainer**: Wei Zeng, Azadeh Davoodi, Rasit Onur Topaloglu (UW–Madison, IBM), DATE 2020 **[칩-레벨]**. 글로벌 라우팅 단계에서 랜덤포레스트로 DRC 핫스팟을 예측하는데, 기존 연구보다 성능이 크게 높고 개발 시간은 일부만 든다. SHAP 값으로 개별 예측을 설명한 첫 사례라고 주장한다 — [DATE 2020 아카이브](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)
- Wei Zeng의 박사논문은 설명 가능한 routability 예측(설계 개선 힌트 제공), 설명 가능한 DRC 핫스팟 예측, SHAP 기반 라우팅 난독화를 다룬다 — [UW–Madison 저장소](https://asset.library.wisc.edu/1711.dl/BC2C46IWG3FZ38I/R/file-ccbba.pdf)
- MLCAD 2023 논문은 전통 EDA 방법이 학습 데이터가 덜 필요하고, 알려진 문제 영역에서 해를 보장하며, 해석 가능성이 좋다는 점에서 ML 방법과 대비된다고 지적한다 — [CUHK MLCAD 2023 PDF](https://www.cse.cuhk.edu.hk/~byu/papers/C176-MLCAD2023-MLEDA.pdf)
- 한 AI-for-EDA 리뷰는 Circuit Foundation Models와 함께 XAI를 신흥 연구 방향으로 꼽는다(스니펫이 목차 수준이라 상세 내용은 확인하지 못함) — [검색 결과](https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/81896/751375162472/)
- **데이터시트 근거 리뷰**: DRCY는 회로도 연결을 데이터시트와 대조하고, critic 에이전트가 추출 품질(핀 기능 커버리지, 전형 응용회로 등)을 점수화한다. 벤더 스스로 "사람의 판단을 대체하지 않는다"고 밝혔다 — [arXiv 2603.15672](https://arxiv.org/pdf/2603.15672); [AllSpice](https://www.allspice.io/post/under-the-hood-how-drcy-reviews-your-schematics)
- **검증기 기반 설명**: PCBSchemaGen(NeurIPS 2026 판)의 결정론적 5층 검증기는 핀 단위 오류 위치 정보를 준다 — [NeurIPS](https://neurips.cc/virtual/2026/poster/149018)
- **규칙형 근거**: Lim(2026)의 RL 배치는 "수동소자를 전원 핀 근처에 배치해 배선 단축과 겹침 회피"라는 해석 가능한 원칙에 기반한다 — [arXiv HTML](https://arxiv.org/html/2602.23540v1). Vassallo & Bajada는 정책이 "기본 배치 기법"을 학습했다는 정성 분석을 냈다 — [UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)

### Inferences
- 설계 근거 기능은 학술적으로 거의 비어 있는 영역이라 차별화 여지가 크다. 가장 근거 있는 구현은 세 층 구조다. ① 결정론적 사실(DRC, ERC, 넷 길이, 전원 플레인 DCR 등 측정값), ② 데이터시트와 규칙 인용(DRCY 방식), ③ LLM의 자연어 서술. 이때 LLM 서술이 ①·②에 없는 주장을 하지 못하도록 "근거 인용 강제"를 두어야 한다.
- 예측 모델(혼잡도, DRC 위반 예측 등)을 쓰면 SHAP 같은 특성 기여도 설명을 붙일 수 있다는 선례가 있다(Zeng DATE 2020).
- 벤치마크 결과(Q4)로 볼 때 "그럴듯하지만 동작하지 않는" 출력 위험이 높다. 그래서 근거 리포트에는 수행한 검증과 수행하지 못한 검증(예: SI·열 시뮬레이션 미수행)을 명시하는 것이 신뢰 확보에 중요하다.

### Gaps
- PCB 배치·라우팅 결정을 설명하는 전용 XAI 논문은 찾지 못했다.
- LLM이 생성한 설계 근거의 정확성이나 환각을 평가한 연구도 찾지 못했다.
- XAI for physical design 전용 서베이는 확인하지 못했다.

---

## Q6. ML·LLM for EDA 서베이 논문: PCB 관련 부분 요약

### Takeaway
고전 서베이(Huang 외 TODAES 2021)와 LLM-EDA 서베이(Pan 외 2025, He 외 2025, Agentic EDA 2025)는 거의 전적으로 IC/VLSI 흐름 중심이고 PCB는 사실상 다루지 않는다. 2026년 6월 UNSW의 "Surveying GenAI-based Automation in Printed Circuit Board Design and Test"가 PCB 생애주기 전체를 다루는 첫 GenAI 서베이로 보이며, 데이터 부족과 기존 PCB 도구와의 통합 부족을 핵심 장애물로 꼽는다.

### Cited Findings
- **Machine Learning for Electronic Design Automation: A Survey**: Guyue Huang 외 16명(Tsinghua, CUHK), *ACM TODAES*, DOI 10.1145/3451179 (2021), arXiv:2102.03357 **[칩-레벨]** — [arXiv](https://arxiv.org/abs/2102.03357v2)
  - 구성: EDA 설계 계층별 정리(물리 설계, 아날로그, 테스트·검증 등). 분류는 ① 전통 방법 안의 의사결정, ② 성능 예측, ③ 블랙박스 최적화, ④ 자동 설계의 네 가지다 — [ar5iv](https://ar5iv.labs.arxiv.org/html/2102.03357)
  - PCB 관련: 배치와 라우팅이 강하게 결합돼 있어 배치 단계에서 라우팅 성능을 고려해야 한다는 관찰은 PCB에도 그대로 적용된다 — [검색 결과(ar5iv)](https://ar5iv.labs.arxiv.org/html/2102.03357). PCB를 직접 다룬 절은 검색으로 확인되지 않았다.
- **A Survey of Research in Large Language Models for Electronic Design Automation**: Pan 외, arXiv:2501.09655 (2025-01), 이후 *ACM TODAES* 게재 — [arXiv](https://arxiv.org/pdf/2501.09655); [Duke CEI](https://cei.pratt.duke.edu/research/electronic-design-automation/survey-research-large-language-models-electronic-design). 모델 구조, 크기, 커스터마이징 기법, 미해결 과제를 다룬다.
- **Large Language Models for EDA: From Assistants to Agents**: He 외, *Foundations and Trends in EDA* 14(4):295 (2025). 어시스턴트(QA, 스크립트 생성)에서 자율 에이전트로의 진화를 다룬다 — [Emerald/FnT](https://www.emerald.com/fteda/article/14/4/295/1325096/Large-Language-Models-for-EDA-From-Assistants-to)
- **The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design**: arXiv:2512.23189 (2025-12) **[칩-레벨]**. 디지털 칩 설계용 생성형·에이전트 AI를 다룬다 — [arXiv HTML](https://arxiv.org/html/2512.23189v1)
- **Surveying GenAI-based Automation in Printed Circuit Board Design and Test**: Sahana Srinivasan, Benjamin Turnbull, Hammond Pearce (UNSW), arXiv:2606.17074 (2026-06-10) — [arXiv](https://arxiv.org/pdf/2606.17074)
  - 범위: 공급망, 시스템 사양, 회로 설계, 레이아웃, 검증·테스트, 조립까지 PCB 생애주기 전체를 다룬다. 기존 연구를 의도와 기여 기준의 분류 체계로 정리한다 — [deeppaper 요약](https://arxiv.deeppaper.ai/papers/2606.17074v1)
  - 핵심 장애물: 도메인 특화 데이터 부족과 기존 PCB 도구와의 통합 부족 — [arXiv](https://arxiv.org/pdf/2606.17074)

### Inferences
- 보고서에서 "PCB AI 학술 현황"을 요약할 때는 Srinivasan 외(2026)를 1차 서베이로, Huang 외(2021)와 Pan 외(2025)를 칩 쪽 방법론의 배경으로 인용하는 구성이 적절하다.
- 서베이들이 지목한 "도구 통합 부족"은 KiCad, Altium 등 기존 파일을 받아 처리하는 이 서비스가 메울 수 있는 틈이다.

### Gaps
- Srinivasan 외(2026) 서베이의 세부 분류 체계와 인용 논문 목록은 원문 접근 차단으로 확인하지 못했다. 원문을 열 수 있게 되면 이 서베이의 참고문헌으로 이 목록을 교차 검증하기를 권장한다.
- Huang 외(2021)에 PCB 전용 절이 있는지는 확인하지 못했다(검색상 없음).

---

## Q7. 주요 미해결 문제와 한계: SI, 열, 제조성, 일반화 등

### Takeaway
문헌이 공통으로 지적하는 한계는 다섯 가지다. ① 기능 정확성 격차(DRC는 통과해도 전기적으로는 오동작), ② 학습형 라우팅이 규칙 기반에 열세, ③ 신호·전원 무결성과 열을 다루는 ML 연구의 희소성, ④ 데이터 부족과 일반화 문제, ⑤ 재현성과 평가 신뢰성(AlphaChip 논쟁). 업로드 후 90분 안에 결과를 주는 서비스는 이 한계를 전제로 사람 검토 루프와 명시적 검증 범위 고지를 설계에 넣어야 한다.

### Cited Findings
- **기능 정확성**: EDA Bench에서 최강 하네스는 4.58%를 기록했다. 35개 중 21개는 빌드했지만 기능 검사 대부분에 실패했고, 저자들은 "파싱되고 그럴듯해 보여도 전기적으로 동작하지 않는다"고 결론지었다 — [ICML 2026](https://icml.cc/virtual/2026/77908). PCB Gym에서는 DRC를 통과하고 완전 라우팅된 비율이 약 32.1%였고, 전원 레일을 신호 넷처럼 다루는 실패가 흔했다 — [NeurIPS 2026](https://neurips.cc/virtual/2026/161602)
- **에이전트의 워크플로 이해**: PCBInnoBench의 최고 Pass@1은 22.0%(가이드 있음)와 7.3%(없음)였다. 워크플로 발견과 ECAD 실행 모두 어렵다 — [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/139034)
- **공간·기하 추론**: PCB-Bench와 OmniLayout 모두 LLM의 공간 배치 추론, 제약 준수, routability 최적화, 전기 기능 보존이 약하다고 보고했다 — [ICLR 2026](https://iclr.cc/virtual/2026/poster/10009621); [OmniLayout](https://arxiv.org/abs/2607.03261)
- **학습형 라우팅의 열세**: PCBWorld 저자들은 학습 기반 PCB 라우팅이 규칙 기반 라우터에 뒤처진다고 명시했다 — [arXiv 2607.05915](https://djaym7-arxivmedia.hf.space/post/256186)
- **열**: 2024~2025년 PCB 배치에서 RL이나 GNN으로 열을 목표로 삼은 연구는 검색되지 않았다. 확인된 것은 LLM+NSGA-II(ECCE 2025)와 칩렛 열 인지 배치(arXiv 2504.03808) 정도다 — [Chalmers](https://research.chalmers.se/en/publication/550860); [arXiv 2504.03808](https://arxiv.org/pdf/2504.03808)
- **전원 무결성**: PDN 형상과 스택업을 RL로 합성하는 연구(Google/Missouri S&T)가 드문 PCB PI 사례다 — [Google Research](https://research.google/pubs/novel-graph-based-reinforcement-learning-approach-for-multi-power-domain-pcb-pdn-shape-and-stackup-synthesis/)
- **데이터 부족과 도구 통합**: GenAI PCB 서베이가 핵심 장애물로 지목했다 — [arXiv 2606.17074](https://arxiv.org/pdf/2606.17074). CircuitNet도 칩 분야에서 데이터 불균형과 전이성을 핵심 난제로 꼽았다 — [CircuitNet](https://circuitnet.github.io/intro/overview.html)
- **복잡도에 따른 성능 저하**: PCBSchemaGen은 같은 백본이라도 어려운 시스템 레벨 설계에서 성능이 떨어진다고 보고했다 — [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/149018). pcbGPT의 pass@1은 hard에서 0.72로 basic의 1.00보다 낮다 — [arXiv](https://arxiv.org/pdf/2606.01188)
- **재현성과 평가**: AlphaChip 논쟁에서 Cheng 외는 초기 배치 의존성과 재현 불가를 지적했고, 강화된 SA와 인간 기준선이 우수하다고 보고했다. Google 측은 방법론 미적용이라고 반박했다 — [arXiv 2302.11014v3](https://arxiv.org/abs/2302.11014v3); [arXiv 2411.10053](https://arxiv.org/abs/2411.10053v1); [CACM](https://cacm.acm.org/news/updates-spark-uproar)
- **라이브러리 정확도**: 데이터시트 기반 자동 풋프린트 생성 정확도가 80%라 제조 리스크가 남는다 — [SFgen arXiv 2607.19767](https://arxiv.org/pdf/2607.19767)
- **사람 검토 필요성**: pcbGPT 저자는 "전문가 리뷰를 대체할 만큼 신뢰할 수 없다"고 했고 — [arXiv](https://arxiv.org/pdf/2606.01188), DRCY 벤더는 "사람의 판단을 대체하지 않는다"고 했다 — [AllSpice](https://www.allspice.io/post/under-the-hood-how-drcy-reviews-your-schematics)

### Inferences
- 90분 SLA 측면에서 칩 연구의 RL 사전학습과 미세조정 비용, 그리고 초기 DeepPCB의 24시간 처리 시간을 보면, 요청 시점에 학습하는 방식은 맞지 않는다. 사전학습된 정책, GPU 해석적 배치, 결정론적 라우터, LLM 서술로 구성하면 문헌상 90분 안에 들어올 가능성이 높다. 다만 이를 직접 실측한 학술 연구는 없다.
- 서비스의 "설계 제안"은 문헌 수준으로 보면 "전문가 검토용 고품질 초안"이 정직한 포지셔닝이다. 자동 생성 보드를 그대로 제작해도 된다는 근거는 현재 학술 문헌에 없다.
- SI(임피던스, 크로스토크, 차동 페어)와 DFM(제조성)을 ML로 다룬 PCB 연구는 공백에 가깝다. 이 영역은 규칙 기반 검사와 상용 시뮬레이터 연동으로 메우고, 근거 리포트에 "미검증 항목"으로 명시해야 한다.

### Gaps
- PCB SI(크로스토크, 임피던스, 리턴 패스) 최적화에 ML이나 LLM을 적용한 동료심사 논문은 이번 검색에서 확인하지 못했다.
- 학술 문헌에서 PCB DFM(제조성)을 ML로 다룬 연구를 확인하지 못했다(UniPCB 같은 검사·불량 탐지 연구는 설계가 아니라 제조 검사 영역이다).
- "업로드 후 수십 분 안에 처리"하는 PCB 자동 설계 파이프라인의 종단 런타임을 보고한 학술 연구는 찾지 못했다. Cypress의 속도 향상 배율 외에 절대 시간(분 단위) 수치는 확인하지 못했다.
- 이번 조사는 원문 접근이 차단된 상태에서 검색 스니펫으로 검증한 것이다. 특히 2026년 프리프린트(arXiv 26xx.xxxxx)의 수치는 원문 확인 후 인용하기를 권장한다.
