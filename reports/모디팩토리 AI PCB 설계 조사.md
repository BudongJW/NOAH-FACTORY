# 모디팩토리, '설명하는 AI'로 PCB 레이아웃 시장에 도전하다

**요약:** 사용자가 첨부한 랜딩페이지의 "MODI Factory(모디팩토리)"는 모듈형 코딩 교구 MODI를 만든 **㈜럭스로보(2014년 설립, 대표 오상훈)**가 2022년부터 개발한 웹 기반 AI PCB 배치·배선 자동화 서비스다. 회로도를 새로 그려 주는 서비스는 아니다. 사용자가 올린 **회로도·레이아웃 파일로 90분 안에 물리 기반 검증, 부품 배치, 배선을 끝내고, 그렇게 판단한 근거를 '배치 노트'와 '배선 노트'로 설명**한다. 결과물은 Gerber로 내려받아 바로 발주할 수 있고, 2026년 말까지는 가입만 하면 모든 기능이 무료다. 2024년 CES에서는 GPT-4로 부품을 추천하는 '올인원 플랫폼'으로 처음 공개됐다. 2026년에는 배치·배선과 설계 근거로 초점을 좁혔고, 2026년 3월 embedded award Tools 부문 최종 후보 3곳에 들었다. 다만 이 부문 수상작은 다른 제품(Ambiq HeliaAOT)이었다. 학계 문헌은 이 분야가 아직 미성숙하다고 경고한다. 2026년에 쏟아진 벤치마크에서 LLM 에이전트가 실제 보드 수준의 레이아웃을 제대로 완성하거나 기능 검사를 통과한 비율은 4.6~32%에 그쳤다. 학습형 라우터는 여전히 규칙 기반 라우터에 뒤처지고, 배치·배선 결정을 설명하는 XAI 연구는 사실상 없다. 국내 학술 연구도 KAIST의 패키지·HBM 디커플링 커패시터 강화학습과 LG AI연구원의 PCB 배선 벤치마크(PCBWorld, CADET)가 거의 전부다. 해외에서는 Quilter(물리 기반 AI, 2025년 Series B $25M)가 가장 가까운 경쟁자다. 배치·배선은 DeepPCB, Cadence, Siemens, Zuken이, 회로도 쪽은 Flux, Circuit Mind, CELUS가 차지하고 있다. 국내에서는 같은 형태의 서비스가 확인되지 않았다. 모디팩토리의 차별점은 기능 하나하나가 아니다. "파일 업로드형 비동기 서비스, 초보자도 읽을 수 있는 설계 근거, 한국어, Altium 플러그인, 무료 진입"을 한데 묶은 조합에 있다. 한계도 분명하다. 학술적으로는 공개 검증이 없고 대리 지표에 의존한다. 기술적으로는 물리 검증의 범위가 불분명하다. 기능적으로는 회로도가 있어야 시작할 수 있고, 출력은 Gerber만 확인되며, 모회사의 매출 급감이라는 사업 지속성 위험도 있다. 더 나은 서비스는 요구사항에서 발주까지 이어지고, 분 단위로 반복할 수 있으며, 모든 설계 근거를 검사 결과에 연결하고, 성능을 공개 벤치마크로 증명하는 방향으로 가야 한다.

> **조사 방법상 한계:** 이 조사 세션은 네트워크 정책 때문에 modifactory.com, 국내 언론사 사이트, KCI·RISS·DBpia·KIPRIS·NTIS, arXiv 등 1차 출처 상당수를 직접 열지 못했다. 그래서 많은 사실이 웹 검색 결과의 스니펫과 요약에 근거한다. "스니펫 기준"이라고 표시한 수치와 출처끼리 충돌하는 수치는 원문을 확인하기 전까지 잠정치로 읽어야 한다. 출처가 충돌하는 대표 사례는 럭스로보 매출, Quilter 누적 투자액, PCBSchemaGen 성능이다. 확인하지 못한 항목은 사실로 서술하지 않았다. GitHub 저장소 수치는 2026-11-16에 직접 확인한 값이다.

## 1. 모디팩토리는 회로도가 아니라 배치·배선을 90분 안에 자동화한다

### 운영사 럭스로보는 매출이 급감하는 가운데 교구 기업에서 EDA 기업으로 방향을 틀었다

공식 사이트는 www.modifactory.com(한국어 /ko)이다. 영문 소개는 서비스를 "웹 기반 AI PCB 설계 플랫폼"으로 정의한다([modifactory.com](https://www.modifactory.com/)). 운영사는 **㈜럭스로보(LUXROBO)**다. 2024년 1월 CES 공개 기사부터 2026년 9월 기사까지 국내 언론은 일관되게 이 서비스를 럭스로보의 서비스로 보도했다([전자신문](https://www.etnews.com/20240104000261); [서울경제](https://www.sedaily.com/article/20019757)). embedded award 2026 후보 목록에도 "MODI Factory (exhibitor: LUXROBO)"로 올라 있다([embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/02/tools-nominees)). 다만 사이트 푸터나 이용약관의 법적 고지(사업자등록번호, 주소)는 직접 확인하지 못했다. 럭스로보는 **2014년 11월 13일에 설립**됐고([TheVC](https://thevc.kr/luxrobo)) 대표는 **오상훈**이다([이투데이](https://www.etoday.co.kr/news/view/2363460)). 주력 제품은 자석 커넥터로 결합하는 모듈형 코딩 교구 MODI와 MODI Plus다([넥스트유니콘](https://www.nextunicorn.kr/company/7f582af41601f4fb)). 50여 개국에 수출한다고 소개되고([테크42](https://www.tech42.co.kr/%EC%98%A4%EC%83%81%ED%9B%88-%EB%9F%AD%EC%8A%A4%EB%A1%9C%EB%B3%B4-%EB%8C%80%ED%91%9C-%ED%95%99%EC%83%9D-%EC%8B%9C%EC%A0%88-%EC%B0%BD%EC%97%85%ED%95%B4-50%EC%97%AC%EA%B0%9C%EA%B5%AD%EC%97%90/)), MODI 시절 CES 혁신상과 K-Startup 최우수상을 받았다는 보도가 있다([아주경제](https://www.ajunews.com/view/20191117170033660)). 랜딩페이지의 "MODI"는 이 교구 브랜드에서 온 이름이다. "초보자 친화"라는 포지셔닝도 교육 사업의 연장선에 있다.

투자는 2017년 카카오인베스트먼트·카카오브레인의 40억 원([파이낸셜뉴스](https://www.fnnews.com/news/201706071046598737)), 시리즈B 90억 원([벤처스퀘어](https://www.venturesquare.net/802751)), 2025년 10월 Pre-IPO 투자([TheVC](https://thevc.kr/luxrobo)) 순으로 확인된다. 누적 투자액은 출처에 따라 "약 379억 원"과 "350억 원 이상"으로 갈린다. Pre-IPO 기업가치 2,200억 원대라는 수치도 검색 요약에서만 확인했다([이투데이](https://www.etoday.co.kr/news/view/2363460); [뉴스톱](http://www.newstopkorea.com/news/articleView.html?idxno=23326)). 상장 추진 과정은 다음과 같다. 2021년에 "내년 상장 추진"을 발표했고([전자신문](https://m.etnews.com/20210624000165)), 2024년 4월 기술성 평가 A등급을 받으며 삼성증권을 대표주관사로 정했다([메트로신문](https://www.metroseoul.co.kr/article/20240416500511)). 이어 코스닥 상장예비심사를 청구했지만([더스탁](https://www.the-stock.kr/news/articleView.html?idxno=20592)) 결국 **자진 철회**했다. 철회 뒤 오상훈 대표가 유상증자 물량을 전량 인수해 최대주주(29.59%)가 됐다는 보도가 있다. 철회 날짜와 사유는 확인하지 못했다([뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685)).

매출은 출처마다 크게 다르다. 아래 수치는 모두 검색 요약 기준이며, DART 감사보고서와 대조하지 못했다.

| 출처 | 2022년 | 2023년 | 2024년 | 2025년 |
|---|---|---|---|---|
| [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) (스니펫) | 연결 179억 원 | 114억 원 | 49억 원("지난해") | 3분기 누적 12억 원 |
| [TheVC](https://thevc.kr/luxrobo) | — | — | 별도 49억 원, 연결 66억 원 | — |
| [이투데이](https://www.etoday.co.kr/news/view/2363460) | — | 연결 242억 원(영업손실 60억 원) | — | — |

2023년 매출은 114억 원과 242억 원으로 두 배 넘게 차이 나서, 어느 쪽이 맞는지 판단할 수 없다. 그래도 어느 수치를 택하든 **2022년 정점 이후 매출이 급감했다는 방향은 같다.** 2026년 3월 언론은 럭스로보를 "교육용 IoT 모듈 기업에서 AI PCB 설계 자동화 플랫폼 기업으로 사업 영역을 넓히는" 회사로 소개했다([서울경제](https://www.sedaily.com/article/20019757); [빅데이터뉴스](https://www.thebigdata.co.kr/view.php?ud=2026031615220030386cf2d78c68_23)). 이런 정황을 함께 보면 모디팩토리는 곁가지 사업이 아니라 회사의 다음 성장을 건 핵심 사업이다.

### 랜딩페이지 약속은 대부분 확인되지만 '다양한 포맷'은 Gerber만 확인된다

| 랜딩페이지 문구 | 확인된 실제 내용 | 근거 |
|---|---|---|
| 파일 업로드 | 회로도와 레이아웃 파일을 업로드한다. FAQ에 "기존 EDA(Altium, KiCad 등) 파일을 쓸 수 있나" 질문은 있으나, 답변과 지원 확장자는 미확인 | [modifactory.com](https://www.modifactory.com/) |
| 90분 | "물리 기반 검증, 배치, 배선"을 90분 이내에 수행. PCB 밀도와 서버 환경에 따라 달라질 수 있다고 명시 | [modifactory.com](https://www.modifactory.com/); [블로그 insights-001](https://www.modifactory.com/blog/ko/insights-001) |
| AI 설계안(설계 근거 포함) | 배치·배선을 마친 레이아웃 후보 여러 개. 배치 노트(디커플링 커패시터 거리, 노이즈 취약 부품 격리 이유 등)와 배선 노트(경로 자유도, 통로 포화도, 교차 빈도, 정렬 민감도의 4개 지표) | [modifactory.com/ko](https://www.modifactory.com/ko) (검색 요약 기준) |
| 회원가입만으로 즉시 시작 | 설치나 라이선스 구매 없이 웹 브라우저에서 사용. 2026년 말까지 가입하면 전 기능 무료 | [네이트뉴스](https://news.nate.com/view/20260911n18067); [event-001](https://www.modifactory.com/news/en/event-001) |
| 초보자도 막힘없는 자동 설계 | 자동 배치·배선. 커넥터, MCU, 외곽선 같은 핵심 부품을 고정(Lock)하고 나머지만 재배치 | [modifactory.com/ko](https://www.modifactory.com/ko) |
| 다양한 포맷으로 출력 | 확인된 출력은 Gerber 생성·다운로드뿐. Altium Designer 플러그인(전용 메뉴, 도킹 패널)은 있음. ODB++, IPC-2581, KiCad 네이티브 등은 미확인 | [JLCPCB 직구 가이드](https://www.modifactory.com/blog/ko/jlcpcb-order-guide); [modifactory.com/ko](https://www.modifactory.com/ko) |

이 표에서 가장 중요한 사실은 **입력이 "회로도와 레이아웃 파일"이라는 점**이다. 모디팩토리의 "AI 설계안"은 요구사항을 받아 회로를 새로 만드는 결과물이 아니다. 이미 확정된 회로도(넷리스트)와 보드 외곽·풋프린트 정보를 받아 **부품 배치와 배선까지 끝낸 레이아웃 후보**를 돌려준다. 따라서 "초보자도 막힘없는"이라는 약속은 회로 설계를 마친 사람이 PCB 아트웍 단계에서 막히지 않는다는 뜻으로 읽어야 한다. 회로도를 그릴 줄 모르는 완전한 입문자에게는 해당하지 않는다. 사용 흐름은 가입, 파일 업로드, 웹 작업 화면에서 자동 배치·배선 실행, 노트로 AI 판단 검토, 메뉴에서 Gerber 생성·다운로드, JLCPCB 등에 발주 순서다. 회사 블로그는 "배치·배선 최종 검토 후 몇 번의 클릭으로 추출이 완료"된다고 설명한다([JLCPCB 직구 가이드](https://www.modifactory.com/blog/ko/jlcpcb-order-guide)). 블로그에는 JLCPCB 직구, 풋프린트 실수, 레이어 수 선택 같은 실무 입문 글이 올라 있다([블로그 목록](https://www.modifactory.com/blog/ko/all); [footprint 글](https://www.modifactory.com/blog/en/top-3-pcb-footprint-mistakes)). 메이커와 스타트업 하드웨어 개발자를 끌어들이려는 콘텐츠 마케팅이다.

반면 Lock 기능과 Altium 플러그인은 현업 엔지니어용 기능이다. 플러그인을 설치하면 Altium Designer 안에 전용 메뉴와 도킹 패널이 생긴다. 사용자는 창을 바꾸지 않고 자동 배치·배선을 돌릴 수 있고, 고정한 부품 좌표는 그대로 유지된다([modifactory.com/ko](https://www.modifactory.com/ko)). 결국 모디팩토리는 입문자와 현업 엔지니어라는 두 시장을 동시에 겨냥한다. 2027년 이후 요금은 공개되지 않았다. "무료 요금제로 사용자를 늘린 뒤 구독형을 도입한다"는 계획만 보도됐다([네이트뉴스](https://news.nate.com/view/20260911n18067)). 지원 레이어 수, 최대 부품 수, 고속 신호·차동쌍·임피던스 제어 지원 여부도 확인되지 않는다. 90분이 보장 시간인지 평균 시간인지도 알 수 없다.

### 기술은 '에어와이어' 특허와 채용공고로만 짐작할 수 있다

럭스로보는 모델 구조, 학습 데이터, 기술 논문을 공개하지 않았다. 공개된 단서는 세 가지다. 첫째는 제품 설명의 변화다. 2024년 CES 버전은 "AI 챗봇 GPT-4를 접목해 사용자와의 채팅을 기반으로 필요한 회로 부품을 추천"하는 올인원 플랫폼으로 소개됐다([전자신문](https://www.etnews.com/20240104000261), 검색 요약 기준). 2026년 버전의 설명은 "physics-based verification, placement, and routing"으로 바뀌었다([modifactory.com](https://www.modifactory.com/)). 2년 사이에 대화형 부품 추천에서 배치·배선 자동화로 초점이 좁혀진 것이다.

둘째는 특허다. 럭스로보가 **「부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법」** 특허로 2026 대한민국 우수특허대상을 받았다고 기업정보 사이트에 적혀 있다. 이 특허는 물리 배선 전 단계의 부품 간 가상 연결선을 '에어와이어'로 정의한다. 그리고 에어와이어의 길이, 밀집도, 교차 같은 구조 데이터로 배치와 배선 경로를 미리 최적화한다. 보도는 이 특허를 모디팩토리의 핵심 엔진으로 소개한다([TheVC](https://thevc.kr/luxrobo)). KIPRIS 접근이 막혀 특허번호, 출원일, 청구항은 확인하지 못했다. 럭스로보 보유 특허 수도 같은 기업정보 페이지를 두고 검색 요약이 29건과 34건으로 엇갈린다.

셋째는 채용공고다. 원티드 공고에서는 PCB AI 라우터와 자동 배선 알고리즘 개발자, **LLM 기반 PCB 부품 자동 배치 모델**(회로 설계 규칙과 PCB 데이터로 주요 부품의 위치·방향 결정) 개발자, 회로 시뮬레이션 엔진 개발자를 찾는다([원티드: 라우터](https://www.wanted.co.kr/wd/382684); [원티드: LLM Placement](https://www.wanted.co.kr/wd/382685); [원티드: 시뮬레이션](https://www.wanted.co.kr/wd/382675)). 2024년에 "자동설계 관련 국가 R&D"를 수행한 이력도 있지만 사업명과 금액은 확인하지 못했다([TheVC](https://thevc.kr/luxrobo)).

이 단서들을 겹쳐 보면 흥미로운 대응이 보인다. 배선 노트의 네 지표(경로 자유도, 통로 포화도, 교차 빈도, 정렬 민감도)는 특허가 말하는 에어와이어의 길이·밀집도·교차 특징과 거의 같은 개념을 쓴다. 설계 근거가 LLM의 자유 서술이 아니라 **엔진이 실제로 계산한 기하·그래프 특징에 기반한다면**, 2절에서 볼 학계 권고(측정값에 근거한 설명)와 맞아떨어진다. 반대로 채용공고에 나온 "LLM 기반 부품 배치" 방향은 LLM의 공간 추론이 약하다는 2026년 벤치마크 결과와 긴장 관계에 있다. 두 해석 모두 추론이다. 회사가 엔진 구조를 공개하기 전까지는 검증할 수 없다.

### '글로벌 톱3'는 수상이 아니라 최종 후보 3곳 중 하나였다

| 시점 | 사건 | 근거 |
|---|---|---|
| 2014-11-13 | 럭스로보 설립 | [TheVC](https://thevc.kr/luxrobo) |
| 2022년~ | 모디팩토리 자체 개발 시작(검색 요약 기준) | [뉴스톱](https://www.newstopkorea.com/news/articleView.html?idxno=41685) |
| 2023년 | 홍보 영상 제작(영상 제작사 포트폴리오) | [4bfilm](https://4bfilm.com/portfolio-item/%EB%9F%AD%EC%8A%A4%EB%A1%9C%EB%B3%B4-%EB%AA%A8%EB%94%94%ED%8C%A9%ED%86%A0%EB%A6%AC/) |
| 2024-01-04 | CES 2024에서 GPT-4 기반 'AI 올인원 플랫폼'으로 첫 공개 | [전자신문](https://www.etnews.com/20240104000261) |
| 2024-04-16 | 기술성 평가 A등급, 삼성증권 주관 IPO 추진(이후 자진 철회, 날짜 미확인) | [메트로신문](https://www.metroseoul.co.kr/article/20240416500511) |
| 2025-10 | Pre-IPO 투자 유치 | [TheVC](https://thevc.kr/luxrobo) |
| 2026-02-23 | embedded award 2026 Tools 부문 후보 3곳 발표(MODI Factory, Ambiq HeliaAOT, Parasoft C/C++test CT) | [embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/02/tools-nominees) |
| 2026-03-10 | 뉘른베르크 시상식. Tools 부문 수상작은 Ambiq HeliaAOT | [embedded-world.de](https://www.embedded-world.de/en/knowledge/2026/03/winner-embedded-awrd-2026) |
| 2026-03-16 | 국내 언론 "글로벌 톱3" 보도. 당시 정식 출시 전 베타. 한국·미국·인도 글로벌 베타와 EDA 기업 협업 "방침" | [서울경제](https://www.sedaily.com/article/20019757) |
| 2026-07-21 | "AI·로봇 회로설계 자동화 플랫폼 개발 총력" 보도 | [네이트뉴스](https://m.news.nate.com/view/20260721n00645) |
| 2026-09-11 | "2026 하반기 혁신 IT 대상" 보도 | [네이트뉴스](https://news.nate.com/view/20260911n18067) |
| 2026년(게시일 미확인) | 2026년 말까지 가입하면 전 기능 무료 이벤트 | [modifactory.com](https://www.modifactory.com/news/en/event-001) |

국내 보도는 모디팩토리가 "Embedded World 2026 설계 자동화 부문 글로벌 톱3, 아시아 기업 중 유일"이라고 전했다([서울경제](https://www.sedaily.com/article/20019757); [뉴스토마토](https://www.newstomato.com/ReadNews.aspx?no=1294739)). 이 표현은 바로잡아 읽어야 한다. 모디팩토리는 **embedded award 2026 Tools 부문 최종 후보(nominee) 3곳 중 하나**였다. 3월 10일 시상식에서 이 부문 **수상작은 Ambiq Micro의 HeliaAOT**였다([embedded-world.de 수상작](https://www.embedded-world.de/en/knowledge/2026/03/winner-embedded-awrd-2026); [Electronics Era](https://electronicsera.in/ambiq-wins-embedded-world-2026-award-for-heliaaot/)). 후보에 오른 것은 국제 전시회가 이 도구를 PCB 배치·배선 병목을 AI로 푸는 제품으로 인정했다는 의미가 있다. 하지만 "수상"이라고 쓰면 틀린 말이다.

같은 기사들이 전한 **알티움·지멘스EDA·케이던스와의 협업도 2026년 3월 시점에 회사가 밝힌 계획(방침)일 뿐**이다. 실제로 체결된 파트너십을 보여 주는 근거는 찾지 못했다([서울경제](https://www.sedaily.com/article/20019757)). 현재 확인되는 EDA 연동은 럭스로보가 직접 만든 Altium 플러그인뿐이다. JLCPCB와도 발주 가이드 블로그가 있을 뿐 공식 제휴 표시는 없다. CES 혁신상은 MODI 교구 시절의 이력이며 모디팩토리가 받은 상이 아니다. "혁신 IT 대상"은 언론사가 주최하는 기획상으로 보이며, 주최와 심사 방식은 확인하지 못했다.

2026년 3월에는 '베타'였던 서비스가 지금은 무료 프로모션으로 공개 운영되고 있다. 정식 출시(GA)를 공식 발표했는지는 확인되지 않는다. 가입자 수, 처리한 설계 건수, 기업 고객은 공개되지 않았다. 한 보도는 "모디팩토리 단일 프로젝트로 유료 매출 5억 원, 유저 1만 명"을 목표로 제시했다([뉴스토마토](http://www.newstomato.com/readnews.aspx?no=1287248), 게재일 미확인, 스니펫 기준). 확인된 사용자 후기는 공식 사이트에 실린 추천사뿐이다. 수동 라우팅 시간을 60분 줄였다는 후기, "4년차 엔지니어급 품질"이라는 후기, 서버 접근 권한과 암호화 방식을 확인한 뒤 도입했다는 보안 관련 후기, Altium 플러그인이 "기대된다"는 후기가 있다([modifactory.com/ko](https://www.modifactory.com/ko), 검색 요약 기준). 독립적인 커뮤니티 반응이나 제3자 성능 벤치마크는 찾지 못했다. 다만 검색 범위가 제한적이었으므로 그런 자료가 없다고 단정할 수는 없다.

## 2. 학계는 보드 레벨 AI 레이아웃을 아직 '전문가 검토용 초안'으로 본다

ML·LLM for EDA 서베이는 대부분 칩(VLSI) 흐름이 중심이다. 고전 서베이인 Huang 외(ACM TODAES 2021)와 LLM-EDA 서베이(Pan 외 2025, He 외 2025)는 PCB를 거의 다루지 않는다([arXiv 2102.03357](https://arxiv.org/abs/2102.03357v2); [arXiv 2501.09655](https://arxiv.org/pdf/2501.09655); [FnT EDA](https://www.emerald.com/fteda/article/14/4/295/1325096/Large-Language-Models-for-EDA-From-Assistants-to)). PCB 생애주기 전체를 다룬 첫 생성형 AI 서베이는 2026년 6월 UNSW의 Srinivasan·Turnbull·Pearce 논문이다. 이 서베이는 **도메인 특화 데이터의 부족과 기존 PCB 도구와의 통합 부족**을 핵심 장애물로 꼽는다. 또 현재 주류 접근은 LLM이 보드를 직접 그리는 방식이 아니라, 기존 EDA용 스크립트를 생성하는 방식이라고 정리한다([arXiv 2606.17074](https://arxiv.org/pdf/2606.17074); [alphaXiv 한글 요약](https://www.alphaxiv.org/ko/abs/2606.17074)). 기존 Altium·KiCad 파일을 받아 처리하는 모디팩토리의 구조는 이 "통합 부족" 틈을 겨냥한다고 볼 수 있다.

### 배치는 GPU 해석적 기법과 사전학습 강화학습이 가장 앞서 있다

보드 레벨 배치에서 가장 성숙한 접근은 두 갈래다. 하나는 강화학습(RL) 정책을 오프라인으로 학습한 뒤 새 회로에 일반화하는 방식이다. 몰타대 Vassallo와 Bajada(DATE 2024)는 TD3와 SAC 정책으로 배치 기법을 학습했다. 학습에 쓰지 않은 회로에서 라우팅 후 배선 길이가 최신 simulated annealing(SA) 대비 각각 **17%, 21% 줄었다**([UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)). 코드(RL_PCB)는 MIT 라이선스로 공개됐고 KiCad 파일 파싱을 포함한다([GitHub](https://github.com/LukeVassallo/RL_PCB)).

다른 하나는 VLSI의 해석적(analytical) 배치를 GPU로 가속해 PCB에 옮긴 방식이다. Cornell과 NVIDIA의 **Cypress(ISPD 2025 최우수논문)**는 DREAMPlace 기반 기법을 PCB용 비용함수와 제약에 맞게 바꿨다. 그 결과 SA-PCB 대비 routability가 1~5.9배 높아졌고 런타임은 **최대 492.3배 빨라졌다**([Cypress 논문](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf); [수상 공지](https://zhang.ece.cornell.edu/news/cypress_ispd_bpa.html)). 저자들은 PCB 배치가 여전히 수작업에 의존해 "수 주"가 걸린다고 지적한다. 공개 벤치마크는 부품 41~476개의 소규모 세트와 5,118~6,628개의 대규모 세트로 구성된다([GitHub NVlabs/Cypress](https://github.com/NVlabs/Cypress)).

A*STAR의 Lim(2026)은 주 부품을 보드 중앙에 고정하고, 수동소자를 전원 핀 근처에 두는 원칙으로 탐색 공간을 줄였다. 저자는 실제 PCB 9개 이상에서 "사람 수준에 가까운" 배치를 얻었다고 주장한다([arXiv 2602.23540](https://arxiv.org/html/2602.23540v1)). 설계 논리가 정책 구조에 드러나 있어서 설명문으로 바꾸기 쉬운 형태다.

칩 분야의 AlphaChip(Nature 2021)은 영향력이 크지만 재현 논쟁에 걸려 있다. UCSD의 Cheng·Kahng 외(ISPD 2023, 2026년 3월 v3)는 Nature 결과를 완전히 재현하지 못했다. 이들은 강화한 SA와 인간 기준선이 최신 AlphaChip보다 여전히 우수하다고 보고했다([arXiv 2302.11014](https://arxiv.org/abs/2302.11014v3)). Markov도 비슷한 비판을 냈다([deeppaper 요약](https://arxiv.deeppaper.ai/papers/2306.09633v10?locale=en)). Google 측은 방법론을 제대로 적용하지 않은 평가라고 반박했고([arXiv 2411.10053](https://arxiv.org/abs/2411.10053v1)), 논쟁은 아직 이어지고 있다([CACM](https://cacm.acm.org/news/updates-spark-uproar)). 이 논쟁에서 PCB 서비스가 얻을 교훈은 분명하다. **"AI라서 더 낫다"는 주장은 강한 SA나 상용 기준선과 공개 벤치마크로 비교하기 전까지 마케팅에 쓰면 안 된다.**

90분이라는 시간 약속에 비춰 보면 문헌은 한 가지 방향을 가리킨다. DeepPCB는 2019년 출시 당시 2층·최대 150쌍 보드의 결과를 24시간 안에 돌려줬다([PCD&F](https://www.pcdandf.com/pcdesign/index.php/editorial/menu-new-indust-prod/17292-instadeep-releases-deeppcb-ai-pcb-routing-platform)). 요청이 들어올 때마다 학습하는 방식은 90분 약속과 맞지 않는다. 사전학습된 정책, GPU 해석적 배치, 결정론적 라우터, LLM 서술을 묶은 파이프라인이 문헌상 가장 현실적이다. 다만 이런 종단 처리 시간을 직접 측정한 학술 연구는 없다.

### 배선에서는 학습형 라우터가 아직 규칙 기반을 넘지 못했다

PCB 배선의 학습 기반 연구는 부분 문제에 집중돼 있다. FanoutNet(AAAI 2023)은 라우팅 전 단계인 팬아웃을 PPO 강화학습으로 자동화했다([AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26030)). Unet-Astar(IEEE Access 2023)는 딥러닝이 A* 라우터에 탐색 영역을 추천해 속도를 높인다([DOAJ](https://doaj.org/article/be16200414264fe48da8f179bd034013)). DQN 이스케이프 라우팅(SPIE 2025)은 25×26 격자 수준의 장난감 규모에 머문다([SPIE](https://remotesensing.spiedigitallibrary.org/conference-proceedings-of-spie/13510/135101B/Escape-routing-using-deep-reinforcement-learning/10.1117/12.3058004.full)). ISQED 2026의 보안 인지 라우팅은 A*에 배선을 맡기고 RL은 테스트 포인트 위치만 고르게 했다. 이 방식으로 평가 보드에서 100% 배선 성공을 보고했다([ISQED 2026](https://isqed.org/English/Archives/2026/Technical_Sessions/131.html)).

결정적인 진단은 한국에서 나왔다. **LG AI연구원의 PCBWorld**(arXiv 2607.05915, KDD 2026 워크숍)는 KiCad 엔진 위에 만든 오픈소스 배선 환경이다. 실제 오픈소스 보드 679개와 엔진이 채점하는 지표 8개로 RL 정책과 LLM 에이전트를 같은 기준에서 비교한다. 초록은 **학습 기반 PCB 라우팅이 여전히 규칙 기반 라우터에 뒤처진다**고 명시한다([arXiv](https://arxiv.org/abs/2607.05915); [요약](https://djaym7-arxivmedia.hf.space/post/256186)). 후속 연구 CADET(arXiv 2611.16913)은 합성 시연 데이터로 행동 복제를 한 뒤 RL로 미세조정했다. 그 결과 실제 테스트 보드에서 DRV(설계 규칙 위반) 없는 배선 완료율이 **38.0%에서 67.2%로** 올랐다([arXiv](https://arxiv.org/html/2611.16913)). 개선 폭은 크지만, 3분의 1은 여전히 실패한다. 고속 신호, 차동쌍, 길이 매칭, 임피던스 제어를 ML로 다룬 동료심사 PCB 논문은 찾지 못했다. 이 영역은 규칙과 제약 기반으로 처리하고, 설계 근거에 "적용한 제약"과 "검증하지 않은 항목"을 명시하는 것이 안전하다.

### 2026년 벤치마크는 'DRC 통과'와 '실제 동작' 사이의 큰 간극을 드러냈다

2026년에는 ICLR, ICML, NeurIPS에 PCB 전용 벤치마크가 한꺼번에 나왔고, 결과는 일관되게 비관적이다. **EDA Bench(ICML 2026)**에서 최강 하네스는 35개 과제 중 21개를 빌드했지만 종합 점수는 **4.58%**였다. 저자들은 결과물이 "파싱되고 그럴듯해 보여도 전기적으로 동작하지 않는다"고 결론지었다([ICML](https://icml.cc/virtual/2026/77908)). **PCB Gym(NeurIPS 2026)**에서 프런티어 LLM이 DRC를 통과하고 완전히 배선된 보드를 낸 비율은 약 **32.1%**였다. 흔한 실패는 전원 레일을 일반 신호 넷처럼 다룬 것이었다([NeurIPS](https://neurips.cc/virtual/2026/161602)). **PCBInnoBench(NeurIPS 2026)**의 최고 Pass@1은 전문가 가이드가 있을 때 22.0%, 없을 때 7.3%였다([NeurIPS](https://neurips.cc/virtual/2026/poster/139034)). PCB-Bench(ICLR 2026)와 OmniLayout(arXiv 2026, 산업급 레이아웃 1,681개)도 LLM의 공간·기하 추론, 제약 준수, routability 최적화가 약하다고 보고했다([ICLR](https://iclr.cc/virtual/2026/poster/10009621); [arXiv 2607.03261](https://arxiv.org/abs/2607.03261)). 이 결과는 모디팩토리의 품질 주장을 해석하는 기준이 된다. DRC 통과율만으로는 부족하고, ERC, 전원 무결성, 기능 검사를 함께 봐야 한다.

회로도 생성 쪽은 성과가 더 낫지만, 과제가 단순할 때로 한정된다. KIT·Bosch Sensortec의 pcbGPT는 임베디드 과제 20개에서 pass@1 0.90을 기록했다. 그래도 저자들은 결과물이 "전문가 리뷰를 대체할 만큼 신뢰할 수 없다"고 결론지었다([arXiv 2606.01188](https://arxiv.org/pdf/2606.01188)). UCSD·MSRA의 SchGen은 KiCad 회로도를 생성하는 Python 코드를 출력하는 방식으로 유효 회로율 82%, 전문가 검증 기능 정확도 60.5%를 냈다. 원시 KiCad 파일을 직접 생성한 기준선은 각각 32.45%와 3.0%에 그쳤다([alphaxiv](https://www.alphaxiv.org/abs/2605.30345.md); [GitHub](https://github.com/microsoft/SchGen)). 반면 실보드 수준의 HWE-Bench(과제 300개)에서 최고 통과율은 **8.15%**였다. 이 수치는 제3자 요약에서만 확인했다([emergentmind](https://www.emergentmind.com/papers/2603.18102)).

PCBSchemaGen은 판마다 수치가 맞지 않는다. v1은 23개 회로로 평가했고([arXiv 2602.00510](https://arxiv.org/html/2602.00510v1)), NeurIPS 2026 판은 22개 도메인 227개 과제로 평가했다([NeurIPS](https://neurips.cc/virtual/2026/poster/149018)). 2026년 7월 DOE 리뷰 슬라이드는 65개 과제에서 Pass@1 77.5%, 전문가 대비 37배 빠르고 570배 저렴하다고 주장한다([DOE 슬라이드](https://doepeerreview.sandia.gov/app/uploads/sites/82/2026/07/Han_Peng_20260727_DOE_Review_AIPE.pdf)). 벤치마크 규모가 서로 달라 이 수치들은 확정할 수 없다.

성공한 시스템의 공통점은 **코드나 DSL 같은 중간표현과 결정론적 검증기 루프**다. 데이터시트에서 심볼과 풋프린트를 생성하는 SFgen의 풋프린트 정확도가 80%에 머문다는 결과도([arXiv 2607.19767](https://arxiv.org/pdf/2607.19767)) 사람의 검증이 여전히 필요하다는 점을 보여 준다.

### 설계 근거를 다루는 연구는 비어 있어 기회이자 검증 공백이다

EDA 분야에서 설명가능성(XAI) 연구는 매우 적다. 가장 직접적인 선례는 UW–Madison·IBM의 Zeng 외(DATE 2020)다. 이 연구는 랜덤포레스트로 칩의 DRC 핫스팟을 예측하고 SHAP으로 개별 예측을 설명했다([DATE 2020](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)). MLCAD 2023 논문은 전통 EDA 방법이 해석 가능성에서 ML보다 낫다고 지적한다([CUHK](https://www.cse.cuhk.edu.hk/~byu/papers/C176-MLCAD2023-MLEDA.pdf)). PCB 배치·배선 결정을 설명하는 전용 연구는 찾지 못했다. LLM이 생성한 설계 근거의 정확도나 환각을 평가한 연구도 없었다.

최근 흐름은 LLM 서술 자체보다 "검증 가능한 근거"에 기대는 쪽이다. AllSpice의 **DRCY**(arXiv 2603.15672, CAIS 2026 데모)는 회로도 연결을 부품 데이터시트와 대조하고, 비평(critic) 에이전트가 추출 품질을 점수화한다. 회사 자체 보고에 따르면 설계 리뷰 11건에서 사람 리뷰를 통과한 실제 이슈 4건을 찾았다. 오탐률은 공개하지 않았고, 회사 스스로 "사람의 판단을 대체하지 않는다"고 밝혔다([arXiv](https://arxiv.org/abs/2603.15672); [AllSpice](https://www.allspice.io/post/under-the-hood-how-drcy-reviews-your-schematics)). PCBSchemaGen의 5층 검증기는 **핀 단위 오류 위치**를 알려 준다([NeurIPS](https://neurips.cc/virtual/2026/poster/149018)).

이 문헌들을 종합하면, 신뢰할 수 있는 설계 근거는 세 층으로 쌓아야 한다. 첫째 층은 결정론적 측정값(DRC, ERC, 넷 길이, 혼잡도)이다. 둘째 층은 데이터시트와 설계 규칙의 인용이다. 셋째 층이 LLM의 자연어 서술이며, LLM은 앞의 두 층에 없는 주장을 하지 못하도록 막아야 한다. 모디팩토리의 'AI 노트'는 바로 이 공백에 놓여 있다. 비교할 학술 기준이 없어 검증이 어렵지만, 그만큼 선점할 여지가 큰 영역이다.

### 국내 학술 연구는 KAIST의 패키지 강화학습과 LG AI연구원의 배선 벤치마크로 양분된다

웹 검색 범위 안에서 **AI/ML로 PCB 부품 배치나 배선을 다룬 KCI 등재 논문은 한 편도 확인하지 못했다.** 국내 학술지의 PCB 자동화 연구는 비AI 알고리즘 연구가 대부분이다. 2003년의 Shape-based 자동 배치([KCI](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART000904787)), 2001년의 최단경로 자동 배선([DBpia](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06329246)), 2011년의 임피던스 시뮬레이터([KCI](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001612461)) 등이 있다. 최근 사례는 생성형 AI로 회로도 파일을 분석해 테스트 포인트 누락과 디커플링 커패시터 거리를 검사하는 2025년 한국산학기술학회 포스터 정도다([KAIS 포스터](https://www.kais99.org/jkais/springNfall/spring2025/poster/2025_spring_227.pdf)). 국내 "PCB × AI" 연구는 압도적으로 결함 검사(AOI) 쪽에 몰려 있다([KoreaScience](https://koreascience.kr/article/CFKO202419335083786.pdf)). KCI, RISS, DBpia를 직접 조회하지 못했으므로 이 공백은 "검색으로 확인되지 않음"이라는 뜻이다. 자료가 없다는 증거는 아니다.

국제 수준의 기여는 두 곳에서 나온다. 첫째는 **KAIST TeraLab(김정호 교수)**이다. 이 연구실은 SI/PI 물리 지표를 보상으로 삼아 패키지·HBM의 디커플링 커패시터 배치를 강화학습으로 최적화해 왔다. IEEE TCPMT 2020([DOI](https://doi.org/10.1109/TCPMT.2020.2972019)), EPEPS 2021([KAIST EE](https://ee.kaist.ac.kr/ai-in-wave/deep-reinforcement-learning-framework-for-optimal-decoupling-capacitor-placement-on-general-pdn-with-an-arbitrary-probing-port-epeps-2021/)), DesignCon 2025 Best Paper([KAIST EE 뉴스](https://ee.kaist.ac.kr/en/research-achieve/dr-taein-shin-from-professor-jeongho-kims-research-lab-selected-for-best-paper-award-at-designcon-2025-international-conference/))가 이 계열의 성과다. 박진규 교수 연구실과 함께 낸 **DevFormer(ICML 2023)**는 오프라인 데이터만으로 학습해 부품 수를 30% 이상 줄였다([PMLR](https://proceedings.mlr.press/v202/kim23h.html)). 이 흐름은 2025년 HBM 로드맵의 LLM 설계 에이전트([HBM Roadmap PDF](https://aionet.tech/KAIST_HBM_Roadmap.pdf))와 2026년 7월 **KiCad MCP 기반 패키지 설계 AI 에이전트** 워크숍으로 이어지고 있다([Korea Times](https://www.koreatimes.co.kr/amp/southkorea/education/20260702/kaist-workshop-to-showcase-ai-agents-for-hbm-design-automation)). 다만 대상은 일반 보드가 아니라 패키지다. "HBM 인터포저 배선 RL"은 로드맵 단계로만 확인된다.

둘째는 **LG AI연구원**이다. 앞서 본 PCBWorld와 CADET 외에, 블로그에서 RRT 기반 연속공간 배선(RRT-PCB)을 LG 계열사 실제 제품으로 검증했다고 소개한다([LG AI Research 블로그](https://www.lgresearch.ai/blog/view?seq=509)). 학위논문은 KAIST의 2019년 DQN 디캡 설계 석사논문([KOASAS](https://koasas.kaist.ac.kr/handle/10203/266736))처럼 패키지 수준 연구만 확인됐다. 일반 보드의 배치·배선을 다룬 학위논문은 찾지 못했다.

특허 측면에서는 공개 정보 기준으로 럭스로보의 에어와이어 특허가 사실상 유일한 국내 "AI PCB 설계" 특허로 보인다. 이름이 비슷한 KR102208989B1 「강화 학습을 통한 디바이스 배치 최적화」는 패밀리 정보로 볼 때 Google의 연산 그래프 디바이스 배치 특허로 추정되며, PCB 특허가 아니다([Google Patents](https://patents.google.com/patent/KR102208989B1/enExample)). 국가 R&D의 "설계 AI" 예산은 칩에 몰려 있다. 2024년 AI-반도체 이니셔티브의 "머신러닝 적용 설계 툴"([국가과학기술자문회의](https://www.pacst.go.kr/jsp/m/initiative/ai_initiative_intro.pdf)), 2025년 과기정통부 AI반도체 최적화 설계지원 198억 원([SVA Korea](https://svakorea.org/news/429)), 2026년 산업통상부 K-온디바이스 AI반도체 사업 8,002억 원([머니투데이](https://www.mt.co.kr/economy/2026/06/15/2026061509331190266))이 그 예다. **PCB 설계 자동화를 명시한 국가 과제는 확인하지 못했다.**

| 주제 | 대표 연구 | 핵심 결과(초록·스니펫 기준) | 모디팩토리에 대한 함의 |
|---|---|---|---|
| 배치: 강화학습 | Vassallo & Bajada, DATE 2024 ([UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)) | 학습하지 않은 회로에서 SA 대비 배선 길이 17~21% 감소 | 사전학습 정책은 추론이 빨라 90분 약속에 맞음 |
| 배치: GPU 해석적 | Cypress, ISPD 2025 최우수논문 ([PDF](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)) | routability 1~5.9배, 최대 492.3배 가속 | 90분 내 처리에 가장 현실적인 1차 엔진, 공개 벤치마크로 비교 가능 |
| 배치: 규칙을 내재한 RL | Lim, arXiv 2026 ([arXiv](https://arxiv.org/html/2602.23540v1)) | 수동소자를 전원 핀 근처에 배치, "사람 수준에 가까움"(저자 주장) | 배치 노트 같은 설명으로 바꾸기 쉬운 구조 |
| 칩 배치 재현 논쟁 | AlphaChip(Nature 2021) vs Cheng 외(ISPD 2023) ([arXiv](https://arxiv.org/abs/2302.11014v3)) | 강화한 SA와 인간 기준선이 우수하다는 반론 | 강한 기준선 비교 없는 "AI 우위" 주장은 위험 |
| 배선: 학습 가이드 | Unet-Astar(IEEE Access 2023), FanoutNet(AAAI 2023) ([DOAJ](https://doaj.org/article/be16200414264fe48da8f179bd034013); [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26030)) | 검증된 탐색(A*)에 학습을 가이드로 추가 | 결정론적 라우터와 ML 가이드의 하이브리드가 합리적 |
| 배선 벤치마크(국내) | PCBWorld, CADET (LG AI연구원) ([arXiv](https://arxiv.org/abs/2607.05915); [arXiv](https://arxiv.org/html/2611.16913)) | 학습형이 규칙 기반에 열세, DRV 없는 완료율 38.0%→67.2% | 국산 공개 벤치마크로 성능을 공개할 수단 |
| LLM 에이전트 레이아웃 | EDA Bench, PCB Gym, PCBInnoBench ([ICML](https://icml.cc/virtual/2026/77908); [NeurIPS](https://neurips.cc/virtual/2026/161602)) | 4.58%, 32.1%, 22.0%/7.3% | "DRC 통과 ≠ 기능 동작", 품질 지표 확장 필요 |
| LLM 회로도 생성 | pcbGPT, SchGen, HWE-Bench ([arXiv](https://arxiv.org/pdf/2606.01188); [alphaxiv](https://www.alphaxiv.org/abs/2605.30345.md)) | 단순 과제 0.90, 실보드 과제 8.15%(제3자 요약) | 회로도 생성으로 확장한다면 중간표현과 검증기 루프가 필수 |
| 설계 리뷰·근거 | DRCY(AllSpice 2026), Zeng 외(DATE 2020) ([arXiv](https://arxiv.org/abs/2603.15672); [DATE](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)) | 데이터시트 대조 리뷰, SHAP 기반 설명 | AI 노트는 측정값과 데이터시트 인용에 근거해야 함 |
| SI/PI 인지 배치(국내) | KAIST DevFormer(ICML 2023) ([PMLR](https://proceedings.mlr.press/v202/kim23h.html)) | 디캡 부품 수 30% 이상 감소 | 고속 보드로 확장할 때 협력·참조 대상 |
| PCB 생성형 AI 서베이 | Srinivasan 외(UNSW 2026) ([arXiv](https://arxiv.org/pdf/2606.17074)) | 데이터 부족과 도구 통합 부족이 핵심 장애물 | 기존 EDA 파일을 받는 구조가 통합 공백을 메움 |

## 3. 해외에는 Quilter라는 근접 경쟁자가 있고, 국내에는 같은 형태의 서비스가 없다

### Quilter와 DeepPCB가 '업로드형 자동 레이아웃'을 먼저 상용화했다

"파일을 올리면 AI가 배치와 배선을 해 준다"는 모디팩토리의 형태와 가장 닮은 해외 제품은 **Quilter**다. 2019년에 설립됐고, 창업자 Sergiy Nesterenko는 SpaceX에서 Falcon 9 2단용 전자장치를 개발했다([CB Insights](https://www.cbinsights.com/company/quilter)). 2024년 2월 Benchmark 주도로 Series A $10M을, 2025년 10월 Index Ventures 주도로 **Series B $25M**을 유치했다([I-Connect007](https://iconnect007.com/article/147236/quilter-secures-25m-series-b-to-eliminate-manual-pcb-design-with-physicsdriven-ai/147233/design); [Pulse 2.0](https://pulse2.com/quilter-25-million-series-b-raised-for-automating-pcb-design-with-physics-driven-ai/)). 누적 투자액은 출처에 따라 $35M, $40M, $50M으로 다르다([Seedtable](https://seedtable.com/companies/quilter); [CapLight](https://www.caplight.com/company/quilter)).

Quilter는 Altium, Cadence, Siemens, KiCad 파일을 받는다. 여러 스택업을 동시에 평가해 레이아웃 후보를 여러 개 만들고 순위를 매긴다. 후보마다 임피던스 제어, 리턴 전류 연속성, 디커플링 효율 같은 **물리 기반 design review**가 붙는다([Quilter Help](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work)). 출력은 RS-274X Gerber와 Excellon 드릴 파일이다([Quilter 블로그](https://www.quilter.ai/blog/from-ai-design-to-manufacturing-how-quilter-automates-gerber-drill-and-fab-file-generation)). 대표 사례인 Project Speedrun은 부품 843개짜리 8층 보드 2장으로 이뤄진 리눅스 컴퓨터다. 사람 작업 시간은 38.5시간이었고 첫 시도에 부팅에 성공했다. 다만 비교 대상인 428시간은 외부 업체의 견적일 뿐 실험값이 아니고, 레이아웃 생성 런타임 약 27시간은 회사 발표다([VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the)). 독립 매체 AtlasPCB는 Quilter의 결과물을 "표준 DRC를 통과하는 제조 가능한 출력"이라고, 회사 주장보다 좁게 평가한다([AtlasPCB](https://atlaspcb.com/blog/autonomous-pcb-layout-quilter-siemens-fuse-flux-2026)). 개인·학술용 무료 티어가 있지만 **무료 티어의 입력 파일은 학습에 쓰인다**. 상용 가격은 견적제다([Futurepedia](https://www.futurepedia.io/tool/quilter)).

**DeepPCB**는 BioNTech가 2023년에 인수한 InstaDeep의 강화학습 배치·배선 엔진이다([AIDb](https://theaidatabase.com/m/instadeep-deeppcb.html)). Altium .PcbDoc, KiCad 플러그인, EasyEDA Pro, Specctra DSN을 지원한다. Altium 안에서 바로 쓰는 "Route" 버튼은 아직 출시 예정 상태다([DeepPCB Help](https://deeppcb.ai/help/)). 무료 체험은 보드 1개, 30분까지다. 유료는 1시간 $30, 10시간 $280, 30시간 $800의 선불 시간권이다(제3자 집계, [cadalts](https://cadalts.com/tools/deeppcb/)). JLCPCB는 EasyEDA에서 배치를 마친 보드를 DeepPCB로 보내 배선하라고 권한다([JLCPCB 블로그](https://jlcpcb.com/blog/ai-tools-for-pcb-design)).

둘을 비교하면 모디팩토리의 "90분"이 어떤 의미인지 드러난다. 소형 보드 배선이 수 분 걸린다는 주장(DeepPCB, 경쟁사 작성 페이지 기준)과 843부품 보드 생성에 약 27시간이 걸린 사례(Quilter) 사이의 간격은 매우 넓다. 따라서 90분이라는 숫자 자체보다 **어떤 복잡도의 보드를 어느 단계까지 90분에 처리하는지**가 비교의 핵심이다.

### EDA 대기업은 보조형 AI에 머물고, 초보자 시장은 Flux가 선점하고 있다

기존 EDA 대기업도 2025~2026년에 AI 기능을 잇달아 냈지만, 대부분 숙련 설계자를 돕는 보조형이다. Cadence는 2023년 Allegro X AI를 냈다. 넷리스트와 제약을 받아 배치, 핵심 넷 배선, 전원 플레인을 생성하며 "수일에서 수분으로" 줄인다고 주장한다([Cadence](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2023/cadence-introduces-allegro-x-ai-accelerating-pcb-design-with.html)). 2026년 7월에는 에이전틱 플랫폼 AuraStack을 발표했다([Cadence Newsroom](https://newsroom.cadence.com/press-releases/press-release-details/2026/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging/default.aspx)). 그래도 애널리스트들은 PCB 설계가 여전히 "완전 자율이 아니라 고도로 보조받는 수준"이라고 평가한다([SiliconANGLE](https://siliconangle.com/2026/07/15/cadence-extends-ai-agents-beyond-chips-aurastack-circuit-boards-packaging/)).

Siemens는 중소기업용 PADS Pro Essentials와 Xpedition Standard를 내놨고, CELUS와 손잡아 AI 회로도 프런트엔드를 붙였다([All About Circuits](https://www.allaboutcircuits.com/news/siemens-unveils-ai-enhanced-pcb-design-tools-for-mid-range-users/); [Siemens](https://news.siemens.com/en-gb/siemens-celus/)). Zuken은 2026년 10월 CR-8000 2026에 AIPR(자율 배치·배선)과 설계 재사용 기능을 넣었지만, 스스로 AI 기능을 "실제적이지만 제한적"이라고 설명한다([Zuken](https://www.zuken.com/en/resource/cr-8000-2026-pcb-design-automation/); [Zuken 블로그](https://www.zuken.com/us/blog/ai-pcb-place-and-route-what-can-ai-actually-do-today/)).

주목할 점은 **Altium 자체에는 2026년 11월 현재 AI 배치·배선 기능이 확인되지 않는다**는 것이다. Altium의 MCP 서버도 "Coming Soon" 상태다([JLCPCB 블로그](https://jlcpcb.com/blog/ai-tools-for-pcb-design); [ProtoFlow, 경쟁사 작성](https://www.protoflow.ai/compare/best-ai-pcb-design-software-2026)). Autodesk Fusion과 EasyEDA도 1st-party AI 자동 배치가 없다([Autodesk](https://www.autodesk.com/products/fusion-360/blog/september-2026-major-product-update-whats-new/); [Adafruit](https://blog.adafruit.com/2026/09/19/jlc-puts-ai-assisted-board-design-in-files-you-can-read-review-and-edit/)). 모디팩토리의 Altium 플러그인은 바로 이 빈자리를 파고든다.

회로도 쪽, 즉 모디팩토리의 앞단에서는 VC 자금을 받은 스타트업이 경쟁한다. **Flux**는 텍스트 프롬프트로 보드를 설계하는 브라우저형 "AI 하드웨어 엔지니어"다. 2026년 2월 총 $37M을 유치했고 **가입자 100만 명**을 넘겨 초보자부터 전문가까지 아우른다([SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)). Pro 요금은 월 $250이다(2026년 10월 제3자 확인, [AnyGen](https://www.anygen.io/showcase/fluxai-review/index.html)). **Circuit Mind**는 블록도를 받아 회로도, BOM, FMEA를 만든다. 2026년 10월 $25M(누적 $33.4M)을 유치하며 데이터시트 대조 검증 에이전트 AVE를 출시했다([SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/)). **CELUS**는 사용 엔지니어 15,000명(2024년 10월)을 확보했다([ChannelLife](https://channellife.com.au/story/siemens-celus-team-up-to-revolutionise-pcb-design)).

회로를 코드로 표현하는 JITX(Series A $12M, [JITX](https://www.jitx.com/blog/series-a-announcement))와 Diode Computers(Series A $11.4M, Anthropic과 협업, [Dealroom](https://app.dealroom.co/news/feed/diode-computers-raises-11-4m-for-ai-pcb-design); [Diode 블로그](https://blog.diode.computer/anthropic-partnership))는 LLM 에이전트와 잘 맞는다. 하지만 진입 장벽이 높아 초보자용은 아니다. 2026년에는 Cherry Blossom, ProtoFlow 같은 프롬프트→보드형 신생 도구도 나왔다([Product Hunt](https://www.producthunt.com/products/cherry-blossom)). 이들은 대부분 대화형 에디터 UX다. "업로드하고 기다리면 완성안이 오는" 모디팩토리의 비동기 서비스형 UX와는 결이 다르다.

### 국내에는 인접 영역만 있고, 현실적 대안은 사람에게 맡기는 외주다

국내에서 "파일 업로드 후 AI가 PCB 배치·배선까지 생성"하는 일반 사용자용 웹 서비스는 **모디팩토리가 사실상 유일하게 확인된다.** 가장 가까운 국내 스타트업은 **세카(SECA)**다. 세카는 LG전자 사내벤처에서 분사해 2026년 6월 법인을 세웠다. 데이터시트, 회로도, BOM, 넷리스트를 지식그래프로 연결하고, AI 에이전트가 문서 간 불일치를 찾는다([ZDNet Korea](https://zdnet.co.kr/view/?no=20261008135433)). 2026년 11월 16일 TIPS에 선정됐고, 대형 제조기업 PoC에서 설계 공수를 66% 줄였다고 밝혔다. 다만 기사마다 절감 수치의 맥락(66%, 92%, 480→160시간)이 다르다([와우테일](https://wowtale.net/2026/11/16/268099/)). 세카는 넷리스트와 배치·배선 정보를 함께 학습하는 설계 특화 파운데이션 모델로 확장할 계획이다. 이 계획이 실현되면 B2B 시장에서 모디팩토리와 겹친다.

LG AI연구원은 계열사용 PCB 자동 배선을 내부에서 개발하고 있다([LG AI Research 블로그](https://www.lgresearch.ai/blog/view?seq=509)). 이는 대기업이 외부 SaaS보다 자체 솔루션을 선호할 수 있다는 신호다. 마키나락스는 PCB 설계가 아니라 SMT 조립 순서를 강화학습으로 최적화한다([마키나락스](https://www.makinarocks.ai/use-case/reinforcement-learning-based-smt-sequence-optimization/)). 알세미는 반도체 소자 모델링 AI EDA 기업이다([혁신의숲](https://www.innoforest.co.kr/company/CP00001930/%EC%95%8C%EC%84%B8%EB%AF%B8)). 둘 다 인접 영역일 뿐 직접 경쟁자는 아니다.

초보자에게 현실적인 대안은 사람에게 맡기는 외주다. 크몽에는 "330,000원부터, 3일 이내 완료" 패키지가 있고([크몽](https://kmong.com/gig/412145)), 2층 이하 단순 회로를 10만 원에 설계해 주는 업체도 있다([(주)제이](https://j-iot.co.kr/product/10)). 제조 중개 플랫폼 캐파에는 PCB 분야 파트너가 7,626곳 등록돼 있다(검색 시점 스니펫 기준, [캐파](https://capa.ai/partners?keyword=%EC%A0%84%EC%9E%90%ED%9A%8C%EB%A1%9C%28PCB%29)). 하지만 AI 설계 기능을 붙인 국내 외주·제조 플랫폼은 확인되지 않았다. 이 외주 가격(10만~33만 원, 수일)이 모디팩토리가 유료로 전환할 때 넘어야 할 가격 기준선이다.

### 오픈소스는 배선과 파일 처리를 갖췄지만 자동 배치와 설계 근거가 비어 있다

모디팩토리와 같은 파이프라인을 오픈소스로 구성하면, 파일 처리·DRC·Gerber 출력은 **KiCad**(GitHub 미러 스타 약 3.2k)가 맡는다. 배선은 **Freerouting**(약 2.2k, GPL-3.0)이 맡을 수 있다. Freerouting은 공개 API 베타와 MCP 연동도 제공한다([GitHub Freerouting](https://github.com/freerouting/freerouting)). 회로를 코드로 표현하는 계층에는 atopile(약 4.1k), tscircuit(약 3.0k), SKiDL(약 1.7k), circuit-synth가 있다([atopile](https://github.com/atopile/atopile); [tscircuit](https://github.com/tscircuit/tscircuit)). 2025~2026년에는 Claude 같은 LLM이 KiCad를 조작하게 하는 MCP 서버가 급증했다. 가장 큰 mixelpixx/KiCAD-MCP-Server(약 3.4k)는 Freerouting과 JLCPCB 부품 연동까지 포함한다. 그래도 README에서 "AI 생성 설계는 자격 있는 엔지니어 검토 필요"라고 고지한다([GitHub](https://github.com/mixelpixx/KiCAD-MCP-Server)).

빈 곳은 분명하다. **실사용 수준의 자동 배치를 제공하는 성숙한 오픈소스는 없다.** RL_PCB(스타 76)와 NVIDIA Cypress(56)는 연구 코드다. Google의 circuit_training(약 1.7k)은 칩 전용이다([RL_PCB](https://github.com/LukeVassallo/RL_PCB); [Cypress](https://github.com/NVlabs/Cypress); [circuit_training](https://github.com/google-research/circuit_training)). 서술형 설계 근거도 MCP와 LLM을 조합해 흉내 낼 수는 있다. 하지만 Claude Desktop이나 Cursor를 설치해야 하는 개발자용이라 "웹 업로드 한 번"이라는 UX와는 거리가 멀다.

KiCad 포럼에는 비공식 실험 보고가 하나 있다. LLM이 배선 실패를 구조화 텍스트로 읽었을 때 recall이 0.82, SVG 이미지로 읽었을 때 0.03이었다는 내용이다([KiCad 포럼](https://forum.kicad.info/t/two-months-of-testing-llms-on-pcb-autorouting-what-worked-what-didnt-and-whats-left-to-try-open-archive/72250)). 일화적 자료지만, 설계 근거를 생성할 때 넷리스트와 제약을 텍스트로 넘기는 설계가 유리하다는 것을 시사한다.

| 서비스 | 입력 | 처리 범위 | 소요 시간 주장 | 설계 근거·리뷰 | 출력 | 가격·무료 | 주 타깃 | 자금·규모 |
|---|---|---|---|---|---|---|---|---|
| **MODI Factory** (럭스로보, 한국) | 회로도 + 레이아웃 파일(확장자 미확인) | 물리 기반 검증, 배치, 배선, 후보 여러 개, Lock 재배치 | 90분 이내(밀도·서버에 따라 변동) | 배치 노트, 배선 노트(4개 지표) | Gerber(그 외 미확인), Altium 플러그인 | 2026년 말까지 전 기능 무료, 이후 구독형 계획(미공개) | 초보자부터 현업 | 모회사 누적 투자 350억~379억 원(상충) |
| **Quilter** (미국) | Altium, Cadence, Siemens, KiCad | 배치, 배선, 후보 순위 | 843부품 보드 약 27시간(회사 발표) | 후보별 물리 design review | Gerber, Excellon | 개인·학술 무료(학습 활용), 상용 견적 | 전문가, 항공·국방 | 누적 $35M~50M(상충) |
| **DeepPCB** (InstaDeep/BioNTech) | .PcbDoc, KiCad, EasyEDA Pro, DSN | RL 배선 중심 | 중앙값 수 분(경쟁사 작성 페이지) | 확인 안 됨 | 배선된 보드 | 체험 1보드, $30/시간 | 전문가 | 모회사 소속 |
| **Cadence Allegro X AI / AuraStack** | 넷리스트 + 제약 | 배치, 핵심 넷 배선, 전원 플레인 | 수일→수분(회사 주장) | 에이전트 기반 제약 관리 | 자사 툴 | 기업 라이선스 | 대기업 | 상장 대기업 |
| **Flux** (미국) | 텍스트 프롬프트, 브라우저 에디터 | 회로도, 자동 레이아웃 | 미공개 | "투명한 AI 에이전트" | 내보내기 | Pro 월 $250, 14일 체험 | 초보자부터 전문가 | $37M, 가입 100만+ |
| **Circuit Mind** (영국) | 블록도, 기존 회로도 | 회로도, BOM, FMEA, 검증 | 약 60초~10분 미만 | 데이터시트 대조 검증(AVE) | 회로도, 리포트 | 미공개 | 기업 | 누적 $33.4M |
| **SECA** (한국) | 데이터시트, 회로도, BOM, 넷리스트 | 문서 간 정합성 검증 | — | 지식그래프 기반 불일치 탐지 | 검증 결과 | 미공개 | 대형 제조기업 | 시드(비공개), TIPS |
| **KiCad + Freerouting (+MCP)** | KiCad, DSN | 배선(배치는 수동) | — | 없음(LLM으로 흉내 가능) | Gerber 등 | 무료(GPL-3.0) | 개발자, 메이커 | 오픈소스 |

표의 근거는 앞의 본문 인용과 같다. 시장 맥락을 덧붙이면, 2026년 PCB 설계 소프트웨어 시장은 조사기관에 따라 **$3.8B~6.2B**로 추정치가 두 배 가까이 벌어진다([Straits Research](https://straitsresearch.com/report/pcb-design-software-market); [Grand View Research](https://www.grandviewresearch.com/industry-analysis/pcb-design-software-market-report); [MarkWide](https://markwideresearch.com/pcb-design-software-market)). AI PCB 설계만 따로 떼어 낸 신뢰할 만한 시장 규모는 찾지 못했다. 그보다 의미 있는 신호는 Diode, Quilter, Flux, Circuit Mind로 이어진 2025~2026년의 연속 투자다. "AI PCB 설계"가 VC의 독립 투자 테마로 자리 잡았다는 뜻이다. 모디팩토리에게 이는 시장이 검증됐다는 신호이자, 자금력 있는 해외 선발 주자가 이미 있다는 경고다.

## 4. 한계 분석 및 차세대 서비스 방향: 승부처는 생성보다 검증이다

이 절은 "학술적·기술적·기능적 관점에서 모디팩토리의 한계는 무엇이고, 더 나은 서비스는 어떤 방향이어야 하는가"라는 질문에 답한다. 각 항목에서 **근거**는 인용한 출처로 확인한 사실이고, **추론**은 그 사실에서 이 보고서가 끌어낸 판단이다. 모디팩토리는 엔진 구조를 공개하지 않았다. 그래서 아래 기술적 한계의 상당수는 "결함이 확인됐다"는 뜻이 아니라 "외부에서 검증할 수 없다"는 뜻이다.

### 학술적 한계: 공개된 검증 성과가 없고, 핵심 특허는 대리 지표에 기대고 있다

**근거.** 럭스로보 팀의 동료심사 논문, 학회 발표, 공개 벤치마크 결과는 찾지 못했다. 공개된 기술 정보는 특허명, 언론의 특허 요약, 채용공고가 전부다([TheVC](https://thevc.kr/luxrobo); [원티드](https://www.wanted.co.kr/wd/382685)). 특허의 핵심은 물리 배선 전 에어와이어의 길이·밀집도·교차 특징으로 배치와 배선 경로를 미리 최적화하는 것이다([TheVC](https://thevc.kr/luxrobo)).

학계는 이런 사전 지표와 최종 품질 사이의 간극을 반복해서 보고한다. ML-for-EDA 서베이는 배치와 라우팅이 강하게 결합돼 있어 배치 단계에서 라우팅 성능을 함께 고려해야 한다고 정리한다([ar5iv](https://ar5iv.labs.arxiv.org/html/2102.03357)). Vassallo & Bajada도 배치 품질을 사전 지표가 아니라 라우팅 후 배선 길이로 평가했다([UM OAR](https://www.um.edu.mt/library/oar/handle/123456789/131782)). EDA Bench에서는 빌드에 성공한 그럴듯한 보드도 기능 검사에서 대부분 실패했고, 종합 점수는 4.58%였다([ICML](https://icml.cc/virtual/2026/77908)). PCB Gym에서 DRC를 통과한 완전 배선 보드는 약 32.1%였다([NeurIPS](https://neurips.cc/virtual/2026/161602)). PCB-Bench와 OmniLayout은 routability 최적화와 전기 기능 보존이 약하다고 보고했다([ICLR](https://iclr.cc/virtual/2026/poster/10009621); [arXiv](https://arxiv.org/abs/2607.03261)). AlphaChip 논쟁은 강한 기준선과 공개 벤치마크 없이 내세운 "AI 우위"가 재현 단계에서 흔들릴 수 있음을 보여 줬다([arXiv 2302.11014](https://arxiv.org/abs/2302.11014v3)). PCB 배치·배선 결정을 설명하는 XAI 연구는 찾지 못했고, LLM이 생성한 설계 근거의 환각을 평가한 연구도 없었다.

**추론.** 에어와이어의 길이·밀집도·교차는 고전 배치 알고리즘이 오래 써 온 배선 길이·혼잡도 대리(proxy) 지표와 성격이 같다. 힘 기반(force-directed) 배치나 배선 길이 최소화가 대표적인 예다. 특허 자체가 잘못됐다는 뜻은 아니다. 다만 대리 지표가 좋아져도 배선 완료율이나 전기적 동작이 보장되지는 않는다. 대리 지표 개선이 라우팅 후 품질로 이어진다는 것을 공개 벤치마크로 보여 주기 전까지, 모디팩토리의 품질 주장은 학술적으로 검증할 수 없다. AI 노트도 같은 문제를 안고 있다. 노트의 근거가 실제 검사 결과와 연결됐는지 외부에서 확인할 수 없기 때문에, 설명이 매끄러울수록 잘못된 확신을 줄 위험도 커진다.

### 기술적 한계: 물리 검증의 실체가 불분명하고, 배선·데이터·속도에서 약점이 남는다

**근거.** 공식 설명은 "physics-based verification"이라고만 할 뿐, 어떤 SI·PI·열·EMC 해석을 하는지 밝히지 않는다([modifactory.com](https://www.modifactory.com/)). 학계에도 보드 레벨 SI(임피던스, 크로스토크, 차동쌍)를 ML로 다룬 동료심사 논문은 찾지 못했다. 드문 사례로 열 쪽에는 LLM과 NSGA-II를 결합한 ECCE 2025 연구가 있고([Chalmers](https://research.chalmers.se/en/publication/550860)), 전원 무결성 쪽에는 Google·Missouri S&T의 PDN 형상·스택업 RL 연구가 있다([Google Research](https://research.google/pubs/novel-graph-based-reinforcement-learning-approach-for-multi-power-domain-pcb-pdn-shape-and-stackup-synthesis/)).

배선에서는 PCBWorld가 학습형 라우터가 규칙 기반에 뒤처진다고 진단했다([arXiv](https://arxiv.org/abs/2607.05915)). CADET도 DRV 없는 완료율을 67.2%까지 올리는 데 그쳤다([arXiv](https://arxiv.org/html/2611.16913)). 채용공고가 내건 "LLM 기반 부품 배치" 방향([원티드](https://www.wanted.co.kr/wd/382685))은 LLM의 공간 추론이 약하다는 PCB-Bench·OmniLayout 결과와 부딪친다.

데이터 측면에서 UNSW 서베이는 도메인 특화 데이터 부족을 핵심 장애물로 꼽았다([arXiv](https://arxiv.org/pdf/2606.17074)). 칩 분야의 CircuitNet([CircuitNet](https://circuitnet.github.io/intro/overview.html))에 해당하는 대규모 PCB 레이아웃 데이터셋은 아직 없다. 연구자들은 KiCad 포럼에서 회로도·PCB 쌍을 구하고 있는 실정이다([KiCad 포럼](https://forum.kicad.info/t/seeking-a-samples-of-kicad-projects-schematics-pcbs-for-a-non-commercial-research-dataset/61531)). 모디팩토리의 학습 데이터 출처, 지원 레이어 수, 최대 부품 수, 고속 신호 지원 여부는 공개되지 않았다.

처리 시간은 90분 이내라고 밝히면서도 PCB 밀도와 서버 환경에 따라 달라진다고 단서를 단다([블로그 insights-001](https://www.modifactory.com/blog/ko/insights-001)). 반면 경쟁 쪽에서는 분 단위 주장이 나온다. DeepPCB는 배선 중앙값 수 분(경쟁사 작성 페이지, [ProtoFlow](https://www.protoflow.ai/compare/ai-pcb-autorouter-comparison)), Cadence Allegro X AI는 "수일에서 수분으로"([Cadence](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2023/cadence-introduces-allegro-x-ai-accelerating-pcb-design-with.html)), Circuit Mind ACE는 회로도 단계 약 60초~10분 미만([ipXchange](https://ipxchange.tech/product-news/go-from-block-diagram-to-bom-in-minutes-meet-circuit-minds-ace-tool/))을 내세운다.

**추론.** "물리 기반 검증"의 범위가 공개되지 않는 한, USB·DDR·RF 같은 고속 인터페이스가 있는 보드에 모디팩토리 결과를 그대로 쓸 근거가 없다. 학계에도 이 영역의 ML 해법이 거의 없다. 그러니 모디팩토리가 이 문제를 독자적으로 풀었다기보다는 규칙 기반 검사 수준일 가능성이 높다. 학습 데이터가 공개 하드웨어 위주라면 산업용 고밀도 보드로 일반화하기 어렵다. 엔진이 블랙박스라 사용자는 어떤 보드에서 실패할지 미리 알 수 없다. 경쟁사의 분 단위 주장은 처리 범위가 서로 달라 직접 비교할 수 없다. 그래도 사용자 체감으로는 90분짜리 배치(batch) 처리가 느린 쪽에 속한다.

### 기능적 한계: '초보자용 자동 설계'는 레이아웃 단계에 한정되고, 앞뒤 공정이 비어 있다

**근거.** 입력은 회로도와 레이아웃 파일이다([modifactory.com](https://www.modifactory.com/)). Altium 플러그인도 Altium에서 이미 회로와 보드를 만든 사용자를 전제로 한다([modifactory.com/ko](https://www.modifactory.com/ko)). 입력 포맷은 FAQ 질문 제목 수준까지만 확인했고, 출력은 Gerber만 확인됐다([JLCPCB 직구 가이드](https://www.modifactory.com/blog/ko/jlcpcb-order-guide)). 부품 선정·재고·가격, BOM, DFM 검사, 제조 발주와의 연동도 확인되지 않는다. JLCPCB와의 연결은 발주 가이드 블로그 한 편이 전부다.

다른 서비스는 이 앞뒤 공정을 채우고 있다. atopile은 파라메트릭 부품 자동 선정을 제공한다([GitHub](https://github.com/atopile/atopile)). KiCAD-MCP-Server는 JLCPCB 부품의 가격과 재고를 조회한다([GitHub](https://github.com/mixelpixx/KiCAD-MCP-Server)). Circuit Mind는 BOM과 FMEA를 내고([SiliconANGLE](https://siliconangle.com/2026/10/28/circuit-mind-lands-25m-and-puts-ai-agents-to-work-checking-circuit-board-schematics/)), Diode는 즉시 제조·조립 견적을 제공한다([yespress](https://yespress.io/diode-computers-inc)).

그 밖에도 확인되지 않은 것이 많다. 서비스는 2026년 3월에 베타였고, 2027년 이후 요금은 공개되지 않았으며, 독립 사용자 후기는 찾지 못했다. 업로드 데이터를 학습에 쓰는지, 얼마나 보관하는지에 대한 정책도 확인하지 못했다. 사업 측면에서는 모회사의 매출이 급감하고 IPO를 철회했다(1절). 반면 경쟁사는 Quilter $25M, Flux $37M, Circuit Mind $25M 같은 대규모 투자를 받았고, Cadence와 Siemens 같은 대기업도 AI 기능을 내놓고 있다(3절).

**추론.** 회로도를 스스로 만들 수 없는 사용자에게 모디팩토리는 출발점이 되지 못한다. 그래서 "초보자도 막힘없는 자동 설계"라는 문구는 실제 사용 범위보다 넓게 읽힌다. 90분짜리 비동기 루프는 "고치고 다시 돌려 보는" 반복을 느리게 만든다. 부품 조달과 DFM이 빠져 있어서, 초보자는 Gerber를 받은 뒤에도 다시 막힌다. 데이터 정책이 공개되지 않은 것은 기업 고객이 도입을 망설이게 하는 장벽이다. 자금력이 큰 경쟁자 사이에서 무료 기간이 끝난 뒤에도 사용자를 붙잡아 둘 수 있을지 역시 불확실하다.

### 더 나은 서비스는 '의도에서 주문까지, 분 단위로, 검증된 근거와 함께' 가야 한다

아래 방향은 이 보고서의 추론이다. 다만 방향마다 그렇게 판단한 근거가 된 연구나 제품 사례를 함께 달았다.

**(가) 의도에서 주문까지 이어지는 엔드투엔드.** 요구사항, 자연어, 블록도를 입력받아 시작해야 한다. 이어서 실시간 재고와 가격을 반영해 부품을 고르고, 회로도는 코드나 DSL로 생성해 LLM과 결정론적 검사기가 루프를 돌게 한다. 그다음 배치, 배선, DFM, 발주로 이어진다. 근거는 다음과 같다. pcbGPT는 라이브러리 검색과 결정론적 검사로 자연어를 KiCad 회로도 초안으로 바꿨다([arXiv](https://arxiv.org/pdf/2606.01188)). SchGen은 코드 표현을 썼을 때 유효 회로율 82%를 얻었는데, 원시 KiCad 직접 생성은 32.45%에 그쳤다([alphaxiv](https://www.alphaxiv.org/abs/2605.30345.md)). PCBSchemaGen은 검증기 루프를 돌렸다([NeurIPS](https://neurips.cc/virtual/2026/poster/149018)). 제품 쪽에서도 Circuit Mind ACE(블록도→회로도·BOM, [Circuit Mind](https://www.circuitmind.io/resource-center/unveiling-ace-architecture-to-pcb-schematic-in-60-seconds)), atopile의 파라메트릭 부품 선정, KiCAD-MCP-Server의 JLCPCB 재고·가격 연동이 이 흐름의 조각을 이미 보여 준다. 다만 실보드 수준 회로도 생성 통과율이 8.15%라는 HWE-Bench 결과(제3자 요약, [emergentmind](https://www.emergentmind.com/papers/2603.18102))를 고려하면, 회로도 단계에는 사람이 확인하는 체크포인트를 남겨야 한다.

**(나) 분 단위의 대화형 반복.** GPU 해석적 배치로 전역 배치를 하고 검증된 결정론적 라우터로 배선해, 첫 초안을 수 분 안에 보여 줘야 한다. 정밀화는 백그라운드에서 점진적으로 진행한다. "이 커넥터는 보드 가장자리에", "이 넷은 짧게" 같은 자연어 지시는 제약으로 바꿔 반영하고, 부분 고정 후 재실행을 지원한다. 근거는 다음과 같다. Cypress는 SA-PCB 대비 최대 492.3배 빠른 배치를 보였다([Cypress 논문](https://www.csl.cornell.edu/~zhiruz/pdfs/cypress-ispd2025.pdf)). Freerouting은 공개 API와 셀프호스팅을 제공한다([GitHub](https://github.com/freerouting/freerouting)). Unet-Astar는 학습이 A* 탐색을 안내하는 하이브리드 구조다([DOAJ](https://doaj.org/article/be16200414264fe48da8f179bd034013)). 모디팩토리의 Lock 기능은 이 방향의 출발점이 될 수 있다.

**(다) 검증 결과에 연결된 설계 근거.** 설계 근거의 모든 문장을 측정된 검사 결과, 데이터시트 조항, 설계 규칙 중 하나에 연결해야 한다. "검사하지 않은 항목"(SI, 열 등)은 명시하고, 판단마다 신뢰도를 표시한다. 근거는 다음과 같다. DRCY는 데이터시트와 대조해 리뷰한다([arXiv](https://arxiv.org/abs/2603.15672)). PCBSchemaGen은 오류를 핀 단위로 짚어 준다([NeurIPS](https://neurips.cc/virtual/2026/poster/149018)). Zeng 외는 SHAP으로 예측을 설명했다([DATE 2020](https://past.date-conference.com/proceedings-archive/2020/html/0046.html)). DRCY 벤더도 이 도구가 사람의 판단을 대체하지 않는다고 밝힌다([AllSpice](https://www.allspice.io/post/under-the-hood-how-drcy-reviews-your-schematics)). 모디팩토리 배선 노트의 4개 지표는 이 구조에서 측정값 층으로 쓸 수 있다.

**(라) 물리 해석을 루프 안으로.** 전원, 고속, 차동 넷 같은 핵심 넷은 PI·SI·열 시뮬레이션을 연동하고, 그 결과를 후보 순위에 반영해야 한다. 근거는 다음과 같다. Quilter는 후보마다 임피던스, 리턴 전류 연속성, 디커플링 효율을 검토한다([Quilter Help](https://help.quilter.ai/en/articles/11670146-how-does-quilter-work)). PCB Gym에서 흔했던 실패 중 하나가 전원 레일을 신호 넷처럼 다룬 것이었다([NeurIPS](https://neurips.cc/virtual/2026/161602)). Google의 PDN RL과 KAIST DevFormer([PMLR](https://proceedings.mlr.press/v202/kim23h.html))는 PI 인지 배치의 학술적 토대를 보여 준다. KAIST의 2026년 워크숍은 PyAEDT로 Ansys 전자기 시뮬레이션을 자동화하는 발표를 예고했다([Korea Times](https://www.koreatimes.co.kr/amp/southkorea/education/20260702/kaist-workshop-to-showcase-ai-agents-for-hbm-design-automation)). Cadence AuraStack도 멀티피직스 해석을 에이전트 흐름에 넣었다([Cadence](https://newsroom.cadence.com/press-releases/press-release-details/2026/Cadence-Introduces-AuraStack-AI-Super-Agent-the-Worlds-First-Agentic-AI-Platform-for-PCB-and-Advanced-Packaging/default.aspx)).

**(마) 도구에 묶이지 않는 왕복 입출력.** KiCad를 1급으로 지원하고, Altium과 Specctra DSN도 지원해야 한다. 결과는 네이티브 프로젝트 파일로 돌려줘 사용자가 계속 편집할 수 있게 하고, 제조 출력은 Gerber·Excellon과 함께 ODB++과 IPC-2581까지 제공해야 한다. 근거는 다음과 같다. 국내의 KAIST(KiCad MCP 에이전트)와 LG AI연구원(KiCad 기반 PCBWorld)이 모두 KiCad로 수렴하고 있다. Quilter는 Altium, Cadence, Siemens, KiCad 입력을 받는다([Quilter docs](https://docs.quilter.ai/prepare-your-input-board-file)). DeepPCB는 DSN을 지원하고([DeepPCB Help](https://deeppcb.ai/help/)), Diode는 KiCad, Altium, Cadence로 내보낸다([GitHub](https://github.com/diodeinc/pcb)). ODB++과 IPC-2581은 경쟁사들의 지원 여부도 확인하지 못했다. 그만큼 선점할 수 있는 지점이다.

**(바) 에이전트·MCP 네이티브.** 배치, 배선, 검사 기능을 API와 MCP 도구로 열어, 사용자가 쓰는 AI 비서가 직접 호출할 수 있게 해야 한다. 결과는 이미지가 아니라 구조화된 텍스트로 돌려줘야 한다. 근거는 다음과 같다. Freerouting은 MCP를 지원하고, KiCAD-MCP-Server는 스타 약 3.4k를 모았다([GitHub](https://github.com/mixelpixx/KiCAD-MCP-Server)). JLC는 EasyEDA Pro와 Claude Code·Codex를 잇는 워크플로를 소개했고 MCP·CLI 베타를 준비 중이다([JLCPCB](https://jlcpcb.com/blog/ai-tools-for-pcb-design); [Adafruit](https://blog.adafruit.com/2026/09/19/jlc-puts-ai-assisted-board-design-in-files-you-can-read-review-and-edit/)). Altium의 MCP 서버는 Coming Soon 상태다. 또 KiCad 포럼의 비공식 실험에서는 LLM이 배선 실패를 구조화 텍스트로 읽었을 때 recall 0.82, SVG 이미지로 읽었을 때 0.03이었다([KiCad 포럼](https://forum.kicad.info/t/two-months-of-testing-llms-on-pcb-autorouting-what-worked-what-didnt-and-whats-left-to-try-open-archive/72250)).

**(사) 데이터 정책을 차별점으로.** 업로드한 설계를 학습에 쓰지 않는다는 명시적 보장, 보관·삭제 정책, 온프레미스나 프라이빗 클라우드 옵션, 보안 인증을 갖춰야 한다. 근거는 다음과 같다. Quilter는 무료 티어 입력 파일을 학습에 쓰지만 엔터프라이즈 설계는 쓰지 않는다([Futurepedia](https://www.futurepedia.io/tool/quilter)). Quilter는 기밀 환경용 온프레미스 배포도 제공하고([CB Insights](https://www.cbinsights.com/company/quilter)), 2026년 3월 SOC 2 Type II 인증을 받았다([Quilter Newsroom](https://www.quilter.ai/newsroom)). ProtoFlow는 옵트아웃하지 않으면 사용자 설계를 학습에 쓴다는 보고가 있다([Cherry Blossom 블로그, 경쟁사 작성](https://www.trycherryblossom.com/blog/protoflow-alternative)). 모디팩토리 추천사에도 보안을 확인한 뒤 도입했다는 내용이 있다. 보안이 실제 도입 기준이라는 뜻이다.

**(아) 공개 벤치마크와 첫 시도 성공률.** PCBWorld-Bench, Cypress 벤치마크, PCB-Bench 같은 공개 벤치마크에서 Freerouting과 경쟁사를 함께 비교한 결과를 공개해야 한다. 실제 제작한 보드가 첫 시도에 동작한 비율도 공개해야 한다. 근거는 다음과 같다. PCBWorld-Bench는 실보드 679개와 엔진 채점 지표 8개를 제공한다([arXiv](https://arxiv.org/abs/2607.05915)). Cypress는 공개 벤치마크를 함께 냈다([GitHub](https://github.com/NVlabs/Cypress)). AlphaChip 논쟁은 공개 기준선이 없을 때 무슨 일이 생기는지 보여 준 교훈이다. Quilter는 "첫 시도에 부팅"이라는 사례를 핵심 마케팅으로 쓴다(회사 발표, [VentureBeat](https://venturebeat.com/ai/quilters-ai-just-designed-an-843-part-linux-computer-that-booted-on-the)).

**(자) 초보자를 위한 튜터형 설명과 국내 생태계.** 설명은 여러 층으로 제공해야 한다. 초보자용 한 줄 요약, 엔지니어용 수치, 근거 문서 순이다. MCU 보드처럼 검증된 레퍼런스 설계를 템플릿으로 제공하고, 한국어 지원과 국내 제조사·부품 유통사 연동을 갖춰야 한다. 근거는 다음과 같다. 국내 외주 가격은 10만~33만 원에 수일이 걸린다([크몽](https://kmong.com/gig/412145)). 한국어 온라인 제조 경로로는 PCBGOGO 한국어 사이트, 와이즈피시비, MPGATE가 있다([PCBGOGO](https://www.pcbgogo.co.kr/); [WISE PCB](https://www.wisepcb.com/); [MPGATE](https://www.mpgate.co.kr/)). 그러나 AI 설계를 붙인 국내 제조·중개 플랫폼은 확인되지 않았다. Flux의 가입자 100만 명은 초보자 수요가 크다는 증거다([SiliconANGLE](https://siliconangle.com/2026/02/27/flux-nabs-37m-automate-printed-circuit-board-development-ai/)). KiCad 포럼 사용자는 AI가 RP2040·ESP32 같은 정형 보드는 잘 다루지만 복잡한 설계에서는 한계가 있다고 보고했다([KiCad 포럼](https://forum.kicad.info/t/two-months-of-testing-llms-on-pcb-autorouting-what-worked-what-didnt-and-whats-left-to-try-open-archive/72250)). 이는 템플릿 중심 접근이 유효하다는 신호다. 공개 회로도 코퍼스인 Open Schematics(약 84,470개, [Hugging Face](https://huggingface.co/datasets/bshada/open-schematics-v4))는 템플릿과 학습 데이터의 출발점이 될 수 있다. 단, 레코드별로 라이선스를 확인해야 한다.

| 한계 | 근거 | 개선 방향 |
|---|---|---|
| 동료심사 논문·공개 벤치마크 없음 | 팀 논문 미발견. AlphaChip 재현 논쟁 | PCBWorld-Bench 등에서 Freerouting·경쟁사와의 비교 결과 공개 (아) |
| 에어와이어 대리 지표에 의존 | EDA Bench 4.58%, PCB Gym 32.1%, OmniLayout | 라우팅 후 지표, ERC, PI, 기능 검사로 평가 (다)(라)(아) |
| 근거 없는 설명의 환각 위험 | PCB 배치·배선 XAI 연구 공백 | 모든 근거를 검사 결과·데이터시트·규칙에 연결하고 미검사 항목 명시 (다) |
| SI·PI·열·EMC 검증 범위 불명 | "physics-based verification"만 공개. 보드 SI ML 논문 부재 | 핵심 넷 시뮬레이션 연동, 결과를 후보 순위에 반영 (라) |
| 학습형 배선의 열세 | PCBWorld 진단, CADET 67.2% | 결정론적 라우터에 ML 가이드를 더한 하이브리드 (나) |
| 데이터 부족과 일반화 위험 | UNSW 서베이. CircuitNet급 PCB 데이터 부재 | 동의 기반 데이터 수집, 공개 코퍼스 활용 (사)(자) |
| 블랙박스, 복잡도 한계 미공개 | 레이어·부품 수·고속 지원 미공개 | 지원 범위 공개와 업로드 시 난이도 사전 진단 (아) |
| 90분 배치 처리 | 회사 설명. 경쟁사 분 단위 주장 | 수 분 내 초안과 점진적 정밀화 (나) |
| 회로도·레이아웃 파일이 있어야 시작 가능 | 입력 설명, Altium 플러그인 전제 | 요구사항에서 회로도까지 생성 (가) |
| 입출력 포맷 확인 범위가 좁음 | Gerber만 확인 | KiCad 1급 지원, ODB++·IPC-2581, 네이티브 왕복 (마) |
| 부품 조달·BOM·DFM·발주 미연동 | JLCPCB는 블로그 가이드뿐 | 실시간 재고·가격, DFM, 발주 연동 (가)(자) |
| 데이터 정책 미공개 | 약관 미확인. Quilter 무료 티어는 학습에 활용 | 학습 미사용 보장, 온프레미스, 보안 인증 (사) |
| 베타 상태, 가격 미정, 모회사 재무 위험 | 1절 매출·IPO 철회. 경쟁사 대규모 투자 | 투명한 요금과 성능 공개로 유료 전환 근거 확보 (아) |

## 5. 시사점: 차별점은 기능의 조합에, 승부처는 검증과 유료 전환에 있다

### 차별점은 '초보자가 읽을 수 있는 근거'와 '기존 도구 안으로 들어가는 연동'이다

개별 기능만 보면 새로울 것이 거의 없다. 다중 후보와 물리 리뷰는 Quilter에, 무료 진입은 Quilter·Cherry Blossom·오픈소스에, 분 단위 처리 주장은 DeepPCB·Cadence·Circuit Mind에 이미 있다. 모디팩토리가 다른 지점은 네 가지다.

첫째, **설계 근거의 독자층**이다. 해외의 리뷰 기능은 임피던스, FMEA, 리턴 전류처럼 전문가용 물리 검토다. 모디팩토리의 배치 노트는 "왜 디커플링 커패시터가 이 거리에 있는가"를 서술한다. 이는 학계에서도 비어 있는 "배치·배선 결정의 설명" 영역을 초보자 눈높이로 채우려는 시도다. 노트의 지표가 특허의 에어와이어 특징처럼 엔진이 실제로 계산한 값에 근거한다면, 학계가 권하는 "측정값에 근거한 설명" 구조와도 맞는다.

둘째, **기존 도구 안으로 들어가는 연동**이다. Altium 자체에는 AI 배치·배선이 없고 DeepPCB의 Altium 버튼은 아직 출시 예정이다. 이런 상황에서 Altium 안에서 바로 돌아가는 플러그인과 Lock 재배치는 현업 엔지니어의 작업 흐름을 깨지 않는다.

셋째, **현지화와 가격**이다. 한국어 지원, JLCPCB 직구 가이드, 무료 진입은 10만~33만 원짜리 외주와 직접 경쟁한다.

넷째, **국내 학술 공백**이다. 국내에는 보드 레벨 AI PCB 설계 학술 연구가 거의 없다. LG AI연구원의 PCBWorld와 KAIST의 KiCad MCP 에이전트가 같은 KiCad 생태계에 있으므로, 공동 연구나 벤치마크 공개로 선점 효과를 얻을 수 있다.

### 4절의 한계 가운데 가장 시급한 것은 검증 공백과 유료 전환 시점이다

4절에서 정리한 한계들은 모두 중요하지만 시급한 정도가 다르다. 무료 프로모션은 2026년 말, 즉 약 6주 뒤에 끝난다. 유료 전환 시점에 사용자가 비교할 대상은 무료 티어를 둔 Quilter, 가입자 100만 명의 Flux, 그리고 10만~33만 원짜리 사람 외주다. 이때까지 공개 벤치마크도 독립 후기도 없다면, 유료 전환을 설득할 근거는 공식 사이트 추천사("4년차 엔지니어급 품질")뿐이다.

보도된 목표(유료 매출 5억 원, 유저 1만 명)도 문제다. 모회사의 매출 감소를 메우기에도, 해외 경쟁사의 규모와 견주기에도 작다. 여기에 홍보 문구의 정확성 문제가 겹친다. "글로벌 톱3"를 수상처럼 쓰는 보도나 계획 단계인 EDA 3사 협업을 확정된 것처럼 읽히게 하는 표현은 B2B 고객의 실사 과정에서 오히려 신뢰를 깎을 수 있다.

다행히 두 문제는 같은 처방으로 풀린다. 공개 벤치마크 수치와 명확한 데이터 정책은 유료 전환의 근거가 되고, 동시에 과장 논란을 잠재운다.

### 남은 질문: 원문 확인으로 풀리는 것과 직접 테스트해야 풀리는 것

| 질문 | 현재 확인 수준 | 확인 경로 |
|---|---|---|
| 지원 입력 포맷(Altium, KiCad, 넷리스트, ODB++ 등)과 FAQ 답변 | FAQ 질문 제목만 확인 | modifactory.com FAQ·이용 가이드 원문 |
| Gerber 외 출력 포맷(Altium·KiCad 네이티브, ODB++, IPC-2581, STEP) | Gerber만 확인 | 서비스 직접 사용 |
| 90분의 조건(부품 수, 레이어, 고속 신호 지원) | "밀도·서버 환경에 따라 변동"만 확인 | 복잡도가 다른 보드로 직접 테스트 |
| 엔진 구조와 AI 노트 생성 방식(측정값 기반인지, LLM 서술인지) | 특허명·채용공고로 추론 | 회사 문의, KIPRIS 특허 청구항 |
| 독립 성능 지표(배선 완료율, DRC·ERC 통과율, SI) | 없음 | PCBWorld-Bench 8개 지표로 Quilter·Freerouting과 동일 보드 비교 |
| 업로드 데이터의 학습 활용·보관·삭제 정책 | 미확인 | 이용약관·개인정보처리방침 원문 |
| 2027년 이후 요금제와 정식 출시(GA) 여부 | "구독형 도입 계획"만 보도 | 공식 공지, 회사 문의 |
| 가입자 수와 기업 고객 | 비공개(목표 1만 명만 스니펫) | 회사 IR 자료, 언론 원문 |
| 럭스로보 매출(2023년 114억 vs 242억 원)과 재무 건전성 | 출처 간 충돌 | DART 감사보고서 |
| Altium·Siemens EDA·Cadence·JLCPCB와의 공식 제휴 | 계획 단계로만 확인 | 각사 파트너 목록, 보도자료 |

## 결론

모디팩토리를 평가할 때 던져야 할 질문은 "90분이 빠른가"가 아니다. **"어떤 복잡도의 보드에서, 사람이 검토할 만한 레이아웃을, 측정값에 근거한 설명과 함께 내놓는가"**가 올바른 질문이다. 이 질문에 가장 빨리 답하는 방법은 공개 자료를 더 찾는 것이 아니라 직접 비교하는 것이다. 무료 기간이 끝나기 전에 같은 보드를 모디팩토리, Quilter 무료 티어, KiCad+Freerouting에 넣는다. 그리고 PCBWorld의 8개 지표로 결과를 채점하고, 배치 노트의 주장이 실제 측정값과 맞는지 대조하면 된다.

문헌과 경쟁 지형을 함께 보면 더 큰 흐름이 보인다. 레이아웃 "생성"의 진입 장벽은 낮아지고 있고, 가치의 중심은 "검증"으로 옮겨 가고 있다. 실사용 수준의 오픈소스 자동 배치는 아직 없지만, GPU 배치 엔진(Cypress, 연구 코드)과 결정론적 라우터(Freerouting)가 오픈소스로 공개돼 있어 출발점으로 쓸 수 있다. LLM 에이전트는 그럴듯하지만 동작하지 않는 보드를 쉽게 만들어 낸다. 따라서 차세대 서비스의 경쟁력은 더 영리한 생성기보다 세 가지에서 나온다. 모든 판단을 검사 결과에 묶는 근거 체계, 공개 벤치마크, 그리고 업로드 데이터에 대한 신뢰다.

모디팩토리는 'AI 노트'라는 형태로 이 방향의 씨앗을 이미 갖고 있다. 2027년 유료 전환 전에 할 일은 세 가지다. 노트를 측정값과 연결하고, 국산 공개 벤치마크인 PCBWorld로 성능을 공개하고, KAIST·LG AI연구원과 같은 KiCad 생태계에서 협력하는 것이다. 이를 해낸다면 과장된 수상 문구 없이도 국내 AI PCB 설계의 기준점이 될 수 있다. 그러지 못하면 Flux와 Quilter가 무료 티어로 초보자와 비상업 사용자를 흡수하는 사이에 차별점이 희석될 것이다.
