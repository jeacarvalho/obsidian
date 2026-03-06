---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:57.831142+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: automacao_leitura_log_acesso
    weight: 10
    confidence: 0.98
  - name: indicadores_uso_sistema
    weight: 9
    confidence: 0.95
  - name: reengenharia_sistema
    weight: 8
    confidence: 0.9
  - name: processamento_dados_pentaho
    weight: 7
    confidence: 0.85
  - name: visualizacao_dados_datastudio
    weight: 7
    confidence: 0.88
  - name: coleta_informacoes_servlet
    weight: 8
    confidence: 0.92
  - name: monitoramento_prometheus
    weight: 8
    confidence: 0.91
  - name: painel_grafana
    weight: 9
    confidence: 0.94
  - name: geracao_planilha_sheets
    weight: 6
    confidence: 0.8
  - name: otimizacao_performance_sistema
    weight: 7
    confidence: 0.87
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.6'
  - '004.7'
  - '004.8'
  cdu_description: 004.4 - Programação de computadores; 004.6 - Gestão de dados; 004.7 - Processamento de dados; 004.8 - Sistemas de informação
---
#### DWBK Isenção

| links | Arquivos |
| ----- | -------- |
|       |          |

##### 20210126
- Flop explicando o estudo que fez e documentou [aqui](https://meet.google.com/linkredirect?authuser=2&dest=https%3A%2F%2Fgit.[[serpro]]%2Fdedat%2Fdeat7%2Fsuporte%2F-%2Fissues%2F10)
- A princípio a proposta 1 abaixo seria a melhor alternativa
- Nova reunião será marcada para 20210209

___
##### 20210119 - Definição do problema: Automatizar leitura de log, carga de sheets

- Com o uso do sistema a performance foi caindo. Telas quebraram inclusive
- Houve reengenharia e cliente demandou indicadores de uso do sistema
- Pegar log de acesso para apresentar ao cliente indicadores de funcionalidades do sistema
- Extraindo pelo HPOO, manualmente, uma vez por semana
- Pentaho (PDI) para fazer transformação com arquivo muito grande
- Datastudio apresenta os resultados
- Necessidade: ou automatizar isso ou gerar solução nova que não demande intervenção manual

**Proposta 1:**

a) Automatizar leitura de log do HPOO - Danilo conhece, demanda cpf e senha pessoal
b) Criar um script que faça o processamento que hoje é feito com Pentaho
c) Automatizar a população das informações da planilha sheets que o datastudio usa

**Proposta 2:** 

a) Filtro de servlet que fique coletando as informações expondo as informações no formato do prometheus
b) Criar um painel grafana no estaleiro e aposentar o datastudio

DEDAT vai estudar item da proposta 2. Nova reunião DWBK Isenção para 