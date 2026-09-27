---
description: Estruturar mudança de escopo, processo ou sistema
argument-hint: "<mudança>"
---

**CV-MUD-001** · `/mudanca` — estruturar mudança que afete escopo, processo ou sistema (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — mapear o impacto a jusante no grafo (o que a mudança desbloqueia ou bloqueia) e os Gates afetados.
2. **Delegar:** usar a skill `operations:change-request` com `$ARGUMENTS`. Se o plugin `operations@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. **Busca web:** obrigatória quando a mudança envolver referência externa (norma, fornecedor, plataforma); citar a fonte.
4. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
