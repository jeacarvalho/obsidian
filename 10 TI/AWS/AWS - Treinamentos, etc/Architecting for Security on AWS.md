---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.736105+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: arquitetura_seguranca_aws
    weight: 10
    confidence: 0.98
  - name: protecao_credenciais_aws
    weight: 9
    confidence: 0.97
  - name: confidencialidade_integridade_disponibilidade_aws
    weight: 8
    confidence: 0.96
  - name: seguranca_armazenamento_aws
    weight: 7
    confidence: 0.94
  - name: seguranca_computacao_aws
    weight: 7
    confidence: 0.93
  - name: seguranca_rede_aws
    weight: 7
    confidence: 0.92
  - name: configuracao_servicos_aws
    weight: 6
    confidence: 0.9
  - name: seguranca_sistema_operacional_ec2
    weight: 6
    confidence: 0.89
  - name: criptografia_dados_aws
    weight: 8
    confidence: 0.95
  - name: gerenciamento_logs_aws
    weight: 7
    confidence: 0.91
  cdu_primary: 004.414.2
  cdu_secondary:
  - '004.89'
  - '004.77'
  cdu_description: Segurança de sistemas de computadores. Segurança em redes de computadores. Segurança de dados.
---
Architecting for Security on AWS

Protecting AWS Credentials

- CIA - Confidencialidade (ACL), Integridade (DB seguro), Avaliabilty
- Proteger storage, computing and network
- Levels of security
    - AWS services bem configurados
    - OS ok na instância EC2
    - Aplicações
    - Proteger:
        - Credenciais
        - Capturar e analisar logs
        - Redes
        - Data armazenada (in rest)
            - Criptografia
            - Permissões
        - Data trafegando (in transit)
            - Cirptografia
        - Configurar backup, replicação e recovery