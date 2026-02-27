# Skills Instaladas

## Repositório Original
https://github.com/kepano/obsidian-skills

## Skills Disponíveis

| Skill | Descrição |
|-------|-----------|
| `obsidian-markdown/` | OFM: wikilinks, callouts, embeds, properties |
| `obsidian-bases/` | Bases (.base) com views, filtros, fórmulas |
| `json-canvas/` | Canvas (.canvas) com nós e conexões |
| `obsidian-cli/` | CLI para interacting com Obsidian |
| `defuddle/` | Extrair markdown limpo de páginas web |
| `vault-context/` | Contexto do seu vault Obsidian |

## Instalação

### defuddle (obrigatório para usar a skill)
```bash
npm install -g defuddle-cli
```

### Para ativar no opencode
Use: `/skill <nome-da-skill>` ou peça para ativar a skill desejada.

## Uso Recomendado

1. **Nova sessão**: Ativar `vault-context` primeiro
2. **Criar/editar notas**: Ativar `obsidian-markdown`
3. **Salvar artigos web**: Usar `defuddle` para limpar conteúdo
4. **Trabalhar com bases**: Ativar `obsidian-bases`
5. **Canvas**: Ativar `json-canvas`
