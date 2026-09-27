# Índice CMD-COP — IDs verbais, slash e módulos (fonte única)

**Base normativa:** CMD-COP-001, "Índice de Slash Commands e IDs Verbais". O texto original está preservado na §1, sem remoções nem renomeações.
**Extensão:** HANDOFF-AGENTES-001 §4 (Camadas 2 e 3) e ADR-0003.
**Regra de manutenção:** todo ID novo entra aqui **antes** de virar command, skill ou agente. IDs e slashes existentes nunca são removidos nem renomeados; legados viram aliases.
**Validação:** `python3 scripts/validar_plugin.py` confere unicidade, correspondência ID ↔ command e referências ao grafo.

Formato canônico das linhas de ID (lidas pelo validador): `CV-XXX-NNN — /comando — ação única`.

---

## 1. CMD-COP-001 (original, íntegro)

REGRA
O usuário pode operar por comando com barra ou por frase equivalente. O Orquestrador resolve o ID verbal e carrega somente o módulo necessário.

### Comandos de rotina
- CV-BOMDIA-001 — /bomdia — abrir o dia, validar continuidade e mostrar trabalho liberado.
- CV-AGORA-001 — /agora — mostrar somente o objeto atual, duração, DoD, evidência e próxima ação.
- CV-ESTADO-001 — /estado — mostrar progresso, Sprint/C72, Gate, bloqueios e estado atual.
- CV-FECHAR-001 — /fechardia — validar resultado, evidência, registrar transição e preparar continuidade.
- CV-REPLAN-001 — /replanejamento — recalcular apenas o trecho afetado por dependências, capacidade ou bloqueio.
- CV-MAPA-001 — /mapa — emitir MAPA-OS visual a partir da fonte canônica.
- CV-EVID-001 — /evidencia — consultar ou registrar evidência do objeto atual.
- CV-BLOQ-001 — /bloqueio — registrar impedimento ou consultar bloqueios ativos.

### Comandos de produtividade
- CV-ATUAL-001 — /atualizar — sincronização mínima de tarefas e contexto.
- CV-ATUAL-002 — /atualizar-abrangente — varredura profunda somente quando necessária.
- CV-CONTEXTO-001 — /contexto — recuperar contexto necessário ao objeto atual.
- CV-MEMORIA-001 — /memoria — consultar ou ajustar memória operacional.

### Comandos de operações
- CV-CAP-001 — /capacidade — planejar ou validar capacidade.
- CV-MUD-001 — /mudanca — estruturar mudança que afete escopo, processo ou sistema.
- CV-PROC-001 — /processo — documentar processo.
- CV-POP-001 — /procedimento — criar ou consultar procedimento operacional.
- CV-SIT-001 — /situacao — emitir situação operacional compacta.
- CV-FORN-001 — /fornecedor — avaliar fornecedor.
- CV-RISCO-001 — /risco — avaliar risco do objeto atual.
- CV-CONF-001 — /conformidade — validar critérios, normas e evidências.
- CV-OTIM-001 — /otimizar — reduzir desperdício, duplicação, espera e fricção do fluxo atual.

### Sinônimos verbais (originais)
- "Bom dia, copiloto" = /bomdia.
- "O que faço agora?" = /agora.
- "Como estamos?" = /estado.
- "Terminei por hoje" = /fechardia.
- "Preciso mudar o plano" = /replanejamento.
- "Me mostra o mapa" = /mapa.
- "Estou bloqueado" = /bloqueio.

### Regras de interação (originais, agora válidas para todo o plugin)
- Um comando deve produzir uma ação principal, não um relatório geral.
- O usuário não precisa informar o módulo.
- O usuário não precisa repetir IDs conhecidos quando o contexto atual for inequívoco.
- Se houver ambiguidade material entre dois objetos, o Orquestrador pede a mínima decisão necessária.
- Comandos antigos do legado podem ser aceitos como aliases, mas a interface preferida usa os comandos curtos deste índice.
- Todas as respostas visíveis em português do Brasil.

### Mapeamento do legado de operações (aliases)
- /planejar-capacidade → /capacidade.
- /solicitar-mudanca → /mudanca.
- /documentar-processo → /processo.
- /procedimento-operacional → /procedimento.
- /relatorio-situacao → /situacao.
- /avaliar-fornecedor → /fornecedor.

### Critério de aceite (original)
O operador deve conseguir conduzir o dia apenas com /bomdia, /agora, /estado, /fechardia e /replanejamento; os demais comandos são disclosure progressivo para situações específicas.

---

## 2. Extensão — Camada 2 (produto)
Termos "roadmap, spec, pesquisa" citados na Camada 2 do HANDOFF-AGENTES-001 §2.

- CV-ROADMAP-001 — /roadmap — atualizar, criar ou repriorizar o roadmap de produto.
- CV-SPEC-001 — /spec — escrever a spec/PRD de uma funcionalidade ou problema.
- CV-PESQ-001 — /pesquisa — sintetizar pesquisa com usuários (entrevistas, questionários, feedback) em insights.

Sinônimos:
- CV-ROADMAP-001: "Atualiza o roadmap"; "Repriorizar o roadmap"; "Como fica o roadmap com essa mudança?".
- CV-SPEC-001: "Escreve a spec disso"; "Transforma essa ideia em PRD"; "Preciso de um documento de requisitos".
- CV-PESQ-001: "Sintetiza essas entrevistas"; "Organiza esse feedback em insights"; "O que a pesquisa com usuários mostra?".

## 3. Extensão — Camada 3 (cadeia de valor proprietária)
- CV-DEPEND-001 — /dependencias — reconstruir a rede de dependências do Control Plane e entregar 16_REG, mapa e arquitetura de preenchimento.
- CV-ARVORE-001 — /arvore — converter um plano em árvore navegável a partir do estrutura.json.
- CV-VISUAL-001 — /arvore-visual — gerar a visualização Executar · Árvore Visual (JSON/HTML) de um plano ou projeto.
- CV-EDITORIAL-001 — /editorial — criar, continuar ou empacotar um ciclo editorial faseado no Obsidian.

Sinônimos:
- CV-DEPEND-001: "Reconstrói as dependências da planilha"; "Qual a ordem certa de preenchimento?"; "Monta o 16_REG_Dependencias".
- CV-ARVORE-001: "Transforma esse plano em árvore"; "Gera o kit da árvore"; "Quero esse plano em vault Obsidian".
- CV-VISUAL-001: "Mostra isso como árvore visual"; "Gera o HTML da árvore"; "Quero navegar esse projeto por ramos".
- CV-EDITORIAL-001: "Abre um ciclo editorial"; "Continua o job editorial"; "Empacota o handoff editorial".

Aliases de modo (IDs da própria skill `executar-arvore-roadmap`; resolvem para CV-ARVORE-001 com o modo como argumento):
- ARVORE-TXT-01 → /arvore txt.
- ARVORE-ZIP-02 → /arvore zip.
- ARVORE-OBSIDIAN-03 → /arvore obsidian.
- ARVORE-CSV-04 → /arvore csv.
- ARVOREKIT → /arvore kit.

---

## 4. Roteamento (ID → módulo → nó do grafo)
Proveniência do mapeamento pelo modelo epistêmico (`nucleo-dependencias.md` §1).

| ID | Slash | Módulo alvo | Nó | Proveniência | Visual | Busca web |
|---|---|---|---|---|---|---|
| CV-BOMDIA-001 | /bomdia | skill `copiloto-executar` | COPILOTO-EXECUTAR | DIRECT — a description da skill lista /bomdia | não | não |
| CV-AGORA-001 | /agora | skill `copiloto-executar` | COPILOTO-EXECUTAR | DIRECT — idem /agora | não | não |
| CV-ESTADO-001 | /estado | skill `copiloto-executar` | COPILOTO-EXECUTAR | DIRECT — idem /estado | não | não |
| CV-FECHAR-001 | /fechardia | skill `copiloto-executar` | COPILOTO-EXECUTAR | DIRECT — idem /fechardia | não | não |
| CV-REPLAN-001 | /replanejamento | skill `copiloto-executar` | COPILOTO-EXECUTAR | DIRECT — idem /replanejamento | não | não |
| CV-MAPA-001 | /mapa | skill `executar-mapa-os` | MAPA-OS | DERIVED — "emitir MAPA-OS" = objeto da skill executar-mapa-os | **sim** | não |
| CV-EVID-001 | /evidencia | skill `copiloto-executar` | COPILOTO-EXECUTAR | DERIVED — a skill cobre "registrar evidência" | não | não |
| CV-BLOQ-001 | /bloqueio | skill `copiloto-executar` | COPILOTO-EXECUTAR | DERIVED — a skill cobre "tratar bloqueio" | não | não |
| CV-ATUAL-001 | /atualizar | `productivity:update` | PRODUCTIVITY | DERIVED — seção "produtividade" + skill update (sync mínimo) | não | não |
| CV-ATUAL-002 | /atualizar-abrangente | `productivity:update --comprehensive` | PRODUCTIVITY | DERIVED — argumento `--comprehensive` da skill update | não | não |
| CV-CONTEXTO-001 | /contexto | `productivity:memory-management` | PRODUCTIVITY | DERIVED — memória de trabalho decodifica o contexto | não | não |
| CV-MEMORIA-001 | /memoria | `productivity:memory-management` | PRODUCTIVITY | DERIVED — "memória operacional" = skill memory-management | não | não |
| CV-CAP-001 | /capacidade | `operations:capacity-plan` | OPERATIONS | DIRECT — legado /planejar-capacidade | não | sim, se houver benchmark |
| CV-MUD-001 | /mudanca | `operations:change-request` | OPERATIONS | DIRECT — legado /solicitar-mudanca | não | sim, se houver referência externa |
| CV-PROC-001 | /processo | `operations:process-doc` | OPERATIONS | DIRECT — legado /documentar-processo | não | sim, se houver referência externa |
| CV-POP-001 | /procedimento | `operations:runbook` | OPERATIONS | DIRECT — legado /procedimento-operacional | não | sim, se houver referência externa |
| CV-SIT-001 | /situacao | `operations:status-report` | OPERATIONS | DIRECT — legado /relatorio-situacao | não | sim, se houver benchmark |
| CV-FORN-001 | /fornecedor | `operations:vendor-review` | OPERATIONS | DIRECT — legado /avaliar-fornecedor | não | **sim** (dados de mercado) |
| CV-RISCO-001 | /risco | `operations:risk-assessment` | OPERATIONS | DERIVED — seção "operações" + skill risk-assessment | não | sim, se houver fato externo |
| CV-CONF-001 | /conformidade | `operations:compliance-tracking` | OPERATIONS | DERIVED — "normas" = skill compliance-tracking | não | **sim** (normas vigentes) |
| CV-OTIM-001 | /otimizar | `operations:process-optimization` | OPERATIONS | DERIVED — "reduzir desperdício" = process-optimization | não | sim, se houver benchmark |
| CV-ROADMAP-001 | /roadmap | `product-management:roadmap-update` | PRODUCT-MANAGEMENT | DIRECT — handoff §2 "roadmap" | não | sim, se houver fato de mercado |
| CV-SPEC-001 | /spec | `product-management:write-spec` | PRODUCT-MANAGEMENT | DIRECT — handoff §2 "spec" | não | sim, se houver referência externa |
| CV-PESQ-001 | /pesquisa | `product-management:synthesize-research` | PRODUCT-MANAGEMENT | DIRECT — handoff §2 "pesquisa" | não | sim, se houver dado externo |
| CV-DEPEND-001 | /dependencias | `executar-cop:executar-dependency-architect` | DEPENDENCY-ARCHITECT | DIRECT — handoff §6 | não | sim, se houver referência externa |
| CV-ARVORE-001 | /arvore | `executar-cop:executar-arvore-roadmap` | ARVORE-ROADMAP | DIRECT — handoff §6 | não | sim, se houver fato externo |
| CV-VISUAL-001 | /arvore-visual | `executar-cop:executar-mergulhe` | ARVORE-VISUAL | DIRECT — handoff §6 | **sim** | sim, se houver fato externo |
| CV-EDITORIAL-001 | /editorial | `executar-cop:obsidian-editorial-pipeline` | EDITORIAL-OBSIDIAN | DIRECT — handoff §6 | **sim** | **sim** (evidências e fontes) |

## 5. Desambiguação (o Orquestrador pede a decisão mínima)
- "mapa" sozinho → /mapa (sinônimo original). "Mapa de dependências" → /dependencias (parte 2). "Árvore" ou "ramos" → /arvore-visual se o pedido for visual, /arvore se for texto, zip, CSV ou vault.
- "pesquisa" sobre usuários → /pesquisa. "Pesquisa na web" não é comando: é a busca web obrigatória das skills.
- "status" ou "situação" operacional → /situacao. "Como estamos?" → /estado.

## 6. Fora deste índice (sem fonte que os mapeie)
- Comandos do plugin `copiloto-operacional` (`/hoje`, `/fila`, `/feito`, `/progresso`, `/campanha`, `/status-report`) — outro plugin, em `Sas-Executar/executar-Blog`. Não viram aliases até que exista decisão registrada.
- IDs `OBS-*` pertencem à skill `obsidian-editorial` (formatação), **não** ao `obsidian-editorial-pipeline`; não são aliases de /editorial.
