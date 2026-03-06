---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:59.284593+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: computacao_em_nuvem
    weight: 10
    confidence: 0.98
  - name: entrega_sob_demanda
    weight: 9
    confidence: 0.95
  - name: escalabilidade_nuvem
    weight: 8
    confidence: 0.92
  - name: elasticidade_nuvem
    weight: 8
    confidence: 0.91
  - name: confiabilidade_nuvem
    weight: 7
    confidence: 0.88
  - name: seguranca_nuvem
    weight: 7
    confidence: 0.87
  - name: iaas
    weight: 6
    confidence: 0.85
  - name: paas
    weight: 6
    confidence: 0.85
  - name: saas
    weight: 6
    confidence: 0.85
  - name: arquitetura_software_nuvem
    weight: 5
    confidence: 0.8
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.77'
  - '004.78'
  cdu_description: Redes de computadores. Internet. Serviços de rede. Serviços de computação em nuvem
---
_"Computação em nuvem refere-se a entrega sob demanda de recursos e aplicativos de TI por meio da internet"_

- Entrega: Buscamos, não entregamos.
- sob demanda: conforme necessidade. Nem mais, nem menos, se soubermos configurar e acompanhar corretamente. Equilíbrio entre custo e performance aqui.
- recursos e aplicativos: [[IAAS]], [[PASS]], [[SASS]]

Conceitos **importantes** ressaltados aqui:

- **Escalabilidade** - "Adicionar recursos conforme necessidade". capacidade de crescer conforme aumento de demanda e voltar ao padrão anterior conforme normalização da mesma
- **Elasticidade** - "Poder de ajustar a escala de recursos, para baixo ou para cima, facilmente" (poderia ser escalável, mas não elástica, ou seja, não ser fácil escalar e reduzir...)
- **Confiabilidade** (Relaiabilty) - Capacidade de se recuperar de falhas... Mitigar interrupções e aumentar recursos com facilidade. [[Arquitetura de software]] deve ser bem planejada para detectar falhas e se corrigir automaticamente (essa palavra é chave aqui)
	- Regiões AWS ([[AWS Regions]])
	- Zonas de disponibilidade ([[AWS Avaibility Zones]])
	- [[edge locations]]
- **Segurança** - Você lida com seus dados, onde (quais regiões) e como os armazena e a criptografia envolvida. Além disso, é possível monitorar continuamente o uso dos recursos

next: [[Introdução às interfaces AWS]]