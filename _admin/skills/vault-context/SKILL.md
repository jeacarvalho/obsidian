---
name: vault-context
description: Contexto do vault Obsidian do usuário. Contém estrutura de pastas, padrões, plugins instalados e observações importantes. Use no início de cada sessão para entender o ambiente de trabalho antes de做任何事情.
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:38:55.665162+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: interacao_com_vault_obsidian
    weight: 10
    confidence: 0.98
  - name: gerenciamento_de_notas_obsidian
    weight: 9
    confidence: 0.97
  - name: criacao_de_notas_obsidian
    weight: 8
    confidence: 0.96
  - name: busca_em_vault_obsidian
    weight: 8
    confidence: 0.95
  - name: gerenciamento_de_tarefas_obsidian
    weight: 7
    confidence: 0.94
  - name: desenvolvimento_de_plugins_obsidian
    weight: 9
    confidence: 0.93
  - name: desenvolvimento_de_temas_obsidian
    weight: 8
    confidence: 0.92
  - name: execucao_de_javascript_em_obsidian
    weight: 7
    confidence: 0.91
  - name: depuracao_de_plugins_obsidian
    weight: 8
    confidence: 0.9
  - name: automacao_de_comandos_obsidian
    weight: 10
    confidence: 0.99
  cdu_primary: '004.4'
  cdu_secondary:
  - '004.77'
  - '004.8'
  - '004.9'
  cdu_description: Sistemas de computadores; Organização de computadores; Programação; Desenvolvimento de software; Aplicações de software; Ferramentas de linha de comando; Automação; Gerenciamento de notas digitais; Plugins e extensões.
---

# Contexto do Vault Obsidian

Este arquivo fornece contexto sobre o vault Obsidian do usuário para orientar o trabalho.

## Arquivo de Referência

Para contexto completo, leia: `../vault_resumo.md`

## Informações Essenciais

### Estrutura Principal
- **~3.500 notas** em pastas numeradas (10-150)
- Maior pasta: `20 TEOLOGIA` (1.250 notas)
- Segunda maior: `110 TRABALHO` (722 notas)
- Terceira: `50 VIDA SAUDAVEL` (465 notas)

### Pastas Principais
- `20 TEOLOGIA` - Vida cristã, bíblia, ministério
- `110 TRABALHO E GESTAO` - Gestão, SERPRO, projetos
- `50 VIDA SAUDAVEL` - Saúde, alimentação low-carb
- `90 FAMILIA` - Vida familiar
- `100 ARQUIVOS E REFERENCIAS` - Bibliografia
- `40 COMO CONHECEMOS` - Aprendizagem
- `10 TI` - Tecnologia

### Plugins Principais
- AI: copilot, smart-connections, text-generator
- Produtividade: tasks, dataview, calendar, quickadd
- Visual: excalidraw, mind-map
- Busca: omnisearch, find-unlinked-files

### Padrões do Vault
- Poucas notas usam frontmatter YAML (~107 de ~3.500)
- Tags na maioria vazias
- Template diário em `templates/Template diário.md`
- Versionamento git ativo

### Arquivos Importantes
- Resumo: `_admin/vault_resumo.md`
- Templates: `templates/`
- Processar: `_processar/` (55 notas para triagem)

## Como Usar

1. No início de cada sessão, ler `vault_resumo.md` para contexto
2. Antes de criar notas, verificar padrões existentes na pasta
3. Usar skills obsidian-markdown para formatação correta
4. Considerar uso de defuddle para limpar artigos antes de salvar

## Workflow Recomendado

1. **Nova sessão**: Ler `_admin/vault_resumo.md`
2. **Criar nota**: Usar template adequado ou seguir padrões da pasta
3. **Salvar artigo web**: Usar defuddle antes de salvar em `_processar/`
4. **Editar**: Usar obsidian-markdown para formatação OFM
