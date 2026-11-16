# NOAH Factory

증거 기반 AI PCB 설계 서비스를 만드는 프로젝트입니다. 현재 **Phase 0(기술 검증)** 단계로, KiCad 보드를 받아 자동 배치 → 자동 배선 → DRC 검증 → **모든 문장이 검사 결과를 인용하는 설계 리뷰 리포트** → 제조 파일까지 만드는 파이프라인이 들어 있습니다.

## 문서

| 문서 | 내용 |
|---|---|
| [`reports/모디팩토리 AI PCB 설계 조사.md`](reports/모디팩토리%20AI%20PCB%20설계%20조사.md) | MODI Factory 분석, 국내외 학술자료, 유사 프로젝트, 한계와 개선 방향 |
| [`docs/product-plan.md`](docs/product-plan.md) | 제품 기획서 |
| [`docs/architecture.md`](docs/architecture.md) | 기술 아키텍처 |
| [`docs/decisions.md`](docs/decisions.md) | 결정 기록 |
| [`bench/results/summary.md`](bench/results/summary.md) | Phase 0 벤치마크 결과 |

## 파이프라인

```
KiCad 보드 ─► Design IR ─► 배치 (어닐링 + 디커플링·커넥터·고정·장애물 규칙, 시드 병렬)
          ─► Freerouting 배선 ─► kicad-cli DRC (+ 회로도 일치성)
          ─► 증거(evidence.json) ─► 검증된 주장(claims.json) ─► report.md
          ─► Gerber·드릴·부품 좌표 (fab/)
```

리포트의 문장은 증거 레코드를 인용해야 하며, 문장 속 숫자나 부품·넷 이름이 증거와 다르면 자동으로 제외됩니다(`noah_factory/evidence.py`).

## 설치 (Ubuntu 24.04 기준)

KiCad 10 (PPA, 라이브러리 없이 설치):

```bash
sudo python3.12 /usr/bin/add-apt-repository -y ppa:kicad/kicad-10.0-releases
```

```bash
sudo apt-get install -y --no-install-recommends kicad kicad-demos
```

Freerouting은 Java 25가 필요합니다. 소스에서 빌드하면 Gradle이 JDK 25를 내려받습니다:

```bash
git clone --depth 1 https://github.com/freerouting/freerouting && cd freerouting && ./gradlew --max-workers=1 executableJar -x test
```

빌드된 `build/libs/freerouting-current-executable.jar` 위치와 Java 25 경로를 환경 변수로 지정합니다(기본값: `/opt/freerouting/freerouting.jar`, `/opt/jdk25/bin/java`):

```bash
export NOAH_FREEROUTING_JAR=/path/to/freerouting-current-executable.jar NOAH_JAVA=/path/to/jdk25/bin/java
```

Python 환경 (`pcbnew` 모듈을 쓰기 위해 시스템 Python 3.12 + `--system-site-packages`):

```bash
python3.12 -m venv --system-site-packages .venv && .venv/bin/pip install numpy pytest
```

## 사용법

```bash
.venv/bin/python -m noah_factory run /usr/share/kicad/demos/ecc83/ecc83-pp.kicad_pcb --out runs/ecc83 --lock P1,P2 --init random
```

주요 옵션: `--lock`(고정 부품), `--edge`(가장자리에 둘 부품), `--seeds`, `--candidates`, `--place-time`(시드당 초), `--init random|current`, `--route-passes`, `--no-route`, `--no-export`.

결과 폴더:

| 경로 | 내용 |
|---|---|
| `report.md` | 설계 리뷰 리포트 (검증된 문장, 확인 필요한 DRC 항목, 검증하지 않은 항목) |
| `evidence.json`, `claims.json` | 증거 레코드와 주장 |
| `candidates/` | 배치 후보 (배선 전) |
| `final/` | 배선까지 끝난 KiCad 프로젝트 |
| `fab/` | Gerber·드릴·부품 좌표, `fabrication.zip` |
| `run.json` | 단계별 시간, 지표 요약 |

## 테스트와 벤치마크

```bash
.venv/bin/python -m pytest -q
```

```bash
.venv/bin/python bench/run_bench.py
```

## 라이선스 메모

KiCad와 Freerouting(GPL-3.0)은 별도 프로세스로 실행하며 이 저장소에 포함하지 않습니다. 배포 형태가 정해지면 법률 검토가 필요합니다(`docs/architecture.md` §11).
