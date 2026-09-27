---
description: Sincronização mínima de tarefas e contexto
---

**CV-ATUAL-001** · `/atualizar` — sincronização mínima de tarefas e contexto (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — sincronizar só o necessário ao objeto atual e às suas entradas.
2. **Delegar:** usar a skill `productivity:update` com `$ARGUMENTS`. Se o plugin `productivity@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
