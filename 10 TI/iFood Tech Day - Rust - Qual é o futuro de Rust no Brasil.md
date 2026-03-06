---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:56.419402+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: borrow_checker_rust
    weight: 9
    confidence: 0.9
  - name: produtividade_desenvolvedor_rust
    weight: 8
    confidence: 0.85
  - name: tooling_rust
    weight: 7
    confidence: 0.8
  - name: sistema_tipos_rust
    weight: 7
    confidence: 0.8
  - name: bibliotecas_rust
    weight: 6
    confidence: 0.75
  - name: clippy_rust
    weight: 6
    confidence: 0.7
  - name: curva_aprendizado_rust
    weight: 8
    confidence: 0.88
  - name: rust_edu
    weight: 5
    confidence: 0.65
  - name: monitoramento_codigo_rust
    weight: 8
    confidence: 0.82
  - name: escalabilidade_aws_ecs
    weight: 7
    confidence: 0.78
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.73'
  - '004.6'
  - '004.21'
  cdu_description: Programação de computadores; Sistemas de computadores; Redes de computadores; Linguagens de programação
---
[[Rust]]
# Matsakis
- Manter a evolução do código é mais fácil com o borrow checker
- Mesmo em rust há relatos de aumento de velocidade dos desenvolvedores. POr quê?
	- Tooling
	- type system
	- libraries
- Clippy - tools para analisar o código ainda mais profundamente do que o compiler
- 3 a 6 meses para aprender a linguagem. No início, duro e frustrante. Mas uma vez na esquina, ao virar, vc não entende como usar outras linguagens. Rust: A linguagem onde a ressaca vem antes da diversão.
- Rust Edu --> Esforço de ensino da linguagem

# 2o palestrante, de Maria Paula, Niterói
- Open telemetry + TRacing (tokio) --> Monitorando o código rust
- Escalabilidade - AWS ECS --> Livre-se do kubernetes?
- Failover  - Kafka, Amazon SQ, RabbitMq, Amazon SNS, Amazon Kinesis
- Solid - Escreva para outras pessoas!
- CI/CD - Faça rollback rápido! Canary test