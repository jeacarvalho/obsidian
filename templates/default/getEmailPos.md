---
PromptInfo:
  promptId: getEmailPos
  name: ✉️ Reply to Email positively 😄
  description: select the email and a positive reply will be generated
  author: Noureddine
  tags: communication, email
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:10.905531+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_resposta_email
    weight: 10
    confidence: 0.98
  - name: resposta_positiva_email
    weight: 9
    confidence: 0.97
  - name: comunicacao_profissional
    weight: 8
    confidence: 0.96
  - name: processamento_linguagem_natural
    weight: 7
    confidence: 0.9
  - name: automacao_resposta
    weight: 6
    confidence: 0.85
  - name: analise_contexto_email
    weight: 5
    confidence: 0.8
  - name: redacao_profissional
    weight: 7
    confidence: 0.92
  - name: inteligencia_artificial_comunicacao
    weight: 6
    confidence: 0.88
  - name: ferramenta_assistente_email
    weight: 5
    confidence: 0.82
  - name: otimizacao_comunicacao
    weight: 5
    confidence: 0.78
  cdu_primary: '004.77'
  cdu_secondary:
  - '801.314'
  cdu_description: Sistemas de comunicação eletrônica; Redação e estilo de comunicação
---
prompt:
reply to this email positively in professional way. 
email: 
{{context}}
reply: 
