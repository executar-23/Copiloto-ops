---
description: Planejar ou validar capacidade
argument-hint: "<equipe ou escopo>"
---

**CV-CAP-001** · `/capacidade` — planejar ou validar capacidade (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — listar as entregas que consomem a capacidade e as dependências entre elas; um gargalo bloqueante vira bloqueio.
2. **Delegar:** usar a skill `operations:capacity-plan` com `$ARGUMENTS`. Se o plugin `operations@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. **Busca web:** obrigatória quando a análise usar benchmark de utilização ou produtividade; citar a fonte.
4. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
