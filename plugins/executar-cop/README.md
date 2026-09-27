# executar-cop — Orquestrador CMD-COP do EXECUTAR

Plugin do Claude Code/Cowork que implementa o [HANDOFF-AGENTES-001](../../docs/architecture/HANDOFF-AGENTES-001.md), conforme o [ADR-0003](../../docs/ADR-0003-PLUGIN-EXECUTAR-COP.md).

O plugin oferece uma interface única, por slash ou por frase, que resolve um **ID verbal** (`CV-XXX-NNN`), roda o **pré-voo de dependências** e delega ao módulo certo. Toda resposta sai em português do Brasil. Toda saída visual segue o **token do calendário**.

```
CAMADA 1 — Orquestração e setup    orquestrador-cop · rotina (copiloto-executar, executar-mapa-os) · update/start/task-management/memory-management
CAMADA 2 — Skills técnicas         dominio-operacoes (9 skills de operações) · dominio-produto (roadmap-update, write-spec, synthesize-research)
CAMADA 3 — Cadeia proprietária     executar-dependency-architect → executar-arvore-roadmap → executar-mergulhe → obsidian-editorial-pipeline
```

## Componentes
| Tipo | Itens |
|---|---|
| Agentes | `orquestrador-cop` (entrada única), `dominio-operacoes`, `dominio-produto`, `cadeia-de-valor-proprietaria` |
| Skills proprietárias (4) | `executar-dependency-architect`, `executar-arvore-roadmap`, `executar-mergulhe` (Árvore Visual), `obsidian-editorial-pipeline` v2.2 |
| Skills proprietárias de apoio (3) | `executar-plan-mode` (`/plano`), `product-code-development` (`/produto-codigo`), `execution-toolkit` (`/execucao`) |
| Skills incorporadas da Anthropic (23, Apache-2.0) | operações: `capacity-plan`, `change-request`, `process-doc`, `runbook`, `status-report`, `vendor-review`, `risk-assessment`, `compliance-tracking`, `process-optimization` · produtividade: `update`, `start`, `task-management`, `memory-management` (+ `skills/dashboard.html`) · produto: `roadmap-update`, `write-spec`, `synthesize-research`, `competitive-brief`, `metrics-review`, `product-brainstorming`, `sprint-planning`, `stakeholder-update` · setup: `cowork-plugin-customizer`, `create-cowork-plugin`. Todas são `user-invocable: false`, e a interface do usuário são os commands CV. Ver `THIRD_PARTY_NOTICES.md` e `CONNECTORS.md` |
| Commands | 40 slashes, um por ID verbal. Todo componente tem ID, nada fica de fora (lista em `references/cmd-cop-index.md`) |
| Referências | `cmd-cop-index.md` (índice único), `nucleo-dependencias.md` (contrato transversal), `grafo-dependencias.schema.json` + `grafo-dependencias.json` |
| Assets | `design-tokens/calendario-light-mode.md` + PNG de referência |
| Validação | `scripts/validar_plugin.py`; testes em `skills/*/tests/` |

Não há `.mcp.json` nem hooks: nenhum ID verbal exige isso nesta versão.

## Instalação
```text
/plugin marketplace add executar-23/Copiloto-ops
/plugin install executar-cop@copiloto-ops
```
Para desenvolvimento local: `claude --plugin-dir plugins/executar-cop`.

### Skills incorporadas e dependências externas
Desde a emenda b do ADR-0003, as skills de `operations`, `productivity` e `product-management` estão **dentro** deste plugin: não é preciso instalar nada da Anthropic. Os conectores (`~~project tracker`, `~~chat` etc.) vêm da sua conta; ver `CONNECTORS.md`.

A rotina (`/bomdia`, `/agora`, `/estado`, `/fechardia`, `/replanejamento`, `/evidencia`, `/bloqueio`) usa a skill `copiloto-executar`. O `/mapa` usa `executar-mapa-os`. As duas são skills da conta claude.ai, com fonte fora deste repositório. Quando ausentes, esses comandos respondem `bloqueado-externo`, e o restante do plugin segue funcionando (núcleo §2.9).

## Uso
- **Rotina diária:** `/bomdia`, `/agora`, `/estado`, `/fechardia` e `/replanejamento`, ou os sinônimos "Bom dia, copiloto", "O que faço agora?", "Como estamos?", "Terminei por hoje" e "Preciso mudar o plano".
- **Cadeia proprietária:**
  - `/dependencias <planilha.xlsx>` gera o 16_REG, o mapa e a arquitetura de preenchimento;
  - `/arvore [txt|zip|obsidian|csv|kit]`;
  - `/arvore-visual`;
  - `/editorial`.
- **Operações e produto:** `/capacidade`, `/mudanca`, `/processo`, `/procedimento`, `/situacao`, `/fornecedor`, `/risco`, `/conformidade`, `/otimizar`, `/roadmap`, `/spec` e `/pesquisa`.

## Regras transversais
1. **Dependências** (`references/nucleo-dependencias.md`): todo command, skill e agente faz o pré-voo e fecha com `Dependências de entrada → Saída → Gate`. Tags DIRECT, DERIVED, PROPOSED, CONFLICT e GAP. Posição de pasta não é dependência.
2. **Token visual** (`assets/design-tokens/calendario-light-mode.md`): paleta suíça, com vermelho só para hoje, prioridade e atual.
3. **Busca web** obrigatória quando a análise tocar fato externo, benchmark ou dado desatualizável.
4. **Índice único:** todo ID novo entra em `cmd-cop-index.md` antes de virar componente. IDs existentes nunca são removidos; legados viram aliases.

## Manutenção
```bash
python3 plugins/executar-cop/scripts/validar_plugin.py
claude plugin validate plugins/executar-cop --strict
python3 plugins/executar-cop/skills/executar-dependency-architect/tests/test_scripts.py
python3 plugins/executar-cop/skills/obsidian-editorial-pipeline/tests/run_tests.py
```

## Lacunas conhecidas
- A primeira execução real do especialista (PF-24) está em `projects/EXECUTAR-HUB/control-plane/PF-24/`. Ela aguarda validação humana do domínio de valores do 16_REG, do mapeamento de Gates e da decisão sobre a A03.
- As skills da conta `copiloto-executar` e `executar-mapa-os` não têm fonte neste repositório.
