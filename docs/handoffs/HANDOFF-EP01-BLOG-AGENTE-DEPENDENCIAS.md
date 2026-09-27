# HANDOFF — EP-01 Lançamento do Blog → Agente de Dependências

- Origem: sessão `executar-prompt` (modo `transform`), 2026-09-27
- Destino: Agente de Dependências (aplica o workflow próprio dele)
- Status: `approval:pendente` — nenhuma Issue criada; aprovação é ato humano
- Gate: `gate:tbd` (exceto gates já confirmados na fonte: G-SCAFFOLD, G-PILAR1..3)
- Owner: A_DEFINIR

## 1. O que está sendo entregue
Um prompt normalizado (seção 4) que converte o pedido do usuário em especificação para o agente de dependências. O agente **não** monta o workbook: ele produz o grafo de dependências e a cadeia única de valor que depois alimentarão o workbook impresso.

## 2. Fontes recebidas (anexos do usuário, lidas nesta sessão)
| ID | Arquivo | Conteúdo observado |
|---|---|---|
| F1 | `Prompt/texto.txt` | Pedido original (transcrição de voz) — workbook A4, 1 página/dia, 3 workflows |
| F2 | `creator-led-platform-setup_DADOS.csv` | 1 tarefa: SETUP-001 (2026-09-27, marco, porta G-SCAFFOLD) |
| F3 | `blog-riscos-cognitivos-tres-pilares_DADOS.csv` | 15 tarefas P1-001…P3-005, 2026-09-28→2026-10-16, gates G-PILAR1/2/3, dependências lineares |
| F4 | `Process_Document_Produção_Editorial_Multiplataforma.docx` (PD-CLB-20260922-F01-DOC-V02) | 22 steps editoriais, estados 0/33/66/99/100%, Entry Gate 4 dias, matriz de derivados |
| F5 | `arvore-projeto-creator-led.txt` / `creator-led-platform_ARVORE-ZIP.zip` | Árvore do monorepo (apps, packages, content, editorial, knowledge, agents…) — já espelhada neste repositório |

Os anexos não estão versionados aqui; o agente deve solicitá-los ao usuário ou ao repositório onde forem depositados. Não inventar conteúdo ausente.

## 3. Lacunas conhecidas
- Plano do workflow Estúdio: sem fonte granular; apenas escopo inferido (Fase 2 do F4: imagens, vídeos, infográficos).
- Áreas locais de engenharia a subir: nomes de área vêm da árvore F5; conteúdo local real não inspecionado.
- Página Notion / Master Index do EP-01: não confirmados nesta sessão.

## 4. Prompt anexado

```xml
<objective>
Aplicar seu workflow de dependências ao EPIC "EP-01 Lançamento do Blog" (Creator-Led Platform) por working backwards: partir do blog publicado e derivar tudo que precisa acontecer antes, organizando uma cadeia única de valor com dependências explícitas entre três workflows diários.
</objective>

<context>
- O usuário executará tudo a partir de um workbook impresso (A4, 1 página = 1 dia, organizado por semana/sprint). Seu resultado é o insumo dele; você não gera o workbook.
- O ecossistema (Creator-Led Platform) é contexto à parte e deve ser descrito separadamente do EP-01.
- Workflows do dia, nesta ordem:
  W1 Engenharia — subir para o GitHub, por área (ex.: design tokens, identidade visual, design-system, apps/web), os arquivos já desenvolvidos localmente, cobrindo planejamento → desenvolvimento → lançamento do blog.
  W2 Editorial — plano existente e granular (F3 + steps do F4): peças-mãe dos 3 pilares e seus desmembramentos/derivados distribuídos no roadmap.
  W3 Estúdio — produção visual/vídeo (infográficos, carrosséis, vídeos) que fecha o dia.
- Toda evidência sobe como zip para o GitHub da organização (executar-23/Copiloto-ops é o único GitHub operacional).
</context>

<input>
F1–F5 conforme seção 2 do handoff. Datas, IDs e gates confirmados: SETUP-001/G-SCAFFOLD; P1-001…P3-005 com G-PILAR1→G-PILAR2→G-PILAR3; janela 2026-09-28 a 2026-10-16 (15 dias úteis).
</input>

<constraints>
- Não inventar IDs, owners, gates, datas ou conteúdo de arquivos; lacuna vira A_DEFINIR / gate:tbd.
- Preservar integralmente as dependências já declaradas em F3.
- WIP=1 por workflow por dia; cada dia tem no máximo uma entrega por workflow.
- Dependências cruzadas obrigatórias: nenhuma publicação editorial (G-PILARn) antes de o blog estar no ar (W1); nenhum asset de estúdio antes do texto-fonte aprovado (W2).
- Issues somente propostas (approval:pendente); não criar Issues nem alegar sincronização Notion↔GitHub.
- Saída em pt-BR.
</constraints>

<execution>
1. Definir o estado final do EP-01 (blog publicado + 3 pilares + derivados) e os entregáveis do epic.
2. Working backwards: listar entregáveis de W1, W2, W3 e decompor em Epic → Issue → Sub-issue.
3. Montar o grafo (DAG): dependências intra e entre workflows; detectar ciclos e caminho crítico.
4. Agrupar em sprints/ciclos (sugestão: 3 sprints de 5 dias, um por pilar) e alocar por dia respeitando WIP.
5. Para cada item: entregável, DoD, evidência (nome do zip), destino no repositório e o que acontece depois (próximo consumidor).
</execution>

<output_contract>
1. Descrição do ecossistema (≤ 1 página).
2. Tabela de itens: id | workflow (W1/W2/W3) | tipo (epic/issue/sub-issue) | título | depende_de | gate | sprint | data | DoD | evidência_zip | destino_repo | consumidor_seguinte | fonte (F1–F5 ou INFERIDO).
3. DAG em Mermaid + caminho crítico.
4. Roadmap por sprint/dia (3 linhas por dia: W1, W2, W3).
5. Lista de lacunas e decisões pendentes para o humano.
Formato preferido: CSV compatível com o schema de F3 (task_id,data,ciclo,titulo,peso,status,depende_de,porta,evidencia,fluxo_de_valor_provavel) + Markdown.
</output_contract>

<validation>
- Todas as 15 tarefas de F3 e SETUP-001 presentes, dependências intactas.
- Grafo sem ciclos; toda aresta cruzada justificada.
- Nenhum dia com mais de 1 item por workflow.
- Todo item marcado com fonte ou INFERIDO.
</validation>

<stop_conditions>
Parar e reportar se: faltar anexo necessário; houver conflito entre F3 e F4 sem regra de resolução; ou a alocação violar a janela de 15 dias sem aprovação humana.
</stop_conditions>
```
