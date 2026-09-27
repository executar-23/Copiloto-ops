# executar-cop — Orquestrador CMD-COP do EXECUTAR

Plugin do Claude Code/Cowork que implementa o [HANDOFF-AGENTES-001](../../docs/architecture/HANDOFF-AGENTES-001.md), conforme o [ADR-0003](../../docs/ADR-0003-PLUGIN-EXECUTAR-COP.md).

O plugin oferece uma interface única, por slash ou por frase, que resolve um **ID verbal** (`CV-XXX-NNN`), roda o **pré-voo de dependências** e delega ao módulo certo. Toda resposta sai em português do Brasil. Toda saída visual segue o **token do calendário**.

```
CAMADA 1 — Orquestração e setup    orquestrador-cop · rotina (copiloto-executar, executar-mapa-os) · productivity
CAMADA 2 — Skills técnicas         dominio-operacoes (operations) · dominio-produto (product-management)
CAMADA 3 — Cadeia proprietária     executar-dependency-architect → executar-arvore-roadmap → executar-mergulhe → obsidian-editorial-pipeline
```

## Componentes
| Tipo | Itens |
|---|---|
| Agentes | `orquestrador-cop` (entrada única), `dominio-operacoes`, `dominio-produto`, `cadeia-de-valor-proprietaria` |
| Skills | `executar-dependency-architect`, `executar-arvore-roadmap`, `executar-mergulhe` (Árvore Visual), `obsidian-editorial-pipeline` v2.2 |
| Commands | 28 slashes, um por ID verbal (lista em `references/cmd-cop-index.md`) |
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

### Pré-requisitos das Camadas 1 e 2 (dependências externas)
Os comandos de produtividade, operações e produto delegam a plugins da Anthropic:
```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins
/plugin install operations@knowledge-work-plugins
/plugin install product-management@knowledge-work-plugins
```
Eles **não** estão em `dependencies` do `plugin.json`, por uma razão prática. Uma dependência declarada ali que não se resolve impede o plugin inteiro de carregar, o que derrubaria também a cadeia proprietária. Por isso, quando um desses plugins está ausente, o comando correspondente responde `bloqueado-externo`, e os demais seguem funcionando (núcleo §2.9).

A rotina (`/bomdia`, `/agora`, `/estado`, `/fechardia`, `/replanejamento`, `/evidencia`, `/bloqueio`) usa a skill `copiloto-executar`. O `/mapa` usa `executar-mapa-os`. As duas são skills da conta claude.ai, com fonte fora deste repositório. Opcional: `cowork-plugin-management@knowledge-work-plugins`, para customizar conectores, sem ID verbal.

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
- A planilha `EXECUTAR_HUB_Control_Plane_v2.xlsx` real não foi recebida. O especialista foi testado com uma fixture **fictícia** (`skills/executar-dependency-architect/tests/fixtures/`).
- A definição do PF-24 (reconciliação cruzada) não foi fornecida.
- As skills da conta `copiloto-executar` e `executar-mapa-os` não têm fonte neste repositório.
