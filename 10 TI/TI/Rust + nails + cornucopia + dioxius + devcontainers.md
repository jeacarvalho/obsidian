---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.945336+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: linguagem_programacao_rust
    weight: 10
    confidence: 0.98
  - name: desenvolvimento_startup_rust
    weight: 9
    confidence: 0.9
  - name: infraestrutura_como_codigo_alternativas
    weight: 8
    confidence: 0.85
  - name: geracao_codigo_rust_sql
    weight: 7
    confidence: 0.8
  - name: framework_ui_rust
    weight: 7
    confidence: 0.82
  - name: ferramentas_desenvolvimento_devcontainers
    weight: 6
    confidence: 0.75
  - name: arquitetura_software_rust
    weight: 8
    confidence: 0.88
  - name: componentes_rust_cornucopia
    weight: 6
    confidence: 0.78
  - name: geracao_interface_visual_rust
    weight: 7
    confidence: 0.81
  - name: configuracao_ambiente_devcontainers
    weight: 6
    confidence: 0.76
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.7'
  - '004.8'
  cdu_description: Programação e desenvolvimento de software com foco na linguagem Rust, incluindo ferramentas de infraestrutura como código, geração de código a partir de SQL, frameworks de interface visual e containers de desenvolvimento.
---
#### Rust + nails + cornucopia + dioxius + devcontainers
- Estudando sobre rust. Hoje, no weekly, veio um link para um artigo sobre um cara ter usado rust em sua startup e falando que faria a mesma escolha hoje.
- Ali no artigo muito coisa legal apareceu
- Se entendi, o cara criou o [Rust on nails](https://rust-on-nails.com/docs/ide-setup/introduction/). E, na documentação, um monte de decisão arquitetural que trouxe um monte de novidade. 
- A 1a, uma alternativa ao Terraform - [[Iac_Serpro#20230317 - Pulumi x terraform]]
- Depois, um monte de decisão arquitetural com componentes que nunca tinha ouvido falar: cornucopia - https://github.com/cornucopia-rs/cornucopia; um treco que gera functions rust a partir do sql; [diouxious](https://dioxuslabs.com/) um treco que gera interface visual a partir do rust
- Na mesma thread, conheci a possibilidade de dev containers: [https://code.visualstudio.com/docs/devcontainers/containers](https://code.visualstudio.com/docs/devcontainers/containers "https://code.visualstudio.com/docs/devcontainers/containers")