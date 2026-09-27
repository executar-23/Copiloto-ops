---
description: Recuperar o contexto do objeto atual
argument-hint: "[objeto]"
---

**CV-CONTEXTO-001** · `/contexto` — recuperar contexto necessário ao objeto atual (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — trazer só o contexto de que o objeto atual depende.
2. **Delegar:** usar a skill `productivity:memory-management` com `$ARGUMENTS`. Se o plugin `productivity@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
