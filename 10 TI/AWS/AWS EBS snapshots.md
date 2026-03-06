---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:58.672918+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: snapshots_incrementais
    weight: 10
    confidence: 0.98
  - name: backup_incremental
    weight: 9
    confidence: 0.97
  - name: blocos_modificados
    weight: 8
    confidence: 0.96
  - name: armazenamento_em_nuvem
    weight: 7
    confidence: 0.95
  - name: gerenciamento_de_dados
    weight: 6
    confidence: 0.94
  - name: recuperacao_de_dados
    weight: 5
    confidence: 0.93
  - name: snapshots_aws
    weight: 10
    confidence: 0.98
  - name: ebs_snapshots
    weight: 9
    confidence: 0.97
  - name: aws_ec2
    weight: 8
    confidence: 0.96
  - name: tecnologia_de_backup
    weight: 7
    confidence: 0.95
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.6'
  cdu_description: 004.4 - Armazenamento de dados; 004.6 - Redes de computadores e telecomunicações
---
*Snapshots são backups incrementais, o que significa que somente os blocos no dispositivo que tiverem mudado depois do snapshot mais recente serão salvos
*

fonte: https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/EBSSnapshots.html