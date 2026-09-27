---
description: Varredura profunda de tarefas (só se necessária)
---

**CV-ATUAL-002** · `/atualizar-abrangente` — varredura profunda somente quando necessária (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — confirmar que a sincronização mínima não basta antes de rodar a varredura profunda.
2. **Delegar:** usar a skill `productivity:update` com o argumento `--comprehensive` com `$ARGUMENTS`. Se o plugin `productivity@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
