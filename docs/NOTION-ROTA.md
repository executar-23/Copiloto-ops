# Rota Notion ↔ GitHub
A arquitetura atual utiliza somente o Notion do projeto como banco de informações e o repositório GitHub executar-23/Copiloto-ops para execução.

| Função | Página Notion |
|---|---|
| Entrada do projeto | [GTM-Blog — Launch Control](https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac) |
| Entrada e saída do agente | [00 — Agent Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) |
| Registro transversal e backlinks | [01 — Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62) |
| Fundamentos | [02 — Foundation Doc](https://app.notion.com/p/3e7d1d673fb3815cb133cd8aeda89397) |
| Decisões | [03 — ADRs](https://app.notion.com/p/3e7d1d673fb381aeb3e4dda7c9f37b61) |
| Plano executável | [05 — Plano de Implementação](https://app.notion.com/p/3e7d1d673fb381368574fa687f7cf0eb) |
| Tarefas planejadas | [04 — Tasks](https://app.notion.com/p/3e7d1d673fb381bd8f88e5c38979d403) |

## Contrato de correlação
1. Consulte a página Notion-fonte e confirme seus IDs. Registre URL e ID no corpo da Issue do [Copiloto-ops](https://github.com/executar-23/Copiloto-ops/issues).
2. Ao concluir, registre no Master Index a Issue, commit, resultado, estado de aprovação e próximo passo.
3. Registre decisões relevantes em ADRs. Não duplique o conteúdo do Notion em Issues sem necessidade.
4. Acesso a uma plataforma não concede acesso à outra. Links são referências, não sincronização automática.

Não inferir rotas, IDs ou permissões além destas páginas verificadas.

## Copiloto Operacional como conector
O Copiloto executa sobre as Issues deste repositório (`OPS_REPO = executar-23/Copiloto-ops`). Há duas portas com o mesmo núcleo: o plugin do Claude Code e o conector MCP remoto do claude.ai, servido pelo Worker `executar-copiloto` no Cloudflare em `POST /mcp/<segredo>`. O código fica em `Sas-Executar/executar-Blog`; decisão registrada no ADR-016, emenda 2026-09-26b.

| Pedido no claude.ai | Ferramenta | Registro |
|---|---|---|
| Contexto, schema, IDs | conector Notion (Agent Runner → Master Index → 04 — Tasks) | só IDs confirmados na fonte |
| `/hoje`, `/amanha`, `/urgente`, `/%`, `/status-report` | Copiloto `consultar` | leitura; nada muda |
| `/fila`, `/ideia`, `/feito`, `/campanha`, `/criar-*` | Copiloto `executar` (aprovação a cada chamada) | linha `Fonte Notion: <url>` no payload → corpo da Issue |
| Enviar status report | conector Gmail (`create_draft`) | rascunho; o envio é do usuário |
| Fechamento | conector Notion (Master Index) | Issue, evidência, resultado, aprovação, próximo passo |

O papel do conector vem do secret `MCP_PAPEL` (padrão LEITOR). A URL do conector é credencial e não deve ser publicada neste repositório.

### Convenção de labels (decidida em 2026-09-26)
O Copiloto lê e escreve o schema aprovado em `.github/labels.yml` (`OPS_LABELS=copiloto-ops`). Não cria `state/*`.

| Copiloto | Neste repositório |
|---|---|
| fila / pronta | `state:planned`; pronta = DoD + dependências concluídas, calculado na leitura |
| fazendo | `state:structured` ou `state:implemented` |
| verificando | `state:produced` |
| concluída | `state:verified` + issue fechada |
| bloqueada | `status:blocked` |
| cancelada | issue fechada como not_planned |

- Issue nova nasce com `approval:pendente` + `gate:tbd`.
- `approval:*` nunca é alterada pelo Copiloto.
- `/ideia` é recusada (não há tipo aprovado para ideia); registre a ideia no Notion.
- As issues #9–#12 (padrão antigo `type/tarefa` + `state/backlog_validated`) continuam sendo lidas e migram para o schema aprovado na primeira transição.

### Lacunas antes de ativar a escrita (verificado em 2026-09-26)
- **Labels:** existe `type/tarefa`. Não existem `state/*` (usadas pela máquina de estados do Copiloto), `approval:pendente`, `approval:aprovado` nem `gate:tbd`. Além disso, o schema aprovado em `.github/labels.yml` usa outra convenção: `state:planned…verified` e `type:issue`, com dois-pontos. O Copiloto usa `state/ready`, `type/tarefa`, com barra. Convenção escolhida: o Copiloto usa o schema aprovado (tabela acima). As labels aprovadas ainda não existem no GitHub e são criadas na primeira escrita. Para aparecer nos relatórios, uma issue precisa de `type:issue` (ou `type:sub-issue`), um `state:*` e o bloco `task-spec`. Hoje só #9–#12 atendem. O GitHub cria labels ausentes na primeira escrita; por isso a escrita (`MCP_PAPEL=OPERADOR`) só deve ser ligada depois da decisão humana sobre o schema (regra 4 do AGENTS.md).
- **Dois modelos de estado (resolvido pela tabela acima):** o Copiloto usa `state/backlog_validated → ready → doing → verify → done` (mais `blocked` e `cancelado`). Já `docs/SCHEMA-TRABALHO.md` define `PLANNED → STRUCTURED → IMPLEMENTED → PRODUCED → VERIFIED` e títulos `[EPIC]`/`[ISSUE]`/`[SUB]`. A equivalência entre os dois é decisão pendente (registrar em 03 — ADRs).
- **Aprovação:** o Copiloto não aplica `approval:pendente` automaticamente; enquanto isso não mudar, a label é aplicada à mão.
