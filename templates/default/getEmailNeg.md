---
PromptInfo:
  promptId: getEmailNeg
  name: ✉️ Reply to Email negatively 😡
  description: select the email content and negative reply will be generated
  author: Noureddine
  tags: communication, email
  version: 0.0.1
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:11.049462+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_resposta_email_negativa
    weight: 10
    confidence: 0.98
  - name: automacao_comunicacao_escrita
    weight: 9
    confidence: 0.95
  - name: processamento_linguagem_natural_email
    weight: 8
    confidence: 0.92
  - name: redacao_profissional_negativa
    weight: 7
    confidence: 0.9
  - name: analise_conteudo_email
    weight: 6
    confidence: 0.88
  - name: ferramenta_assistente_escrita
    weight: 5
    confidence: 0.85
  - name: geracao_texto_inteligente
    weight: 7
    confidence: 0.87
  - name: comunicacao_empresarial_digital
    weight: 6
    confidence: 0.86
  - name: resposta_automatizada_email
    weight: 8
    confidence: 0.91
  - name: etica_comunicacao_negativa
    weight: 5
    confidence: 0.8
  cdu_primary: '004.77'
  cdu_secondary:
  - '801.314'
  cdu_description: Sistemas de comunicação eletrônica; Processamento de texto e linguagem natural para comunicação escrita.
---
prompt:
reply to this email negatively in professional way. 
email: 
{{context}}
reply: 
''