---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:53.872823+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: sistema_cadin_pgfn
    weight: 10
    confidence: 0.98
  - name: requisitos_api_gateway
    weight: 9
    confidence: 0.95
  - name: alta_disponibilidade_sistema
    weight: 8
    confidence: 0.92
  - name: gestao_api_cadastro_entidades
    weight: 7
    confidence: 0.9
  - name: monitoracao_logs_api
    weight: 6
    confidence: 0.88
  - name: plin_governo_sgd
    weight: 7
    confidence: 0.85
  - name: migracao_base_adabas
    weight: 8
    confidence: 0.93
  - name: datalake_sira_entes_publicos
    weight: 9
    confidence: 0.96
  - name: troca_arquivos_cadin
    weight: 6
    confidence: 0.8
  - name: cliente_cadin_caixa_economica
    weight: 5
    confidence: 0.75
  cdu_primary: '351.7'
  cdu_secondary:
  - '004.6'
  - '336.2'
  - '351.8'
  cdu_description: Administração pública. Finanças públicas. Gestão de dados e sistemas de informação governamentais.
---
## 20230531 - Api gateway novo Cadin
- Requisitos 
	- Ser utilizado por entidades públicas e privadas  
	- Alta disponibilidade: 99,9% com 1000 requisições em 1 segundo  
	- Mecanismo de gestão da API (cadastro de entidades que vão usar, geração de token, bilhetagem, etc) que possa ser operado pela própria PGFN  
	- Monitoração  
	- Logs
- 
___
## 202200928 - Novo CADIN X Plin
- ConectaGOV - Plin para governo, controlado pela SGD
- Plin não pode ser usado por entes externos
	- Mas Bisotto só não faz pq não tem recurso para isso.

___
## 202200810 - Apoio Arquitetural - Novo CADIN PGFN + SIRA
- Cadin - cad. inadimplentes, gerido pelo BC. Uma lei transfere para a PGFN. 
- PGFN quer fazer novo sistema
- 22 a 26/08 inception em Brasília
- Grande base adabas com 110 milhões de registros, que devem ser migrados para nova solução
- Solução nova vai englobar essa base, api que permita que consultar, inserir e excluir do Cadin. 
- Uma app web para gestão da PGFN
- Manter mecanismo que existe de troca de arquivos
- Principal cliente do Cadin é Caixa econômica
- Stamato líder conduzindo.
### SIRA
- Grande datalake cujos dados serão servidos a entes públicos e privados
- Time SUPAI estava presente (Osnir)
- Armazenamento dos dados foi bem discutido