---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:54.973187+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: automacao_vault
    weight: 10
    confidence: 0.98
  - name: gerenciamento_arquivos
    weight: 9
    confidence: 0.95
  - name: politicas_exclusao_arquivos
    weight: 8
    confidence: 0.92
  - name: politicas_movimentacao_arquivos
    weight: 8
    confidence: 0.92
  - name: modo_plano_automacao
    weight: 7
    confidence: 0.9
  - name: lotes_alteracao
    weight: 7
    confidence: 0.88
  - name: registro_mudancas
    weight: 8
    confidence: 0.93
  - name: padronizacao_reversivel
    weight: 7
    confidence: 0.85
  - name: seguranca_dados_vault
    weight: 6
    confidence: 0.8
  - name: auditoria_automacao
    weight: 6
    confidence: 0.82
  cdu_primary: '004.7'
  cdu_secondary:
  - '004.5'
  - '004.8'
  cdu_description: Gestão de sistemas de computadores. Redes de computadores. Gerenciamento de arquivos e dados. Automação de processos.
---
# Regras para automações no Vault

1. Nunca deletar arquivos.
2. Nunca mover arquivos sem propor antes.
3. Sempre rodar em modo plano primeiro.
4. Toda alteração deve ser feita em pequenos lotes.
5. Sempre registrar mudanças em /_admin/vault-cleaning-log.md
6. Prefira padronização mínima e reversível.
''