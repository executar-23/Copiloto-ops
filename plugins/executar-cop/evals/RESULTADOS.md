# Resultados de `claude plugin eval` — 2026-09-27

Comando: `claude plugin eval plugins/executar-cop --runs 1 -j 4 --trust-plugin --no-publish` (Claude Code 2.1.283).
A ablação `with-without` também roda cada caso sem o plugin. Juiz LLM com 3 votos. Custo total: US$ 0,86. Duração: 117 s.

| Caso | Com plugin | Sem plugin | O que diferencia |
|---|---|---|---|
| `rotina-sinonimo-bomdia` | PASS (3/3 votos) | FAIL | Com plugin, resolve CV-BOMDIA-001 e declara bloqueado-externo porque `copiloto-executar` está ausente, sem inventar o dia. Sem plugin, responde só "Bom dia! Como posso ajudar?". |
| `operacoes-capacidade-sem-plugin` | PASS (3/3) | FAIL | Com plugin, faz o pré-voo, nomeia `operations@knowledge-work-plugins` ausente e mostra como instalar, sem números inventados. |
| `ambiguidade-mapa` | PASS (3/3) | FAIL | Com plugin, faz uma pergunta mínima entre /mapa (Mapa-OS) e a parte 2 de /dependencias. |
| `cadeia-bloqueio-interno` | PASS (3/3) | FAIL | Com plugin, identifica DEP-COP-001: /arvore fica bloqueado-interno até /dependencias. |

**Resultado:** 4/4 com o plugin e 0/4 sem ele.

O ambiente de avaliação não tem os plugins Anthropic nem as skills da conta. Por isso estes casos exercitam o roteamento, o pré-voo e o bloqueio externo, e não a execução dessas skills.

A avaliação da skill `executar-dependency-architect` pela skill-creator está em `../skills/executar-dependency-architect/evals/benchmark-iteracao-1.md`.
