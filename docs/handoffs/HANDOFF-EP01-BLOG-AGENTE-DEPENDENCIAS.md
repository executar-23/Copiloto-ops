# HANDOFF — EP-01 Lançamento do Blog → Agente de Dependências

- Origem: sessão `executar-prompt` (modo `transform`), 2026-09-27
- Destino: Agente de Dependências (aplica o workflow próprio dele)
- Status: `approval:pendente` — nenhuma Issue criada; aprovação é ato humano
- Gate: `gate:tbd` (exceto gates já confirmados na fonte: G-SCAFFOLD, G-PILAR1..3)
- Owner: A_DEFINIR
- Escopo desta entrega: **especificação do workbook** (não o workbook final, não execução do Epic)

## 1. O que está sendo entregue
Um prompt normalizado (seção 4) que converte o pedido do usuário em especificação para o agente de dependências. O agente **não** monta o workbook final nem executa tarefas do projeto: ele produz a especificação completa do workbook (arquitetura, modelo hierárquico, cadeia de valor, templates e schema de tarefa) que orienta uma etapa posterior a gerar o documento.

## 2. Fontes recebidas (anexos do usuário, lidas nesta sessão)
| ID | Arquivo | Conteúdo observado |
|---|---|---|
| F1 | `Prompt/texto.txt` | Pedido original (transcrição de voz) — workbook A4, 1 página/dia, 3 workflows |
| F2 | `creator-led-platform-setup_DADOS.csv` | 1 tarefa: SETUP-001 (2026-09-27, marco, porta G-SCAFFOLD) |
| F3 | `blog-riscos-cognitivos-tres-pilares_DADOS.csv` | 15 tarefas P1-001…P3-005, 2026-09-28→2026-10-16, gates G-PILAR1/2/3, dependências lineares |
| F4 | `Process_Document_Produção_Editorial_Multiplataforma.docx` (PD-CLB-20260922-F01-DOC-V02) | 22 steps editoriais, estados 0/33/66/99/100%, Entry Gate 4 dias, matriz de derivados |
| F5 | `arvore-projeto-creator-led.txt` / `creator-led-platform_ARVORE-ZIP.zip` | Árvore do monorepo (apps, packages, content, editorial, knowledge, agents…) |

Os anexos não estão versionados aqui; o agente deve solicitá-los ao usuário ou ao repositório onde forem depositados. Não inventar conteúdo ausente.

## 3. Schema canônico obrigatório (não é o task-spec:v1 do plugin externo)

Fonte: `docs/SCHEMA-TRABALHO.md`, `.github/labels.yml`, `AGENTS.md`. O plugin `copiloto-operacional` usa outro contrato (`type/tarefa`, `state/backlog_validated`..., `<!-- task-spec:v1 -->`) que **não** é o schema aceito neste repositório. Toda estrutura produzida pelo agente deve usar o schema abaixo, não o do plugin.

**Hierarquia canônica:**
```
Project #1
└── Epic
    ├── Issue de entrega/ciclo
    │   └── Sub-issue de etapa/grupo
    │       └── Checklist + evidência
    └── Issue de entrega/ciclo
```

| Objeto | Título esperado | Função |
|---|---|---|
| Epic | `[EPIC] <ID> — <resultado>` | agrega múltiplas entregas |
| Issue | `[ISSUE] <ID pai> — <entrega>` | unidade executável/verificável |
| Sub-issue | `[SUB] #<pai> — <etapa>` | etapa com execução/evidência própria |
| Checklist | item dentro da Issue | passo atômico |

**Campos obrigatórios no corpo de cada tarefa:** fonte Notion/documento-fonte; ID confirmado quando existir; Epic pai; Runbook; Owner; Aprovação; Gate; Estado operacional; objetivo e escopo; critérios de aceite; dependências; evidências; decisões humanas pendentes.

**Defaults do repositório:** Owner ausente → `A_DEFINIR`; Aprovação inicial → `pendente`; Gate ausente → `gate:tbd`; WIP → 1 por agente.

**Máquina de estados aceita:** `PLANNED → STRUCTURED → IMPLEMENTED → PRODUCED → VERIFIED`. Aprovação é eixo separado — `VERIFIED` não implica `approval:aprovado`.

**Labels do schema:** `type:epic`, `type:issue`, `type:sub-issue`, `area:editorial`, `approval:pendente`, `approval:aprovado`, `gate:tbd`, `state:planned`, `state:structured`, `state:implemented`, `state:produced`, `state:verified`, `status:blocked`, `requires-human-decision`, `priority:alta`, `priority:media`, `priority:baixa`. `.github/labels.yml` declara o estado desejado do schema, mas não comprova que todas as labels estão criadas/aplicadas no GitHub — verificar antes de assumir.

## 4. Lacunas conhecidas
- Plano do workflow Studios: sem fonte granular; escopo a descobrir exclusivamente nas fontes disponíveis — se ausente, registrar `A_DEFINIR`, nunca inventar.
- Áreas locais de engenharia a subir: nomes de área vêm da árvore F5; conteúdo local real não inspecionado.
- Página Notion / Master Index do EP-01: não confirmados nesta sessão.
- Duração de ciclos/sprints: não decidir antecipadamente (nem 2, 3 nem N semanas) — só depois de conhecida a cadeia de dependências.

## 5. Prompt anexado

```xml
<objective>
Projetar a especificação completa de um workbook físico, imprimível, autossuficiente e operacional para conduzir de ponta a ponta o primeiro Epic do projeto: Lançamento do Blog.

O workbook deve ser construído por working backwards a partir do resultado final esperado — blog lançado, operacional e com suas entregas editoriais publicadas — decompondo tudo em:
Epic → Roadmap → Ciclos/Sprints → Issues → Sub-issues → tarefas → evidências.

O workbook será a interface operacional principal do usuário. Durante a execução diária, o usuário não deve precisar consultar aplicativos, dashboards, Notion, GitHub, planilhas ou outras ferramentas para descobrir: o que fazer; em qual ordem; por que fazer; de que depende; qual é o critério de pronto; onde salvar; onde subir; qual evidência registrar; o que é liberado depois da conclusão.

O GitHub continua sendo o destino de arquivos, código, artefatos e evidências, mas o workbook precisa conter previamente todas as instruções necessárias para operar esse fluxo.

NÃO executar tarefas do projeto nesta etapa. O resultado é exclusivamente o planejamento e a especificação completa do workbook — não o workbook final.
</objective>

<context>
1. Ecossistema: existe um ecossistema EXECUTAR mais amplo, descrito no workbook apenas como contexto estrutural, sem se confundir com o Epic atual. O primeiro Epic operacional é EPIC 01 — LANÇAMENTO DO BLOG.

2. Estado atual: grande parte dos ativos já existe localmente (identidade, elementos visuais, estruturas editoriais, documentação, hardcode). O trabalho não começa do zero. Parte essencial do planejamento de engenharia é: identificar o que já existe; organizar por área; definir a sequência de ingestão; definir os destinos corretos no GitHub; transformar em estrutura versionada utilizável; seguir para integração, desenvolvimento, validação e lançamento.

3. Princípio operacional: todo dia de execução corresponde a uma página A4. Cada página deve permitir que o usuário acorde, abra o workbook e execute o dia inteiro sem procurar instruções em outro lugar. Organizado por semanas, ciclos/sprints e pelo Epic.

4. Três workflows diários, nesta ordem:
   - Workflow 1 — Engenharia/lançamento do Blog: tudo que precisa acontecer tecnicamente para o blog ser organizado, integrado, desenvolvido, validado e lançado, partindo dos artefatos locais existentes. Categorias possíveis (só quando sustentadas pelas fontes): identidade visual, logo, design tokens, componentes, conteúdo, configuração, código, infraestrutura, documentação, arquivos de projeto.
   - Workflow 2 — Editorial: usar o planejamento editorial existente (F3, F4) como fonte, preservando estrutura, granularidade e sequência em vez de recriar genericamente. Distribuir no mesmo roadmap do lançamento.
   - Workflow 3 — Studios: descobrir etapas exclusivamente nas fontes disponíveis; não inventar estrutura. Ausência de informação → `A_DEFINIR`. O fechamento do Workflow 3 também serve como fechamento operacional do dia quando compatível com as fontes.
</context>

<input>
Fontes de verdade, nesta ordem: (1) regras e documentação canônica do repositório operacional — `docs/SCHEMA-TRABALHO.md`, `.github/labels.yml`, `AGENTS.md`; (2) Issues, Epics, Sub-issues, Runbooks e arquivos reais existentes no repositório; (3) documentos e planejamento editorial já registrados (F3, F4); (4) arquivos locais fornecidos pelo usuário (F1, F2, F5); (5) documentação do ecossistema EXECUTAR necessária para contextualização; (6) decisões humanas explicitamente registradas.

Preservar IDs já existentes (SETUP-001, P1-001…P3-005, gates G-SCAFFOLD/G-PILAR1-3). Não reconstruir tarefas existentes com IDs novos. Inventariar o que já está definido antes de criar qualquer estrutura conceitual.
</input>

<constraints>
- Aplicar working backwards a partir do estado final "Blog lançado".
- Estruturar uma cadeia única de valor com toda dependência explícita.
- WIP coerente com as regras operacionais existentes (WIP=1 por agente).
- Não inventar Epic, gate, owner, dependência, data ou evidência.
- Não apagar granularidade existente nem substituir o planejamento editorial já definido por um planejamento genérico.
- Não misturar contexto do ecossistema com execução do Epic.
- Não criar atividades apenas para preencher dias; não paralelizar quando uma tarefa depende da outra.
- Nada é "feito" sem critério de pronto e evidência; cada artefato produzido tem destino definido; cada tarefa diz o que é liberado imediatamente depois.
- O workbook deve funcionar offline em papel. Links podem ser impressos como referência, mas nenhuma instrução essencial pode existir só atrás de um link.
- Priorizar instrução operacional sobre texto explicativo.
- Usar o schema canônico de `docs/SCHEMA-TRABALHO.md` (Epic/Issue/Sub-issue/Checklist, títulos `[EPIC]`/`[ISSUE]`/`[SUB]`, labels e defaults do repositório) — nunca o `task-spec:v1` do plugin `copiloto-operacional`.
- Nenhuma tarefa do projeto deve ser executada durante esta solicitação (não criar/alterar Issues, não modificar GitHub, não publicar arquivos, não gerar PDF/DOCX, não iniciar o lançamento).
</constraints>

<tools>
- Repositório: ler regras, descobrir estrutura real, inventariar Issues/Sub-issues/Epics existentes, identificar Runbooks, localizar caminhos reais e dependências. Verificar antes de assumir qualquer estado (inclusive se as labels de `.github/labels.yml` existem de fato no GitHub).
- Arquivos fornecidos (F1–F5): identificar ativos já existentes, mapear conteúdos locais para áreas, localizar planejamento editorial, descobrir artefatos a enviar ao GitHub.
- Fontes documentais: usar apenas quando alterarem decisões do planejamento.
- Não usar nenhuma ferramenta para executar, publicar, mover ou modificar artefatos durante esta etapa.
</tools>

<execution>
ETAPA 1 — Definir o resultado final: formalizar o Definition of Done do Epic "Blog lançado" e decompor em entregáveis finais verificáveis, sem inventar critérios não sustentados pelas fontes.

ETAPA 2 — Working backwards: para cada entregável final, perguntar sucessivamente (a) o que precisa estar concluído imediatamente antes; (b) de que isso depende; (c) qual artefato comprova a conclusão; (d) que atividade produz esse artefato; (e) que input essa atividade exige — repetir até chegar aos ativos já disponíveis hoje.

ETAPA 3 — Construir a cadeia única de valor: INPUT → TRABALHO → ARTEFATO → EVIDÊNCIA → GATE → PRÓXIMA ATIVIDADE. Eliminar duplicações, tarefas sem saída, tarefas sem dependência clara, entregáveis sem responsável operacional e atividades que não contribuam para o lançamento.

ETAPA 4 — Estruturar o Epic (EPIC 01 — Lançamento do Blog) com, conforme evidência real: objetivo; DoD; entregáveis; riscos; gates; cadeia de valor; ciclos; sprints; roadmap; Issues; Sub-issues; dependências; evidências — no schema canônico (seção 3 do handoff).

ETAPA 5 — Planejar ciclos e sprints: determinar duração somente depois de conhecida a cadeia de dependências (não decidir antecipadamente 2, 3 ou N semanas). Agrupar em ciclos coerentes com resultados verificáveis; cada ciclo tem objetivo, entrada, saída, gate, conjunto de Issues e datas só quando sustentadas.

ETAPA 6 — Integrar os três workflows: para cada dia do roadmap, montar Workflow Engenharia, Workflow Editorial, Workflow Studios e Fechamento do dia, respeitando dependências globais (ex.: não planejar produção editorial que dependa de algo técnico ainda inexistente).

ETAPA 7 — Produzir o modelo diário A4 (uma folha por dia) com: cabeçalho (Epic, ciclo/sprint, semana, dia/data, objetivo do dia, entrega principal, gate/marco relacionado, estado de entrada, estado esperado ao final); Workflow 1 Engenharia, Workflow 2 Editorial e Workflow 3 Studios, cada um com por tarefa: ID, ação, input, origem, passos, DoD, artefato gerado, nome/formato, destino GitHub, evidência, dependência, o que desbloqueia, checkbox de conclusão (Editorial preserva IDs/sequência existentes; Studios usa `A_DEFINIR` onde faltar fonte); e Fechamento do dia com checklist (entregáveis concluídos; arquivos salvos; arquivos enviados ao destino correto; evidências registradas; gates verificados; pendências; bloqueios; preparação para amanhã) e campos manuscritos `FEITO:` `EVIDÊNCIA:` `BLOQUEIO:` `OBSERVAÇÃO:` `AMANHÃ COMEÇA COM:`.

ETAPA 8 — Criar a estrutura do workbook, nesta ordem: Capa (nome do workbook e Epic); Seção 1 Ecossistema (mapa resumido do EXECUTAR, só contexto necessário); Seção 2 Epic (objetivo, DoD, entregáveis finais, cadeia de valor, dependências, gates); Seção 3 Roadmap (visão completa do Epic no tempo); Seção 4 Ciclos/Sprints (uma abertura por ciclo: objetivo, entregáveis, Issues, dependências, gate final); Seção 5 Semanas (visão semanal com os três workflows); Seção 6 Páginas diárias (uma A4 por dia); Seção 7 Evidências e índice (mapa para localizar artefatos e evidências no GitHub — o workbook não armazena os arquivos digitais, só indica onde cada evidência está ou deverá ser armazenada).
</execution>

<output_contract>
Entregar uma especificação de workbook — não o workbook final, não a execução do projeto — contendo:
1. Arquitetura do workbook: sumário completo das seções.
2. Modelo hierárquico: Epic → Roadmap → Ciclos/Sprints → Semanas → Dias → Workflows → tarefas.
3. Cadeia de valor: representação ordenada das principais dependências do lançamento.
4. Estrutura dos três workflows: papel e contrato operacional de Engenharia, Editorial e Studios.
5. Template A4 diário: modelo completo e reutilizável da página de um dia.
6. Template de abertura de ciclo/sprint.
7. Template da página do Epic.
8. Schema de tarefa do workbook, no formato canônico de `docs/SCHEMA-TRABALHO.md`, com por tarefa (quando aplicável): ID; Epic; ciclo; workflow; área; título; objetivo; input; origem; dependências; passos; Definition of Done; artefato; nome/formato; destino; evidência; gate; estado (`PLANNED`/`STRUCTURED`/`IMPLEMENTED`/`PRODUCED`/`VERIFIED`); aprovação (eixo separado do estado); próxima ação/desbloqueio.
9. Lacunas: listar explicitamente tudo que as fontes não permitem determinar, usando `A_DEFINIR` — nunca preencher por inferência silenciosa.
</output_contract>

<validation>
Antes de finalizar, confirmar: o workbook orienta um dia completo sem consulta externa; toda tarefa tem resultado observável e critério de pronto; todo artefato tem destino; toda conclusão tem evidência; toda dependência está explícita; está claro o que cada tarefa desbloqueia; Engenharia/Editorial/Studios aparecem em todo dia com trabalho real neles; nenhuma tarefa foi criada só para ocupar espaço; o roadmap foi derivado por working backwards; o planejamento editorial existente foi preservado; Epic/Issues/IDs existentes foram preservados; o ecossistema foi separado do Epic; as páginas diárias cabem conceitualmente em uma A4; uma pessoa consegue imprimir e operar somente pelo workbook. Qualquer requisito essencial sem sustentação em fonte é marcado `A_DEFINIR`.
</validation>

<stop_conditions>
Finalizar quando existir uma especificação completa e verificável do workbook, suficiente para uma etapa posterior gerar o documento final. Nesta execução: NÃO gerar PDF; NÃO gerar DOCX; NÃO criar ou alterar Issues; NÃO modificar GitHub; NÃO executar tarefas do Epic; NÃO publicar arquivos; NÃO enviar e-mails; NÃO iniciar o lançamento. Parar após entregar a especificação formal do workbook. Parar também e reportar se faltar anexo necessário, se houver conflito entre F3 e F4 sem regra de resolução, ou se a alocação de ciclos violar a janela de dependências conhecida sem aprovação humana.
</stop_conditions>
```
