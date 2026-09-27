---
description: Sintetizar pesquisa com usuários
argument-hint: "<tema ou material>"
---

**CV-PESQ-001** · `/pesquisa` — sintetizar pesquisa com usuários (entrevistas, questionários, feedback) em insights (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — cada insight aponta para a evidência que o sustenta; insight sem evidência vira GAP.
2. **Delegar:** usar a skill `product-management:synthesize-research` com `$ARGUMENTS`. Se o plugin `product-management@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. **Busca web:** obrigatória quando cruzar os achados com dado externo; citar a fonte.
4. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
