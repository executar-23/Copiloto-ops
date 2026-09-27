---
description: Situação operacional compacta
argument-hint: "[escopo]"
---

**CV-SIT-001** · `/situacao` — emitir situação operacional compacta (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — relatar os bloqueios por Gate e a próxima dependência a destravar.
2. **Delegar:** usar a skill `operations:status-report` com `$ARGUMENTS`. Se o plugin `operations@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. **Busca web:** obrigatória quando comparar com benchmark externo; citar a fonte.
4. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
