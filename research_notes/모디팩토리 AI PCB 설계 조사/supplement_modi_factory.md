# 모디팩토리(MODI Factory) 보강 조사: 새로 확인했거나 검증 수준을 올린 사실

> 조사일: 2026-11-16. `modi_factory_profile.md`(이하 "기존 노트")를 보완한다. 기존 노트에 있던 내용은 반복하지 않고, **새로 확인한 사실, 검증 수준을 올린 사실, 기존 내용과 충돌하는 사실**만 적는다.
>
> **표기 등급**
> - **[원문 확인]**: 이번 세션에서 `curl`로 원문을 직접 받아 읽음.
> - **[GitHub-verified]**: github.com이나 raw.githubusercontent.com에서 확인함.
> - **[search-snippet]**: WebSearch 요약에만 근거함.
> - **[unverified]**: 근거가 약하거나 출처끼리 충돌함.
>
> **원문 확보 범위:** 세션 네트워크가 무제한으로 바뀐 뒤 다음 자료를 원문으로 읽었다.
> - 공식 사이트 www.modifactory.com: 사이트맵 기준 블로그·공지 28개 페이지, 그리고 Framer JS 번들에 들어 있는 FAQ 답변
> - **서비스 앱(workspace.modifactory.com)의 공개 JS 번들**: 업로드·내보내기 형식, 한도, 이용약관, 개인정보처리방침 전문
> - DART 2023 감사보고서, Google Patents 서지·청구항
> - 전자신문·서울경제·이투데이·뉴스토마토·뉴스톱·네이트 기사 원문
>
> 여전히 막힌 곳: kipris.or.kr(타임아웃), reddit.com(403), catch.co.kr(403).

---

## 1. 럭스로보 GitHub에 MODI Factory 관련 공개 저장소가 있는가?

### Takeaway
**없다.** LUXROBO 조직의 공개 저장소 36개는 모두 MODI 교구, IoT, 펌웨어 관련이다. "modifactory"나 "MODI Factory"로 검색되는 저장소도 0건이다. 그래서 플러그인, SDK, 변환기, 릴리스 노트를 GitHub에서 볼 수 없다. 대신 GitHub Pages 소스(강원대 연구실 홈페이지)에서 **정부 R&D 과제명**을 처음 확인했다(6번 항목).

### Cited Findings
- LUXROBO 조직의 공개 저장소는 36개다(최근 갱신 순: pymodi-plus 2026-10-28, carrot_production 2026-08-07, pymodi 2026-03-12 등). PCB, EDA, Altium, KiCad, Gerber, 배치·배선 관련 저장소는 없다 [GitHub-verified] — [github.com/orgs/LUXROBO/repositories](https://github.com/orgs/LUXROBO/repositories?type=all&sort=updated), [2페이지](https://github.com/orgs/LUXROBO/repositories?type=all&sort=updated&page=2)
- 저장소 검색 결과는 "modifactory" 0건, "MODI Factory" 0건이다 [GitHub-verified] — [검색 1](https://github.com/search?q=modifactory&type=repositories), [검색 2](https://github.com/search?q=%22MODI+Factory%22&type=repositories)
- 사이트맵에도 docs/API 페이지가 없다. 앱 번들에서도 외부 공개 API나 SDK 문서 링크는 발견되지 않았다 [원문 확인] — [modifactory.com/sitemap.xml](https://www.modifactory.com/sitemap.xml)

### Inferences
- 폐쇄형 SaaS다. 아키텍처 정보는 GitHub보다 공식 블로그의 팀 인터뷰와 앱 번들에서 더 많이 나온다(2·4번 항목).

### Gaps
- Altium 익스텐션의 배포 경로(Altium 공식 Extensions 마켓 등록 여부)

---

## 2. 정확한 입력 파일 형식, 출력 형식, 지원 EDA, 작업 흐름

### Takeaway
앱 번들 원문으로 **정확한 확장자**를 확인했다.

- **입력** (회로도와 레이아웃 두 파일을 한 쌍으로 올림, 파일당 최대 100MB)
  - Altium: .SchDoc + .PcbDoc
  - **KiCad 8.0 이상**: .kicad_sch + .kicad_pcb
  - EasyEDA: .json + .json
  - MODI Factory 자체 형식: .json
- **출력**
  - EDA 형식: EasyEDA(.json), KiCad(.kicad_pcb), Altium(.PcbDoc), MODI Factory(.zip)
  - 제조·리뷰용: Gerber(.zip), PDF
- **소요 시간:** "90분"은 배치 약 30분과 배선 약 60분을 더한 값이다.
- **미지원:** OrCAD, Allegro, PADS, ODB++, IPC-2581, STEP

### Cited Findings
**업로드 형식 (앱 번들)** [원문 확인]
- 업로드 형식 표: `Easy_EDA:{pcb:[".json"],schematic:[".json"]}, KiCAD:{pcb:[".kicad_pcb"],schematic:[".kicad_sch"]}, MF:{pcb:[".json"],schematic:[".json"]}, Altium:{pcb:[".PcbDoc"],schematic:[".SchDoc"]}` — [workspace.modifactory.com 번들 447-3cbb73ad59de8403.js](https://workspace.modifactory.com/_next/static/chunks/447-3cbb73ad59de8403.js)
- UI 선택지: "Altium", "KiCad (8.0+)", "Easy EDA", "MODI Factory" — 같은 출처
- 같은 표에 OrCAD(".GBO")와 PADS(".GBP") 항목도 정의되어 있지만, 선택지 목록에는 없다 — 같은 출처
- 업로드 안내 문구: "지원 형식: {format} (최대 파일 용량: 100MB)"이다. 코드에는 `MAX_FILE_SIZE:104857600`, 프로젝트명 최대 30자로 정의되어 있다 — [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js), [5042 번들](https://workspace.modifactory.com/_next/static/chunks/5042-83eb17b2865d24c0.js)
- 업로드 검토 단계 오류 메시지:
  - "회로도 파일과 레이아웃 파일이 일치하지 않습니다"
  - "보드 아웃라인 정보가 유효하지 않습니다"
  - "부품이 서로 겹쳐 있어 라우팅을 진행할 수 없습니다"
  - 부품명이나 Net명에 허용되지 않는 특수문자가 있으면 하이픈으로 자동 대체한다(허용: `! @ # $ % ^ * + = - _ .`)
  - 출처: _app 번들
- 배치 옵션은 "전체 재배치"와 "수동 소자만 배치" 두 가지다 — _app 번들

**내보내기 형식 (앱 번들)** [원문 확인]
- 내보내기 정의: `easyeda .json / kicad .kicad_pcb / altium .PcbDoc / gerber .zip / pdf .pdf / mf .zip`이며, 모두 `isImplemented:!0`(구현됨) — [layout/[id] 번들](https://workspace.modifactory.com/_next/static/chunks/pages/layout/%5Bid%5D-d2890299c950859f.js)
- 메뉴 라벨: "KiCAD(.kicad_pcb)", "Altium (.PcbDoc)", "EasyEDA (.json)", "MODI Factory (.zip)", Gerber, PDF — 같은 출처
- 튜토리얼 ④(2026-04-14)는 용도를 이렇게 나눈다: Gerber는 제조 발주, PDF는 리뷰·보고, Project 파일은 외부 EDA 재편집 — [blog/ko/tutorials-004](https://www.modifactory.com/blog/ko/tutorials-004)

**FAQ 답변 원문** (기존 노트에서는 질문만 확인) [원문 확인] — [modifactory.com/ko](https://www.modifactory.com/ko), [Framer 번들](https://framerusercontent.com/sites/48gDNeWr5taVlAK00jZK02/TsGrrmNGW.QvdX1RoJ.mjs)
- Q2: "네, 현재 Altium Designer, KiCad, EasyEDA 포맷을 지원합니다. 해당 툴에서 작업한 회로도 및 레이아웃 파일을 업로드하면 바로 AI 자동 설계를 진행하실 수 있습니다."
- Q4: Component Lock으로 커넥터나 MCU를 고정한 뒤 나머지 영역만 AI로 재계산한다. 웹 에디터로 수동 미세 조정한 뒤 재배선할 수 있다.
- Q5: 크롬 등 브라우저에서 로그인만 하면 되고 설치가 필요 없다.
- Q3(보안)과 Q6(가격)은 3번과 5번 항목 참조

**지원 이력과 작업 흐름** [원문 확인]
- 튜토리얼 ①(2026-04-11): 준비 파일은 "Schematic 파일 (.kicad_sch 또는 EasyEDA JSON)"과 "PCB Layout 파일 (.kicad_pcb 또는 EasyEDA PCB JSON)"이다. 업로드 전 체크리스트는 Net 이름 일치, KiCad ERC 무오류, 최신 저장본이다. 배치는 "평균 30분" — [tutorials-001](https://www.modifactory.com/blog/ko/tutorials-001)
- 튜토리얼 ②(2026-04-12): 배선에는 배치가 끝난 PCB 파일이 필요하고, "약 60분 이내" 끝난다. 작업은 서버에서 계속된다 — [tutorials-002](https://www.modifactory.com/blog/ko/tutorials-002)
- 튜토리얼 ③(2026-04-13): 배치 결과로 **2~3개 후보안**이 나오고, 후보마다 전체 배치 코멘트가 붙는다 — [tutorials-003](https://www.modifactory.com/blog/ko/tutorials-003)
- 튜토리얼 ⑤(2026-07-15): 당시에는 "KiCad와 EasyEDA 포맷 지원, Altium 연동 예정"이었다.
  - 그래서 Altium 사용자에게는 KiCad 9.0.3 이상으로 .SchDoc/.PcbDoc/.PrjPcb를 불러오는 우회 경로를 안내했다.
  - 이 경로로는 "알티움의 디자인 룰은 KiCad로 넘어오지 않는다."
  - AI 배치에는 회로도가 필수다. OrCAD/Allegro는 아직 안내하지 않으며, "회로도 없이 레이아웃 파일만으로도 자동 배치가 가능하도록 개발을 진행 중"이다.
  - 출처: [tutorials-005](https://www.modifactory.com/blog/ko/tutorials-005)
- R2.3.0(2026-08-21): "Altium 파일 지원 — File Upload > File Type에서 'Altium' 선택" — [news/ko/notice-004](https://www.modifactory.com/news/ko/notice-004)
- 기존 노트가 인용한 /blog/getting-started는 2026-11-16 현재 Framer 404("Page Not Found")다 — [링크](https://www.modifactory.com/blog/getting-started)

### Inferences
- 기존 노트에서 확인하지 못했던 "Altium 형식으로 되돌려 보내기"는 **지원된다**(.PcbDoc 내보내기, 구현 플래그 true). 다만 내보내기는 **PCB 파일만** 대상이고, 회로도를 다시 내보내는 기능은 정의되어 있지 않다.
- 공식 "90분"은 튜토리얼 ①과 ②의 시간을 더한 값으로 보인다. 홈페이지 각주도 "처리 시간은 PCB 밀도 및 서버 환경에 따라 달라질 수 있습니다"라고 적는다. 고정 SLA가 아니다.
- KiCad는 8.0 이상만 지원하므로, KiCad 7 이하 파일은 먼저 업그레이드해야 할 것으로 보인다.

### Gaps
- Altium .PrjPcb나 zip 묶음 업로드 지원 여부(번들에는 .SchDoc/.PcbDoc 단일 파일만 정의됨)
- Altium .PcbDoc 내보내기에서 룰, 폴리곤, 레이어 스택이 보존되는지

---

## 3. "물리 기반 검증"의 범위, 보드 한도, 성능 주장

### Takeaway
**공식 처리 한도를 처음 확인했다.** 메인 부품 100개 이하를 포함해 **총 300개 부품**, **와이어(연결) 1,200개**, **보드 크기 최대 200×200**까지 처리한다. 실행 횟수는 **배치·배선 각각 하루 5회**다.

2026-11 현재 사용자에게 제공되는 "검증"은 두 가지다.
- 설계 규칙(선폭, 간격, 층간 규칙)을 배선 중에 자동으로 적용
- 룰 엔진 기반 배치 진단(예: 디커플링 캡 ≤8mm)

열 시뮬레이터는 개발 중이다. PI/SI는 "순서만 잡아 둔" 로드맵 단계다. 독립 DRC/DRS는 "업데이트 예정"이다. 성능 수치는 모두 업체 자체 주장이다.

### Cited Findings
**처리 한도 (앱 번들)** [원문 확인] — [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js)
- "현재 MODI Factory 버전에서는 메인 부품 최대 100개를 포함하여 총 300개 부품 배치, 최대 1,200개 와이어 라우팅까지 지원합니다. 더 큰 보드 지원이 필요하신 경우, support@modifactory.com 으로 문의해주세요."
- 검토 오류 메시지:
  - "와이어 개수가 1200개를 초과 했습니다"
  - "메인 부품이 100개를 초과 했습니다"
  - "전체 부품이 300개를 초과 했습니다"
  - "보드 사이즈 {width}\*{height}는 지원 범위를 초과했습니다. 최대 200\*200까지 가능합니다." (단위 표기는 없지만 mm로 추정)
  - "현재 MODI Factory에서는 지원하지 않는 스펙의 보드입니다"
- 배선 실패 메시지: "현재 MODI Factory 버전의 처리 한계를 초과하여 배선을 진행할 수 없습니다"
- 실행 횟수: "AI 배치와 AI 라우팅은 각각 하루 최대 5회까지 실행할 수 있으며, 매일 자정(KST) 기준으로 초기화됩니다."
- 레이어 수 상한은 번들 문자열에서 발견되지 않았다.

**검증 범위**
- 튜토리얼 ②(2026-04-12): "최소 선 굵기, 부품 간 간격, 층 간 규칙 등의 제약 조건 … AI가 배선 과정 중에 자동으로 검증 … 배선이 끝난 후 DRC를 별도로 돌릴 필요가 없는 이유" [원문 확인] — [tutorials-002](https://www.modifactory.com/blog/ko/tutorials-002)
- 앱의 배선 기능 설명: "신호 흐름, 간섭 최소화, 레이어 활용 최적화를 고려하여 배선을 수행합니다." 결과 화면에는 "사용된 비아 수"와 "레이어"가 표시된다 [원문 확인] — _app 번들
- 홈페이지: 배치 노트는 "디커플링 캡 배치 거리(권장 ≤ 8mm) 자동 진단 및 중심 IC / 커넥터 접근성 검증"을 한다. 영문판은 "automatic DRC checks"라고 쓴다 [원문 확인] — [modifactory.com/ko](https://www.modifactory.com/ko), [modifactory.com](https://www.modifactory.com/)
- 배치 노트는 "단순 AI 텍스트 생성이 아닙니다. 룰 엔진(Rule Engine)이 부품 분류, 거리, 판정 가능 여부 등을 결정한 뒤, 구조화하여 제공"한다 [원문 확인] — [tutorials-006 (2026-09-09)](https://www.modifactory.com/blog/ko/tutorials-006)
- 앱 문구에 따르면 "2026.04.29 이전 생성 프로젝트는 AI Comment 가 지원되지 않습니다" [원문 확인] — _app 번들
- **열 시뮬레이터** (AI 엔지니어 Ethan 인터뷰, 2026-09-03경) [원문 확인] — [ai-ethan-interview](https://www.modifactory.com/blog/ko/ai-ethan-interview)
  - AI팀은 [배치 / 배선 / 시뮬레이터] 세 파트로 나뉜다.
  - 열 해석은 "상용 툴이 약 10분 … 모디팩토리는 30초~1분 내외로 … 약 10~20배" 빠르다고 주장한다.
  - 정확도는 "오차 범위 약 ±5°C 이내"이지만, "지금은 특정 PCB 조건에 맞춰 최적화된 상태"다.
  - "전원 무결성, 신호 무결성은 순서만 잡아 둔 상태"
- Hazel 인터뷰(2026-10-07경): electronica India 현장에서 "DRS나 DRC 등 업데이트 예정인 기능에 대한 요구"를 확인했다 [원문 확인] — [planning-lead-hazel-interview](https://www.modifactory.com/blog/ko/planning-lead-hazel-interview)
- 앱 오류 목록에 "데이터시트 파일 300MB 초과 / PDF만 업로드 가능"(DATASHEET_FILE_TOO_LARGE)이 정의되어 있다. 데이터시트 PDF 업로드 기능이 준비 중이거나 내부용으로 있는 것으로 보인다 [원문 확인] — _app 번들
- 채용공고 '회로 시뮬레이션 엔진 개발자'(2026-10-27 게시): "PI/SI를 포함한 PCB·회로 시뮬레이션 알고리즘 연구 및 개발", "ECAD 설계 데이터 기반 해석 모델 생성 및 수치 솔버" [원문 확인] — [freehire(원출처 점핏)](https://freehire.me/jobs/hoero-simyulreisyeon-enjin-gaebalja-reogseurobo-ds72wlha)

**업체가 주장하는 성능** (모두 자체 주장, 제3자 검증 없음) [원문 확인]
- 홈페이지 문구:
  - "16시간 걸리던 수작업 레이아웃을 … 60분에 완료"
  - "초보 개발자도 30분 이내 설계 시작"
  - "4년차 엔지니어급 품질"
  - 각주: 비교는 "일반적 시장 조사를 기반으로 하며, 특정 제품을 지칭하지 않습니다"
  - 출처: [modifactory.com/ko](https://www.modifactory.com/ko)
- Hugo 인터뷰(2026-07-22): 상용 자동 배치 툴과 범용 LLM(GPT) 베이스라인을 **양산 보드 4종**으로 비교했다고 한다. 비교 툴 이름과 보드 사양은 공개하지 않았다 — [autoplacer-engineer-interview](https://www.modifactory.com/blog/ko/autoplacer-engineer-interview)
  - "4개 보드 전부 설계 의도 명세를 만족시킨 건 모디팩토리뿐"
  - "100% 배치 가능", "3~12배 빨랐어요. 보드 하나에 3~12분"
  - 경쟁 툴 하나는 배선 길이를 34% 줄였지만 디커플링 커버리지가 0%였다.
- 뉴스토마토(2026-01-08): "개발 인원 … 5분의1, 개발 기간 … 10분의1", "한 시간 이내 설계 완성", "약 5년 6개월 연구" — [뉴스토마토 1287248](http://www.newstomato.com/readnews.aspx?no=1287248)
- 홈페이지: "광운대학교 로봇학부 정규 커리큘럼 공식 실습 툴 채택". 레이어명은 "\<AI 로봇학 실험 II\>"다(업체 게재) — [modifactory.com/ko](https://www.modifactory.com/ko)

### Inferences
- 공개된 한도(300부품, 1,200와이어, 200×200)로 보면 **소·중형 보드(IoT, MCU 보드, 교육·시제품)**가 주 대상이다. 고밀도·대형 보드는 현재 범위 밖이다.
- "물리 기반 검증"은 현재 **설계 규칙 준수 배선과 규칙 기반 배치 진단**에 가깝다. SI, PI, EMC는 제품 기능이 아니다.
- 열 해석이 지금 UI에 노출되는지는 불분명하다. 릴리스 노트(R1.5.2~R2.4.0)에는 나오지 않는다.

### Gaps
- 레이어 수 상한(2층/4층 등), 차동쌍·임피던스·길이 매칭 지원 여부
- 사용자 업로드 기준 배선 완료율, DRC 위반률. 제3자 벤치마크는 없다.

---

## 4. AI 모델과 아키텍처

### Takeaway
배치 엔진은 하이브리드다. 용도에 따라 위치가 정해지는 **메인 부품(MCU, USB, 버튼 등)은 LLM**이 배치하고, 보조 부품은 **정량 평가(스코어링) 루프**가 처리한다. 배선은 그래프 탐색, 조합 최적화, 메타휴리스틱 계열이며 RL/GNN을 연구 중이다. 노트는 룰 엔진의 판정을 구조화한 것이다. 인프라는 Kubernetes Operator와 메시지 큐를 쓰며, 온프레미스 AI 서버를 AWS로 옮기는 중이다. LLM 공급사와 모델명은 공개되지 않았다.

### Cited Findings
- Hugo 인터뷰(2026-07-22) [원문 확인] — [autoplacer-engineer-interview](https://www.modifactory.com/blog/ko/autoplacer-engineer-interview)
  - 부품 분담: "MCU나 USB, 버튼처럼 용도와 사용자 맥락에 따라 위치가 정해지는 부품들은 LLM이 배치를 맡고, 저항이나 캐패시터 같은 보조 부품들은 정량 평가 루프가 처리"
  - 출발점: "미리 설계된 다양한 회로와 PCB를 보면서 … 규칙을 세우고, 그 규칙을 지키는 초기 엔진"
  - 초기 구상: MODI 블록코딩 방식으로 블록 다이어그램에서 회로도를 자동 구성하고, 부품 DB와 서플라이 체인 연결까지 포함하려 했다. 이후 배치·배선으로 범위를 좁혔다.
- 앱 업로드 단계는 부품을 "메인 부품 {M}개, 서브 부품 {S}개"로 나눠 보여 준다. LLM과 스코어링 루프의 분담과 일치한다 [원문 확인] — [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js)
- 채용공고 [원문 확인]
  - 'ML/AI 엔지니어'(2026-10-27): "LLM 기반 PCB 메인 부품 자동 배치 모델 개발", "PCB 배치 데이터셋 구축 및 모델 학습·고도화", "AI API 서버 운영·배포" — [freehire](https://freehire.me/jobs/ml-ai-enjinieo-reogseurobo-7nzmi4uk)
  - 'PCB AI 라우터'(2026-10-27): "그래프 탐색, 조합 최적화, 휴리스틱 및 메타휴리스틱 기반 배선 경로 생성", "강화학습, GNN 및 머신러닝을 활용한 배선 순서·경로·비용 함수 최적화" — [freehire](https://freehire.me/jobs/pcb-ai-rauteo-jadong-baeseon-algorijeum-reogseurobo-idiz63gn)
- Rob 인터뷰(2026-08-20): "AI 서버 작업을 쿠버네티스 오퍼레이터 패턴으로 … 스케줄링", "메시지 큐", "온프레미스에서 가동 중이던 AI 서버 환경을 AWS 클라우드로 전환하는 작업을 진행" [원문 확인] — [be-rob-interview](https://www.modifactory.com/blog/ko/be-rob-interview)
- 앱에는 "현재 접속 중인 사용자가 많아 대기 시간이 평소보다 길어지고 있습니다"라는 대기열 안내가 있다. 작업 큐 방식으로 처리한다는 뜻이다 [원문 확인] — _app 번들
- 전자신문 원문(2024-01-04): CES 2024 유레카파크에서 **알파버전**을 공개했다. "AI 챗봇 GPT-4를 접목해 … 회로 부품을 추천"했고, 2024년 2월 MWC 참가를 계획했다. 당시 **손승배 럭스로보 대표**는 "GPT에 원하는 제품을 말하면 … '자비스'와 같은 하드웨어 제작 보조 기능"을 예고했다 [원문 확인] — [전자신문](https://www.etnews.com/20240104000261)

### Inferences
- 기존 노트의 "GNN 기반 배치" 추정은 수정이 필요하다. 원문상 배치는 "LLM + 규칙/스코어링", GNN/RL은 배선 쪽 연구 과제다.
- 2024년 GPT-4 챗봇 구상은 2026년 제품에서 사라졌다. 그 흔적은 2024-02 출원 특허 4건에 남아 있다(5번 항목).
- 손승배는 2024-01 기사에서 "대표"로 나오고, 특허 4건의 공통 발명자이기도 하다. 기술 총괄 인물로 보인다(직함 변동은 미확인).

### Gaps
- 사용하는 LLM(자체 파인튜닝인지 외부 API인지)과 학습 데이터 출처

---

## 5. 데이터·학습 정책, 보안, 이용약관 (새 항목: 중요 충돌)

### Takeaway
**FAQ·홈페이지 문구와 이용약관이 충돌한다.**
- **FAQ·홈페이지:** "업로드된 프로젝트 파일은 고객의 명시적 동의 없이 AI 학습용으로 사용되지 않습니다", "AI 무단 학습 차단"
- **이용약관(2026-02-27 시행):**
  - 가입하면 업로드한 **원본 파일을 R&D와 알고리즘 고도화에 활용하는 데 동의**한 것이 된다(제18조 7항).
  - AI 산출물, 중간 데이터, 메타데이터는 비식별화하여 **AI 모델 학습에 쓸 수 있다**(제19조).
  - **AI 산출물(생성된 레이아웃)의 저작권과 일체의 지식재산권은 회사(럭스로보)에 귀속**된다. 회원은 비독점·영구·무상 이용권만 받는다(제18조).

결국 FAQ가 말하는 "명시적 동의"는 약관 동의로 갈음되는 구조다.

### Cited Findings
**이용약관** (앱 /terms 원문, "이 서비스 이용약관은 2026.02.27부터 적용됩니다") [원문 확인] — [workspace.modifactory.com/terms](https://workspace.modifactory.com/terms), [terms 번들](https://workspace.modifactory.com/_next/static/chunks/pages/terms-ec54ed9b10d29642.js)
- **제18조 (프로젝트 및 AI 산출물의 저작권)**
  - 원본 파일(업로드한 회로도와 설계 자료)의 저작권은 회원에게 귀속된다.
  - 반면 "결과물, 중간 산출물, 파생 데이터, 자동 생성된 설계 결과 … (AI 산출물)에 대한 저작권 및 이에 관한 일체의 지식재산권은 회사에 귀속됩니다."
  - 회원이 받는 권리는 "비독점적·영구적·무상"이다. 범위는 이용·수정·복제, 제조·판매 등 상업적 이용, 사업·연구·양산·외주 목적의 실시다. 단 "제3자에게 이용하게 하거나 실시권을 부여할 권한은 부여되지 않습니다."
  - "회원은 … AI 산출물의 저작권이 회사에 귀속됨을 명시적으로 동의합니다."
  - 7항: "회원은 회사가 … 연구·개발, 알고리즘 고도화, 성능 개선 및 품질 향상을 목적으로 하는 범위 내에서, 회원이 업로드한 원본 파일을 활용할 수 있음에 동의합니다. 다만 … 회원 식별이 불가능하도록 처리하거나 필요한 범위로 제한"
- **제19조 (AI 학습 및 서비스 개선을 위한 데이터 활용)**
  - 활용 대상 데이터에 "회원이 업로드한 원본 파일 및 그로부터 파생되는 데이터가 포함"된다.
  - "AI 산출물 및 AI 실행 과정에서 생성되는 중간 데이터, 메타데이터, 통계 정보 등을 비식별화 또는 익명화하여 AI 모델의 학습, 검증 및 개선에 사용할 수 있습니다."
- **제9조 (무료 재화)**
  - "자동 배치 프로젝트: 1일 최대 5회", "자동 라우팅 프로젝트: 1일 최대 5회", 00시(KST)에 초기화되며 이월되지 않는다.
  - 회원 측 입력(파일, 설계 조건, 보드 크기 부족 등) 때문에 실패하면 횟수를 복원하지 않는다.
- **제20~21조:** AI 산출물은 기존 설계와 유사할 수 있고, 권리 침해 여부를 검토할 책임은 회원에게 있다. "AI 산출물은 참고 또는 설계 지원을 목적으로 제공되는 결과물로서, 실제 제조, 양산, 제품화 또는 상용 환경에서의 사용을 보장하지 않습니다."
- **제12조:** 탈퇴하면 "해지 즉시 회원의 모든 개인정보 및 데이터를 삭제"한다(법령상 보유분 제외).
- **제25조:** 준거법은 대한민국이다. 해외 회원의 분쟁 관할은 서울중앙지방법원이다.

**FAQ와 홈페이지 문구** [원문 확인] — [modifactory.com/ko](https://www.modifactory.com/ko), [Framer 번들](https://framerusercontent.com/sites/48gDNeWr5taVlAK00jZK02/TsGrrmNGW.QvdX1RoJ.mjs)
- FAQ Q3: "ISO/IEC 27001 인증을 받은 보안 환경에서 운영되며, 모든 데이터는 전송 구간에서 암호화됩니다. 업로드된 프로젝트 파일은 고객의 명시적 동의 없이 AI 학습용으로 사용되지 않습니다."
- 홈페이지: "AI 무단 학습 차단 — 사용자 프로젝트 데이터의 AI 학습용 무단 활용 및 외부 유출 격리", "글로벌 표준 ISO 27001 인증 환경". KAB-IC-16 마크가 표시된다.

**개인정보처리방침** (2026-02-27 시행) [원문 확인] — terms 번들
- 수집 항목: 이메일, 비밀번호, 닉네임, 브라우저 정보, 접속 IP, 쿠키
- Google Analytics를 사용한다.
- 위탁은 "고객상담 및 지원, 이벤트 등 필요한 경우" 제3자에게 맡길 수 있다고만 적혀 있다. 클라우드 수탁사(AWS 등) 명시는 없다.
- 홈페이지 번들에는 이전 버전으로 보이는 Notion 링크(luxrobo.notion.site/MODI-Factory-Privacy-Policy-…)가 남아 있다.

### Inferences
- 기업 사용자 관점에서 핵심 리스크는 두 가지다(약관 원문에 근거한 해석).
  - (1) 업로드한 원본을 R&D와 학습에 쓸 수 있다(비식별 조건).
  - (2) 생성된 레이아웃의 **IP가 회사에 귀속**된다. 회원은 실시권만 받고 제3자 실시권 부여 권한은 없다.
- 이 때문에 외주 설계사가 고객사 대신 쓰는 경우 등에서 권리관계가 복잡해질 수 있다(추론).
- 홈페이지 추천사("사내 회로 도면 … 서버 접근 권한 관리와 암호화 방식을 확인한 후 팀 전체 공식 툴로 도입")와 약관 내용 사이에 간극이 있다.

### Gaps
- ISO/IEC 27001 인증의 주체(럭스로보 법인인지 클라우드 사업자인지), 범위, 인증서 번호
- 유료 플랜이나 엔터프라이즈 계약에서 데이터와 IP 조항이 달라지는지

---

## 6. 특허: 핵심 특허 번호와 관련 출원

### Takeaway
수상 특허("부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법")의 **번호는 여전히 미확인**이다. Google Patents에 색인되어 있지 않고 KIPRIS는 접속되지 않았다.

대신 같은 "설계자동화 파이프라인"에 대응하는 것으로 보이는 **럭스로보 출원 4건**의 번호와 청구항 원문을 확인했다. 4건 모두 2024-02-29에 출원됐고, 2025-09-05에 공개됐으며, Pending 상태다. 수상 시점(2026-07)과 기술 요지도 원문 기사로 확인했다.

### Cited Findings
- **수상 기사 원문** (2026-07-21, 네이트 전재) [원문 확인] — [m.news.nate.com/view/20260721n00645](https://m.news.nate.com/view/20260721n00645)
  - 제목: "[2026 우수특허대상] 럭스로보"
  - 수상 특허는 "MODI Factory의 핵심 표준화 엔진"이다.
  - 배선 전 부품 간 가상 연결선을 '에어와이어(Air Wire)'로 정의하고, 여기서 "길이·밀집도·교차 등 구조적 특징 데이터를 산출"해 배치와 배선 경로를 사전에 최적화한다.
  - 특징 데이터는 "표준 JSON·벡터 형태로 정형화"된다.
  - "제품 정의·기판 배치·배치 최적화·회로 자동설계·AI 챗봇 설계 지원·부품 DB 관리 등 총 7건의 연관특허가 하나의 설계자동화 파이프라인"을 이룬다.
- **Google Patents 원문** (출원인: 주식회사 럭스로보) [원문 확인]
  - **KR20250132817A** "부품 배치 최적화 서버, 방법 및 컴퓨팅 장치" — [링크](https://patents.google.com/patent/KR20250132817A/ko)
    - 출원 10-2024-0029832, 청구항 10개
    - 청구항 1: 설계 조건에서 부품 특징점과 부품 연결 특징점을 추출한다. 이를 **AI 모델 안의 스코어링 모델**에 넣고, 특징점의 **랜덤 배열**에 따라 추천 레이아웃을 출력한다.
    - 종속항: 자연어 입력, 거리에 따른 가중치, 반도체 > 수동 > 능동 소자 순서의 배치 순위 가중치
  - **KR20250132825A** "전자기판 상의 부품 배치 시스템" — [링크](https://patents.google.com/patent/KR20250132825A/ko)
    - 출원 10-2024-0029848, 청구항 11개
    - 기제작 제품의 기판 설계 DB로 학습한 모델이 유사도로 최적 기판 설계를 고른 뒤 부품을 배열한다.
    - 입력부에 챗봇이 있고, 부품 그룹은 입력, 출력, 전원으로 나뉜다.
  - **KR20250133044A** "회로 자동 설계 서버, 방법 및 컴퓨팅 장치" — [링크](https://patents.google.com/patent/KR20250133044A/ko)
    - 출원 10-2024-0030274, 청구항 10개
    - 설계 조건에서 부품, 연결(Prefix, Footprint, Pin name), 레이아웃을 차례로 결정한다. 입력에 "대규모 언어 모델(LLM) 기반의 자연어 입력 형태"가 들어간다.
  - **KR20250132824A** "제품 카테고리 제공 시스템" — [링크](https://patents.google.com/patent/KR20250132824A/ko)
    - 출원 10-2024-0029847
    - 부품 정보를 넣으면 학습 모델이 설계 제품 카테고리를 추정하고 신뢰도를 매긴다.
  - 발명자로 손승배가 4건 모두에 올라 있다(발명자 검색 결과 기준). 그 밖에 정재우, 최성우, 박휘재가 있다.
  - Google Patents에서 발명자 '손승배'로 검색하면 33건이 나오지만 에어와이어 특허는 없다. 제목 구문("가상 연결 정보")으로 검색해도 0건이다.
- 특허 건수는 출처마다 다르다: TheVC 34건, 다른 기업정보 사이트 36건·29건 [search-snippet], Google Patents 럭스로보 명의 공개문헌 43건(공보 중복 포함) [원문 확인]. 기준이 달라 비교할 수 없다.

### Inferences
- "7건" 가운데 제품 정의, 기판 배치, 배치 최적화, 회로 자동설계 4건은 위 출원과 대응하는 것으로 보인다(추론). 나머지(에어와이어, 챗봇 설계 지원, 부품 DB)는 공개 전이거나 아직 색인되지 않은 것으로 보인다.
- 2024-02 출원 4건은 CES 2024 당시의 "올인원(GPT-4 챗봇, 부품 추천)" 구상을 반영한다. 현재 제품과 직접 대응하는 것은 KR20250132817A(스코어링 배치)와 수상한 에어와이어 특허로 판단된다.

### Gaps
- 수상 특허의 출원번호, 등록번호, 청구항(KIPRIS 타임아웃)
- PCT 또는 미국 출원 여부(EDA 관련 WO 공보는 발견되지 않음)

---

## 7. 정부 R&D, 출시·버전, 가격, 사용자 수, 글로벌 활동

### Takeaway
- **정부 과제명 확인:** 중기부 **글로벌 팁스** "AI 기반 하이브리드 PCB 설계 공정 통합 시스템 개발"(2026~)이다.
- **첫 공개 릴리스:** 2026-03-06이다. 2026-11 현재도 **얼리 액세스** 단계다.
- **가격:** 2026년 말까지 무료다. 앱에는 이미 "크레딧 추가 구매/플랜 업그레이드" UI 문구가 있고, 구독형 요금제를 계획하고 있다.
- **사용자:** 실제 사용자 수는 공개되지 않았다. 2026년 목표는 1만 명, 유료 매출 5억 원이었다.
- **글로벌:** 인도 electronica 참가는 확인됐다. 미국 베타는 실체를 확인하지 못했다.

### Cited Findings
**정부 R&D**
- 강원대 ACE Lab(박찬선 교수) 홈페이지 소스 [GitHub-verified] — [github.com/acelab24/acelab24.github.io](https://github.com/acelab24/acelab24.github.io), [raw index.html](https://raw.githubusercontent.com/acelab24/acelab24.github.io/main/index.html)
  - "중소벤처기업부 · 글로벌 팁스 | 수행 중 | AI 기반 하이브리드 PCB 설계 공정 통합 시스템 개발 | PCB 신호무결성(SI) 수치해석 엔진 개발 · (주)럭스로보 컨소시엄, 연세대학교 공동 | 2026 ~"
- TheVC: "2026년 AI, PCB설계, 통합시스템 관련 국가 R&D 수행", 국가 R&D 11개 [search-snippet] — [TheVC](https://thevc.kr/luxrobo)

**버전 타임라인** (공식 공지 원문) [원문 확인]
- 2024-01: CES 2024에서 알파버전 공개 — [전자신문](https://www.etnews.com/20240104000261)
- 2026-03-06: "MODI Factory가 시작합니다". AI 배치, AI 배선, 파일 Export — [notice-001](https://www.modifactory.com/news/ko/notice-001)
- 2026-03-09: R1.5.2. AI 실행 횟수 제한 도입 — [notice-002](https://www.modifactory.com/news/ko/notice-002)
- 2026-07-09: R2.2.0. AI 배선 노트 무료 베타 — [notice-003](https://www.modifactory.com/news/ko/notice-003)
- 2026-08-21: R2.3.0. 수동 편집, Altium 파일 지원 — [notice-004](https://www.modifactory.com/news/ko/notice-004)
- 2026-09-07: R2.4.0. AI 배치 노트 — [notice-005](https://www.modifactory.com/news/ko/notice-005)
- 2026-09-14: "2026년 연말까지 전 기능 100% 무료" 이벤트 — [event-001](https://www.modifactory.com/news/ko/event-001)
- 홈페이지(2026-11-16): "Altium 플러그인 공식 지원 / 2026 하반기 정식 지원 예정" — [modifactory.com/ko](https://www.modifactory.com/ko)
- PM Joe(2026-08-06경): 현재는 "기존 EDA와 함께 사용하는 확장 기능" 형태이고, "내년에는 자체 에디터"를 오픈할 계획이다 — [pm-joe-interview](https://www.modifactory.com/blog/ko/pm-joe-interview)

**가격** [원문 확인]
- FAQ Q6: "얼리 액세스(Early Access) 기간 동안은 전 기능을 무료 … 정식 출시 시 유료 플랜이 도입될 예정이며, 요금제 변경 전 미리 안내" — [modifactory.com/ko](https://www.modifactory.com/ko)
- 앱 문구에 "크레딧 추가 구매", "플랜 업그레이드"가 이미 정의되어 있다. 약관 제9조는 무료 재화가 "요금제 도입 … 에 따라 변경될 수 있"다고 적는다 — [_app 번들](https://workspace.modifactory.com/_next/static/chunks/pages/_app-ec4fd2cdbc834116.js), [terms 번들](https://workspace.modifactory.com/_next/static/chunks/pages/terms-ec54ed9b10d29642.js)
- 2026-09-11 기사: "무료 요금제를 기반으로 이용자를 확대하고 사용량과 기능에 따른 구독형 서비스를 도입" — [네이트 (2026-09-11, 중앙일보 인턴기자 바이라인)](https://news.nate.com/view/20260911n18067)
- 구체적 가격표는 공개되지 않았다.

**사용자 수와 재무 목표** [원문 확인]
- 뉴스토마토(2026-01-08): "올해 모디 팩토리 단일 프로젝트로 유료 매출 5억원, 유저 1만명을 목표" — [뉴스토마토 1287248](http://www.newstomato.com/readnews.aspx?no=1287248)
- 이투데이(2024-05-26) 오상훈 대표 인터뷰 — [이투데이](https://www.etoday.co.kr/news/view/2363460)
  - 2023년 매출 243억 원
  - "2026년 목표 매출 813억", "2027년엔 매출 2000억 원", "올해엔 BEP 근접"
  - 누적 투자 약 379억 원, MODI 납품 약 4,000개 학교
  - 이 수치들은 MODI Factory 매출이 아니라 회사 전체 목표다.
- 서울경제(2026-03-16): Embedded World 기간 중 "하루 평균 200명 이상의 바이어와 엔지니어가 … 부스를 찾아 상담" — [서울경제](https://www.sedaily.com/article/20019757)
- 앱 관리자 화면 문자열에는 "누적 프로젝트 수", "프로젝트 별 평균 부품 수", "오늘 실패한 프로젝트"가 있다. 그러나 실제 값은 공개되지 않았다 — _app 번들
- 실제 가입자 수나 유료 실적을 공개한 원문은 없다.

**글로벌**
- electronica India 2026(2026-09-16~18, 벵갈루루 BIEC, Hall 5 D73)에서 "알티움 익스텐션 환경에서 모디팩토리가 구동되는 실시간 데모"를 처음 공개했다 [원문 확인] — [blog/ko/electronica-india-2026](https://www.modifactory.com/blog/ko/electronica-india-2026)
- "한국, 미국, 인도를 중심으로 … 글로벌 베타테스트를 준비 중" [원문 확인] — [뉴스토마토 1294739 (2026-03-18)](https://www.newstomato.com/ReadNews.aspx?no=1294739), [서울경제 (2026-03-16)](https://www.sedaily.com/article/20019757)
- 미국 베타, 전시, 파트너 활동은 발견되지 않았다.
- JLCPCB, 국내 PCB 제조사, Altium, Siemens, Cadence와의 공식 제휴 공지는 없다 [원문 확인: 부재]

**Embedded Award 결과 정정**
- PM Joe 원문: "아쉽게도 최종 선정되지는 못했지만 … Tool 분야에서 EDA 관련 툴로는 저희가 최초" [원문 확인] — [pm-joe-interview](https://www.modifactory.com/blog/ko/pm-joe-interview)
- 서울경제(2026-03-16)와 뉴스토마토(2026-03-18)는 모두 "최종 3개 제품에 올라 **2위에 해당하는 성적**"이라고 썼다. 서울경제 사진 설명은 "'설계 자동화' 부문 **수상 후**"다. 주최 측 근거가 없고 회사 PM의 설명과도 맞지 않는다. 보도자료 표현을 그대로 옮긴 것으로 보인다 [unverified] — [서울경제](https://www.sedaily.com/article/20019757), [뉴스토마토](https://www.newstomato.com/ReadNews.aspx?no=1294739)

### Inferences
- 공식 "정식 출시일"은 아직 없다. 2026-03-06부터 얼리 액세스가 이어지고 있고, 유료 전환은 2027년 이후로 보인다. 2026년 말까지 무료이므로 "2026년 유료 매출 5억 원" 목표는 사실상 달성이 어렵다(추론).

### Gaps
- 글로벌 팁스 과제의 금액, 기간, 기관별 역할(NTIS 원문 미확인)
- 실제 가입자 수와 기업 고객 수
- Altium 익스텐션 정식 배포일

---

## 8. 독립 사용자 반응과 비판

### Takeaway
**독립 사용자 후기는 0건이다.** 확인한 곳은 HN, KiCad 포럼, 국내 검색이고, Reddit은 403으로 막혔다. 공식 추천사는 **한국어판과 영어판의 내용이 서로 모순**된다.

### Cited Findings
- HN Algolia 검색에서 `"MODI Factory"`는 0건이다. `luxrobo`는 2016년 MODI 교구 리뷰 외에는 관련 글이 없다 [원문 확인] — [hn.algolia.com API](https://hn.algolia.com/api/v1/search?query=%22MODI%20Factory%22)
- KiCad 공식 포럼 검색에서 "modifactory"와 "MODI Factory"는 모두 0건이다 [원문 확인] — [forum.kicad.info/search.json?q=modifactory](https://forum.kicad.info/search.json?q=modifactory)
- 국내에서 "모디팩토리 후기"를 검색하면 보도자료와 공식 블로그만 나온다 [search-snippet]
- **추천사 모순** [원문 확인] — [modifactory.com/ko](https://www.modifactory.com/ko), [modifactory.com](https://www.modifactory.com/)
  - 한국어판: "Altium Designer 플러그인까지 연동되면 더 편리해 질 것 같아서 기대됩니다." 아직 쓰지 않았다는 뜻이다.
  - 영어판 같은 자리: "running placement and routing directly inside the Altium Designer panel is what actually changed how we work." 이미 쓰고 있다는 뜻이다.
  - 작성자 실명이나 소속은 없다.
- 회사가 스스로 밝힌 한계 [원문 확인]
  - "아직 완벽하진 않습니다" — [notice-001](https://www.modifactory.com/news/ko/notice-001)
  - "어떨 때는 결과가 깔끔하고 어떨 때는 아쉬워요" — [tutorials-004](https://www.modifactory.com/blog/ko/tutorials-004)
  - 열 해석은 "특정 PCB 조건에 맞춰 최적화된 상태"다.
  - 약관 제21조는 "실제 제조, 양산 … 사용을 보장하지 않습니다"라고 명시한다.
- 뉴스토마토 원문(2026-01-08)은 럭스로보를 "산업용 로봇 제조업체"로 소개한다. 기존 노트가 "요약 오류"로 판단한 표현은 실제 원문 표현이었다 [원문 확인] — [뉴스토마토 1287248](http://www.newstomato.com/readnews.aspx?no=1287248)

### Gaps
- 디시인사이드, 클리앙, 네이버 카페, EEVblog 원문 전수 확인. EEVblog 검색 페이지는 결과가 렌더링되지 않았다.

---

## 9. 럭스로보 매출 수치 충돌 해소 (DART와 기사 원문)

### Takeaway
**충돌이 해소됐다.**
- 2023년 매출 **242.8억 원은 연결** 기준이다. 이투데이 "243억", 이데일리 "243억"과 맞는다.
- **113.7억 원은 별도** 기준이다.
- 뉴스톱(2025-12-11)은 2022년 연결(179억)과 2023년 별도(114억)를 섞어 "연결"이라고 썼다.
- 2024년과 2025년 감사보고서는 DART에 없다.

### Cited Findings
- **2023 연결감사보고서** (이촌회계법인, 2024-04-05, 적정) [원문 확인] — [DART 20240405001142](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001142)

  | 항목 | 2023 | 2022 |
  |---|---|---|
  | 매출 | 24,279,298,188원 | 17,907,796,112원 |
  | 영업손실 | 60.79억 | 118.12억 |
  | 당기순이익 | -174.24억 | +59.35억 (금융수익 179.6억 영향) |

- **2023 별도감사보고서** [원문 확인] — [DART 20240405001133](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20240405001133)

  | 항목 | 2023 | 2022 |
  |---|---|---|
  | 매출 | 11,367,996,301원 | 10,348,173,636원 |
  | 영업손실 | 44.69억 | 108.99억 |
  | 당기순이익 | -160.95억 | — |

- 연결과 별도의 차이는 종속기업 때문이다: (주)큐버(지분 50.57%, 유선 통신장비, 2023 매출 117.9억), (주)럭키박스솔루션(63.83%, 2023 매출 11.8억) [원문 확인] — 같은 감사보고서 주석
- 주석상 설립일은 **2014-11-14**다(TheVC는 11-13). 2023년 말 본사는 **서울 서초구 강남대로 311(한화생명보험빌딩)**이다 [원문 확인]
- 이투데이 원문(2024-05-26): "지난해 매출 243억" [원문 확인] — [이투데이](https://www.etoday.co.kr/news/view/2363460)
- 뉴스톱 원문(2025-12-11) [원문 확인] — [뉴스톱 41685](https://www.newstopkorea.com/news/articleView.html?idxno=41685)
  - 매출: "연결기준 매출액은 2022년 179억원 … 2023년부터 114억원, 지난해 49억원 … 올해 3분기 기준 매출액은 12억원"
  - 상장: 2024-07 코스닥 예비심사 신청, **2024-10 철회**
  - 2025-10: 에이프로 대상 RCPS 3억 원(전환가 24,500원, 기업가치 약 2,300억 원)
  - 2025-12: 벤처펀드 대상 RCPS 30억 원. **전환가 7,500원으로 직전의 약 30%**다. 같은 달 오상훈 대표가 보통주 약 30억 원을 인수했다.
  - 차입금 80억 원이 2026-04부터 만기다.
  - 최대주주는 오상훈 29.59%, 2대주주는 한화시스템 11.61%다.
  - "2022년부터 … 모디 팩토리를 자체 개발"
- 2024년과 2025년 감사보고서(F001~F004)는 DART 상세검색(2023-01-01~2026-11-16)에 없다 [원문 확인: 부재] — [DART](https://dart.fss.or.kr/dsab007/main.do)
- Wadiz 프로필 매출 표기는 2023년 11,367, 2024년 4,944, 2025년 1,666이다(단위 미표기) [search-snippet] — [wadiz](https://www.wadiz.io/maker/detail/1122379/makerInfo)
- 직원 수는 원티드 42명, 캐치 49명이다 [search-snippet] — [원티드](https://www.wanted.co.kr/company/455), [캐치](https://www.catch.co.kr/Comp/CompSummary/M33133)

### Inferences
- Wadiz의 11,367은 DART 별도 매출(11,367,996,301원)과 정확히 일치한다. 따라서 Wadiz 표기는 **별도 기준, 단위 백만 원**으로 판단된다. 이에 따르면 별도 매출은 2024년 49.4억, **2025년 16.7억**이다(2024·2025는 감사보고서 원문이 없어 미검증).
- 2025년 말 투자 단가가 70% 할인됐고 차입금 만기도 다가온다. 2024-05 인터뷰의 "2026년 목표 매출 813억"과 대비하면 서비스 지속성 리스크를 보여 주는 정량 근거다.

### Gaps
- 2024년과 2025년 감사보고서 원문
- 현재 본사 주소. 원티드는 '서울 강남구'로 표기한다(검색 요약 기준).

---

## 여전히 미해결인 항목 (요약)

1. 수상 특허 "부품 간 가상 연결 정보의 구조적 특징 데이터를 이용한 설계 최적화 장치 및 방법"의 출원번호, 등록번호, 청구항: KIPRIS 타임아웃, Google Patents 미색인
2. 레이어 수 상한, 차동쌍·임피던스 지원 여부, Altium .PcbDoc 내보내기에서 룰과 스택이 보존되는지
3. SI/PI/EMC의 제품화 시점, 열 해석이 현재 UI에 노출되는지 여부
4. 실제 가입자 수와 기업 고객, 2027년 이후 요금표와 크레딧 단가
5. 글로벌 팁스 과제 금액과 기간, 미국 베타의 실체
6. 사용하는 LLM, ISO/IEC 27001 인증 주체와 범위, 유료·엔터프라이즈 플랜의 데이터·IP 조항
7. 2024년과 2025년 감사보고서(DART 미공시)
8. 독립 사용자 후기와 제3자 벤치마크: 없음
