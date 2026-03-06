---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:58.581913+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: zonas_de_disponibilidade_aws
    weight: 10
    confidence: 0.98
  - name: regioes_aws
    weight: 9
    confidence: 0.95
  - name: data_centers_aws
    weight: 8
    confidence: 0.92
  - name: infraestrutura_nuvem_aws
    weight: 7
    confidence: 0.9
  - name: rede_aws
    weight: 6
    confidence: 0.85
  - name: isolamento_geografico_aws
    weight: 7
    confidence: 0.88
  - name: provedores_eletricidade_aws
    weight: 5
    confidence: 0.8
  - name: seguranca_infraestrutura_aws
    weight: 6
    confidence: 0.82
  - name: alta_disponibilidade_aws
    weight: 8
    confidence: 0.91
  - name: arquitetura_nuvem_aws
    weight: 7
    confidence: 0.89
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.6'
  - '004.8'
  cdu_description: Redes de computadores. Redes de telecomunicações. Infraestrutura de computação em nuvem. Arquitetura de sistemas de computadores.
---
- Na aula em [[aws202001]] a tutora a define como um conjunto de data centers de uma [[AWS Regions]] específica. Cada zona é separada fisicamente, conectadas entre si por recursos rápidos de rede. 
- Na mesma aula a tutora fala que cada zona deve ser provida por diferentes provedores de eletricidade, por exemplo.

*Availability Zones are multiple, isolated locations within each [[AWS Regions]]*

fonte: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html