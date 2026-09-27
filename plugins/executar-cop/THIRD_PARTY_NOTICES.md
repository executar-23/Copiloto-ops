# Avisos de terceiros

## Anthropic — knowledge-work-plugins (Apache License 2.0)
Parte das skills deste plugin vem dos plugins `operations` 1.3.0, `productivity` 1.3.1 e `product-management` 1.2.0 do repositório `anthropics/knowledge-work-plugins`. Copyright Anthropic.

Esse material é licenciado sob a Apache License, Version 2.0, cujo texto integral está em [`LICENSE-APACHE-2.0`](LICENSE-APACHE-2.0). As skills foram incorporadas ao `executar-cop` por decisão do usuário em 2026-09-27; ver [ADR-0003](../../docs/ADR-0003-PLUGIN-EXECUTAR-COP.md), emenda b.

| Origem | Skills incorporadas |
|---|---|
| operations | `capacity-plan`, `change-request`, `process-doc`, `runbook`, `status-report`, `vendor-review`, `risk-assessment`, `compliance-tracking`, `process-optimization` |
| productivity | `update`, `start`, `task-management`, `memory-management`, `skills/dashboard.html` |
| product-management | `roadmap-update`, `write-spec`, `synthesize-research` |

**Modificações** (Apache-2.0, §4b; cada arquivo modificado traz aviso próprio):
1. Em cada `SKILL.md` acima, foi acrescentada ao final a seção "Integração executar-cop" (ID verbal, pré-voo de dependências, busca web, idioma e proteção do `CLAUDE.md`). Também foi acrescentado `user-invocable: false` ao frontmatter quando ausente, para que a interface do usuário continue sendo a dos comandos CV. O corpo original não foi alterado.
2. Em `skills/dashboard.html`, a paleta e a tipografia foram migradas para o token do calendário (`assets/design-tokens/calendario-light-mode.md`).
3. O `CONNECTORS.md` na raiz deste plugin une os três `CONNECTORS.md` originais.

Não foram incorporados: os `.mcp.json`, o comando `product-management/commands/brainstorm.md` e as skills `stakeholder-update`, `product-brainstorming`, `sprint-planning`, `competitive-brief` e `metrics-review`. Nenhum deles tem ID verbal no índice CMD-COP.
