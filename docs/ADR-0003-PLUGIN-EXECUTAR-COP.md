# ADR-0003 — Plugin `executar-cop`: orquestrador, índice CMD-COP e dependências transversais

**Status:** Aceito por decisão explícita do usuário em 2026-09-27  
**Data:** 2026-09-27  
**Escopo:** `plugins/executar-cop/`, `.claude-plugin/marketplace.json`, regra 8 do `AGENTS.md`  
**Fonte:** [HANDOFF-AGENTES-001](architecture/HANDOFF-AGENTES-001.md) (sha256 `69911423ddcdfbcd3ff14cda82936a9d4e6f1d96284129abc1716876b9a2c9d7`); pacote `EXECUTAR-OPERACOES._.zip` (sha256 `ddc571ee5660b5761f5b5682e517db937e1a95b8952a4c1c0f799d055ec77e92`); prompt mestre `EXECUTAR-DEPENDENCY-ARCHITECT-001`  
**Rastreio:** [Issue #24](https://github.com/executar-23/Copiloto-ops/issues/24) · Notion [04 — Tasks](https://app.notion.com/p/3e7d1d673fb381bd8f88e5c38979d403) (FASE 2, "Definir agentes e skills")

## Contexto

O HANDOFF-AGENTES-001 propõe uma arquitetura em três camadas (Orquestração → Skills técnicas → Skills proprietárias) com um Orquestrador fino. Cada capacidade teria um ID verbal `CV-XXX-NNN`, um slash determinístico e sinônimos. As dependências seriam declaradas explicitamente, e toda saída visual seguiria o token do calendário.

O handoff previa o registro epistêmico de dependências apenas na skill `executar-dependency-architect`, "sem obrigação de retrofit" das demais.

## Decisões

1. **Local.** O plugin vive em `plugins/executar-cop/` deste repositório, com marketplace `copiloto-ops` em `.claude-plugin/marketplace.json`. As fontes das skills proprietárias são versionadas aqui integralmente.
2. **Regra 8 do AGENTS.md.** A regra que proibia "conteúdo privado neste repositório público" estava desatualizada. Passa a proibir apenas segredos, credenciais, tokens e dados pessoais de terceiros, e permite versionar skills, agentes e documentação proprietária do EXECUTAR.
3. **Dependências como capacidade transversal.** Esta decisão substitui o §6.2 do handoff. O núcleo portátil do prompt mestre fica em `plugins/executar-cop/references/nucleo-dependencias.md` e reúne: o modelo epistêmico DIRECT/DERIVED/PROPOSED/CONFLICT/GAP, o princípio de agrupamento, as regras, os critérios de fase e de saída e os bloqueios interno e externo.

   Esse núcleo é **obrigatório em toda skill, command e agente**. Cada um executa um pré-voo de dependências antes de agir e declara `Dependências de entrada → Saída → Gate`. O especialista `executar-dependency-architect` mantém o que é específico da planilha `EXECUTAR_HUB_Control_Plane_v2.xlsx`. As skills continuam módulos independentes e compartilham apenas o núcleo e o grafo.
4. **Grafo.** A dependência só existe quando está declarada em `references/grafo-dependencias.json`, validado por `grafo-dependencias.schema.json`. As arestas usam o schema exato de `16_REG_Dependencias`, com `status_epistemico` obrigatório. A posição no diretório não implica dependência.
5. **Token visual.** O token do calendário (`assets/design-tokens/calendario-light-mode.md`) é a fonte única de paleta. A paleta DESK-OS (laranja) do `obsidian-editorial-pipeline` e a paleta laranja/verde/amarelo da Árvore Visual são migradas para ele nesta entrega.
6. **Commits.** O trabalho é feito diretamente em `main`, pela regra 9, sem branch nem PR.

## Alternativas consideradas

- **Agente monolítico** (opção A do handoff): descartada porque viola o progressive disclosure e o isolamento por cliente.
- **Um agente por skill, sem orquestrador** (opção C): descartada porque obriga o usuário a saber qual módulo chamar.
- **Estender `copiloto-operacional` em `Sas-Executar/executar-Blog`**: descartada porque este repositório é o único GitHub operacional e aquele repositório está fora do escopo.
- **Manter a paleta própria de cada skill**: descartada pelo usuário.

## Consequências

- O Orquestrador resolve slash, sinônimo ou alias legado → ID → pré-voo → delegação. Um bloqueio bloqueante não satisfeito impede a delegação.
- `scripts/validar_plugin.py` e `claude plugin validate --strict` passam a ser a verificação mínima antes de qualquer commit no plugin.
- Plugins Anthropic (`operations`, `productivity`, `product-management`) e skills da conta (`copiloto-executar`, `executar-mapa-os`) são dependências externas. Quando estão ausentes, o comando responde com bloqueado-externo, sem simular a execução.
- A validação do especialista com dados reais depende do envio da planilha (GAP).
- Não há `.mcp.json` nem hooks nesta etapa, porque nenhum ID verbal os exige.

## Emenda b — 2026-09-27: plugins da Anthropic incorporados
**Decisão do usuário:** `operations`, `productivity` e `product-management` passam a ficar **dentro** do `executar-cop`, e não como dependências externas.

- **Incorporadas:** só as skills mapeadas a IDs verbais, mais as dependências documentadas delas:
  - 9 de operações;
  - `update` e `memory-management`, além de `start` e `task-management`, que são exigidas por `update` (DEP-COP-004 e 005, DIRECT);
  - 3 de produto.
  - O resto (outras skills de PM, o comando `brainstorm` e os `.mcp.json`) fica fora, por não ter ID verbal.
- **Licença:** Apache-2.0, com `LICENSE-APACHE-2.0` e `THIRD_PARTY_NOTICES.md`. Cada arquivo modificado traz um aviso próprio.
- **Modificações:**
  - seção "Integração executar-cop" e `user-invocable: false` nos `SKILL.md`;
  - dashboard migrado para o token do calendário;
  - `CONNECTORS.md` unificado.
- **Consequência:** a consequência anterior sobre "plugins Anthropic como dependências externas" fica **substituída**. Continuam externas apenas as skills da conta `copiloto-executar` e `executar-mapa-os`.
- **Grafo:** os nós agregados OPERATIONS, PRODUCTIVITY e PRODUCT-MANAGEMENT foram substituídos por um nó por skill.
