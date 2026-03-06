---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.483731+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: aws_availability_zones
    weight: 9
    confidence: 0.98
  - name: aws_regioes_geograficas
    weight: 10
    confidence: 0.99
  - name: latencia_rede_aws
    weight: 8
    confidence: 0.95
  - name: custo_servicos_aws
    weight: 7
    confidence: 0.9
  - name: requisitos_legais_aws
    weight: 7
    confidence: 0.92
  - name: acesso_servicos_aws_china
    weight: 6
    confidence: 0.88
  - name: disponibilizacao_servicos_multiplas_regioes
    weight: 8
    confidence: 0.93
  - name: separacao_regioes_aws
    weight: 6
    confidence: 0.85
  - name: produtos_disponiveis_por_regiao_aws
    weight: 7
    confidence: 0.89
  - name: curso_aws202001
    weight: 5
    confidence: 0.8
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.77'
  - '338.4'
  - '341.1'
  cdu_description: Organização de sistemas de computadores, redes de computadores, infraestrutura de nuvem, com considerações sobre custos e regulamentações.
---
Um conjunto de [[AWS Avaibility Zones]]? Sim, na aula do curso [[aws202001]] a tutora fala que regiões são "regiões geográficas com duas ou mais [[AWS Avaibility Zones]]"

- Pontos a levar em consideração : latência x custo x requisitos legais. Usuários da China, por exemplo, só podem acessar serviços daquela região.
	- Você pode disponibilizar os seus serviços em múltiplas regiões para se beneficiar da latência de rede quando tem muitos usuários em certos países.
- Regiões são completamente separadas umas das outras. Nem todas as regiões tem todos os produtos.

Não encontrei definição [documentação](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)