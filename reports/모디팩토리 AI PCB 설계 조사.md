# 모디팩토리, '설명하는 AI'로 PCB 레이아웃 시장에 도전하다

**요약:** 사용자가 첨부한 랜딩페이지의 "MODI Factory(모디팩토리)"는 모듈형 코딩 교구 MODI를 만든 **㈜럭스로보(2014년 설립, 대표 오상훈)**가 운영하는 웹 기반 AI PCB 배치·배선 서비스다. 2026년 3월 6일 처음 공개됐고, 지금도 얼리 액세스 단계이며, 2026년 말까지 모든 기능이 무료다. 회로도를 새로 만들어 주는 서비스는 아니다. 사용자가 Altium, KiCad(8.0 이상), EasyEDA의 **회로도와 레이아웃 파일을 한 쌍으로 올리면, 약 30분 배치와 약 60분 배선을 거쳐 2~3개 배치 후보와 배선 결과를 돌려준다.** 규칙 엔진이 내린 판정은 '배치 노트'와 '배선 노트'로 설명한다. 출력은 KiCad·Altium·EasyEDA PCB 파일, Gerber, PDF다. 처리 한도는 부품 300개, 연결 1,200개, 보드 200×200이고, 배치와 배선은 각각 하루 5회까지 실행할 수 있다. 엔진은 하이브리드다. LLM이 MCU·커넥터 같은 주요 부품을 놓고, 점수 루프가 수동소자를 채운다. "물리 기반 검증"은 현재 설계 규칙 준수와 규칙 기반 배치 진단을 뜻한다. 열 해석은 개발 중이고 SI/PI는 로드맵에만 있다. embedded award 2026에서는 Tools 부문 최종 후보 3곳에 들었지만 수상하지는 못했고, 이는 회사 PM도 인정했다. 학계는 이 분야를 아직 "전문가 검토용 초안" 수준으로 본다. 2026년 벤치마크에서 LLM 에이전트가 실보드 레이아웃과 기능 검사를 통과한 비율은 4.58~32.1%에 그쳤다. 학습형 라우터는 소형 보드에서만 규칙 기반 라우터(Freerouting)를 따라잡았고, 배치·배선 결정을 설명하는 연구는 사실상 없다. 국내에서는 LG AI연구원(PCBWorld, CADET)과 KAIST(디캡 강화학습)에 더해, 연세대의 LLM+RL 부품 배치 학술대회 논문(2024)과 보드 레벨 디캡 RL 학위논문(2025)이 나왔다. 그러나 학술지 논문은 아직 없다. 해외에서는 Quilter가 가장 가까운 경쟁자다. 배치·배선은 DeepPCB, Cadence, Siemens, Zuken이, 회로도 쪽은 Flux와 Circuit Mind가 맡고 있고, 2026년 하반기에는 GPT-6 Astra 같은 범용 모델도 KiCad 레이아웃에 들어왔다. 독립 레이아웃 벤치마크는 아직 없다. 실무 엔지니어는 AI를 리뷰와 BOM에는 쓰지만 배치는 믿지 않는다. 국내에는 같은 형태의 서비스가 없다. 모디팩토리의 차별점은 "파일 업로드형 서비스, 규칙 엔진에 근거한 설명, 한국어, Altium 연동, 무료 진입"의 조합이다. 한계는 공개 검증이 없다는 점, 처리 범위가 소·중형 보드에 한정되고 SI/PI가 구현되지 않았다는 점, 회로도가 있어야 시작할 수 있다는 점이다. 특히 **이용약관이 FAQ와 달리 업로드 원본의 R&D 활용과 생성 레이아웃의 지식재산권 회사 귀속을 규정**한다는 점은 구체적인 리스크다. 더 나은 서비스는 다섯 방향으로 가야 한다. 요구사항에서 발주까지 이어지고, 분 단위로 반복할 수 있고, 모든 설계 근거를 검사 결과에 연결하고, 성능을 공개 벤치마크로 증명하고, 설계 소유권을 사용자에게 돌려주는 것이다.

> **조사 방법과 검증 수준:** 1차 조사에서는 세션 네트워크 정책 때문에 modifactory.com, 국내 언론사, KCI·RISS·DBpia·KIPRIS·NTIS, arXiv를 열지 못해 많은 사실을 검색 스니펫에 의존했다. 네트워크가 열린 뒤의 보충 조사에서 다음 자료를 **원문으로 확인**했다.
> - 모디팩토리 공식 사이트·블로그·공지 28개 페이지와 서비스 앱(workspace.modifactory.com)의 공개 JS 번들(입출력 형식, 처리 한도, 이용약관, 개인정보처리방침)
> - DART 2023 감사보고서, Google Patents 서지·청구항, 주요 국내 기사
> - 핵심 논문의 arXiv·학회 페이지·GitHub 저장소, RISS 학위논문 레코드
> - Quilter·DeepPCB·Flux·Zuken 공식 페이지, Hacker News·EEVblog·KiCad 포럼 원문
>
> 그 결과 1차 조사의 충돌 중 럭스로보 2023년 매출과 PCBSchemaGen 수치는 해소됐다. **아직 스니펫이나 제3자 집계에만 근거한 항목**은 본문에 따로 표시했다. 럭스로보 2024~2025년 매출(Wadiz·TheVC), 직원 수, 수상 특허의 번호와 청구항(KIPRIS 접속 실패), Quilter 누적 투자액, Flux 플랜 금액, Cadence AuraStack·Siemens Fuse·Altium AI 기능의 세부, 세카의 92% 단축 수치, PCB-Bench 모델별 점수, DRCY 성과 수치(벤더 블로그), KAIST 2019·2023 석사논문, 시장 규모 추정치가 여기에 해당한다. Reddit은 끝내 접근하지 못했다. 확인하지 못한 항목은 사실로 서술하지 않았다. GitHub 스타 수는 2026-11-16 1차 조사 때 확인한 값이다.

## 1. 모디팩토리는 회로도가 아니라 배치·배선을 90분 안에 자동화한다

### 운영사 럭스로보는 교구 매출이 급감하는 가운데 EDA 기업으로 방향을 틀었다

공식 사이트는 www.modifactory.com(한국어 /ko)이고, 실제 서비스는 workspace.modifactory.com에서 돌아간다([modifactory.com](https://www.modifactory.com/); [이용약관](https://workspace.modifactory.com/terms)). 운영사는 **㈜럭스로보(LUXROBO)**다. 2024년 CES 공개 기사부터 2026년 기사까지 국내 언론이 일관되게 이 서비스를 럭스로보의 것으로 보도했다([전자신문](https://www.etnews.com/20240104000261); [서울경제](https://www.sedaily.com/article/20019757)). embedded award 2026 후보 목록에도 "MODI Factory (exhibitor: LUXROBO)"로 올라 있다([embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/02/tools-nominees)).

설립일은 출처마다 하루 차이가 난다. TheVC는 2014년 11월 13일, DART 감사보고서 주석은 11월 14일로 적는다. 2023년 말 본사는 서울 서초구 강남대로 311이다([TheVC](https://thevc.kr/luxrobo); [DART 연결감사보고서](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001142)). 대표는 **오상훈**이다. 주력 제품 MODI는 2024년 인터뷰 기준으로 약 4,000개 학교에 납품됐다([이투데이](https://www.etoday.co.kr/news/view/2363460)). MODI 시절에는 CES 혁신상과 K-Startup 최우수상을 받았다는 보도가 있다([아주경제](https://www.ajunews.com/view/20191117170033660)).

2024년 1월 CES 기사에는 손승배 씨가 "럭스로보 대표"로 인용됐다([전자신문](https://www.etnews.com/20240104000261)). 그는 2024년 2월 출원된 럭스로보 PCB 설계 특허 4건 모두에 발명자로 올라 있다([Google Patents](https://patents.google.com/patent/KR20250132817A/ko)). 직함이 어떻게 바뀌었는지는 확인하지 못했다. 랜딩페이지의 "MODI"는 이 교구 브랜드에서 온 이름이고, "초보자 친화"라는 포지셔닝도 교육 사업의 연장선에 있다.

투자는 2017년 카카오인베스트먼트·카카오브레인의 40억 원([파이낸셜뉴스](https://www.fnnews.com/news/201706071046598737))과 시리즈B 90억 원([벤처스퀘어](https://www.venturesquare.net/802751))을 거쳐, 2024년 5월 기준 누적 약 379억 원이다([이투데이](https://www.etoday.co.kr/news/view/2363460)). 2024년 4월에는 기술성 평가 A등급을 받고 삼성증권을 대표주관사로 정했다([메트로신문](https://www.metroseoul.co.kr/article/20240416500511)). 2024년 7월 코스닥 예비심사를 신청했지만 **2024년 10월 철회**했다.

철회 이후의 자금 조달은 기업가치 하락을 보여 준다. 2025년 10월 에이프로를 상대로 발행한 RCPS 3억 원은 전환가 24,500원, 기업가치 약 2,300억 원이었다. 그런데 2025년 12월 벤처펀드를 상대로 발행한 RCPS 30억 원은 **전환가 7,500원으로, 직전의 약 30% 수준**이었다. 같은 달 오상훈 대표가 보통주 약 30억 원어치를 인수했다. 차입금 80억 원은 2026년 4월부터 만기가 돌아온다. 최대주주는 오상훈(29.59%), 2대주주는 한화시스템(11.61%)이다([뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685)).

1차 조사의 매출 충돌은 DART 원문으로 풀렸다.

| 기준 | 2022년 | 2023년 | 2024년 | 2025년 | 근거 |
|---|---|---|---|---|---|
| 연결 매출 | 179.1억 원 | 242.8억 원 | — | — | [DART 연결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001142) (원문) |
| 연결 영업손실 | 118.1억 원 | 60.8억 원 | — | — | 같은 출처 |
| 별도 매출 | 103.5억 원 | 113.7억 원 | 49.4억 원 | 16.7억 원 | 2022~2023: [DART 별도](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001133) (원문). 2024~2025: [Wadiz](https://www.wadiz.io/maker/detail/1122379/makerInfo) (스니펫, 단위 추정) |
| 기타 보도 | — | — | TheVC 별도 49억·연결 66억 원(스니펫) | 뉴스톱 3분기 누적 12억 원(기준 불명) | [TheVC](https://thevc.kr/luxrobo); [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) |

2023년 매출 "114억 원 대 242억 원" 충돌은 **별도와 연결이라는 기준 차이**였다. 연결 매출의 절반가량은 종속기업 ㈜큐버(지분 50.57%, 유선 통신장비, 2023년 매출 117.9억 원)에서 나온다([DART](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001142)). 뉴스톱은 2022년 연결 수치와 2023년 별도 수치를 섞어 모두 "연결"이라고 썼다. 2024~2025년 감사보고서는 DART에 공시되지 않았다. Wadiz의 2023년 수치는 DART 별도 매출과 정확히 일치한다. 그래서 Wadiz의 2024~2025년 수치도 별도 기준으로 보는 것이 합리적이지만, 원문으로 검증하지는 못했다.

이 수치대로라면 **별도 매출은 2년 만에 7분의 1 수준으로 줄었다.** 2024년 5월 인터뷰에서 내건 "2026년 목표 매출 813억 원, 2027년 2,000억 원"([이투데이](https://www.etoday.co.kr/news/view/2363460))과는 거리가 멀다. 2026년 3월 언론은 럭스로보를 "교육용 IoT 모듈 기업에서 AI PCB 설계 자동화 플랫폼 기업으로" 전환 중인 회사로 소개했다([서울경제](https://www.sedaily.com/article/20019757)). 다운라운드와 차입금 만기를 함께 보면, 모디팩토리는 곁가지 사업이 아니라 회사의 생존이 걸린 사업이다.

### 랜딩페이지 약속은 원문으로 확인되지만, 회로도 필수와 300부품 한도라는 조건이 붙는다

| 랜딩페이지 문구 | 원문으로 확인한 실제 내용 | 근거 |
|---|---|---|
| 파일 업로드 | 회로도와 레이아웃 파일을 한 쌍으로 올린다(파일당 최대 100MB). 지원 형식은 Altium(.SchDoc+.PcbDoc, 2026-08-21 R2.3.0부터), KiCad 8.0 이상(.kicad_sch+.kicad_pcb), EasyEDA(.json 한 쌍), MODI Factory 자체 .json이다. OrCAD, Allegro, PADS는 지원하지 않는다. 업로드할 때 회로도·레이아웃 불일치, 보드 외곽 오류, 부품 겹침을 검사한다 | [앱 번들](https://workspace.modifactory.com/_next/static/chunks/447-3cbb73ad59de8403.js); [R2.3.0 공지](https://www.modifactory.com/news/ko/notice-004) |
| 90분 | 배치 평균 약 30분과 배선 약 60분 이내를 합친 시간이다. "PCB 밀도 및 서버 환경에 따라 달라질 수 있다"는 각주가 붙는다. 배치와 배선은 각각 하루 5회까지 실행할 수 있고, 매일 자정(KST)에 초기화된다 | [튜토리얼 ①](https://www.modifactory.com/blog/ko/tutorials-001); [튜토리얼 ②](https://www.modifactory.com/blog/ko/tutorials-002); [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js) |
| AI 설계안(설계 근거 포함) | 배치 결과로 후보 2~3개와 후보별 전체 코멘트가 나온다. 배치 노트(R2.4.0, 2026-09-07)는 디커플링 커패시터 거리(권장 8mm 이하)를 진단하고 IC·커넥터 접근성을 검증한다. 배선 노트(R2.2.0, 2026-07-09, 무료 베타)도 있다. 2026-04-29 이전 프로젝트에는 AI 코멘트가 지원되지 않는다 | [튜토리얼 ③](https://www.modifactory.com/blog/ko/tutorials-003); [modifactory.com/ko](https://www.modifactory.com/ko); [R2.2.0](https://www.modifactory.com/news/ko/notice-003); [R2.4.0](https://www.modifactory.com/news/ko/notice-005) |
| 회원가입만으로 즉시 시작 | 브라우저에 로그인하면 바로 쓸 수 있고 설치는 필요 없다. 얼리 액세스 기간에는 전 기능이 무료이며, "2026년 연말까지 전 기능 100% 무료" 이벤트(2026-09-14)가 진행 중이다 | [FAQ 번들](https://framerusercontent.com/sites/48gDNeWr5taVlAK00jZK02/TsGrrmNGW.QvdX1RoJ.mjs); [이벤트](https://www.modifactory.com/news/ko/event-001) |
| 초보자도 막힘없는 자동 설계 | 배치 방식은 "전체 재배치"와 "수동 소자만 배치" 중에서 고른다. 핵심 부품을 고정(Component Lock)한 뒤 나머지만 재계산할 수 있고, 웹 에디터로 손본 뒤 다시 배선할 수 있다(R2.3.0). 업로드 전에 Net 이름 일치와 KiCad ERC 무오류가 필요하다 | [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js); [튜토리얼 ①](https://www.modifactory.com/blog/ko/tutorials-001) |
| 다양한 포맷으로 출력 | KiCad(.kicad_pcb), Altium(.PcbDoc), EasyEDA(.json), MODI Factory(.zip), Gerber(.zip), PDF로 내보낼 수 있다. 내보내기는 **PCB만** 대상이고 회로도는 내보내지 않는다. ODB++, IPC-2581, STEP은 없다 | [레이아웃 번들](https://workspace.modifactory.com/_next/static/chunks/pages/layout/%5Bid%5D-d2890299c950859f.js); [튜토리얼 ④](https://www.modifactory.com/blog/ko/tutorials-004) |
| (랜딩페이지에 없음) 처리 한도 | 메인 부품 100개를 포함해 총 300개 부품, 와이어(연결) 1,200개, 보드 최대 200×200(단위 표기 없음, mm로 추정)까지 처리한다. 레이어 수 상한은 번들에서 찾지 못했다 | [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js) |

입출력 범위는 1차 조사에서 "Gerber만 확인"으로 적었던 것보다 넓다. 주요 저가·중급 EDA 세 종류를 받고, 같은 형식의 PCB 파일로 되돌려 준다. 그래서 "다양한 포맷"이라는 문구는 PCB 파일 기준으로는 사실이다. 다만 회로도 역출력, 제조용 ODB++와 IPC-2581, 기구 협업용 STEP, 그리고 OrCAD·Allegro·PADS와 KiCad 7 이하는 빠져 있다.

더 중요한 사실은 **AI 배치에 회로도가 반드시 필요하다**는 점이다. 튜토리얼 ⑤는 "회로도 없이 레이아웃 파일만으로도 자동 배치가 가능하도록 개발을 진행 중"이라고 밝힌다([튜토리얼 ⑤](https://www.modifactory.com/blog/ko/tutorials-005)). 모디팩토리의 "AI 설계안"은 요구사항을 받아 회로를 만들어 주는 결과물이 아니다. 이미 확정된 회로도, 보드 외곽, 풋프린트를 받아 **배치와 배선을 끝낸 레이아웃**을 돌려준다. 홈페이지는 "초보 개발자도 30분 이내 설계 시작"을 내세운다([modifactory.com/ko](https://www.modifactory.com/ko)). 그러나 ERC를 통과한 회로도와 레이아웃 파일을 직접 준비할 수 있는 사람만 그 30분에 들어설 수 있다.

블로그에는 JLCPCB 직구, 풋프린트 실수, 레이어 수 선택 같은 입문 글이 올라 있다([JLCPCB 직구 가이드](https://www.modifactory.com/blog/ko/jlcpcb-order-guide)). 홈페이지는 광운대 로봇학부 정규 실습 툴로 채택됐다고 밝힌다(업체 게재). 메이커와 교육 시장을 겨냥한다는 뜻이다.

Altium 쪽은 단계별로 진행 중이다. 파일 업로드는 2026년 8월부터 지원된다. Altium 안에서 도는 익스텐션은 2026년 9월 electronica India에서 처음 실시간 시연됐다([electronica India 후기](https://www.modifactory.com/blog/ko/electronica-india-2026)). 홈페이지는 이 익스텐션을 "2026 하반기 정식 지원 예정"으로 표기한다([modifactory.com/ko](https://www.modifactory.com/ko)). PM은 현재 모디팩토리를 "기존 EDA와 함께 사용하는 확장 기능"으로 규정하고, 내년에 자체 에디터를 열 계획이라고 밝혔다([PM Joe 인터뷰](https://www.modifactory.com/blog/ko/pm-joe-interview)).

### 엔진은 LLM이 주요 부품을, 점수 루프가 수동소자를 놓는 하이브리드다

모델 이름과 학습 데이터는 공개되지 않았다. 하지만 공식 블로그의 팀 인터뷰, 앱 번들, 채용공고를 겹쳐 보면 구조가 보인다.

**배치.** "MCU나 USB, 버튼처럼 용도와 사용자 맥락에 따라 위치가 정해지는 부품들은 LLM이 배치를 맡고, 저항이나 캐패시터 같은 보조 부품들은 정량 평가 루프가 처리"한다([배치 엔지니어 인터뷰](https://www.modifactory.com/blog/ko/autoplacer-engineer-interview)). 앱도 업로드 단계에서 부품을 "메인 부품"과 "서브 부품"으로 나눠 보여 준다. 채용공고는 "LLM 기반 PCB 메인 부품 자동 배치 모델"과 "PCB 배치 데이터셋 구축"을 업무로 적는다([ML/AI 엔지니어 공고](https://freehire.me/jobs/ml-ai-enjinieo-reogseurobo-7nzmi4uk)).

**배선.** 그래프 탐색, 조합 최적화, 휴리스틱과 메타휴리스틱으로 경로를 만든다. 강화학습과 GNN은 연구 과제로 남아 있다([PCB AI 라우터 공고](https://freehire.me/jobs/pcb-ai-rauteo-jadong-baeseon-algorijeum-reogseurobo-idiz63gn)).

**노트.** 배치 노트는 "단순 AI 텍스트 생성이 아니"다. 룰 엔진이 부품 분류, 거리, 판정 가능 여부를 정한 뒤 그 결과를 구조화해 보여 준다([튜토리얼 ⑥](https://www.modifactory.com/blog/ko/tutorials-006)).

**검증.** 배선 중에 최소 선폭, 부품 간 간격, 층간 규칙을 자동으로 적용한다. 회사는 이것을 "배선이 끝난 후 DRC를 별도로 돌릴 필요가 없는 이유"로 설명한다([튜토리얼 ②](https://www.modifactory.com/blog/ko/tutorials-002)). 열 시뮬레이터는 개발 중이다. AI 엔지니어 인터뷰에 따르면 상용 툴 대비 10~20배 빠르고 오차는 ±5°C 이내지만, "지금은 특정 PCB 조건에 맞춰 최적화된 상태"다. 전원 무결성과 신호 무결성은 "순서만 잡아 둔 상태"다([AI 엔지니어 인터뷰](https://www.modifactory.com/blog/ko/ai-ethan-interview)). 독립 DRC/DRS 기능은 "업데이트 예정"이다([기획 리드 인터뷰](https://www.modifactory.com/blog/ko/planning-lead-hazel-interview)).

**인프라.** 쿠버네티스 오퍼레이터와 메시지 큐로 작업을 스케줄링하고, 온프레미스 AI 서버를 AWS로 옮기는 중이다([백엔드 인터뷰](https://www.modifactory.com/blog/ko/be-rob-interview)).

LUXROBO GitHub 조직의 공개 저장소 36개 가운데 PCB나 EDA 관련 저장소는 하나도 없고, 공개 API나 SDK 문서도 없다([GitHub LUXROBO](https://github.com/orgs/LUXROBO/repositories?type=all&sort=updated); [사이트맵](https://www.modifactory.com/sitemap.xml)).

이 구조는 2024년 CES 때의 구상에서 크게 좁혀진 것이다. CES 2024의 알파버전은 "AI 챗봇 GPT-4를 접목해 … 회로 부품을 추천"하는 올인원 플랫폼이었다([전자신문](https://www.etnews.com/20240104000261)). 배치 엔지니어도 초기에는 블록 다이어그램에서 회로도를 만들고 부품 DB와 공급망까지 연결하려 했다가 배치·배선으로 범위를 줄였다고 말한다. 그 흔적은 2024년 2월 29일 출원돼 2025년 9월 공개된 특허 4건에 남아 있다.

| 출원 | 제목 | 핵심 청구 내용 |
|---|---|---|
| [KR20250132817A](https://patents.google.com/patent/KR20250132817A/ko) | 부품 배치 최적화 서버 | 부품 특징점과 연결 특징점을 AI 모델 안의 **스코어링 모델**에 넣고, 랜덤 배열에 따라 추천 레이아웃을 출력 |
| [KR20250132825A](https://patents.google.com/patent/KR20250132825A/ko) | 전자기판 상의 부품 배치 시스템 | 기존 제품 기판 DB로 학습한 모델로 유사 설계를 고른 뒤 배열, 챗봇 입력 |
| [KR20250133044A](https://patents.google.com/patent/KR20250133044A/ko) | 회로 자동 설계 서버 | LLM 기반 자연어 입력에서 부품, 연결, 레이아웃을 차례로 결정 |
| [KR20250132824A](https://patents.google.com/patent/KR20250132824A/ko) | 제품 카테고리 제공 시스템 | 부품 정보로 설계 제품 카테고리와 신뢰도를 추정 |

2026년 7월에는 「부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법」 특허로 2026 대한민국 우수특허대상을 받았다. 기사 원문은 이 특허를 "MODI Factory의 핵심 표준화 엔진"으로 소개한다. 배선 전의 가상 연결선(에어와이어)에서 길이·밀집도·교차 특징을 뽑아 "표준 JSON·벡터 형태로 정형화"하고, 이를 바탕으로 배치와 배선 경로를 미리 최적화한다. 기사는 이 특허를 포함한 연관 특허 7건이 하나의 설계자동화 파이프라인을 이룬다고 설명한다([네이트뉴스 2026-07-21](https://m.news.nate.com/view/20260721n00645)). 수상 특허의 번호와 청구항은 KIPRIS 타임아웃 때문에 확인하지 못했고, Google Patents에도 색인되지 않았다.

국가 R&D 과제명은 처음으로 확인됐다. 중소벤처기업부 **글로벌 팁스 「AI 기반 하이브리드 PCB 설계 공정 통합 시스템 개발」**(2026~)이다. 럭스로보 컨소시엄과 연세대가 함께 수행하고, 강원대 연구실이 PCB 신호무결성 수치해석 엔진을 맡는다([강원대 ACE Lab 저장소](https://github.com/acelab24/acelab24.github.io)). 금액은 확인하지 못했다.

여기서 추론 하나를 덧붙인다. 하이브리드 분업은 LLM의 약점을 피하는 설계로 읽힌다. LLM에는 "USB는 가장자리에" 같은 의미 판단만 맡기고, 기하 최적화는 점수 루프에 맡긴다. 2026년 벤치마크가 지적한 LLM의 공간 추론 약점(2절)과도 맞는 선택이다. 다만 LLM이 좌표를 어떻게 내는지, 점수 함수가 무엇인지는 공개되지 않았다.

### 이용약관은 FAQ와 달리 업로드 파일의 R&D 활용과 생성 레이아웃의 회사 귀속을 규정한다

FAQ와 홈페이지는 이렇게 약속한다. "업로드된 프로젝트 파일은 고객의 명시적 동의 없이 AI 학습용으로 사용되지 않습니다", "AI 무단 학습 차단", "ISO/IEC 27001 인증을 받은 보안 환경"([FAQ 번들](https://framerusercontent.com/sites/48gDNeWr5taVlAK00jZK02/TsGrrmNGW.QvdX1RoJ.mjs); [modifactory.com/ko](https://www.modifactory.com/ko)).

그러나 2026년 2월 27일 시행된 **이용약관 원문은 다르게 규정한다**([이용약관](https://workspace.modifactory.com/terms)). 차이는 세 가지다.

첫째는 업로드 원본의 활용이다(제18조 7항). 회원은 가입하면서 회사가 업로드 원본 파일을 "연구·개발, 알고리즘 고도화, 성능 개선"에 쓰는 데 동의하게 된다. 조건은 비식별 처리와 필요 범위 제한이다.

둘째는 AI 학습이다(제19조). 활용 대상에는 "회원이 업로드한 원본 파일 및 그로부터 파생되는 데이터가 포함"된다. AI 산출물과 중간 데이터, 메타데이터는 비식별화해 "AI 모델의 학습, 검증 및 개선"에 쓸 수 있다.

셋째는 생성 레이아웃의 권리다(제18조). 원본의 저작권은 회원에게 남는다. 하지만 **자동 생성된 설계 결과의 저작권과 일체의 지식재산권은 회사에 귀속**된다. 회원은 상업적 이용·제조·판매가 가능한 비독점·영구·무상 이용권만 받고, "제3자에게 이용하게 하거나 실시권을 부여할 권한"은 받지 못한다.

결국 FAQ가 말하는 "명시적 동의"는 가입 시 약관 동의로 갈음되는 구조다. 약관에는 다른 제약도 있다. 제21조는 AI 산출물이 "실제 제조, 양산 … 사용을 보장하지 않"는다고 적는다. 개인정보처리방침은 클라우드 수탁사를 명시하지 않는데, 회사는 AWS로 이전 중이다. ISO 27001 인증의 주체(럭스로보인지 클라우드 사업자인지)와 범위도 확인되지 않는다.

이 조항들은 2027년 이후 B2B 판매에 직접 걸리는 문제다(추론). 고객사 설계를 대신 맡는 외주 설계사는 생성 레이아웃을 고객에게 넘기는 것 자체가 "제3자 실시권 부여"에 해당할 수 있다. 사내 IP 정책이 있는 기업도 생성물의 IP가 서비스 업체에 귀속되는 구조를 받아들이기 어렵다.

### '글로벌 톱3'는 수상이 아니라 최종 후보 3곳 중 하나였다

| 시점 | 사건 | 근거 |
|---|---|---|
| 2014-11 | 럭스로보 설립(13일 또는 14일) | [TheVC](https://thevc.kr/luxrobo); [DART](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001142) |
| 2022년~ | 모디팩토리 자체 개발 시작 | [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) |
| 2024-01-04 | CES 2024에서 GPT-4 기반 알파버전 공개 | [전자신문](https://www.etnews.com/20240104000261) |
| 2024-02-29 | 배치·회로 자동설계 특허 4건 출원(2025-09 공개, 심사 중) | [Google Patents](https://patents.google.com/patent/KR20250132817A/ko) |
| 2024-07 / 2024-10 | 코스닥 예비심사 신청 / 철회 | [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) |
| 2025-12 | 직전의 약 30% 전환가로 RCPS 30억 원 발행 | [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) |
| 2026-01-08 | "올해 유료 매출 5억 원, 유저 1만 명 목표" 보도 | [뉴스토마토](http://www.newstomato.com/readnews.aspx?no=1287248) |
| 2026-02-23 | embedded award Tools 부문 후보 3곳 발표(MODI Factory, Ambiq HeliaAOT, Parasoft C/C++test CT) | [embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/02/tools-nominees) |
| 2026-03-06 | 첫 공개 릴리스("MODI Factory가 시작합니다"). 3-09에 하루 실행 횟수 제한 도입 | [notice-001](https://www.modifactory.com/news/ko/notice-001); [notice-002](https://www.modifactory.com/news/ko/notice-002) |
| 2026-03-10 | 시상식. Tools 부문 수상작은 Ambiq HeliaAOT | [embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/03/winner-embedded-awrd-2026) |
| 2026-07-09 / 08-21 / 09-07 | R2.2.0 배선 노트 / R2.3.0 수동 편집·Altium 파일 / R2.4.0 배치 노트 | [notice-003](https://www.modifactory.com/news/ko/notice-003); [notice-004](https://www.modifactory.com/news/ko/notice-004); [notice-005](https://www.modifactory.com/news/ko/notice-005) |
| 2026-07-21 | 2026 우수특허대상(에어와이어 특허) | [네이트뉴스](https://m.news.nate.com/view/20260721n00645) |
| 2026-09-14 | "2026년 연말까지 전 기능 100% 무료" 이벤트 | [event-001](https://www.modifactory.com/news/ko/event-001) |
| 2026-09-16~18 | electronica India에서 Altium 익스텐션 첫 실시간 시연 | [블로그](https://www.modifactory.com/blog/ko/electronica-india-2026) |
| 2026~ | 글로벌 팁스 과제 수행 중. Altium 익스텐션은 2026 하반기 정식 지원 예정 | [ACE Lab](https://github.com/acelab24/acelab24.github.io); [modifactory.com/ko](https://www.modifactory.com/ko) |

국내 보도는 모디팩토리가 "Embedded World 2026 설계 자동화 부문 글로벌 톱3, 아시아 기업 중 유일"이라고 전했다. 서울경제와 뉴스토마토는 여기서 더 나가 "**2위에 해당하는 성적**"이라고 썼고, 사진 설명에는 "수상 후"라는 표현까지 붙였다([서울경제](https://www.sedaily.com/article/20019757); [뉴스토마토](https://www.newstomato.com/ReadNews.aspx?no=1294739)). 주최 측은 순위를 발표하지 않았다. Tools 부문 **수상작은 Ambiq Micro의 HeliaAOT**였다([embedded-world.de 수상작](https://www.embedded-world.de/en/knowledge/2026/03/winner-embedded-awrd-2026)). 럭스로보 PM도 "아쉽게도 최종 선정되지는 못했지만 … Tool 분야에서 EDA 관련 툴로는 저희가 최초"라고 밝혔다([PM Joe 인터뷰](https://www.modifactory.com/blog/ko/pm-joe-interview)). 정확한 표현은 "**최종 후보(nominee) 3곳 중 하나, 수상 실패**"다. "2위"와 "수상"은 근거가 없다.

같은 시기 보도된 **알티움·지멘스EDA·케이던스 협업은 회사가 밝힌 계획**이다. 2026년 11월 현재 이들 회사는 물론 JLCPCB나 국내 PCB 제조사와의 공식 제휴 공지도 사이트에 없다. 미국 베타의 실체도 찾지 못했다. CES 혁신상은 MODI 교구 시절의 이력이다.

현재 상태는 얼리 액세스다. 정식 출시일은 공지되지 않았다. FAQ는 "정식 출시 시 유료 플랜이 도입될 예정"이라고만 밝힌다. 앱에는 이미 "크레딧 추가 구매"와 "플랜 업그레이드" 문구가 들어 있지만 가격표는 없다([_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js)). 실제 가입자 수와 기업 고객 수도 공개되지 않았다. 2026년 1월에 내건 "유료 매출 5억 원" 목표는 연말까지 전 기능을 무료로 풀면서 사실상 달성이 어려워졌다(추론).

**독립 사용자 후기는 0건이다.** Hacker News와 KiCad 포럼에서 "MODI Factory"를 검색하면 결과가 없고, 국내 검색 결과도 보도자료와 공식 블로그뿐이다([HN 검색](https://hn.algolia.com/api/v1/search?query=%22MODI%20Factory%22); [KiCad 포럼 검색](https://forum.kicad.info/search.json?q=modifactory)). 공식 추천사는 한국어판과 영어판이 서로 맞지 않는다. 한국어판은 Altium 플러그인 연동을 "기대된다"고 쓰고, 같은 자리의 영어판은 Altium 패널 안에서 돌리는 것이 "작업 방식을 바꿨다"고 쓴다([modifactory.com/ko](https://www.modifactory.com/ko); [modifactory.com](https://www.modifactory.com/)).

성능 수치는 모두 회사 주장이다. "16시간 걸리던 수작업 레이아웃을 60분에 완료", "4년차 엔지니어급 품질" 같은 문구가 있다. 배치 엔지니어는 양산 보드 4종에서 상용 자동 배치 툴과 범용 LLM 기준선을 비교했더니 "설계 의도 명세를 만족시킨 건 모디팩토리뿐"이었고 보드당 3~12분이 걸렸다고 말한다. 다만 비교 툴의 이름과 보드 사양은 공개하지 않았다([배치 엔지니어 인터뷰](https://www.modifactory.com/blog/ko/autoplacer-engineer-interview)). 회사도 한계를 인정한다. 공지에서는 "아직 완벽하진 않습니다"라고 했고, 튜토리얼에서는 "어떨 때는 결과가 깔끔하고 어떨 때는 아쉬워요"라고 썼다([notice-001](https://www.modifactory.com/news/ko/notice-001); [튜토리얼 ④](https://www.modifactory.com/blog/ko/tutorials-004)).

## 2. 학계는 보드 레벨 AI 레이아웃을 아직 '전문가 검토용 초안'으로 본다

ML·LLM for EDA 서베이는 대부분 칩 설계 흐름이 중심이고 PCB는 거의 다루지 않는다([arXiv 2102.03357](https://arxiv.org/abs/2102.03357v2); [arXiv 2501.09655](https://arxiv.org/pdf/2501.09655)). PCB 생애주기 전체를 다룬 첫 생성형 AI 서베이는 Srinivasan·Turnbull·Pearce의 논문이다(arXiv:2606.17074, 2026-06-10 제출, 심사 중). 이 서베이는 **도메인 특화 데이터의 부족과 기존 PCB 도구와의 통합 부족**을 핵심 장애물로 꼽는다([arXiv](https://arxiv.org/abs/2606.17074)).

같은 저자 그룹은 같은 날 PCB-QA도 제출했다. 오픈소스 하드웨어 8개에서 뽑은 QA 480쌍으로 LLM을 평가한 결과, PCB 정보를 JSON 텍스트로 주었을 때 Gemini 3 Flash Preview가 93% 정확도를 냈다([arXiv 2606.23704](https://arxiv.org/abs/2606.23704)). 기존 Altium·KiCad·EasyEDA 파일을 받아 처리하는 모디팩토리의 구조는 서베이가 말한 "통합 부족"을 겨냥한다.

### 배치는 GPU 해석적 기법과 사전학습 강화학습이 가장 앞서 있다

보드 레벨 배치에서 가장 성숙한 접근은 두 갈래다.

첫째는 강화학습(RL) 정책을 오프라인으로 학습한 뒤 새 회로에 일반화하는 방식이다. 몰타대 Vassallo와 Bajada(DATE 2024)는 학습에 쓰지 않은 회로에서 라우팅 후 배선 길이를 SA(simulated annealing) 대비 TD3 정책으로 **17%, SAC 정책으로 21%** 줄였다. 배치 수렴도 빨라졌다([UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782); [GitHub RL_PCB, MIT](https://github.com/LukeVassallo/RL_PCB)).

둘째는 VLSI의 해석적 배치를 GPU로 가속해 PCB에 옮기는 방식이다. Cornell과 NVIDIA의 **Cypress(ISPD 2025 최우수논문)**는 routability를 1~5.9배 높였고, 완전 배선된 설계의 트랙 길이를 1~19.7배 줄였으며, 런타임을 **최대 492.3배** 단축했다([Cypress 논문](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf); [GitHub](https://github.com/NVlabs/Cypress)).

Cypress의 비교 기준선에는 상용 Quilter(2024년 4월 버전)도 들어 있었다. routability는 FreeRouting v1.9.0으로 쟀다. 논문은 당시 Quilter가 부품 176개 설계에 2.6시간이 걸렸고, 지원 범위가 핀 1,000개, 부품 100개, 밀도 10%, 500 MHz, 2 A 미만이었다고 적는다. 업로드형 상용 서비스들의 처리 한도는 소·중형 보드에 몰려 있다. 2024년 Quilter는 부품 100개, DeepPCB 종량제는 airwire 1,200개, 모디팩토리는 부품 300개·연결 1,200개다.

LLM을 배치에 쓰는 연구도 나왔다. CUHK 등의 ModuPlace는 LLM을 미세조정하고 선호 최적화해 모듈 단위 **제약 그래프**를 생성하게 한다. LLM이 좌표가 아니라 제약을 만든다는 점이 핵심이다([ModuPlace PDF](https://yhhan.com/PDFs/ModuPlace_paper.pdf), DAC 2026 게재는 미확인). A*STAR의 Lim(2026)은 주 부품을 중앙에 고정하고 수동소자를 전원 핀 근처에 두는 원칙으로, 실제 PCB 9개 이상에서 "사람에 가까운" 배치를 얻었다([arXiv 2602.23540](https://arxiv.org/abs/2602.23540)).

칩 분야의 AlphaChip(Nature 2021)은 재현 논쟁에 걸려 있다. UCSD의 Cheng·Kahng 외 비판 논문은 "An Updated Assessment of Reinforcement Learning for Macro Placement"라는 제목으로 IEEE TCAD에 실렸다. 결론은 강화한 SA가 사전학습된 AlphaChip보다 여전히 우수하다는 것이고, 익명 심사위원과 다른 연구 그룹이 이 결과를 재현했다([arXiv 2302.11014](https://arxiv.org/abs/2302.11014); [MacroPlacement](https://github.com/TILOS-AI-Institute/MacroPlacement)). Google 측은 반박을 이어 가고 있다([arXiv 2411.10053](https://arxiv.org/abs/2411.10053v1)). PCB 서비스가 얻을 교훈은 분명하다. **"AI라서 더 낫다"는 주장은 강한 SA나 상용 기준선과 공개 벤치마크로 비교하기 전까지 마케팅에 쓰면 안 된다.**

처리 시간에 관해서는 국내 비ML 연구가 참고가 된다. 연세대 석사논문의 규칙·점수 기반 수동소자 배치는 IoT 보드 7종에서 **설계당 10초 이내**에 끝났고, KiCad 대비 배선 길이를 평균 16% 줄였다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=6656cc9e3edaf0faffe0bdc3ef48d419)). 소형 보드 배치 자체는 분 단위 미만으로도 가능하다는 뜻이다. 모디팩토리의 "평균 30분"에는 LLM 호출, 후보 생성, 작업 대기열이 포함됐을 가능성이 높다(추론). 회사 엔지니어가 말한 "보드당 3~12분"과 튜토리얼의 "평균 30분" 사이에 차이가 나는 것도 이렇게 설명된다.

### 학습형 라우터는 소형 보드에서 규칙 기반을 따라잡았지만 대형 보드에서는 뒤처진다

PCB 배선의 학습 기반 연구는 오랫동안 부분 문제에 머물렀다. FanoutNet(AAAI 2023)은 팬아웃을 PPO로 자동화했지만 공식 코드가 없다([AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26030)). Unet-Astar(IEEE Access 2023)는 A* 탐색 영역을 딥러닝으로 추천하는데, 저장소에는 "코드는 논문 채택 후 제공"이라는 문구만 있고 **코드는 공개되지 않았다**([GitHub](https://github.com/Firesuiry/Unet-Astar-For-PCB-Routing)).

이후 연구 범위가 넓어졌다. GPT 계열로 배선하는 GPCB Routing(IEEE TCAD 2025)과, freerouting.jar를 강화학습 환경으로 감싼 월드모델 RL(Expert Systems with Applications 2026, 코드 공개)이 나왔다([CADET 참고문헌](https://github.com/LGAI-Research/CADET/blob/main/CADET.pdf); [dreamer-Autorouting](https://github.com/yinqimakeitfun/dreamer-Autorouting)).

판도를 보여 준 것은 **LG AI연구원**의 연구다. **PCBWorld**(arXiv 2607.05915, KDD 2026 워크숍)는 KiCad 엔진 위에 만든 배선 환경으로, 실보드 679개와 엔진이 채점하는 지표 8개를 갖췄다. 초록은 "학습 기반 방법이 아직 규칙 기반 라우터에 뒤처진다"는 문제의식에서 출발한다. 그러나 실험 결과는 더 미묘하다. 소형 실보드 99개(D3-A)에서 완료율은 PPO 0.86, Freerouting 0.80, KiCad 라우팅 도구 0.74, GPT-5.4 에이전트 0.65 순이었다. 본문 결론은 "**PPO가 소형 보드에서는 모든 기준선을 능가했지만, 대형 보드에서는 가장 강한 규칙 기반 라우터에 뒤처졌다**"다([arXiv](https://arxiv.org/abs/2607.05915); [README](https://github.com/LGAI-Research/PCBWorld)).

후속 연구 **CADET**(arXiv 2611.16913)은 합성 시연 보드 10만 개로 행동 복제를 한 뒤 RL로 미세조정했다. 실제 테스트 보드에서 DRV 없는 완료율을 RL-only 기준선의 38.0%에서 **67.2%로** 올렸다. 이는 **FreeRouting(65.6%)과 비슷한 수준**이며, 보드당 시간은 15.5초로 FreeRouting(45.6초)보다 짧다. 세 번 시도하면 79.8%까지 오른다([arXiv](https://arxiv.org/abs/2611.16913); [README](https://github.com/LGAI-Research/CADET)).

2026년 11월에 나온 **PCBRouteAgent**는 LLM이 연결 토폴로지·순서·통로·레이어 전환을 계획하고 KiCad 엔진이 실행하는 구조다. PCBWorld-Bench 247개 보드에서 D3-A 클린패스 94.9%를 냈지만, 대형 보드 분할(D3-C)에서는 40%에 그쳤다([arXiv 2611.08175](https://arxiv.org/abs/2611.08175)).

종합하면 **소형 보드에서는 학습형·LLM 라우팅이 Freerouting을 따라잡았고, 남은 격차는 대형 보드에 있다.** 모디팩토리의 처리 한도(300부품)는 바로 이 소형 구간 안에 있다. 그렇다면 모디팩토리의 휴리스틱·메타휴리스틱 라우터와 이 학술 엔진들을 같은 보드에서 비교할 수 있다(추론).

고속 신호와 차동쌍은 여전히 ML이 다루지 못한 영역이다. 비ML 연구로는 차동쌍을 포함한 통합 PCB 라우팅(ASP-DAC 2021)과 아주대의 ILP 이스케이프 라우팅이 있다([PCBWorld 참고문헌](https://github.com/LGAI-Research/PCBWorld/blob/main/PCBWorld.pdf); [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=ef3a59ff65a9a9c6ffe0bdc3ef48d419)).

### 2026년 벤치마크는 'DRC 통과'와 '실제 동작' 사이의 큰 간극을 드러냈다

2026년에 나온 PCB 벤치마크들은 일관되게 비관적이다(모두 원문 확인).

- **EDA Bench(ICML 2026):** 가장 강한 하네스가 35개 과제 중 21개를 빌드했지만 종합 점수는 **4.58%**였다. 저자들은 결과물이 "파싱되고 그럴듯해 보여도 전기적으로 동작하지 않는다"고 결론지었다([ICML](https://icml.cc/virtual/2026/77908)).
- **PCB Gym(NeurIPS 2026):** 프런티어 LLM이 DRC를 통과하고 완전 배선된 보드를 낸 비율은 **32.1%**였다. 전원 레일을 신호 넷처럼 다루는 실수가 잦았다([NeurIPS](https://neurips.cc/virtual/2026/161602)).
- **PCBInnoBench(NeurIPS 2026):** 최고 에이전트의 Pass@1이 전문가 가이드가 있을 때 22.0%, 없을 때 7.3%였다([NeurIPS](https://neurips.cc/virtual/2026/poster/139034)).
- **PCB-Bench(ICLR 2026, 실제 프로젝트 174개):** LLM의 공간 배치 추론과 제약 준수가 약하다고 보고했다. 모델별 점수는 OpenReview가 막혀 확인하지 못했다([프로젝트 페이지](https://digailab.github.io/PCB-Bench/)).
- **OmniLayout(산업급 레이아웃 1,681개)과 라우팅판 OmniRouting:** 기하 추론과 경로 계획이 약하다고 보고했다([arXiv 2607.03261](https://arxiv.org/abs/2607.03261); [arXiv 2608.04434](https://arxiv.org/abs/2608.04434)).

이 결과는 모디팩토리의 품질 주장을 읽는 기준이 된다. 회사는 배선 중 규칙 적용으로 "DRC를 따로 돌릴 필요가 없다"고 말하지만, DRC 통과는 출발점일 뿐이다. ERC, 전원 무결성, 기능 검사를 함께 봐야 한다.

회로도 생성 쪽은 성과가 낫지만 과제가 단순할 때로 한정된다.

- **pcbGPT:** 임베디드 과제 20개에서 pass@1 0.90을 냈다(hard 0.72). 그래도 저자들은 "전문가 리뷰를 대체할 만큼 신뢰할 수 없다"고 결론지었다([arXiv 2606.01188](https://arxiv.org/abs/2606.01188)).
- **SchGen:** KiCad 회로도를 생성하는 코드를 출력하는 방식으로 유효 회로율 82%, 전문가 검증 기능 정확도 60.5%를 냈다. 원시 KiCad 파일을 직접 생성한 기준선의 유효 회로율은 32%에 그쳤다([arXiv HTML](https://arxiv.org/html/2605.30345v1)).
- **PCBSchemaGen:** 판본 충돌이 풀렸다. NeurIPS 2026 판(v2)은 2개 벤치마크의 227개 과제로 평가했고, Gemma-4-31B가 PCBBench 62개 과제의 **81.3%**를 통과했다([arXiv v2](https://arxiv.org/abs/2602.00510v2)). DOE 리뷰 슬라이드의 "65개 과제 77.5%"는 어느 원문 판본과도 맞지 않으므로 쓰지 않는다.
- **CircuitLM(IEEE ICLAD 2026 채택):** 부품 지식베이스와 5단계 파이프라인을 결정론적 ERC 엔진과 LLM 심사로 이중 평가했다([arXiv 2601.04505](https://arxiv.org/abs/2601.04505)).
- **HWE-Bench:** 실보드 수준 과제 300개에서 최고 통과율이 **8.15%**였다(원문 확인, 저자 Qiu·Xiao·Pan, [arXiv 2603.18102](https://arxiv.org/abs/2603.18102)).

성공한 시스템의 공통점은 **코드나 DSL 같은 중간표현과 결정론적 검증기 루프**다.

상용 서비스가 학술 자산을 쓰려면 라이선스도 따져야 한다. PCBWorld·CADET의 학습 체크포인트는 **EXAONE 비상업 라이선스**여서 체크포인트와 그 출력 모두 상업적으로 쓸 수 없다. PCBSchemaGen v2 코드는 **PolyForm Noncommercial**이다. OmniLayout 데이터셋은 출처별 라이선스 검토를 위해 **배포가 철회**됐다([PCBWorld README](https://github.com/LGAI-Research/PCBWorld); [PCBSchemaGen v2](https://github.com/HZou9/PCBSchemaGen_v2); [OmniLayout](https://github.com/AAAAAiden/OmniLayout-Benchmark)). 반면 RL_PCB와 SchGen 코드(MIT)와 PCBWorld 환경 코드(BSD-3)는 비교적 자유롭다. 다만 PCBWorld 엔진은 GPLv3다. 요약하면, 가장 강한 공개 모델은 상업 서비스에 바로 들어갈 수 없고, 평가 환경만 쓸 수 있다.

### 설계 근거를 다루는 연구는 비어 있어 기회이자 검증 공백이다

EDA 분야의 설명가능성(XAI) 연구는 매우 적다. 가장 직접적인 선례는 칩의 DRC 핫스팟 예측을 SHAP으로 설명한 Zeng 외(DATE 2020)다([DATE 2020](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)). PCB 배치·배선 결정을 설명하는 전용 연구는 보충 조사에서도 찾지 못했다. LLM이 생성한 설계 근거의 환각을 평가한 연구도 없다.

최근 흐름은 LLM 서술 자체보다 검증 가능한 근거에 기댄다. AllSpice의 **DRCY**(arXiv 2603.15672)는 데이터시트를 자동으로 가져와 핀 단위로 분석하는 5-에이전트 파이프라인이다. 여러 번 실행해 합의를 내는 방식(multi-run consensus)으로 신뢰도를 높인다([arXiv](https://arxiv.org/abs/2603.15672)). 1차 조사에서 인용한 "리뷰 11건에서 실제 이슈 4건, DDR5 주입 오류 100% 검출"은 논문에는 없고 **벤더 블로그에만 있는 수치**다([AllSpice 블로그](https://www.allspice.io/post/how-hardware-engineering-teams-evaluate-drcy)). PCBSchemaGen v2의 5층 검증기는 **핀 단위 오류 위치**를 알려 준다([arXiv v2](https://arxiv.org/abs/2602.00510v2)).

이 문헌들을 종합하면 신뢰할 수 있는 설계 근거는 세 층으로 쌓아야 한다. 첫째 층은 결정론적 측정값(DRC, ERC, 넷 길이, 혼잡도)이고, 둘째 층은 데이터시트와 설계 규칙의 인용이다. LLM의 자연어 서술은 그 위의 셋째 층이어야 하며, 앞의 두 층에 없는 주장을 하지 못하게 막아야 한다.

모디팩토리의 배치 노트는 룰 엔진의 판정을 구조화해 보여 준다고 밝혔다. 그러니 첫째·둘째 층을 갖춘 셈이다. 남은 문제는 두 가지다. 판정 기준과 수치를 사용자에게 얼마나 공개하는지, 그리고 LLM 문장이 판정 밖으로 나가지 못하도록 막는 장치가 있는지다.

### 국내 연구는 2024~2025년 보드 레벨로 내려왔지만 학술지 논문은 아직 없다

RISS 원문 레코드로 다시 확인했다. "국내에는 보드 레벨 AI PCB 학위논문이 사실상 없다"던 1차 결론은 **부분적으로 고쳐야 한다.** 2024~2025년에 보드 레벨 연구가 나타났다.

- **LLM+RL 배치(연세대):** 최성우·이충용의 「전자 회로 설계를 위한 PCB 부품 자동 배치 시스템」(대한전자공학회 학술대회 2024.11)은 센서·IC 같은 주요 부품은 **LLM 기반 모듈**로, 저항·커패시터는 **RL 기반 모듈**로 배치한다. 대상은 코딩 교육·메이커·비전문가다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=1bbed88c8b28d298d18150b21a227875)).
- **보드 레벨 디캡 RL:** 성균관대 옥기훈 석사논문(2025.2)은 여러 부하가 있는 PCB 전력전달망에서 Double DQN으로 디캡 종류와 포트를 고른다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=c7a362e1fb76b395ffe0bdc3ef48d419)). KAIST 강형민 박사논문(2025)의 주제어는 PCB와 강화학습이고, 김경묵 석사논문(2025)은 DDR5 PDN을 RL로 설계한다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=240b9d5e4445a07cffe0bdc3ef48d419); [RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=17d971b24de8ec09ffe0bdc3ef48d419)).
- **비ML 최적화:** 아주대 조범근 박사논문(2025.2)과 전자공학회논문지 62(1)은 차동쌍을 포함한 다층 이스케이프 라우팅을 ILP로 푼다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=25244f2f4a38ac1eb7998d826d417196)). ㈜티에스이 등의 GPU 휴리스틱 배치(멀티미디어학회논문지 29(8), 2026)는 부품 4,356개 중 98.83%를 배치했다([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=2fc2e7a24ce235f07ecd42904f0c5d65)).
- **생성형 AI 설계 검증:** 2025년 한국산학기술학회 포스터는 피에이치에이 H/W설계팀의 사례로, 생성형 AI와 파이썬으로 테스트 포인트 누락과 디캡 거리를 검사했다([KAIS 포스터](https://www.kais99.org/jkais/springNfall/spring2025/poster/2025_spring_227.pdf)).

그래도 **ML이나 LLM으로 일반 보드의 배치·배선을 다룬 학술지 논문은 0건이고, LLM 회로도 생성 국내 논문도 0건**이다. 위 학술지들의 KCI 등재 여부는 직접 확인하지 못했다.

국제 수준의 기여는 여전히 두 곳에 있다. **KAIST TeraLab(김정호 교수)**은 SI/PI 지표를 보상으로 쓰는 패키지·HBM 디캡 RL을 이어 왔다. DevFormer(ICML 2023)는 디캡 부품 수를 30% 이상 줄였고, 신태인 박사는 DesignCon 2025 Best Paper를 받았다([arXiv](https://arxiv.org/abs/2205.13225); [KAIST EE 뉴스](https://ee.kaist.ac.kr/en/research-achieve/dr-taein-shin-from-professor-jeongho-kims-research-lab-selected-for-best-paper-award-at-designcon-2025-international-conference/)). 이 흐름은 2026년 7월 KiCad MCP 기반 패키지 설계 에이전트 워크숍으로 이어졌다([Korea Times](https://www.koreatimes.co.kr/amp/southkorea/education/20260702/kaist-workshop-to-showcase-ai-agents-for-hbm-design-automation)). KAIST 2019·2023 석사논문은 저장소 접속에 실패해 아직 스니펫 수준이다. **LG AI연구원**은 PCBWorld와 CADET으로 국제 표준 평가 환경을 만들었고, 외부 연구(PCBRouteAgent)가 이미 이 환경을 쓰기 시작했다.

모디팩토리와 국내 학계의 관계는 생각보다 가까울 수 있다. 연세대 2024년 논문의 구조는 모디팩토리 엔진과 거의 같다. 주요 부품은 LLM이, 수동소자는 RL·점수 루프가 맡고, 대상도 교육·메이커다. 글로벌 팁스 과제에는 연세대가 공동 참여한다. 따라서 모디팩토리와 가장 가까운 국내 학술 선행연구가 같은 산학 협력권에서 나왔을 가능성이 있다(추론, 기관 수준의 정황). 그래도 4쪽짜리 학술대회 논문이라 동료심사 학술지 수준의 검증은 아니다.

특허 쪽에서는 럭스로보의 공개 출원 4건과 수상 특허가 국내 "AI PCB 설계" 특허의 사실상 전부다. 이름이 비슷한 KR102208989B1은 Google의 디바이스 배치 특허로, PCB와는 관련이 없다([Google Patents](https://patents.google.com/patent/KR102208989B1/enExample)). 국가 R&D의 설계 AI 예산은 여전히 칩에 몰려 있다([머니투데이](https://www.mt.co.kr/economy/2026/06/15/2026061509331190266)). PCB를 명시한 과제로는 모디팩토리의 글로벌 팁스 과제가 처음 확인됐다.

| 주제 | 대표 연구 | 핵심 결과(원문 확인) | 모디팩토리에 대한 함의 |
|---|---|---|---|
| 배치: 강화학습 | Vassallo & Bajada, DATE 2024 ([UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)) | SA 대비 라우팅 후 배선 길이 17~21% 감소 | 사전학습 정책은 추론이 빨라 분 단위 처리에 유리 |
| 배치: GPU 해석적 | Cypress, ISPD 2025 최우수논문 ([PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)) | routability 1~5.9배, 최대 492.3배 가속. Quilter(2024)를 기준선에 포함 | 빠른 1차 엔진과 공개 비교의 본보기 |
| 배치: LLM 활용 | ModuPlace ([PDF](https://yhhan.com/PDFs/ModuPlace_paper.pdf)), 연세대 2024 ([RISS](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=1a0202e37d52c72d&control_no=1bbed88c8b28d298d18150b21a227875)) | LLM이 제약 그래프나 주요 부품 배치를 맡고 기하는 최적화기가 처리 | 모디팩토리 하이브리드 구조의 학술적 근거 |
| 칩 배치 재현 논쟁 | Cheng 외, IEEE TCAD ([arXiv](https://arxiv.org/abs/2302.11014)) | 강화 SA가 사전학습 AlphaChip보다 우수, 제3자 재현 | 강한 기준선 없는 "AI 우위" 주장은 위험 |
| 배선: 학습형 vs 규칙 기반 | PCBWorld, CADET (LG AI연구원) ([arXiv](https://arxiv.org/abs/2607.05915); [arXiv](https://arxiv.org/abs/2611.16913)) | 소형 보드 PPO 0.86 > Freerouting 0.80, CADET 67.2% ≈ Freerouting 65.6%, 대형 보드에서는 열세. 체크포인트 비상업 | 300부품 구간에서는 공개 비교가 가능. 학술 모델을 상업적으로 재사용할 수는 없음 |
| 배선: LLM 에이전트 | PCBRouteAgent ([arXiv](https://arxiv.org/abs/2611.08175)) | D3-A 94.9%, 대형 보드 40% | LLM은 계획을, 엔진은 실행을 맡는 분업이 유효 |
| LLM 에이전트 레이아웃 | EDA Bench, PCB Gym, PCBInnoBench ([ICML](https://icml.cc/virtual/2026/77908); [NeurIPS](https://neurips.cc/virtual/2026/161602)) | 4.58%, 32.1%, 22.0%/7.3% | "DRC 통과 ≠ 기능 동작", 품질 지표 확장 필요 |
| LLM 회로도 생성 | pcbGPT, SchGen, PCBSchemaGen v2, HWE-Bench ([arXiv](https://arxiv.org/abs/2606.01188); [arXiv](https://arxiv.org/abs/2602.00510v2); [arXiv](https://arxiv.org/abs/2603.18102)) | 0.90, 82%/60.5%, 81.3%, 실보드 8.15% | 회로도 생성으로 확장한다면 중간표현과 검증기 루프가 필수 |
| 설계 리뷰·근거 | DRCY, Zeng 외 ([arXiv](https://arxiv.org/abs/2603.15672); [DATE](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)) | 데이터시트 대조와 다회 합의, SHAP 설명. DRCY 성과 수치는 벤더 블로그 | AI 노트를 측정값과 데이터시트에 묶어야 함 |
| SI/PI 인지 배치(국내) | DevFormer(ICML 2023), 성균관대·KAIST 2025 학위논문 | 디캡 수 30% 이상 감소, 보드 PDN 디캡 RL | SI/PI 로드맵의 협력·참조 대상 |
| PCB 생성형 AI 서베이 | Srinivasan 외, arXiv 2606.17074 ([arXiv](https://arxiv.org/abs/2606.17074)) | 데이터 부족과 도구 통합 부족 | 기존 EDA 파일을 받는 구조가 통합 공백을 메움 |

## 3. 해외에는 Quilter라는 근접 경쟁자가 있고, 국내에는 같은 형태의 서비스가 없다

### Quilter와 DeepPCB가 '업로드형 자동 레이아웃'을 먼저 상용화했다

모디팩토리와 가장 닮은 해외 제품은 **Quilter**다. 2019년에 설립됐고, 2024년 2월 Series A $10M(Benchmark 주도)에 이어 2025년 10월 **Series B $25M**(Index Ventures 주도)을 유치했다([I-Connect007](https://iconnect007.com/article/147236/quilter-secures-25m-series-b-to-eliminate-manual-pcb-design-with-physicsdriven-ai/147233/design)). 누적 투자액은 제3자 집계에 따라 $35M~$50M으로 엇갈린다([Seedtable](https://seedtable.com/companies/quilter); [CapLight](https://www.caplight.com/company/quilter)).

Quilter는 Altium, Cadence, Siemens, KiCad 파일을 받는다. 여러 스택업을 동시에 평가해 후보를 만들고 순위를 매기며, 후보마다 임피던스, 리턴 전류, 디커플링 같은 물리 리뷰를 붙인다([Quilter Help](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work)).

가격 구조는 원문으로 확인했다. 표어는 "Pay per Project. Not per Seat."다. 업로드 시점의 **미배선 핀 수**로 프로젝트 비용을 매기고, 반복 실행은 무제한이며, 금액은 영업 견적이다. 네이티브 ECAD 출력(Altium, Allegro, Xpedition, KiCad)을 주고, **출력물 소유권은 사용자에게 있다.** 배포는 AWS 클라우드(SOC 2 Type 2)와 고객 쿠버네티스 셀프호스팅(에어갭 가능) 중에서 고른다([Quilter Pricing](https://www.quilter.ai/pricing)).

무료 티어는 **10인 미만이면서 매출 $50K 미만**인 팀의 학술·개인·탐색적 R&D 용도로 제한된다. 무료 티어에서는 보드 메타데이터와 입력 파일을 학습 퍼즐 생성에 쓰고, 엔터프라이즈 설계는 "직간접적으로 학습에 쓰지 않는다"([Quilter Free](https://www.quilter.ai/free-ai-pcb-design)). Quilter는 스스로 "AI 회로도 생성기가 아니고 고급 시뮬레이션 기능은 제한적"이라고 범위를 긋는다. 그러면서 "첫 후보는 보통 첫 1시간 안에, 회로도에서 제조 준비까지 4시간 이내"를 내세운다.

대표 사례인 Project Speedrun은 부품 843개짜리 8층 보드 2장을 사람 작업 38.5시간으로 끝내고 첫 시도에 부팅했다. 하지만 비교 대상인 428시간은 외부 견적이고, 레이아웃 생성 런타임 약 27시간은 회사 발표다([VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the)). "기존 회로도를 배선한 것이지 컴퓨터를 설계한 것은 아니다"라는 반론도 있었다([Slashdot](https://hardware.slashdot.org/story/25/12/16/229209/dual-pcb-linux-computer-with-843-components-designed-by-ai-boots-on-first-attempt)).

**DeepPCB**(InstaDeep, BioNTech 산하)는 공개 단가가 있는 유일한 곳이다. 선불 시간권은 1시간 $30, 10시간 $280, 30시간 $800이다. 무료 체험은 30분, 보드 1개, 4층, airwire 150개, 부품 100개까지다. 종량제 한도는 **8층, airwire 1,200개, 부품 1,000개, 핀 2,200개**이고, 이를 넘으면 엔터프라이즈로 넘어간다([DeepPCB Pricing](https://deeppcb.ai/pricing/)). airwire 상한 1,200개는 모디팩토리의 연결 상한과 같다.

KiCad 플러그인은 Apache-2.0 오픈소스다. 2026년 10월에는 설정 보조 에이전트 "Cooper"가 플러그인에 들어왔다. Cooper는 넷클래스, 차동쌍, 플레인, 스택업을 읽고 설정 변경을 제안하며, 사용자가 변경마다 승인하거나 거절한다([GitHub](https://github.com/instadeepai/deeppcb-kicad-plugin); [DeepPCB 블로그](https://deeppcb.ai/cooper-kicad-plugin/)). "AI가 판단을 설명하고 사람이 승인한다"는 점에서 모디팩토리의 AI 노트와 가장 가까운 해외 기능이다.

처리 시간을 나란히 놓으면 이렇다. DeepPCB는 첫 결과까지 1~2분(벤더 주장), Quilter는 첫 후보까지 1시간 안팎, 모디팩토리는 배치 약 30분과 배선 약 60분이다. 모디팩토리가 가장 느린 쪽에 속한다. 다만 처리 범위가 서로 다르므로 직접 비교에는 한계가 있다.

### EDA 대기업은 보조형 AI에 머물고, 초보자 시장은 Flux와 범용 LLM이 다툰다

기존 EDA 대기업의 AI는 대부분 숙련 설계자를 돕는 보조형이다.

- **Cadence:** AuraStack AI Super Agent는 2026년 7월에 발표됐고 얼리 액세스를 거쳐 공급 중이다. 고객 인용으로 FORVIA HELLA가 "부품 300개 배치를 최대 4일에서 4분으로" 줄였다고 한다. 이는 벤더 보도자료 인용이다([Fierce Sensors](https://www.fiercesensors.com/ai/cadence-aurastack-debuts-boost-pcb-and-packaging-designers), 스니펫).
- **Siemens:** 2026년 3월 Fuse EDA AI Agent를 내놓고 Xpedition·HyperLynx의 레이아웃·SI 작업까지 에이전트로 묶었다([Siemens](https://news.siemens.com/en-us/siemens-fuse-eda-ai-agent/), 스니펫).
- **Zuken:** 2026년 10월 20일 CR-8000 2026을 출시했다. 과거 배치를 재사용하는 AI-PR 기반 Smart Design Reuse와, 배치 지식을 "클라우드가 아닌 고객 네트워크 안에" 두는 Dynamic Brain을 넣었다([Zuken](https://www.zuken.com/en/resource/cr-8000-2026-pcb-design-automation/)).
- **Altium:** 2024년 8월 Renesas에 인수됐다. 2026년의 AI 기능은 Requirements Portal 안의 Agentic Requirements Engineering(10월 14일)이며, **레이아웃·배선 AI는 아니다.** 공식 MCP 서버는 "Coming Soon"이다([Altium 문서](https://www.altium.com/documentation/altium-365/requirements-portal/agentic-requirements-engineering); [Altium](https://www.altium.com/company/newsroom/press-releases/renesas-completes-acquisition-altium), 스니펫).

모디팩토리의 Altium 연동은 Altium 자신이 비워 둔 자리를 노린다.

회로도와 초보자 쪽 경쟁은 거세다. **Flux**는 2026년 2월 총 $37M을 유치했고 가입자가 100만 명을 넘었다([SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)). 원문으로 확인한 플랜은 Explore, Build, Pro, Teams, Enterprise이고, 신규 개인 체험 기간은 **7일**로 줄었다. 금액은 페이지에서 스크립트로 채워져 원문 확인이 안 됐고, 제3자 집계끼리도 월 $20~$250로 충돌한다([Flux Pricing](https://www.flux.ai/pricing); [ProtoFlow, 경쟁사 작성](https://www.protoflow.ai/blog/flux-ai-pricing)). Flux는 기구·외함 설계로 범위를 넓혔다. 2026년 6월에는 보안 공개 문제를 둘러싸고 Adafruit와 법적 분쟁을 벌여 평판 리스크도 생겼다([Slashdot](https://yro.slashdot.org/story/26/06/02/1647209/adafruit-pauses-blog-after-demand-letter-from-fluxais-lawyers); [HN](https://news.ycombinator.com/item?id=48368121)).

**Circuit Mind**는 2026년 10월 $25M(누적 $33.4M)을 유치하며 회로도 검증 에이전트 AVE를 냈다([SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/)). Circuit Mind와 CELUS는 공개 가격 페이지가 없다(404).

2026년 하반기의 최대 변수는 **범용 프런티어 모델의 진입**이다. OpenAI는 9월 GPT-6 Astra 발표에서 KiCad 회로도를 제조 가능한 PCB로 바꾸는 배치·배선 데모를 첫 화면에 올렸다([KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487); [EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)). 신생사도 늘었다. Copperhead("Cursor for circuit boards", 2026-09 Show HN), 네덜란드 Schematik, 영국 siliXon($1.5M), CopperPilot($390K)이 있다([HN](https://news.ycombinator.com/item?id=49610059); [AtlasPCB](https://www.atlaspcb.com/news/news-silixon-ai-text-to-pcb-funding-2026/); [Indian Startup News](https://indianstartupnews.com/funding/copperpilot-an-ai-design-agent-startup-for-electronics-hardware-raises-390000-in-funding-12771225)). 뒤의 둘은 스니펫으로만 확인했다. 대부분 프롬프트 기반 대화형 UX다. "파일을 올리면 근거가 붙은 레이아웃을 돌려받는" 모디팩토리와는 입력 방식이 다르다.

### 엔지니어는 AI를 리뷰에는 쓰지만 배치는 믿지 않고, 독립 벤치마크는 아직 없다

**독립적이고 통제된 레이아웃 벤치마크는 2026년 11월 현재 존재하지 않는다.** 숫자가 있는 비교는 모두 벤더가 만든 것이다. 그중 가장 공개적인 것은 DeepPCB가 공개 KiCad 보드 3종(STRF, PocketBeagle, BeagleConnect Freedom)으로 Quilter와 비교한 결과다. 평균 배선 완료율은 DeepPCB 97.3%, Quilter 87.7%였고, via 수도 DeepPCB가 적었다. 다만 이 비교는 배선만 보고 Quilter의 강점인 배치와 물리 검토는 평가하지 않았다([DeepPCB 블로그](https://deeppcb.ai/deeppcb-vs-quilter-open-source-routing-compared-2026/)).

같은 회사는 GPT-6 Astra가 "원샷"으로 만든 보드도 분석했다. 넷클래스를 선언하지 않아 트랙 폭 4종을 DRC로 검증할 수 없었고, via 32개 중 9개가 패드 안에 있었다. DeepPCB의 결론은 "추론 실패가 아니라 라우팅 숙련의 문제"였다([DeepPCB 블로그](https://deeppcb.ai/gpt-6-astra-pcb-routing-deeppcb/)). 업계 비판의 기준이 "완료율"에서 "설계 의도가 규칙으로 선언됐는가"로 옮겨 가고 있다는 신호다. 회로 쪽에는 atopile 팀의 EEBench가 SPICE 기반 공개 벤치마크로 생겼지만 레이아웃은 다루지 않는다([EEBench](https://eebench.org/blog/can-ai-design-circuit-boards-yet/)). 공개 보드로 오토라우터를 채점하는 저장소도 생겼다([Koppar autorouter-bench](https://github.com/Koppar-AI/autorouter-bench)).

실사용자 평판은 일관된다. 2026년 9월 Hacker News 스레드 "Can AI design circuit boards yet?"(422점)에서는 다음 같은 의견이 나왔다.

- "라우팅은 레이아웃에서 가장 쉬운 부분이고, 어려운 것은 부품을 배치하고 그 배치를 조정하는 일"이다([HN](https://news.ycombinator.com/item?id=49569550)).
- AI는 "라이브러리 정리, 풋프린트 재확인, BOM 관리"에는 훌륭하고 "리뷰를 맡기면 내가 놓친 것을 잡는다". 그러나 회로도와 레이아웃은 직접 한다([HN](https://news.ycombinator.com/item?id=49569601)).
- "PCB 레이아웃은 시도할 때마다 형편없었다"([HN](https://news.ycombinator.com/item?id=49569618)).

EEVblog 포럼에서는 "'여기 회로도 있으니 레이아웃 끝나면 알려 줘'는 여전히 환상"이라는 의견이 나왔다([EEVblog](https://www.eevblog.com/forum/chat/ai-pcb-layout/)). KiCad 포럼에서는 Astra가 고주파 신호에 약하고, 학습 데이터가 취미용 오픈 하드웨어에 치우쳐 있다는 지적이 나왔다([KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/8)).

반대 방향의 증거도 있다. RP2040급 단순 취미 보드는 범용 LLM과 KiCad MCP 조합으로 실제 제작과 동작까지 성공한 사례가 늘었다([HN](https://news.ycombinator.com/item?id=49569871)). Flux에는 "$50~$140를 토큰에 썼지만 거의 얻은 게 없다"는 비용 불만이 반복된다([HN](https://news.ycombinator.com/item?id=48368721)). Reddit은 끝내 접근하지 못했다.

이 평판은 모디팩토리의 위치를 양쪽에서 비춘다. 엔지니어들이 가장 어렵다고 꼽는 문제가 바로 모디팩토리가 겨냥하는 **배치**다. 그만큼 품질을 증명하면 차별점이 되지만, 증명하지 못하면 회의론에 그대로 노출된다.

### 국내에는 인접 영역만 있고, 현실적 대안은 사람에게 맡기는 외주다

국내에서 "파일을 업로드하면 AI가 PCB 배치·배선까지 생성"하는 일반 사용자용 웹 서비스는 **모디팩토리가 유일하게 확인된다.** 보충 조사에서도 2026년 신규 국내 진입자는 찾지 못했다.

가장 가까운 국내 스타트업 **세카(SECA)**의 핵심 사실은 기사 원문으로 확인했다([뉴스탭](https://www.newstap.co.kr/news/articleView.html?idxno=337854)).

- **출신과 투자:** LG전자 사내벤처에서 출발해 2026년 6월 독립법인으로 출범했다. LG전자와 블루포인트에서 시드를 받았고, 2026년 11월 16일 TIPS에 선정됐다.
- **제품 범위:** 요구사항, BOM, 데이터시트, 회로도를 AI로 연결해 부품 선정부터 회로 검증까지 자동화한다.
- **성과:** 대형 제조사 PoC에서 엔지니어링 공수를 66% 줄였고(경쟁 솔루션은 25%), 독립 후 매출은 7억 원이다.
- **다음 단계:** 넷리스트와 배치·배선 정보를 함께 이해하는 파운데이션 모델을 개발하고 있다.

세카의 제품은 **PCB 레이아웃 도구가 아니다.** 지금은 모디팩토리와 겹치지 않지만, 파운데이션 모델이 현실화되면 B2B 레이아웃 시장에서 부딪칠 수 있다. 다른 보도의 "92% 단축"은 측정 대상이 다른 수치로 보이며, 스니펫으로만 확인했다.

LG AI연구원은 계열사용 PCB 자동 배선을 내부에서 연구한다([LG AI Research 블로그](https://www.lgresearch.ai/blog/view?seq=509), 스니펫). 마키나락스(SMT 조립 순서 최적화)와 알세미(반도체 소자 모델링)는 인접 영역이다([마키나락스](https://www.makinarocks.ai/use-case/reinforcement-learning-based-smt-sequence-optimization/)).

초보자에게 현실적인 대안은 사람에게 맡기는 외주다. 크몽에는 "330,000원부터, 3일 이내" 패키지가 있고([크몽](https://kmong.com/gig/412145)), 2층 이하 단순 회로를 10만 원에 설계해 주는 업체도 있다([(주)제이](https://j-iot.co.kr/product/10)). 이 가격대가 모디팩토리가 유료로 전환할 때 넘어야 할 기준선이다. 국내에서 실질적인 경쟁 압력은 같은 형태의 국내 서비스보다 해외 서비스, 그리고 범용 LLM과 KiCad MCP의 조합에서 온다(추론).

### 오픈소스는 배선과 파일 처리를 갖췄지만 자동 배치와 설계 근거가 비어 있다

오픈소스로 비슷한 파이프라인을 꾸린다면 이렇게 나눌 수 있다.

- **파일 처리·DRC·Gerber:** **KiCad**(GitHub 미러 스타 약 3.2k)
- **배선:** **Freerouting**(약 2.2k, GPL-3.0). 공개 API 베타와 MCP를 제공한다([GitHub Freerouting](https://github.com/freerouting/freerouting)).
- **회로를 코드로 표현:** atopile, tscircuit, SKiDL([atopile](https://github.com/atopile/atopile); [tscircuit](https://github.com/tscircuit/tscircuit))
- **LLM 연동:** mixelpixx/KiCAD-MCP-Server(v2.9.0)는 도구 257개를 제공하고, Freerouting 연동과 JLCPCB 부품 250만 개의 가격·재고 조회를 지원한다([GitHub](https://github.com/mixelpixx/KiCAD-MCP-Server)).

그러나 세부를 보면 약점이 드러난다. Freerouting 메인테이너는 이제 **주 4시간 정도**만 프로젝트에 쓰고, API 키는 주 1회 수동으로 승인한다. 상용 서비스가 기대기에는 공급 리스크가 있으므로 셀프호스팅이 필요하다. KiCAD-MCP-Server의 변경 기록에는 "실제 333-pad 보드에서 304개 패드가 잘못된 넷을 갖고 있었다"는 버그 수정이 남아 있다. 이 프로젝트의 후속작 Konnect-EDA는 폐쇄형 상용판으로 전환하면서 "아무것도 외부로 전송하지 않는다"를 내세운다([GitHub](https://github.com/Orchis-ai-LLC/Konnect-EDA)). tscircuit의 자동 배치는 아직 "개발 중"이고, atopile과 Diode는 배치·배선을 KiCad에 맡긴다.

빈 곳은 분명하다. **실사용 수준의 자동 배치를 제공하는 성숙한 오픈소스는 없다.** RL_PCB(스타 76)와 Cypress(56)는 연구 코드다. 설계 근거도 MCP와 LLM으로 흉내 낼 수는 있지만, 개발자용 환경이 필요해 "웹 업로드 한 번"이라는 UX와는 거리가 멀다.

| 서비스 | 입력 | 처리 범위·한도 | 소요 시간 주장 | 설계 근거·리뷰 | 출력 | 가격·무료 | 업로드 데이터 학습·산출물 권리 | 주 타깃·규모 |
|---|---|---|---|---|---|---|---|---|
| **MODI Factory** (럭스로보, 한국) | 회로도+레이아웃 쌍: Altium, KiCad 8+, EasyEDA | 배치(후보 2~3개), 배선, 규칙 적용. 300부품·1,200연결·200×200, 하루 각 5회 | 배치 약 30분 + 배선 약 60분 | 룰 엔진 기반 배치·배선 노트 | .kicad_pcb, .PcbDoc, EasyEDA .json, Gerber, PDF(PCB만) | 얼리 액세스, 2026년 말까지 무료, 이후 미정 | 약관상 원본 R&D 활용·비식별 학습 가능, **산출물 IP 회사 귀속**(FAQ와 충돌) | 초보자부터 현업. 모회사 별도 매출 급감 |
| **Quilter** (미국) | Altium, Cadence, Siemens, KiCad | 배치, 배선, 후보 순위, 물리 리뷰 | 첫 후보 1시간 안팎, 제조 준비 4시간 이내 | 후보별 물리 design review | 네이티브 ECAD, Gerber, Excellon | 프로젝트(미배선 핀) 단위 견적. 무료는 10인·$50K 미만 | 무료 티어는 학습에 활용, 엔터프라이즈는 미사용. 산출물은 사용자 소유 | 전문가, 항공·국방. 누적 $35~50M(상충) |
| **DeepPCB** (InstaDeep/BioNTech) | .PcbDoc, KiCad 플러그인, EasyEDA Pro, DSN | RL 배선 중심, 8층·airwire 1,200개·부품 1,000개 | 첫 결과 1~2분(벤더) | Cooper 설정 제안·승인 | 배선된 보드 | $30/시간, 체험 30분 | 확인 안 됨 | 전문가, 취미 |
| **Cadence AuraStack** | 넷리스트 + 제약 | 배치, 배선, 멀티피직스 | 300부품 4일→4분(고객 인용) | 에이전트 기반 제약 관리 | 자사 툴 | 기업 라이선스 | 해당 없음 | 대기업 |
| **Flux** (미국) | 텍스트 프롬프트, 브라우저 에디터 | 회로도, 자동 레이아웃, 외함 | 미공개 | "투명한 AI 에이전트" | 내보내기 | 5개 플랜, 7일 체험, 금액 미확정 | 미확인 | 초보자부터 전문가. $37M, 가입 100만+ |
| **Circuit Mind** (영국) | 블록도, 기존 회로도 | 회로도, BOM, FMEA, 검증 | 약 60초~10분 미만 | 데이터시트 대조 검증(AVE) | 회로도, 리포트 | 비공개 | 미확인 | 기업. 누적 $33.4M |
| **SECA** (한국) | 요구사항, BOM, 데이터시트, 회로도 | 문서 정합성 검증, 부품 선정 | — | 지식그래프 기반 불일치 탐지 | 검증 결과 | 연간 라이선스 계획 | 미확인 | 대형 제조사. 매출 7억 원, TIPS |
| **KiCad + Freerouting (+MCP)** | KiCad, DSN | 배선(배치는 수동) | 수 분~수 시간 | 없음(LLM으로 흉내 가능) | Gerber 등 | 무료(GPL-3.0) | 셀프호스팅 시 외부 전송 없음 | 개발자, 메이커 |

표의 근거는 앞의 본문 인용과 같다. 2026년 PCB 설계 소프트웨어 시장 규모는 조사기관에 따라 **$3.8B~6.2B**로 추정치가 크게 벌어진다(요약 페이지 기준, [Straits Research](https://straitsresearch.com/report/pcb-design-software-market); [Grand View Research](https://www.grandviewresearch.com/industry-analysis/pcb-design-software-market-report)). 이 숫자보다 의미 있는 신호는 2025~2026년 Diode, Quilter, Flux, Circuit Mind로 이어진 연속 투자와 범용 모델의 진입이다. "AI PCB 설계" 시장이 검증됐다는 뜻인 동시에, 자금력 있는 경쟁자가 이미 들어와 있다는 뜻이다.

## 4. 한계 분석 및 차세대 서비스 방향: 승부처는 생성보다 검증이다

이 절은 "학술적·기술적·기능적 관점에서 모디팩토리의 한계는 무엇이고, 더 나은 서비스는 어떤 방향이어야 하는가"라는 질문에 답한다. 각 항목에서 **근거**는 인용한 출처로 확인한 사실이고, **추론**은 그 사실에서 이 보고서가 끌어낸 판단이다. 보충 조사로 엔진 구조와 처리 한도, 약관이 원문으로 확인됐다. 그래서 1차 판단 중 일부는 "검증할 수 없다"에서 "확인된 한계"로 바뀌었고, 일부는 1차 판단보다 좁아졌다.

### 학술적 한계: 공개된 검증 성과가 없고, 자체 비교는 재현할 수 없다

**근거.** 럭스로보 팀의 동료심사 논문이나 공개 벤치마크 결과는 보충 조사에서도 찾지 못했다. 회사가 공개한 비교는 엔지니어 인터뷰 하나뿐이다. 양산 보드 4종에서 상용 자동 배치 툴과 범용 LLM보다 나았다는 내용인데, 비교 툴의 이름과 보드 사양이 없다([배치 엔지니어 인터뷰](https://www.modifactory.com/blog/ko/autoplacer-engineer-interview)). 가장 가까운 국내 학술 선행연구(연세대 2024)는 4쪽짜리 학술대회 논문이다.

공개된 특허 청구항은 부품 특징점을 스코어링 모델에 넣어 추천 레이아웃을 내는 구조다([KR20250132817A](https://patents.google.com/patent/KR20250132817A/ko)). 수상 특허는 에어와이어의 길이·밀집도·교차 특징을 쓴다([네이트뉴스](https://m.news.nate.com/view/20260721n00645)).

학계는 이런 사전 지표와 최종 품질 사이의 간극을 반복해서 보고한다. EDA Bench에서는 빌드된 보드의 대부분이 기능 검사에 실패했다(4.58%). PCB Gym에서 DRC를 통과한 완전 배선 보드는 32.1%였다. Vassallo & Bajada도 배치 품질을 사전 지표가 아니라 라우팅 후 배선 길이로 평가했다. AlphaChip 논쟁은 IEEE TCAD 게재와 제3자 재현까지 거치며, 강한 기준선 없이 내세운 "AI 우위"가 무너질 수 있음을 보여 줬다([arXiv 2302.11014](https://arxiv.org/abs/2302.11014)). PCB 배치·배선 결정을 설명하는 XAI 연구는 여전히 없다.

**추론.** 에어와이어 특징과 스코어링 모델은 고전 배치 알고리즘이 오래 써 온 배선 길이·혼잡도 대리(proxy) 지표와 성격이 같다. 힘 기반 배치나 배선 길이 최소화가 대표적이다. 특허가 잘못됐다는 뜻은 아니다. 다만 대리 지표 개선이 라우팅 후 품질과 전기적 동작으로 이어진다는 것을 공개 벤치마크로 보이기 전까지, 품질 주장은 학술적으로 검증할 수 없다.

AI 노트는 1차 조사 때 걱정한 것보다 낫다. 룰 엔진 판정에 근거하기 때문이다. 그러나 판정 기준과 수치가 얼마나 공개되는지, LLM 문장이 판정 밖으로 나가지 못하게 막는 장치가 있는지는 여전히 외부에서 확인할 수 없다.

### 기술적 한계: '물리 기반 검증'은 아직 규칙 검사이고, 처리 범위는 소·중형 보드에 묶여 있다

**근거.** 현재 "물리 기반 검증"은 두 가지다. 배선 중 설계 규칙(선폭, 간격, 층간 규칙) 자동 적용과, 룰 엔진 기반 배치 진단(디캡 8mm 이하 등)이다([튜토리얼 ②](https://www.modifactory.com/blog/ko/tutorials-002); [modifactory.com/ko](https://www.modifactory.com/ko)). 열 시뮬레이터는 개발 중이며 "특정 PCB 조건에 맞춰 최적화된 상태"다. PI·SI는 "순서만 잡아 둔" 로드맵 단계다([AI 엔지니어 인터뷰](https://www.modifactory.com/blog/ko/ai-ethan-interview)). 독립 DRC/DRS도 "업데이트 예정"이다. PI/SI 시뮬레이션 엔진 개발자는 2026년 10월에야 채용 공고가 났고([공고](https://freehire.me/jobs/hoero-simyulreisyeon-enjin-gaebalja-reogseurobo-ds72wlha)), SI 수치해석 엔진은 글로벌 팁스 과제로 개발 중이다.

처리 한도는 부품 300개(메인 100개), 연결 1,200개, 보드 200×200이다. 레이어 수 상한과 차동쌍·임피던스·길이 매칭 지원 여부는 공개되지 않았다([_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js)).

배선 엔진은 그래프 탐색과 메타휴리스틱 계열이다. 문헌에 따르면 이 계열은 소형 보드에서 학습형과 대등하다. CADET은 67.2%로 Freerouting의 65.6%와 비슷했고, PCBWorld에서도 소형 보드에서는 학습형이 앞섰다. 대형 보드에서는 학습형이 여전히 뒤처진다.

LLM이 주요 부품 배치를 맡는 구조는 LLM의 공간 추론이 약하다는 결과와 부딪친다(PCB-Bench, OmniLayout). 다만 메인 부품을 100개 이하로 제한하고 기하는 점수 루프에 맡겨 그 위험을 줄였다. 데이터 측면에서는 문제가 세 가지다. 서베이가 데이터 부족을 핵심 장애물로 꼽았고, OmniLayout 데이터는 배포가 철회됐으며, PCBWorld·CADET 체크포인트는 비상업 라이선스다. 실무자들은 공개 학습 데이터가 취미용 오픈 하드웨어에 치우쳐 있다고 지적한다([KiCad 포럼](https://forum.kicad.info/t/open-ai-claims-gpt-6-astra-can-make-pcb-boards/71487/8)).

처리 시간은 배치 약 30분과 배선 약 60분이다. 경쟁사 주장은 DeepPCB 첫 결과 1~2분, Quilter 첫 후보 1시간 안팎이다.

**추론.** 모디팩토리의 현재 실체는 **소·중형 디지털 보드(IoT, MCU, 교육·시제품)를 위한 규칙 준수 배치·배선 도구**다. USB 고속, DDR, RF가 있는 보드에 결과를 그대로 쓸 근거는 아직 없다. 이것 자체는 결함이라기보다 단계의 문제다. 문헌도 이 구간에서는 규칙 기반·휴리스틱 엔진이 충분히 경쟁력 있다고 보여 준다.

문제는 마케팅 언어와 실체의 차이다. "physics-based verification"이라는 표현은 SI·PI·열 해석을 기대하게 만든다. 하지만 실제 제공되는 것은 규칙 검사다. 또 가장 강한 공개 학술 모델을 상업적으로 쓸 수 없으므로, 대형 보드로 확장하려면 자체 데이터가 필요하다. 이 점이 아래 데이터 정책 문제와 직결된다.

### 기능적 한계: 회로도가 있어야 시작할 수 있고, 산출물 권리가 회사에 귀속된다

**근거.** 입출력 한계는 1차 판단보다 좁다. Altium, KiCad 8 이상, EasyEDA의 회로도와 레이아웃을 받고, 같은 형식의 PCB 파일과 Gerber, PDF로 돌려준다([앱 번들](https://workspace.modifactory.com/_next/static/chunks/447-3cbb73ad59de8403.js); [레이아웃 번들](https://workspace.modifactory.com/_next/static/chunks/pages/layout/%5Bid%5D-d2890299c950859f.js)). 그래도 남는 공백이 있다.

- 회로도 역출력이 없다.
- 제조용 ODB++, IPC-2581과 기구 협업용 STEP이 없다.
- OrCAD, Allegro, PADS와 KiCad 7 이하를 지원하지 않는다.
- Altium을 KiCad 경로로 우회하면 "알티움의 디자인 룰은 KiCad로 넘어오지 않는다"([튜토리얼 ⑤](https://www.modifactory.com/blog/ko/tutorials-005)).

시작 조건도 까다롭다. AI 배치에는 회로도가 필수이고, 업로드 전에 Net 이름이 일치하고 ERC 오류가 없어야 한다. 실행은 배치·배선 각각 하루 5회다. 회원 측 입력 때문에 실패하면 횟수가 복원되지 않는다(약관 제9조). 부품 선정·BOM·DFM·발주 연동은 없고, 제조사와의 공식 제휴도 없다. 공개 API나 SDK도 없다.

약관 문제는 1절에서 자세히 다뤘다. 약관은 FAQ와 달리 업로드 원본의 R&D 활용과 비식별 학습을 허용하고, **생성 레이아웃의 저작권과 지식재산권을 회사에 귀속**시킨다. 회원에게는 제3자에게 실시권을 부여할 권한이 없다. 또 산출물의 제조·양산 사용을 보장하지 않는다([이용약관](https://workspace.modifactory.com/terms)). 반면 Quilter는 산출물 소유권이 사용자에게 있다고 명시한다([Quilter Pricing](https://www.quilter.ai/pricing)).

서비스 상태와 사업 여건도 약점이다. 서비스는 얼리 액세스이고, 가격은 미정이며, 독립 후기는 0건이다. 모회사는 2025년 말 직전 대비 약 30% 가격으로 투자를 받았고, 차입금 80억 원의 만기가 2026년 4월부터 돌아온다([뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685)). 경쟁사는 $25~37M 규모의 투자를 받았다.

**추론.** "초보자도 막힘없는 자동 설계"는 여전히 실제 범위보다 넓게 읽힌다. ERC를 통과한 회로도를 만들 수 있는 사람만 출발선에 설 수 있기 때문이다. 하루 5회 한도와 90분 비동기 루프는 고치고 다시 돌려 보는 반복을 막는다. 초보자는 Gerber를 받은 뒤 부품 조달과 DFM에서 다시 막힌다.

가장 구체적인 리스크는 **약관**이다. FAQ의 "명시적 동의 없이 학습하지 않는다"는 약속과 약관의 "가입 시 R&D 활용 동의"가 충돌한다. 산출물 IP 귀속은 업계 관행과도 다르다. 외주 설계사, IP 정책이 있는 기업, 해외 B2B 고객이 도입할 때 걸림돌이 된다. 약관 위반이나 소비자 오인 문제로 번질 수도 있다.

### 더 나은 서비스는 '의도에서 주문까지, 분 단위로, 검증된 근거와 함께' 가야 한다

아래 방향은 이 보고서의 추론이다. 방향마다 근거가 된 연구나 제품 사례를 함께 달았다.

**(가) 의도에서 주문까지 이어지는 엔드투엔드.**
- **방향:** 요구사항, 자연어, 블록도에서 시작한다. 실시간 재고·가격으로 부품을 고르고, 회로도는 코드나 DSL로 만들어 LLM과 결정론적 검사기가 루프를 돌게 한다. 그다음 배치, 배선, DFM, 발주로 이어진다.
- **근거:** pcbGPT(0.90), SchGen(코드 표현 82% 대 원시 KiCad 32%), PCBSchemaGen v2(81.3%), CircuitLM(ERC 엔진 결합)이 중간표현과 검증기 루프의 효과를 보여 준다([arXiv](https://arxiv.org/abs/2606.01188); [arXiv](https://arxiv.org/html/2605.30345v1); [arXiv](https://arxiv.org/abs/2602.00510v2); [arXiv](https://arxiv.org/abs/2601.04505)). KiCAD-MCP-Server는 JLCPCB 재고·가격 연동을 이미 제공한다.
- **모디팩토리와의 관계:** 모디팩토리도 처음에는 블록 다이어그램에서 회로도를 만들고 공급망까지 연결하는 구상을 했고, 그 흔적이 회로 자동설계 특허(KR20250133044A)에 남아 있다. 이 방향은 회사가 접었던 구상으로 돌아가는 것이다.
- **주의:** 실보드 수준 회로도 생성 통과율이 8.15%에 불과하다(HWE-Bench). 회로도 단계에는 사람이 확인하는 체크포인트를 남겨야 한다.

**(나) 분 단위의 대화형 반복.**
- **방향:** 첫 초안을 수 분 안에 보여 주고, 정밀화는 백그라운드에서 진행한다. "이 커넥터는 가장자리에" 같은 자연어 지시를 제약으로 바꾼다. 실행 횟수 제한은 결과에 대한 과금 구조로 대체한다.
- **근거:** Cypress는 최대 492.3배 빠르다. CADET은 보드당 15.5초에 Freerouting과 같은 수준을 냈다. 연세대 석사논문의 규칙 배치는 10초 이내에 끝났다. Quilter는 "프로젝트당 무제한 반복"을 판다.
- **모디팩토리와의 관계:** Lock, "수동 소자만 배치", 웹 에디터는 이미 있다. 하루 5회 제한과 대기열이 걸림돌이다.

**(다) 검증 결과에 연결된 설계 근거.**
- **방향:** 근거의 모든 문장을 측정값, 데이터시트 조항, 설계 규칙 중 하나에 연결한다. 넷클래스·폭·클리어런스 같은 설계 의도는 검증 가능한 규칙 파일로 함께 출력한다. "검사하지 않은 항목"과 신뢰도도 표시한다.
- **근거:** DRCY의 데이터시트 대조와 다회 합의, PCBSchemaGen의 핀 단위 오류 위치가 본보기다. DeepPCB의 Astra 비판(넷클래스 미선언, via-in-pad)은 업계 품질 기준이 "의도의 규칙화"로 옮겨 가고 있음을 보여 준다([DeepPCB](https://deeppcb.ai/gpt-6-astra-pcb-routing-deeppcb/)). DeepPCB Cooper의 "제안하고 승인받는" UX도 참고할 만하다.
- **모디팩토리와의 관계:** 노트가 이미 룰 엔진 판정 위에 있으므로, 판정 수치와 규칙을 사용자에게 노출하면 된다.

**(라) 물리 해석을 루프 안으로.**
- **방향:** 전원, 고속, 차동 넷에 PI·SI·열 시뮬레이션을 연동하고, 그 결과를 후보 순위에 반영한다.
- **근거:** Quilter는 후보마다 물리 리뷰를 붙인다. PCB Gym에서는 전원 레일을 신호 넷처럼 다루는 실패가 잦았다. Siemens Fuse는 HyperLynx SI를 에이전트 흐름에 넣었다. 국내에는 KAIST DevFormer와 성균관대·KAIST의 보드 레벨 디캡 RL 학위논문이 있다.
- **모디팩토리와의 관계:** 글로벌 팁스 과제의 SI 엔진과 개발 중인 열 시뮬레이터를 실제 배치 판단에 연결하는 것이 다음 단계다.

**(마) 도구에 묶이지 않는 왕복 입출력.**
- **방향:** 지금의 Altium·KiCad·EasyEDA 지원에 회로도 역출력, KiCad 7 이하와 OrCAD·Allegro·PADS·DSN 입력, ODB++·IPC-2581·STEP 출력을 더한다. Altium에서 넘어온 디자인 룰과 스택업도 보존한다.
- **근거:** Quilter는 Altium·Allegro·Xpedition·KiCad 네이티브 출력을 준다. DeepPCB는 DSN을 받는다. KAIST와 LG AI연구원은 모두 KiCad로 수렴하고 있다. 경쟁사들의 ODB++·IPC-2581 지원은 확인되지 않았으므로, 먼저 갖추면 차별점이 될 수 있다.

**(바) 에이전트·MCP 네이티브.**
- **방향:** 배치, 배선, 검사 기능을 API와 MCP 도구로 열어, 사용자의 AI 비서가 직접 호출하게 한다. 결과는 구조화 텍스트로 돌려준다.
- **근거:** 범용 모델(GPT-6 Astra)이 KiCad를 직접 조작하기 시작했다. DeepPCB도 "모델이 라우터를 구동하는" 구조를 받아들였다. KiCAD-MCP-Server는 도구 257개를 제공하고, Freerouting은 MCP를 지원한다. PCB-QA에서는 JSON 텍스트 형식일 때 LLM 정확도가 93%였다.
- **모디팩토리와의 관계:** 지금은 공개 API가 없다. 범용 모델 사용자에게 "구동 대상 엔진"으로 노출되면 경쟁자가 아닌 공급자가 될 수 있다.

**(사) 데이터와 소유권 정책을 차별점으로.**
- **방향:** 약관과 FAQ를 일치시킨다. 산출물 소유권은 사용자에게 주고, 학습은 명시적 옵트인으로만 한다. 보관·삭제 기한과 클라우드 수탁사를 공개하고, 엔터프라이즈용 온프레미스 옵션을 제공한다.
- **근거:** Quilter는 엔터프라이즈 설계를 학습에 쓰지 않고 산출물도 사용자 소유다. 셀프호스팅·에어갭 배포도 제공한다. Zuken은 데이터를 "고객 네트워크 안에" 둔다. Konnect-EDA는 "아무것도 전송하지 않는다"를 판다. 데이터 정책 자체가 마케팅 포인트가 됐다.
- **모디팩토리와의 관계:** 대형 보드로 확장하려면 동의 기반 데이터가 꼭 필요하다. 신뢰를 얻는 것이 곧 데이터 전략이다.

**(아) 공개 벤치마크와 첫 시도 성공률.**
- **방향:** 공개 보드에서 Freerouting과 경쟁사를 함께 비교한 결과를 낸다. 지표는 완료율, via 수, 시간, 디캡 커버리지다. 실제 제작 보드가 첫 시도에 동작한 비율도 공개한다.
- **근거:** PCBWorld-Bench(실보드 679개, 지표 8개, 환경 코드 BSD-3)는 외부 연구가 쓰기 시작했다. DeepPCB의 공개 보드 3종과 Koppar autorouter-bench도 있다. AlphaChip 논쟁과 Speedrun 반론은 공개 기준선이 없을 때 무슨 일이 생기는지 보여 준다.
- **모디팩토리와의 관계:** 300부품 한도 안에서도 이 비교는 충분히 가능하다.

**(자) 초보자를 위한 튜터형 설명과 국내 생태계.**
- **방향:** 설명을 층으로 나눈다(초보자용 한 줄, 엔지니어용 수치, 근거 문서). 설계가 "단순 회로"의 경계를 넘을 때는 경고한다. 검증된 레퍼런스 설계를 템플릿으로 제공하고, 한국어 지원과 국내 제조사·부품 유통사 연동을 갖춘다.
- **근거:** HN에서는 "AI가 하한선을 끌어올리지만, 경험이 없으면 단순 회로의 경계를 모르고 넘는다"는 경고가 나왔다([HN](https://news.ycombinator.com/item?id=49696205)). RP2040급 단순 보드는 AI로 성공한 사례가 늘었다. 국내 외주는 10만~33만 원이다. 광운대 실습 툴 채택(업체 게재)은 교육 채널이 이미 열려 있다는 신호다.

| 한계 | 근거 | 개선 방향 |
|---|---|---|
| 동료심사 논문·공개 벤치마크 없음, 자체 비교는 재현 불가 | 팀 논문 미발견. 양산 보드 4종 비교는 툴·보드 비공개 | PCBWorld-Bench, 공개 보드 3종에서 비교 공개 (아) |
| 대리 지표·스코어링 모델에 의존 | 특허 청구항. EDA Bench 4.58%, PCB Gym 32.1% | 라우팅 후 지표, ERC, PI, 기능 검사로 평가 (다)(라)(아) |
| 노트 판정 기준과 LLM 서술 통제가 비공개 | 룰 엔진 기반이라고만 공개 | 근거마다 측정값·규칙·데이터시트 연결, 미검사 항목 명시 (다) |
| "물리 기반 검증"이 규칙 검사 수준, SI·PI 미구현, 열 해석 개발 중 | 튜토리얼 ②, AI 엔지니어 인터뷰 | 핵심 넷 시뮬레이션 연동, 결과를 후보 순위에 반영 (라) |
| 300부품·1,200연결·200×200, 레이어·고속 지원 미공개 | 앱 번들 | 한도 공개, 대형 보드 확장, 업로드 시 난이도 진단 (아) |
| 대형 보드 배선 열세, 공개 학술 모델은 비상업 | PCBWorld, CADET, EXAONE NC | 결정론적 라우터 + ML 가이드, 자체 동의 데이터 (나)(사) |
| 배치 30분 + 배선 60분, 하루 각 5회 | 튜토리얼, 약관 제9조 | 수 분 내 초안, 점진 정밀화, 프로젝트 단위 무제한 반복 (나) |
| 회로도 필수, 엔드투엔드 아님 | 튜토리얼 ⑤ | 요구사항에서 회로도까지 생성 (가) |
| 회로도 역출력·ODB++·IPC-2581·STEP 없음, OrCAD·PADS·KiCad 7 이하 미지원 | 앱 번들 | 왕복 입출력 확장, 룰·스택업 보존 (마) |
| 부품 조달·BOM·DFM·발주 미연동, 공식 제휴 없음 | 사이트 공지 부재 | 실시간 재고·가격, DFM, 국내외 발주 연동 (가)(자) |
| 약관과 FAQ 충돌: 원본 R&D 활용, 산출물 IP 회사 귀속, 제3자 실시권 불가 | 약관 제18·19조 | 사용자 소유, 학습 옵트인, 온프레미스 (사) |
| 공개 API·MCP 없음 | 사이트맵, 앱 번들 | API·MCP로 엔진 노출 (바) |
| 얼리 액세스, 가격 미정, 모회사 다운라운드·차입금 만기 | DART, 뉴스톱 | 투명하고 예측 가능한 요금, 성능 공개로 유료 전환 근거 확보 (아) |

## 5. 시사점: 차별점은 기능의 조합에, 승부처는 검증과 신뢰에 있다

### 차별점은 '초보자가 읽을 수 있는 근거'와 '기존 도구 안으로 들어가는 연동'이다

개별 기능만 보면 새로운 것이 거의 없다. 다중 후보와 물리 리뷰는 Quilter에, 무료 진입은 Quilter·오픈소스에, 분 단위 처리는 DeepPCB에 이미 있다. 모디팩토리가 다른 지점은 네 가지다.

첫째는 **설계 근거의 독자층과 근거의 출처**다. 해외의 리뷰 기능은 전문가용 물리 검토이거나(Quilter), 설정을 제안하고 승인받는 방식이다(DeepPCB Cooper). 모디팩토리의 노트는 "왜 이 디캡이 이 거리에 있는가"를 룰 엔진 판정에 근거해 초보자 눈높이로 서술한다. 학계에서 비어 있는 "배치 결정의 설명" 영역이고, 학계가 권하는 "측정값에 근거한 설명" 구조와도 맞는다.

둘째는 **기존 도구 안으로 들어가는 연동**이다. Altium 자신의 2026년 AI 기능은 요구사항 관리에 그친다. DeepPCB의 Altium 버튼은 아직 출시 예정이다. 이런 상황에서 Altium·KiCad·EasyEDA 파일을 받아 같은 형식으로 돌려주고, Altium 익스텐션까지 준비하는 것은 현업 엔지니어의 작업 흐름을 깨지 않는 전략이다.

셋째는 **배치라는 과녁**이다. 실무 엔지니어들은 "라우팅은 쉬운 부분이고 배치가 어렵다"고 말하고 AI 배치를 가장 믿지 않는다. 경쟁사 다수는 배선에 강점이 있다. 모디팩토리가 배치 품질을 공개 지표로 증명한다면 바로 그 불신의 빈자리를 차지할 수 있다.

넷째는 **현지화와 국내 연구 생태계**다. 한국어 지원과 무료 진입은 10만~33만 원짜리 외주와 직접 경쟁한다. 연세대와의 글로벌 팁스 과제, 국산 벤치마크 PCBWorld, KAIST의 KiCad 에이전트 연구가 모두 손 닿는 거리에 있다.

### 4절의 한계 가운데 가장 시급한 것은 약관 정비와 검증 공개다

4절의 한계는 모두 중요하지만 시급한 정도가 다르다. 무료 기간은 약 6주 뒤인 2026년 말에 끝난다. 유료 전환 시점에 사용자가 비교할 대상은 세 가지다. 무료 티어와 사용자 소유 산출물을 내세우는 Quilter, 가입자 100만 명의 Flux, 그리고 범용 LLM과 KiCad MCP 조합이다. 이때 공개 벤치마크도 독립 후기도 없다면 설득 근거는 공식 추천사뿐이다. 게다가 그 추천사마저 한국어판과 영어판이 서로 맞지 않는다.

약관 문제는 더 급하다. 유료 B2B 고객은 반드시 약관을 읽는다. 산출물 IP 귀속 조항과 FAQ와의 불일치는 실사 단계에서 바로 걸린다. 홍보 문구의 정확성도 같은 맥락이다. 회사 PM은 "최종 선정되지는 못했다"고 밝혔는데 언론은 "2위", "수상 후"라고 썼다. 계획 단계의 EDA 3사 협업이 확정된 것처럼 읽히는 표현도 있다. 이런 간극은 B2B 신뢰를 깎는다.

다행히 이 문제들은 같은 처방으로 풀린다. 사용자에게 유리하게 약관을 정비하고, 공개 벤치마크 수치를 내면 된다. 둘 다 돈이 많이 들지 않고, 유료 전환의 근거가 되며, 과장 논란도 잠재운다.

### 남은 질문: 원문 확인으로 풀린 것과 아직 남은 것

보충 조사로 입출력 형식, 처리 한도, 엔진 구조, 데이터 정책, 2023년 매출 기준, 첫 공개일, 정부 과제명, Embedded Award 결과가 해소됐다. 아직 남은 질문은 다음과 같다.

| 질문 | 현재 확인 수준 | 확인 경로 |
|---|---|---|
| 수상 특허의 출원·등록번호와 청구항 | 기사 요지만 확인(KIPRIS 타임아웃) | KIPRIS 원문 |
| 레이어 수 상한, 차동쌍·임피던스·길이 매칭 지원 | 번들에 문자열 없음 | 서비스 직접 테스트, 회사 문의 |
| Altium .PcbDoc 내보내기에서 룰·폴리곤·스택업 보존 여부 | 미확인 | 왕복 테스트 |
| SI/PI 제품화 시점, 열 해석의 UI 노출 여부 | 인터뷰상 로드맵·개발 중 | 릴리스 노트 추적 |
| 실제 가입자 수, 기업 고객 수, 2027년 요금표와 크레딧 단가 | 비공개(앱에 크레딧·플랜 문구만 존재) | 회사 IR, 공식 공지 |
| 사용하는 LLM(외부 API인지 자체 모델인지)과 학습 데이터 출처 | 비공개 | 회사 문의 |
| ISO 27001 인증 주체·범위, 엔터프라이즈 약관의 데이터·IP 조항 | 미확인 | 인증서 번호, 계약서 |
| 독립 성능 지표(배선 완료율, DRC·ERC 통과율, 디캡 커버리지) | 회사 주장만 있음 | PCBWorld-Bench와 공개 보드 3종으로 직접 비교 |
| 럭스로보 2024~2025년 감사 재무와 차입금 상환 여부 | DART 미공시, Wadiz 스니펫 | DART, 신용정보 |
| 글로벌 팁스 과제 금액·기간, 연세대 연구와 모디팩토리 엔진의 관계 | 과제명과 공동 참여 기관만 확인 | NTIS, DBpia 원문 |

## 결론

모디팩토리를 평가할 때 던져야 할 질문은 "90분이 빠른가"가 아니다. **"300부품 이하의 보드에서, 사람이 검토할 만한 배치를, 룰 엔진 판정에 근거한 설명과 함께 내놓는가, 그리고 그 결과물이 누구의 것인가"**가 올바른 질문이다. 이 질문에 답하는 가장 빠른 방법은 직접 비교다. 무료 기간이 끝나기 전에 DeepPCB가 쓴 공개 보드 3종이나 PCBWorld-Bench의 소형 보드를 모디팩토리, Quilter 무료 티어, KiCad+Freerouting에 넣는다. 결과는 완료율, via 수, 디캡 커버리지로 채점하고, 배치 노트의 판정이 실제 측정값과 맞는지 대조한다. 사내 설계를 올리기 전에는 산출물 IP를 회사에 귀속시키는 약관 제18조를 먼저 검토해야 한다.

문헌과 경쟁 지형을 함께 보면 더 큰 흐름이 보인다. 레이아웃 "생성"의 진입 장벽은 낮아지고 있고, 가치의 중심은 "검증"으로 옮겨 가고 있다. 실사용 수준의 오픈소스 자동 배치는 아직 없지만, GPU 배치 엔진(Cypress, 연구 코드)과 결정론적 라우터(Freerouting)가 오픈소스로 공개돼 있어 출발점으로 쓸 수 있다. 소형 보드에서는 학습형 라우터도 Freerouting과 같은 수준에 올라섰다. 반면 LLM 에이전트는 그럴듯하지만 동작하지 않는 보드를 쉽게 만든다. 따라서 차세대 서비스의 경쟁력은 더 영리한 생성기보다 세 가지에서 나온다. 모든 판단을 검사 결과에 묶는 근거 체계, 공개 벤치마크, 그리고 업로드 데이터와 산출물에 대한 신뢰다.

모디팩토리는 룰 엔진 기반 'AI 노트'라는 형태로 이 방향의 씨앗을 이미 갖고 있다. 2027년 유료 전환 전에 할 일은 세 가지다.
1. 노트의 판정 수치를 사용자에게 공개한다.
2. 약관을 FAQ의 약속에 맞게 고쳐 산출물을 사용자에게 돌려준다.
3. 국산 공개 벤치마크인 PCBWorld로 성능을 공개한다.

이를 해낸다면 과장된 수상 문구 없이도 국내 AI PCB 설계의 기준점이 될 수 있다. 그러지 못하면 Quilter의 무료 티어, Flux, 그리고 KiCad를 직접 조작하는 범용 모델 사이에서 차별점이 희석될 것이다.
