# HANDOFF-AGENTES-001 — Arquitetura e Comando de Produção para o Ecossistema de Agentes EXECUTAR

**Status:** Proposto
**Data:** 2026-09-27
**Deciders:** Você (dono do plugin) + Claude Code (executor da produção)
**Skills aplicadas nesta análise:** `engineering:system-design`, `engineering:architecture`, `executar-prompt` (para compilar o comando final), `skill-creator` (workflow de produção referenciado no comando final)

---

## 1. Contexto — o que foi lido no pacote anexado

Antes de desenhar qualquer coisa, o conteúdo de `EXECUTAR-OPERACOES__.zip` foi inventariado:

| Artefato | Papel no sistema |
|---|---|
| `CMD-COP-001 — Índice de Slash Commands e IDs Verbais.docx` | Schema normativo de comandos: cada ação tem um **ID verbal estável** (`CV-XXX-NNN`), um **slash determinístico** (`/comando`) e **sinônimos em linguagem natural**. Regra explícita: *"o usuário não precisa informar o módulo"* — quem resolve o ID é o Orquestrador. |
| `calendario-light-mode-preview.png` | **Design token canônico** de qualquer saída visual: paleta suíça (branco/preto/vermelho), tipografia densa, divisores finos, vermelho reservado para "hoje/prioridade/urgente", grade de calendário mobile-first. |
| `executar-arvore-roadmap/references/schema.md` + `EXECUTAR-ARVORE-VISUAL-v1.0/docs/02-HANDOFF-TECNICO.md` + `.../portas-e-dependencias.md` | **Contrato de dependência** entre unidades executáveis: `depende_de[]`, `porta`, `desbloqueia[]`, estados (`aberta/concluida/bloqueada/marco`), e a distinção crítica `bloqueado-interno` vs `bloqueado-externo`. Regra de ouro: *"a hierarquia visual e o grafo de dependências não são a mesma coisa"* — nunca inferir dependência pela posição na árvore. |
| `cowork-plugin-management/skills/create-cowork-plugin/references/component-schemas.md` | Schema oficial de componentes de plugin Claude Code/Cowork: `skills/*/SKILL.md` (frontmatter `name`+`description` com frases-gatilho), `agents/*.md` (frontmatter `name`+`description`+`model`+`color`+`tools`), `commands/*.md` (legado, mas é exatamente o mecanismo de **slash determinístico** que o CMD-COP-001 exige), `hooks/hooks.json`, `.mcp.json`, `.claude-plugin/plugin.json`. |
| `productivity/`, `operations/`, `product-management/`, `cowork-plugin-management/` (plugins Anthropic) | Camada técnica genérica disponível (produtividade, operações, gestão de produto, gestão de plugins). |
| `executar-arvore-roadmap/`, `EXECUTAR-ARVORE-VISUAL-v1.0/`, `obsidian-editorial-pipeline-v2.2.skill` | **Suas três skills proprietárias** — a cadeia de valor real do negócio. |
| Prompt Mestre `EXECUTAR-DEPENDENCY-ARCHITECT-001` (fornecido depois, fora do zip) | **Quarta skill proprietária**, upstream das demais: reconstrói a rede de dependências do `EXECUTAR_HUB_Control_Plane_v2.xlsx` (registros 10 a 24, incluindo `16_REG_Dependencias` e `17_REG_Gates`) e produz a "Arquitetura de Preenchimento" (Fases → contexto único → entregáveis → Gate) que alimenta o `estrutura.json` da `executar-arvore-roadmap`. |

Essa leitura é a base factual de todo o desenho abaixo — nada foi assumido sem checar o arquivo correspondente.

---

## 2. Decisão arquitetural (ADR)

### Contexto
Você opera um plugin próprio no claude.ai/Claude Code que precisa: (a) ser acionável por comando determinístico **e** por linguagem natural, (b) sempre respeitar um padrão visual único quando produz saída gráfica, (c) orquestrar skills genéricas (produtividade, operações, gestão de produto) e skills proprietárias (árvore-roadmap, árvore-visual, pipeline editorial Obsidian) como **uma cadeia única de valor**, com dependências explícitas, e (d) ser reaplicável a projetos de clientes.

### Decisão
Adotar uma arquitetura em **três camadas** dentro de um único plugin (ou de um conjunto de plugins que o Orquestrador enxerga como um só sistema):

```
CAMADA 1 — ORQUESTRAÇÃO E SETUP
    Productivity + Cowork Plugin Management
    (roteamento de intenção, memória operacional, setup do ambiente)
        ↓
CAMADA 2 — SKILLS TÉCNICAS GENÉRICAS
    Operations + Product Management
    (capacidade, risco, mudança, processo, roadmap, spec, pesquisa)
        ↓
CAMADA 3 — SKILLS PROPRIETÁRIAS (cadeia de valor)
    executar-dependency-architect → executar-arvore-roadmap → executar-arvore-visual
    → obsidian-editorial-pipeline
    (arquitetura de dependências → planejamento canônico → visualização → publicação editorial)
```

### Opções consideradas

**Opção A — Um agente monolítico que sabe tudo.**
| Dimensão | Avaliação |
|---|---|
| Complexidade | Baixa para construir, alta para manter |
| Custo de contexto | Alto — carrega tudo sempre |
| Escalabilidade para clientes | Ruim — não isola dados/skills por cliente |
| Familiaridade da equipe | Alta |

Prós: simples de começar. Contras: viola progressive disclosure, quebra a regra de dependência (tudo vira "achatado"), não separa Orquestrador de execução, não escala para múltiplos clientes.

**Opção B — Orquestrador fino + agentes especialistas por camada (adotada).**
| Dimensão | Avaliação |
|---|---|
| Complexidade | Média — exige registro de IDs e grafo de dependência |
| Custo de contexto | Baixo — progressive disclosure nativo do formato Skill |
| Escalabilidade para clientes | Alta — cada cliente é um "projeto" com seu próprio `estrutura.json`/grafo |
| Familiaridade da equipe | Você já opera nesse padrão (CMD-COP-001, copiloto-executar) |

Prós: reaproveita exatamente o padrão que você já validou (`/bomdia`, `/agora`, `/estado`...); mapeia 1:1 com o schema de dependências já existente; cada skill proprietária continua independente e testável. Contras: exige um passo extra de "registro" (índice de IDs) sempre que uma skill nova entra.

**Opção C — Um agente por skill, sem orquestrador central.**
| Dimensão | Avaliação |
|---|---|
| Complexidade | Baixa por agente, alta na integração |
| Custo de contexto | Médio |
| Escalabilidade | Baixa — usuário precisa saber qual agente chamar |

Contras: quebra a regra explícita do CMD-COP-001 ("o usuário não precisa informar o módulo").

### Trade-off central
A Opção B custa um passo de governança (manter o índice `CMD-COP` e o grafo de dependências sincronizados) em troca de manter a promessa central do produto: **uma única interface conversacional/comando resolve o módulo certo**, sem o usuário precisar saber a arquitetura interna. Esse é exatamente o objetivo que você descreveu.

### Consequência
Todo agente/skill/command produzido por este handoff deve:
1. Ter um ID verbal `CV-XXX-NNN` registrado num índice único (extensão do `CMD-COP-001`).
2. Ter, quando fizer sentido, um slash determinístico (`commands/*.md`) e/ou uma `SKILL.md` com sinônimos na `description`.
3. Declarar suas dependências (`depende_de`, `porta`, `bloqueado-interno`/`bloqueado-externo`) no manifesto do plugin.
4. Aplicar o token visual do calendário sempre que produzir qualquer saída visual.
5. Responder sempre em português do Brasil.
6. Usar busca web para enriquecer qualquer análise antes de fechar o resultado.

---

## 3. System Design da Camada de Orquestração

### 3.1 Requisitos

**Funcionais**
- Resolver um comando de barra OU uma frase equivalente para o mesmo ID verbal.
- Carregar **somente** o módulo necessário (progressive disclosure — nunca a árvore inteira).
- Manter um grafo de dependência entre unidades de trabalho, com portas e bloqueios internos/externos.
- Produzir saída visual sempre no token suíço (calendário) quando o pedido for visual.
- Ser replicável por cliente: cada projeto de cliente é uma instância isolada do mesmo padrão (mesmos IDs, dados diferentes).
- Enriquecer toda análise com pesquisa web quando a skill tocar em fatos externos, benchmarks ou referências.

**Não funcionais**
- Baixo custo de contexto (progressive disclosure obrigatório — `SKILL.md` enxuto, detalhe em `references/`).
- Latência de decisão de roteamento mínima (resolução de ID antes de qualquer execução pesada).
- Auditabilidade: toda ação relevante deve deixar rastro de evidência (herdado do padrão `plano-operacional-rastreavel`/`copiloto-executar` já em uso).
- Multi-tenant "leve": nenhuma skill deve hardcodar dados de um cliente específico.

**Restrições**
- Formato de plugin Claude Code/Cowork (`.claude-plugin/plugin.json`, `skills/`, `agents/`, `commands/`, `hooks/`, `.mcp.json`).
- Idioma único de saída: português do Brasil.
- Reaproveitar, não recriar, as três skills proprietárias já existentes.

### 3.2 Desenho de alto nível

```
                         ENTRADA DO USUÁRIO
                (slash "/comando" OU frase natural)
                                │
                                ▼
                 ┌───────────────────────────┐
                 │   ORQUESTRADOR (agent)      │
                 │   - resolve ID verbal        │
                 │   - consulta índice CMD-COP   │
                 │   - decide camada/skill alvo   │
                 └──────────────┬────────────────┘
                                │
             ┌──────────────────┼───────────────────┐
             ▼                  ▼                    ▼
   CAMADA 1 (setup)   CAMADA 2 (skills técnicas)  CAMADA 3 (cadeia de valor)
   productivity/           operations/          executar-dependency-architect
   cowork-plugin-mgmt      product-management     → executar-arvore-roadmap
                                                    → executar-arvore-visual
                                                    → obsidian-editorial-pipeline
             │                  │                    │
             └──────────────────┴────────────────────┘
                                │
                                ▼
                    CONTRATO DE DEPENDÊNCIA
           (depende_de / porta / bloqueado-interno|externo)
                                │
                                ▼
                    SAÍDA (texto PT-BR + visual no token suíço
                       quando aplicável) + evidência registrada
```

### 3.3 Componentes

- **Orquestrador** (`agents/orquestrador-cop.md`): único ponto de entrada. Não executa trabalho de domínio — resolve intenção → ID → skill/command → delega.
- **Índice `CMD-COP`** (`references/cmd-cop-index.md` no plugin raiz): fonte única de verdade dos IDs verbais, sinônimos, slash e módulo de destino. Extensão direta do `CMD-COP-001` anexado, agora cobrindo também os comandos de Camada 2 e 3.
- **Registro de dependências** (`references/grafo-dependencias.schema.json`): mesmo schema já validado em `executar-arvore-roadmap/references/schema.md`, reaproveitado como contrato entre TODAS as skills do plugin (não só a de roadmap).
- **Módulo de tokens visuais** (`assets/design-tokens/calendario-light-mode.md` + a própria imagem de referência): toda skill que produzir HTML/SVG/imagem consulta este módulo antes de renderizar.

### 3.4 Fluxo de dados

```
usuário → Orquestrador → índice CMD-COP (lookup) → skill/agent alvo
   → [skill consulta grafo de dependências antes de agir]
   → [se saída for visual → aplica design token]
   → [se skill precisar de fato externo/benchmark → web search obrigatório]
   → resposta em PT-BR + evidência registrada
```

### 3.5 Escala e confiabilidade
- **Carga esperada**: uso individual/pequena equipe por cliente — não requer fila/cache distribuído; a "escala" real é o número de clientes/projetos, resolvido por isolamento de dados (cada projeto tem seu próprio `estrutura.json`), não por infraestrutura.
- **Falha controlada**: um bloqueio `bloqueado-externo` (ex.: aprovação de terceiro) nunca deve travar os ramos independentes — regra já definida em `portas-e-dependencias.md` e que este handoff eleva a regra geral do sistema, não só da árvore.
- **Auditoria/monitoramento**: cada execução relevante gera evidência (arquivo, link, ou registro), seguindo o padrão que você já usa em `plano-operacional-rastreavel` e `copiloto-executar`.

### 3.6 O que revisitar quando o sistema crescer
- Se o número de clientes crescer muito, considerar mover o índice `CMD-COP` e o grafo de dependências para um backend externo consultável via MCP, em vez de arquivo estático no plugin.
- Se agentes de Camada 3 começarem a rodar em paralelo (ex.: árvore-visual e pipeline editorial simultâneos para o mesmo projeto), revisitar se `WIP=1` (já usado no `copiloto-executar`) ainda é adequado ou se precisa virar `WIP` por fluxo de valor.

---

## 4. Regra de camada verbal + determinística (extensão do CMD-COP-001)

Cada capacidade nova produzida pelos agentes deve nascer com **três faces simultâneas**, aplicadas transversalmente a todo o diretório do plugin — não apenas nos comandos de rotina do arquivo original:

1. **ID verbal estável**: `CV-<DOMINIO>-<NNN>` (ex.: `CV-ARVORE-001`, `CV-EDITORIAL-004`), registrado no índice único.
2. **Slash determinístico**: um `commands/*.md` (formato `$ARGUMENTS`/`$1`, `@arquivo`, bash inline) OU, quando a capacidade for mais rica que um comando único, uma `skills/*/SKILL.md` cuja `description` contém as frases-gatilho equivalentes (isso substitui o `commands/` legado sem perder o determinismo, pois o Cowork/Claude Code trata as duas formas como a mesma camada de "Skills").
3. **Sinônimos verbais**: pelo menos 2–3 frases naturais mapeadas ao mesmo ID, no padrão já usado ("Bom dia, copiloto" = `/bomdia`).

Regras herdadas do documento original e que continuam valendo para **todo** o plugin, não só para os comandos de rotina:
- Um comando produz uma ação principal, não um relatório genérico.
- O usuário não precisa informar o módulo nem repetir IDs conhecidos quando o contexto for inequívoco.
- Ambiguidade material entre dois objetos → o Orquestrador pergunta a decisão mínima necessária.
- Comandos/IDs legados viram aliases — nunca quebram compatibilidade.
- Toda resposta visível em português do Brasil.

---

## 5. Regra de token visual (obrigatória em toda saída visual)

Toda skill/agente que produzir qualquer artefato visual (HTML, SVG, mockup, dashboard, calendário, board) deve seguir o token demonstrado em `calendario-light-mode-preview.png`:
- Paleta: branco/cinza-claro de fundo, preto para texto e ícones, **vermelho reservado exclusivamente** para "hoje", prioridade alta ou item em destaque.
- Tipografia densa, sem serifa, hierarquia por peso e tamanho — não por cor.
- Divisores finos (1px), espaçamento generoso, cantos levemente arredondados nos blocos de evento.
- Layout mobile-first mas responsivo (o mesmo par light/SVG·HTML mostrado na referência).
- Toda skill de saída visual deve referenciar este arquivo como fonte de verdade, nunca reinventar paleta.

---

## 6. Contrato de dependência entre as skills próprias (cadeia única de valor)

Reaproveitando literalmente o schema já validado (`depende_de`, `porta`, `desbloqueia`, estados `aberta/concluida/bloqueada/marco`, distinção `bloqueado-interno`/`bloqueado-externo`), a cadeia de valor proprietária ganha um quarto nó, **upstream** dos outros três: o **Arquiteto de Dependências** (`EXECUTAR-DEPENDENCY-ARCHITECT-001`). Ele não preenche planilha nem desenha árvore — reconstrói a lógica de dependência (campo → artefato → domínio → macroárea → Gate) do `EXECUTAR_HUB_Control_Plane_v2.xlsx` e entrega o conteúdo formal de `16_REG_Dependencias`, que passa a ser a **fonte de entrada** do `estrutura.json` consumido por `executar-arvore-roadmap` — fechando exatamente o caso já previsto em `schema.md`: *"quando o documento de entrada é uma planilha [...] mapeie colunas/campos para o schema antes de gerar `estrutura.json`"*.

```json
{
  "fluxo_de_valor": "PEM-PIPELINE-PROPRIETARIO",
  "nos": [
    {"id": "DEPENDENCY-ARCHITECT", "titulo": "Reconstrução formal da rede de dependências (16_REG_Dependencias + Arquitetura de Preenchimento)", "depende_de": [], "desbloqueia": ["ARVORE-ROADMAP"]},
    {"id": "ARVORE-ROADMAP", "titulo": "Planejamento canônico (estrutura.json)", "depende_de": ["DEPENDENCY-ARCHITECT"], "desbloqueia": ["ARVORE-VISUAL"]},
    {"id": "ARVORE-VISUAL", "titulo": "Visualização navegável (árvore/grafo)", "depende_de": ["ARVORE-ROADMAP"], "desbloqueia": ["EDITORIAL-OBSIDIAN"]},
    {"id": "EDITORIAL-OBSIDIAN", "titulo": "Publicação editorial (pipeline Obsidian)", "depende_de": ["ARVORE-VISUAL"], "desbloqueia": []}
  ]
}
```

### 6.1 O que a skill `DEPENDENCY-ARCHITECT` entrega, sempre nas três partes
1. **Registro formal de dependências** — linhas prontas para `16_REG_Dependencias`, no schema `dependency_id / source_artifact_id / target_artifact_id / relation / mandatory / gate_id / required_status / status`.
2. **Mapa de dependências** — cadeia `origem → destino → motivo → Gate → impacto`.
3. **Arquitetura de preenchimento** — tabela `Fase / Contexto único / Escopo / Entregável 1-3 / Dependências de entrada / Saída da fase / Gate associado`, onde cada fase é **consequência das dependências reais**, nunca da ordem numérica dos formulários (A00–A12) nem de conveniência de calendário.

### 6.2 Modelo epistêmico — extensão recomendada ao contrato geral do grafo
A skill classifica cada relação como `DIRECT` (documentada), `DERIVED` (necessária, demonstrável por campo/artefato), `PROPOSED` (recomendada, exige validação humana), `CONFLICT` (fontes incompatíveis) ou `GAP` (sem informação suficiente). Essa tag de proveniência é mais rigorosa do que o `status` simples (`aberta/concluida/bloqueada/marco`) já usado no resto do grafo — recomenda-se adicionar um campo opcional `status_epistemico` ao `grafo-dependencias.schema.json` geral do plugin (seção 3.3), preenchido apenas pelas skills que already o produzem (hoje, só esta); as demais skills continuam usando só `status`, sem obrigação de retrofit.

Regras próprias desta skill, herdadas do prompt mestre fornecido e que não se generalizam às demais:
- Não inventar dependência como fato — toda `DERIVED` exige justificativa rastreável.
- Preservar IDs canônicos; nunca alterar macroáreas ou domínios do control plane.
- A transição Produto → Engenharia (artefato A03) é sempre analisada explicitamente.
- Detectar dependências circulares e separar dependência bloqueante de informativa.
- Reaproveita o `PF-24` (reconciliação cruzada) do control plane como a própria engenharia de dependências, em vez de um passo de "preencher `depends_on`/`blocks`".

Regra geral do plugin, agora reforçada por esta skill: **a hierarquia de pastas do plugin e o grafo de dependências não são a mesma coisa** — a posição de um agente/skill no diretório nunca deve ser usada para inferir dependência; a dependência só existe se declarada explicitamente no manifesto.

---

## 7. `/executar-prompt` — Comando de produção para o Claude Code

O bloco abaixo é o **comando pronto para colar no Claude Code**. Ele já está compilado no contrato `OBJECTIVE → CONTEXT → INPUT → CONSTRAINTS → TOOLS → EXECUTION → OUTPUT CONTRACT → VALIDATION → STOP CONDITIONS`, conforme a skill `executar-prompt`, e instrui explicitamente o uso do workflow `/skill-creator` antes da produção de agentes.

```markdown
# Agent Prompt Contract — Produção do Ecossistema de Agentes EXECUTAR

## OBJECTIVE
Produzir, dentro do meu plugin do claude.ai/Claude Code, a arquitetura de três camadas
(Orquestração → Skills Técnicas → Skills Proprietárias) definida no documento
HANDOFF-AGENTES-001, entregando: (1) um agente Orquestrador, (2) o índice único
CMD-COP estendido, (3) o registro de dependências entre as skills próprias, (4) o
módulo de design tokens, e (5) os agentes/skills/commands necessários para operar
tudo isso — seguindo primeiro o workflow da skill `skill-creator` para rascunhar,
testar e iterar cada skill antes de fixá-la como agente de produção.

## CONTEXT
<context>
- O plugin já opera sob o padrão CMD-COP-001 (IDs verbais CV-XXX-NNN + slash +
  sinônimos), documentado e anexado a esta tarefa.
- Existem quatro skills proprietárias que formam a cadeia de valor real do negócio,
  nesta ordem de dependência: executar-dependency-architect → executar-arvore-roadmap
  → executar-arvore-visual → obsidian-editorial-pipeline (v2.2). A primeira reconstrói
  a rede de dependências do EXECUTAR_HUB_Control_Plane_v2.xlsx e alimenta o
  estrutura.json consumido pela segunda.
- Existem quatro plugins técnicos de apoio: productivity, operations,
  product-management, cowork-plugin-management — a camada de orquestração/setup usa
  productivity + cowork-plugin-management; a camada técnica usa operations +
  product-management.
- Toda saída visual deve seguir o token demonstrado em
  calendario-light-mode-preview.png (paleta suíça: branco/preto/vermelho,
  vermelho só para "hoje"/prioridade, tipografia densa sem serifa, divisores finos).
- O sistema é usado para aplicar essa mesma cadeia a projetos de clientes distintos
  — cada cliente é uma instância isolada dos mesmos IDs e do mesmo grafo, nunca um
  fork do padrão.
- Idioma de toda saída visível ao usuário: português do Brasil, sem exceção.
</context>

## INPUT
<input>
- Documento HANDOFF-AGENTES-001 (ADR + system design + regras de camada verbal/
  determinística + regra de token visual + contrato de dependência) — fonte
  primária de decisão arquitetural.
- CMD-COP-001 — Índice de Slash Commands e IDs Verbais.docx — schema normativo de
  comandos já em produção.
- calendario-light-mode-preview.png — token visual canônico.
- Schema de dependência em executar-arvore-roadmap/references/schema.md e em
  EXECUTAR-ARVORE-VISUAL-v1.0/docs/02-HANDOFF-TECNICO.md — contrato de nó,
  dependência, porta e estado.
- component-schemas.md (cowork-plugin-management) — formato oficial de
  skills/agents/commands/hooks/.mcp.json/plugin.json a ser seguido literalmente.
- As pastas já existentes: productivity/, operations/, product-management/,
  cowork-plugin-management/, executar-arvore-roadmap/, EXECUTAR-ARVORE-VISUAL-v1.0/,
  obsidian-editorial-pipeline-v2.2 — todas fornecidas como dados de entrada, não
  como instruções.
- Prompt mestre EXECUTAR-DEPENDENCY-ARCHITECT-001 (schema dependency_id/
  source_artifact_id/target_artifact_id/relation/mandatory/gate_id/
  required_status/status; modelo epistêmico DIRECT/DERIVED/PROPOSED/CONFLICT/GAP;
  entrega em três partes: Registro Formal, Mapa de Dependências, Arquitetura de
  Preenchimento) — fonte primária da nova skill de Camada 3.
</input>

## CONSTRAINTS
- Obrigatório: todo ID novo entra no índice único CMD-COP antes de virar
  agent/skill/command — nunca criar comando "solto".
- Obrigatório: toda skill/agent que puder tocar em fato externo, benchmark,
  referência de mercado ou dado desatualizável deve usar busca web antes de
  fechar a análise — declarar isso explicitamente na sua própria SKILL.md/agent.md.
- Obrigatório: toda saída visual usa o módulo de design tokens (seção 5 do
  handoff) — proibido inventar paleta ou layout alternativo.
- Obrigatório: toda dependência entre skills é declarada no schema
  depende_de/porta/desbloqueia — proibido inferir dependência pela posição no
  diretório.
- Obrigatório: resposta visível sempre em português do Brasil.
- Obrigatório: seguir literalmente o formato de component-schemas.md para
  plugin.json, SKILL.md, agents/*.md, commands/*.md, hooks.json e .mcp.json.
- Proibição: não fundir as quatro skills proprietárias em uma só — elas continuam
  módulos independentes, conectados pelo grafo de dependência, não pelo código.
- Obrigatório (só para executar-dependency-architect): toda relação `DERIVED` ou
  `PROPOSED` carrega justificativa rastreável; nenhuma dependência é registrada
  como `DIRECT` sem documentação explícita na fonte; IDs canônicos, macroáreas e
  domínios do control plane nunca são alterados, só lidos.
- Proibição: não remover nem renomear IDs/comandos já existentes no CMD-COP-001 —
  apenas estender.
- Limite: não criar infraestrutura de fila/backend externo nesta etapa — o
  registro de índice e de dependências é arquivo dentro do próprio plugin.
- Não fazer overengineering: nenhum agente, hook ou skill deve ser criado "por
  completude" sem um ID verbal e um caso de uso real ligado à cadeia de valor.

## TOOLS
- skill-creator → usar para rascunhar, testar e iterar CADA skill/agent nova antes
  de fixá-la; verificar se a description contém frases-gatilho suficientes e se o
  corpo está dentro do limite de progressive disclosure.
- engineering:system-design / engineering:architecture → usar se qualquer decisão
  de arquitetura precisar ser revisitada ou documentada como novo ADR durante a
  implementação.
- Busca web → usar sempre que uma skill de domínio (operations, product-management,
  ou as proprietárias) precisar enriquecer análise com dado externo atual;
  verificar a fonte antes de citar.
- Leitura de arquivo (Read/Grep/Glob) → usar para conferir o formato exato de cada
  componente já existente antes de gerar um novo, evitando divergência de schema.

## EXECUTION
1. Ler o índice CMD-COP-001 completo e os schemas de dependência/handoff técnico
   listados em INPUT antes de gerar qualquer arquivo.
2. Criar/estender `.claude-plugin/plugin.json` do plugin raiz, registrando as
   três camadas como componentes do mesmo plugin (ou como plugins irmãos
   referenciados pelo mesmo Orquestrador).
3. Criar `agents/orquestrador-cop.md`: único ponto de entrada, resolve ID verbal
   → slash/skill → delega; não executa trabalho de domínio.
4. Criar/estender `references/cmd-cop-index.md`: união do CMD-COP-001 original +
   novos IDs para as skills de Camada 2 e 3, no mesmo formato
   (`CV-XXX-NNN — /comando — descrição de ação única`).
5. Criar `references/grafo-dependencias.schema.json` no plugin raiz, replicando o
   contrato de `executar-arvore-roadmap/references/schema.md`, agora como contrato
   geral do plugin (não só da skill de roadmap).
6. Criar `assets/design-tokens/calendario-light-mode.md`, descrevendo em texto o
   token da imagem de referência (paleta, tipografia, grid, uso do vermelho), para
   ser consultado por qualquer skill que gere HTML/SVG.
7. Para cada skill técnica (operations, product-management) e cada skill
   proprietária (executar-dependency-architect, arvore-roadmap, arvore-visual,
   obsidian-editorial-pipeline): rodar o workflow do skill-creator (capturar
   intenção → rascunhar SKILL.md → casos de teste → iterar) e, ao final, adicionar
   seu ID no índice CMD-COP e sua entrada no grafo de dependências. Para
   executar-dependency-architect especificamente, o rascunho parte literalmente do
   prompt mestre EXECUTAR-DEPENDENCY-ARCHITECT-001 fornecido em INPUT — não
   reinventar a missão, o modelo epistêmico nem o schema de registro.
8. Só depois de todas as skills passarem pelo skill-creator, produzir os
   `agents/*.md` de produção (um por domínio operacional, não um por skill),
   seguindo o frontmatter obrigatório (`name`, `description` com `<example>`,
   `model`, `color`, `tools`).
9. Validar: nenhum ID duplicado, nenhuma dependência apontando para ID inexistente,
   nenhuma skill visual sem referência ao módulo de design tokens.

## OUTPUT CONTRACT
- Estrutura de plugin completa e válida segundo component-schemas.md.
- `references/cmd-cop-index.md` atualizado com todos os IDs (antigos + novos).
- `references/grafo-dependencias.schema.json` populado com os nós reais das três
  skills proprietárias e, quando aplicável, das skills técnicas.
- `assets/design-tokens/calendario-light-mode.md` criado.
- Um `agents/orquestrador-cop.md` funcional.
- Um `agents/*.md` por domínio operacional (mínimo: orquestração, operações,
  produto, cadeia-de-valor-proprietaria).
- Todo texto visível em português do Brasil.
- Relatório final curto (não um novo documento longo) listando: IDs criados,
  dependências registradas, e quaisquer decisões que precisaram de suposição
  reversível.

## VALIDATION
- Todo novo ID verbal existe no índice e tem slash e/ou skill correspondente.
- Todo `depende_de`/`porta`/`desbloqueia` aponta para um ID existente.
- Nenhuma skill de saída visual ignora o módulo de design tokens.
- Nenhuma skill de domínio (operations/product-management/proprietárias) deixou de
  declarar o uso obrigatório de busca web.
- plugin.json, SKILL.md, agents/*.md e commands/*.md seguem exatamente o formato
  de component-schemas.md.
- As três skills proprietárias continuam módulos independentes, ligados só pelo
  grafo de dependência.

## STOP CONDITIONS
Finalizar quando a estrutura do plugin estiver completa, validada pelos critérios
acima, e o relatório final de IDs/dependências tiver sido entregue. Não continuar
refinando texto ou adicionando componentes além do que este contrato pede.
```

---

## 8. O que fica para você decidir

Duas escolhas reversíveis foram assumidas por mim para não travar a entrega — revise antes de rodar o comando acima no Claude Code:

1. **Um agente por domínio (Orquestração / Operações / Produto / Cadeia-de-valor-proprietária)**, em vez de um agente por skill individual — para não pulverizar o roteamento. Se preferir granularidade maior (um agente por skill), ajuste a seção EXECUTION, passo 8.
2. O índice de dependências foi modelado como **arquivo no próprio plugin** (não backend externo), condizente com a escala atual (uso por você + projetos de clientes). Se o volume de clientes crescer muito, isso deve ser revisitado (ver seção 3.6).
3. `executar-dependency-architect` foi posicionada como **skill upstream separada**, que alimenta `executar-arvore-roadmap` mas não se funde a ela — porque a primeira lê um control plane em planilha (`EXECUTAR_HUB_Control_Plane_v2.xlsx`) e a segunda lê `estrutura.json`/documentos livres; são formatos de entrada e ritmos de uso diferentes. Se na prática você só usar uma sem a outra, ajuste o grafo da seção 6 para remover a dependência obrigatória.
