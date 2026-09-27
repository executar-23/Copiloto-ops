---
description: Documentar processo (fluxo, RACI, SOP)
argument-hint: "<processo>"
---

**CV-PROC-001** · `/processo` — documentar processo (índice: `${CLAUDE_PLUGIN_ROOT}/references/cmd-cop-index.md`).

1. **Pré-voo de dependências:** aplicar `${CLAUDE_PLUGIN_ROOT}/references/nucleo-dependencias.md` antes de agir — explicitar entradas e saídas de cada etapa; as dependências entre etapas levam tag epistêmica.
2. **Delegar:** usar a skill `operations:process-doc` com `$ARGUMENTS`. Se o plugin `operations@knowledge-work-plugins` não estiver instalado, responder `bloqueado-externo` com a instalação necessária (ver README do plugin), sem simular o resultado.
3. **Busca web:** obrigatória quando o processo seguir norma ou prática de referência externa; citar a fonte.
4. Produzir uma ação principal, não um relatório geral. Se houver ambiguidade material entre dois objetos, pedir a decisão mínima. Responder em pt-BR e fechar com `Dependências de entrada → Saída → Gate`.
