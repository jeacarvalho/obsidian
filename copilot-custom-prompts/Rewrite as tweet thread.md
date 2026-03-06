---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: false
copilot-command-context-menu-order: 1120
copilot-command-model-key: ''
copilot-command-last-used: 0
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:42.009575+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: geracao_de_threads_twitter
    weight: 9
    confidence: 0.98
  - name: formato_de_tweets
    weight: 8
    confidence: 0.95
  - name: limite_de_caracteres_twitter
    weight: 7
    confidence: 0.92
  - name: marcadores_de_inicio_fim_thread
    weight: 6
    confidence: 0.9
  - name: separadores_de_tweets
    weight: 6
    confidence: 0.88
  - name: conteudo_engajador_twitter
    weight: 7
    confidence: 0.85
  - name: conversao_json_para_thread
    weight: 8
    confidence: 0.96
  - name: regras_de_formatacao_twitter
    weight: 9
    confidence: 0.97
  - name: estruturacao_de_conteudo_online
    weight: 5
    confidence: 0.8
  - name: ferramentas_de_automacao_conteudo
    weight: 6
    confidence: 0.82
  cdu_primary: '004.77'
  cdu_secondary:
  - '004.89'
  - '302.23'
  cdu_description: Processamento de dados e informação. Redes de comunicação. Redes sociais. Aplicações de inteligência artificial.
---
Convert {} into a Twitter thread following these rules:
    1. Each tweet must be under 240 characters
    2. Start with "THREAD START" on its own line
    3. Separate tweets with "

---

"
    4. End with "THREAD END" on its own line
    5. Make content engaging and clear
    Return only the formatted thread.