# ⚡ EMag (Ansys Maxwell)

!!! info "Skill Summary"
    **전문 분야:** Delta-type IPM 모터 설계 / AI 최적화 / 손실 분석  
    **주력 툴:** Ansys Maxwell 2D/3D, Ansys Workbench

## 🛠️ Capability & Workflow

=== "✅ 체크리스트 (Skills)"

    **모델링 및 설정**
    - [x] **Parametric Model**: 설계 변수(형상, 권선) 파라미터화 및 최적화 연동
    - [ ] **Mesh Operation**: Air-gap 및 Magnet 주변 정밀 격자 생성 (Skin depth 고려)
    - [ ] **Boundary Condition**: Master/Slave 경계 조건 및 Vector Potential 설정

    **해석 및 결과**
    - [ ] **Loss Analysis**: Core loss, Eddy current loss 분리 및 분석
    - [ ] **Drive Cycle**: 전류 위상각 제어(MTPA/MTPV) 및 효율 맵(Efficiency Map) 도출
    - [ ] **Co-Simulation**: Simplorer 또는 외부 회로 연동 해석

=== "🔄 프로세스 (Workflow)"

    ```mermaid
    graph LR
      A[형상/변수 정의] -->|Maxwell 2D| B(전자기 해석)
      B --> C{결과 분석}
      C -->|OK| D[Workbench 연동]
      C -->|NG| A
      D --> E[구조/열 해석]
      style A fill:#f9f,stroke:#333,stroke-width:2px
      style B fill:#bbf,stroke:#333,stroke-width:2px
    ```

=== "📂 대표 산출물"

    | 날짜 | 프로젝트/주제 | 링크 | 비고 |
    | :--- | :--- | :--- | :--- |
    | 2026-01-26 | IPM Rotor Stress Study | [Log 이동](../log/2026/2026-01-26.md) | 초기 모델링 |
    | 2026-01-20 | Core Loss 비교 | [Log 이동](#) | 재질 변경 테스트 |

---

## 💡 Trouble Shooting & Tips

!!! warning "주의사항: 메시 설정"
    IPM 모터의 경우 Magnet 모서리 부분에서 자속밀도가 급변하므로, **Mesh Operation**에서 `Length Based`보다는 `Inside Selection`을 사용하여 모서리 부분의 격자를 조밀하게 가져가야 해석 오차를 줄일 수 있음.

!!! tip "Tip: Workbench 연동"
    Maxwell에서 파라미터를 변경하고 Update할 때, Workbench의 **Design Point** 기능을 활용하면 여러 케이스를 밤새 돌려놓기 편함. (CSV로 Export 가능)