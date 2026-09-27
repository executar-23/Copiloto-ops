# PF-24 — Rede de dependências do EXECUTAR HUB (CV-DEPEND-001)

**Especialista:** `executar-dependency-architect` (prompt mestre EXECUTAR-DEPENDENCY-ARCHITECT-001), plugin `executar-cop`.
**Fonte:** `EXECUTAR_HUB_Control_Plane_v2.xlsx` (sha256 `2de0a915cfa78170…`), com 37 abas, 37 artefatos, 1.125 campos, 13 macroáreas, 24 domínios e 12 Gates.
**Data:** 2026-09-27. **Rastreio:** [Issue #24](https://github.com/executar-23/Copiloto-ops/issues/24).
**Situação:** todas as linhas estão em `status = PROPOSED`, aguardando validação humana, na mesma convenção do 20_REG_Decisoes. A planilha não foi alterada.

## Pré-voo
`Pré-voo: prosseguir — planilha EXECUTAR_HUB_Control_Plane_v2.xlsx (sha256 2de0a915cfa7); abas obrigatórias ausentes: README_MASTER_INDEX_EXECUTAR.`

- **O que é o PF-24 nesta planilha.** É a "reconciliação cruzada depends_on/blocks entre áreas", registrada como ação NA-03 (origem: `EXECUTAR_CHECKLIST_D01-D23_GRANULAR.yaml#next_actions_register`). Ela não foi executada na fonte, e por isso existem o GAP-DEP-01 e o `06_Visao_Dependencias` vazio. **Esta entrega é a execução do PF-24** como engenharia formal de dependências.
- **Estado de partida:**
  - 16_REG_Dependencias vazio;
  - `depends_on`/`blocks` vazios nos 37 artefatos;
  - coluna Resposta vazia nos 1.125 campos (1.013 PROPOSED, 68 EXTERNAL_EVIDENCE, 40 DIRECT e 4 CONFLICT).
- **Método.** Cada dependência é demonstrada **campo a campo**: um campo do destino consome informação produzida por um campo da origem, e os dois `field_instance_id` são citados. Os 442 campos citados foram verificados contra o 15_REG (`analise_pf24.py`).
  - Como não há conteúdo preenchido, nenhuma relação é DIRECT (documentada). São 105 DERIVED e 7 PROPOSED.
- **Busca web:** não usada. A estrutura vem inteiramente da planilha e não havia referência externa a verificar.

---

## PARTE 1 — REGISTRO FORMAL DE DEPENDÊNCIAS

**112 linhas** prontas para o `16_REG_Dependencias`: 53 bloqueantes (`mandatory TRUE`) e 59 informativas (`FALSE`). Como o 16_REG está vazio, `registro_para_colar.csv` é igual a `registro.csv`.

- **Leitura:** o target depende do source, ou seja, o source precisa existir primeiro.
- **Valores escolhidos (GAP-DEP-A: o domínio não está definido na planilha):**
  - `relation = depends_on`: vem das colunas `depends_on`/`blocks` do 14_REG;
  - `required_status = APPROVED`: vem de `17_REG_Gates.required_statuses`;
  - `status = PROPOSED`: convenção do 20_REG para itens que aguardam validação humana.
- **`gate_id`:** é o Gate que certifica a origem. É PROPOSED, porque o 17_REG não declara `required_artifact_types` (GAP-DEP-B). As três arestas A02 → A04 usam G03 DEVELOPMENT_READY, porque cruzam a transição A03.
- **Arquivo complementar:** `14_REG_depends_on_blocks.csv` traz as colunas `depends_on`/`blocks` de cada artefato (só bloqueantes), no formato JSON do 14_REG.

| dependency_id | source_artifact_id | target_artifact_id | relation | mandatory | gate_id | required_status | status |
|---|---|---|---|---|---|---|---|
| DEP-001 | D01-DOC-DDE-001 | D01-DOC-TAP-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-002 | D01-DOC-DDE-001 | D01-DOC-MNE-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-003 | D01-DOC-DDE-001 | D01-DOC-MRE-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-004 | D01-DOC-MNE-001 | D01-DOC-MRE-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-005 | D01-DOC-DDE-001 | D02-DOC-DGRC-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-006 | D02-DOC-DGRC-001 | D02-DOC-MRC-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-007 | D01-DOC-DDE-001 | D02-DOC-MRC-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-008 | D01-DOC-TAP-001 | D02-DOC-MRC-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-009 | D01-DOC-MNE-001 | D03-DOC-MFO-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-010 | D03-DOC-MFO-001 | D01-DOC-MNE-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-011 | D01-DOC-MNE-001 | D03-DOC-PFO-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-012 | D03-DOC-MFO-001 | D03-DOC-PFO-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-013 | D03-DOC-PFO-001 | D03-DOC-MFO-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-014 | D01-DOC-TAP-001 | D03-DOC-PFO-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-015 | D01-DOC-DDE-001 | D04-DOC-PPC-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-016 | D03-DOC-PFO-001 | D04-DOC-PPC-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-017 | D01-DOC-TAP-001 | D07-DOC-PEX-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-018 | D04-DOC-PPC-001 | D07-DOC-PEX-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-019 | D07-DOC-PEX-001 | D04-DOC-PPC-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-020 | D01-DOC-DDE-001 | D07-DOC-PEX-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-021 | D01-DOC-MNE-001 | D13-DOC-DRM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-022 | D09-DOC-DEB-001 | D13-DOC-DRM-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-023 | D01-DOC-MNE-001 | D09-DOC-PPE-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-024 | D09-DOC-DEB-001 | D09-DOC-PPE-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-025 | D01-DOC-DDE-001 | D10-DOC-DRP-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-026 | D01-DOC-MNE-001 | D10-DOC-DRP-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-027 | D13-DOC-DRM-001 | D10-DOC-DRP-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-028 | D09-DOC-DEB-001 | D10-DOC-DRP-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-029 | D09-DOC-PPE-001 | D10-DOC-DRP-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-030 | D10-DOC-DRP-001 | D11-DOC-EEP-001 | depends_on | TRUE | G02 | APPROVED | PROPOSED |
| DEP-031 | D11-DOC-EEP-001 | D10-DOC-DRP-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-032 | D11-DOC-DSI-001 | D11-DOC-EEP-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-033 | D01-DOC-DDE-001 | D11-DOC-DSI-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-034 | D10-DOC-DRP-001 | D10-DOC-PRD-001 | depends_on | TRUE | G02 | APPROVED | PROPOSED |
| DEP-035 | D11-DOC-EEP-001 | D10-DOC-PRD-001 | depends_on | TRUE | G02 | APPROVED | PROPOSED |
| DEP-036 | D02-DOC-DGRC-001 | D10-DOC-PRD-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-037 | D05-DOC-DCM-001 | D10-DOC-PRD-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-038 | D10-DOC-PRD-001 | D12-DOC-ETE-001 | depends_on | TRUE | G03 | APPROVED | PROPOSED |
| DEP-039 | D11-DOC-DSI-001 | D12-DOC-ETE-001 | depends_on | TRUE | G03 | APPROVED | PROPOSED |
| DEP-040 | D11-DOC-EEP-001 | D12-DOC-ETE-001 | depends_on | FALSE | G03 | APPROVED | PROPOSED |
| DEP-041 | D20-DOC-PPR-001 | D12-DOC-ETE-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-042 | D05-DOC-EPGD-001 | D12-DOC-ETE-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-043 | D22-DOC-DRL-001 | D12-DOC-ETE-001 | depends_on | FALSE | G11 | APPROVED | PROPOSED |
| DEP-044 | D01-DOC-DDE-001 | D20-DOC-PPR-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-045 | D02-DOC-DGRC-001 | D20-DOC-PPR-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-046 | D20-DOC-PPR-001 | D05-DOC-EPGD-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-047 | D02-DOC-DGRC-001 | D05-DOC-EPGD-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-048 | D05-DOC-EPGD-001 | D02-DOC-DGRC-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-049 | D05-DOC-EPGD-001 | D05-DOC-DCM-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-050 | D01-DOC-DDE-001 | D05-DOC-DCM-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-051 | D02-DOC-DGRC-001 | D02-DOC-PPT-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-052 | D05-DOC-EPGD-001 | D02-DOC-PPT-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-053 | D20-DOC-PPR-001 | D02-DOC-PPT-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-054 | D05-DOC-DCM-001 | D02-DOC-PPT-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-055 | D12-DOC-ETE-001 | D18-DOC-PCE-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-056 | D05-DOC-EPGD-001 | D18-DOC-PCE-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-057 | D02-DOC-DGRC-001 | D18-DOC-PCE-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-058 | D06-DOC-EGC-001 | D18-DOC-PCE-001 | depends_on | FALSE | G11 | APPROVED | PROPOSED |
| DEP-059 | D05-DOC-DCM-001 | D18-DOC-PCE-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-060 | D01-DOC-MRE-001 | D18-DOC-PCE-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-061 | D10-DOC-PRD-001 | D23-DOC-PBL-001 | depends_on | TRUE | G02 | APPROVED | PROPOSED |
| DEP-062 | D12-DOC-ETE-001 | D23-DOC-PBL-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-063 | D18-DOC-PCE-001 | D23-DOC-PBL-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-064 | D11-DOC-EEP-001 | D23-DOC-PBL-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-065 | D07-DOC-PEX-001 | D07-DOC-PIM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-066 | D12-DOC-ETE-001 | D07-DOC-PIM-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-067 | D01-DOC-TAP-001 | D07-DOC-PIM-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-068 | D18-DOC-PCE-001 | D07-DOC-PIM-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-069 | D01-DOC-MNE-001 | D08-DOC-MOP-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-070 | D04-DOC-PPC-001 | D08-DOC-MOP-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-071 | D02-DOC-DGRC-001 | D08-DOC-MOP-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-072 | D08-DOC-MOP-001 | D08-DOC-RUN-001 | depends_on | TRUE | G06 | APPROVED | PROPOSED |
| DEP-073 | D20-DOC-PPR-001 | D08-DOC-RUN-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-074 | D12-DOC-ETE-001 | D08-DOC-RUN-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-075 | D13-DOC-DRM-001 | D14-DOC-PCV-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-076 | D03-DOC-PFO-001 | D14-DOC-PCV-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-077 | D01-DOC-MNE-001 | D14-DOC-PCV-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-078 | D14-DOC-PCV-001 | D03-DOC-PFO-001 | depends_on | FALSE | G08 | APPROVED | PROPOSED |
| DEP-079 | D20-DOC-PPR-001 | D14-DOC-PCV-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-080 | D14-DOC-PCV-001 | D15-DOC-PASC-001 | depends_on | FALSE | G08 | APPROVED | PROPOSED |
| DEP-081 | D01-DOC-MNE-001 | D15-DOC-PASC-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-082 | D08-DOC-MOP-001 | D15-DOC-PASC-001 | depends_on | FALSE | G06 | APPROVED | PROPOSED |
| DEP-083 | D10-DOC-PRD-001 | D15-DOC-PASC-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-084 | D15-DOC-PASC-001 | D03-DOC-MFO-001 | depends_on | FALSE | G07 | APPROVED | PROPOSED |
| DEP-085 | D13-DOC-DRM-001 | D13-DOC-GTM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-086 | D03-DOC-PFO-001 | D13-DOC-GTM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-087 | D10-DOC-PRD-001 | D13-DOC-GTM-001 | depends_on | TRUE | G02 | APPROVED | PROPOSED |
| DEP-088 | D07-DOC-PIM-001 | D13-DOC-GTM-001 | depends_on | TRUE | G05 | APPROVED | PROPOSED |
| DEP-089 | D15-DOC-PASC-001 | D13-DOC-GTM-001 | depends_on | TRUE | G07 | APPROVED | PROPOSED |
| DEP-090 | D13-DOC-GTM-001 | D14-DOC-PCV-001 | depends_on | FALSE | G08 | APPROVED | PROPOSED |
| DEP-091 | D05-DOC-DCM-001 | D13-DOC-GTM-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-092 | D13-DOC-GTM-001 | D19-DOC-PAC-001 | depends_on | TRUE | G08 | APPROVED | PROPOSED |
| DEP-093 | D20-DOC-PPR-001 | D19-DOC-PAC-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-094 | D11-DOC-DSI-001 | D19-DOC-PAC-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-095 | D05-DOC-DCM-001 | D19-DOC-PAC-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-096 | D13-DOC-DRM-001 | D16-DOC-PEM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-097 | D09-DOC-DEB-001 | D16-DOC-PEM-001 | depends_on | TRUE | G01 | APPROVED | PROPOSED |
| DEP-098 | D19-DOC-PAC-001 | D16-DOC-PEM-001 | depends_on | TRUE | G08 | APPROVED | PROPOSED |
| DEP-099 | D13-DOC-GTM-001 | D16-DOC-PEM-001 | depends_on | FALSE | G08 | APPROVED | PROPOSED |
| DEP-100 | D11-DOC-DSI-001 | D16-DOC-PEM-001 | depends_on | FALSE | G02 | APPROVED | PROPOSED |
| DEP-101 | D05-DOC-DCM-001 | D16-DOC-PEM-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-102 | D01-DOC-DDE-001 | D17-DOC-PEP-001 | depends_on | FALSE | G00 | APPROVED | PROPOSED |
| DEP-103 | D09-DOC-DEB-001 | D17-DOC-PEP-001 | depends_on | FALSE | G01 | APPROVED | PROPOSED |
| DEP-104 | D19-DOC-PAC-001 | D17-DOC-PEP-001 | depends_on | FALSE | G08 | APPROVED | PROPOSED |
| DEP-105 | D06-DOC-EGC-001 | D06-DOC-RMI-001 | depends_on | TRUE | G11 | APPROVED | PROPOSED |
| DEP-106 | D20-DOC-PPR-001 | D06-DOC-RMI-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-107 | D20-DOC-PPR-001 | D06-DOC-EGC-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-108 | D01-DOC-DDE-001 | D22-DOC-DRL-001 | depends_on | TRUE | G00 | APPROVED | PROPOSED |
| DEP-109 | D06-DOC-EGC-001 | D22-DOC-DRL-001 | depends_on | FALSE | G11 | APPROVED | PROPOSED |
| DEP-110 | D05-DOC-DCM-001 | D21-DOC-PWB-001 | depends_on | TRUE | G04 | APPROVED | PROPOSED |
| DEP-111 | D05-DOC-EPGD-001 | D21-DOC-PWB-001 | depends_on | FALSE | G04 | APPROVED | PROPOSED |
| DEP-112 | D06-DOC-EGC-001 | D21-DOC-PWB-001 | depends_on | FALSE | G11 | APPROVED | PROPOSED |

---

## PARTE 2 — MAPA DE DEPENDÊNCIAS
Cadeia **origem → destino → motivo → Gate → impacto**, agrupada pelo Gate da aresta. O motivo mostra o primeiro par de campos; a lista completa está no `anexo.csv`.

### G00 INITIATIVE_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-001 | D01-DOC-DDE-001 | D01-DOC-TAP-001 | O termo de abertura operacionaliza a direção estratégica: `OBJECTIVE.OBJETIVO_GERAL ← STRATEGIC_DIRECTION.OBJETIVOS_ESTRATEGICOS` (+2) | G00 | D01-DOC-TAP-001 não pode fechar os campos consumidores (29 campos no artefato) | DERIVED | sim |
| DEP-002 | D01-DOC-DDE-001 | D01-DOC-MNE-001 | O modelo de negócio parte do problema e do portfólio declarados na direção: `CUSTOMER.PROBLEMAS ← PROBLEM_AND_OPPORTUNITY.PROBLEMA_CENTRAL` (+2) | G00 | D01-DOC-MNE-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-003 | D01-DOC-DDE-001 | D01-DOC-MRE-001 | Os nós do mapa de relações são os componentes do ecossistema: `NODES.PRODUTOS ← ECOSYSTEM.PRODUTOS` (+3) | G00 | D01-DOC-MRE-001 não pode fechar os campos consumidores (23 campos no artefato) | DERIVED | sim |
| DEP-005 | D01-DOC-DDE-001 | D02-DOC-DGRC-001 | Papéis e autoridades jurídicas seguem o modelo de governança: `GOVERNANCE.PAPEIS ← GOVERNANCE.PAPEIS_DECISORIOS` (+2) | G00 | D02-DOC-DGRC-001 não pode fechar os campos consumidores (33 campos no artefato) | DERIVED | sim |
| DEP-007 | D01-DOC-DDE-001 | D02-DOC-MRC-001 | Riscos estratégicos entram como eventos de risco: `SCHEMA.EVENTO_DE_RISCO ← RISKS.RISCOS_ESTRATEGICOS` | G00 | D02-DOC-MRC-001 segue com premissa; revisar quando D01-DOC-DDE-001 for aprovado | DERIVED | não |
| DEP-008 | D01-DOC-TAP-001 | D02-DOC-MRC-001 | Riscos iniciais do projeto entram como eventos de risco: `SCHEMA.EVENTO_DE_RISCO ← RISKS.RISCOS_INICIAIS` | G00 | D02-DOC-MRC-001 segue com premissa; revisar quando D01-DOC-TAP-001 for aprovado | DERIVED | não |
| DEP-014 | D01-DOC-TAP-001 | D03-DOC-PFO-001 | Orçamento do termo de abertura baliza o limite do plano: `BUDGET.LIMITE ← RESOURCES.ORCAMENTO` | G00 | D03-DOC-PFO-001 segue com premissa; revisar quando D01-DOC-TAP-001 for aprovado | DERIVED | não |
| DEP-015 | D01-DOC-DDE-001 | D04-DOC-PPC-001 | Estrutura e autoridade de pessoas seguem o modelo de governança: `ROLES.AUTORIDADE ← GOVERNANCE.DIREITOS_DE_DECISAO` (+1) | G00 | D04-DOC-PPC-001 não pode fechar os campos consumidores (39 campos no artefato) | DERIVED | sim |
| DEP-017 | D01-DOC-TAP-001 | D07-DOC-PEX-001 | Objetivos, entregáveis e DoD da execução vêm do termo de abertura: `OBJECTIVES.OBJETIVO ← OBJECTIVE.OBJETIVOS_ESPECIFICOS` (+2) | G00 | D07-DOC-PEX-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-020 | D01-DOC-DDE-001 | D07-DOC-PEX-001 | Gates da execução referenciam os gates da governança: `GATES.GATE ← GOVERNANCE.GATES` | G00 | D07-DOC-PEX-001 segue com premissa; revisar quando D01-DOC-DDE-001 for aprovado | DERIVED | não |
| DEP-025 | D01-DOC-DDE-001 | D10-DOC-DRP-001 | O problema do produto é o problema central declarado: `PROBLEM.PROBLEMA ← PROBLEM_AND_OPPORTUNITY.PROBLEMA_CENTRAL` (+1) | G00 | D10-DOC-DRP-001 não pode fechar os campos consumidores (28 campos no artefato) | DERIVED | sim |
| DEP-033 | D01-DOC-DDE-001 | D11-DOC-DSI-001 | Princípios do design system derivam dos princípios do ecossistema: `FOUNDATIONS.PRINCIPIOS ← PURPOSE.PRINCIPIOS` | G00 | D11-DOC-DSI-001 segue com premissa; revisar quando D01-DOC-DDE-001 for aprovado | DERIVED | não |
| DEP-044 | D01-DOC-DDE-001 | D20-DOC-PPR-001 | O inventário de plataformas parte das plataformas declaradas no ecossistema: `SYSTEMS.PLATAFORMA ← ECOSYSTEM.PLATAFORMAS` (+1) | G00 | D20-DOC-PPR-001 não pode fechar os campos consumidores (39 campos no artefato) | DERIVED | sim |
| DEP-050 | D01-DOC-DDE-001 | D05-DOC-DCM-001 | Indicadores estratégicos entram no catálogo de métricas: `SCHEMA.NOME ← MEASUREMENT.INDICADORES` | G00 | D05-DOC-DCM-001 segue com premissa; revisar quando D01-DOC-DDE-001 for aprovado | DERIVED | não |
| DEP-067 | D01-DOC-TAP-001 | D07-DOC-PIM-001 | Marcos da implementação partem dos marcos do termo (campo em CONFLICT: D22-DEC-CFL-02): `MILESTONES.MARCO ← MILESTONES.MARCOS` | G00 | D07-DOC-PIM-001 segue com premissa; revisar quando D01-DOC-TAP-001 for aprovado | DERIVED | não |
| DEP-102 | D01-DOC-DDE-001 | D17-DOC-PEP-001 | Inventário de portfólio profissional cita os produtos do ecossistema: `PORTFOLIO_INVENTORY.PROJETO ← ECOSYSTEM.PRODUTOS` | G00 | D17-DOC-PEP-001 segue com premissa; revisar quando D01-DOC-DDE-001 for aprovado | DERIVED | não |
| DEP-108 | D01-DOC-DDE-001 | D22-DOC-DRL-001 | O log de decisões nasce das decisões vigentes e pendentes: `SCHEMA.DECISION_ID ← DECISIONS.DECISOES_VIGENTES` (+1) | G00 | D22-DOC-DRL-001 não pode fechar os campos consumidores (23 campos no artefato) | DERIVED | sim |

### G01 BUSINESS_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-004 | D01-DOC-MNE-001 | D01-DOC-MRE-001 | Fluxos de valor e comerciais vêm do modelo de negócio: `FLOWS.FLUXO_COMERCIAL ← CHANNELS.DISTRIBUICAO` (+1) | G01 | D01-DOC-MRE-001 segue com premissa; revisar quando D01-DOC-MNE-001 for aprovado | DERIVED | não |
| DEP-006 | D02-DOC-DGRC-001 | D02-DOC-MRC-001 | A matriz detalha riscos, controles e owners definidos na governança: `SCHEMA.CATEGORIA ← RISK_MANAGEMENT.RISCOS` (+2) | G01 | D02-DOC-MRC-001 não pode fechar os campos consumidores (18 campos no artefato) | DERIVED | sim |
| DEP-009 | D01-DOC-MNE-001 | D03-DOC-MFO-001 | O modelo financeiro precifica os produtos e custos do modelo de negócio: `REVENUE_MODEL.PRODUTO ← OFFERINGS.PRODUTOS` (+2) | G01 | D03-DOC-MFO-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-010 | D03-DOC-MFO-001 | D01-DOC-MNE-001 | Economia unitária do MNE resume o modelo financeiro (informativa: quebra o ciclo MNE↔MFO): `ECONOMICS.MARGEM ← UNIT_ECONOMICS.MARGEM` (+3) | G01 | D01-DOC-MNE-001 segue com premissa; revisar quando D03-DOC-MFO-001 for aprovado | PROPOSED | não |
| DEP-011 | D01-DOC-MNE-001 | D03-DOC-PFO-001 | Receitas, preços e custos do plano vêm do modelo de negócio: `REVENUE.FONTES ← REVENUE.FONTES_DE_RECEITA` (+2) | G01 | D03-DOC-PFO-001 não pode fechar os campos consumidores (38 campos no artefato) | DERIVED | sim |
| DEP-012 | D03-DOC-MFO-001 | D03-DOC-PFO-001 | Previsões, cenários e margem do plano são projeções do modelo: `REVENUE.PREVISOES ← REVENUE_MODEL.VOLUME` (+2) | G01 | D03-DOC-PFO-001 não pode fechar os campos consumidores (38 campos no artefato) | DERIVED | sim |
| DEP-013 | D03-DOC-PFO-001 | D03-DOC-MFO-001 | Premissas gerais (período, moeda) do plano calibram o modelo (informativa: quebra o ciclo MFO↔PFO): `MODEL_INPUTS.PREMISSAS ← ASSUMPTIONS.PREMISSAS_FINANCEIRAS` | G01 | D03-DOC-MFO-001 segue com premissa; revisar quando D03-DOC-PFO-001 for aprovado | PROPOSED | não |
| DEP-016 | D03-DOC-PFO-001 | D04-DOC-PPC-001 | Contratações dependem do orçamento por área: `HIRING.NECESSIDADES_FUTURAS ← BUDGET.ORCAMENTO_POR_AREA` | G01 | D04-DOC-PPC-001 segue com premissa; revisar quando D03-DOC-PFO-001 for aprovado | DERIVED | não |
| DEP-018 | D04-DOC-PPC-001 | D07-DOC-PEX-001 | Capacidade da execução é a capacidade de pessoas: `CAPACITY.CAPACIDADE_BRUTA ← CAPACITY.HORAS_DISPONIVEIS` (+1) | G01 | D07-DOC-PEX-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-019 | D07-DOC-PEX-001 | D04-DOC-PPC-001 | Demanda de trabalho alimenta a carga de pessoas (informativa: quebra o ciclo PPC↔PEX): `WORKLOAD.DEMANDA ← BACKLOG.ITEM` | G01 | D04-DOC-PPC-001 segue com premissa; revisar quando D07-DOC-PEX-001 for aprovado | PROPOSED | não |
| DEP-021 | D01-DOC-MNE-001 | D13-DOC-DRM-001 | Segmentos, alternativas e diferenciação de mercado partem do modelo de negócio: `SEGMENTS.SEGMENTO ← CUSTOMER.SEGMENTOS` (+2) | G01 | D13-DOC-DRM-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-022 | D09-DOC-DEB-001 | D13-DOC-DRM-001 | Evidências de mercado citam o dossiê de evidências: `EVIDENCE.ESTUDOS ← SCHEMA.CLAIM` (+1) | G01 | D13-DOC-DRM-001 segue com premissa; revisar quando D09-DOC-DEB-001 for aprovado | DERIVED | não |
| DEP-023 | D01-DOC-MNE-001 | D09-DOC-PPE-001 | Experimentos testam as hipóteses do modelo de negócio: `HYPOTHESIS.HIPOTESE ← ASSUMPTIONS.HIPOTESES` (+1) | G01 | D09-DOC-PPE-001 não pode fechar os campos consumidores (24 campos no artefato) | DERIVED | sim |
| DEP-024 | D09-DOC-DEB-001 | D09-DOC-PPE-001 | Revisão de evidências parte do dossiê existente: `EVIDENCE_REVIEW.FONTES_EXISTENTES ← SCHEMA.SOURCE_ID` (+1) | G01 | D09-DOC-PPE-001 segue com premissa; revisar quando D09-DOC-DEB-001 for aprovado | DERIVED | não |
| DEP-026 | D01-DOC-MNE-001 | D10-DOC-DRP-001 | JTBD, proposta de valor e clientes do produto vêm do modelo de negócio: `JTBD.TRABALHO ← CUSTOMER.JTBD` (+2) | G01 | D10-DOC-DRP-001 não pode fechar os campos consumidores (28 campos no artefato) | DERIVED | sim |
| DEP-027 | D13-DOC-DRM-001 | D10-DOC-DRP-001 | O ICP e os usuários do produto são os definidos no mercado: `AUDIENCE.ICP ← ICP.PERFIL` (+1) | G01 | D10-DOC-DRP-001 não pode fechar os campos consumidores (28 campos no artefato) | DERIVED | sim |
| DEP-028 | D09-DOC-DEB-001 | D10-DOC-DRP-001 | A evidência do problema cita o dossiê: `PROBLEM.EVIDENCIA ← SCHEMA.FINDING` | G01 | D10-DOC-DRP-001 segue com premissa; revisar quando D09-DOC-DEB-001 for aprovado | DERIVED | não |
| DEP-029 | D09-DOC-PPE-001 | D10-DOC-DRP-001 | Decisões de experimentos ajustam o escopo: `SCOPE.INCLUIDO ← DECISION.DECISAO_DERIVADA` | G01 | D10-DOC-DRP-001 segue com premissa; revisar quando D09-DOC-PPE-001 for aprovado | DERIVED | não |
| DEP-036 | D02-DOC-DGRC-001 | D10-DOC-PRD-001 | Requisitos de privacidade e segurança citam bases legais e controles: `SCHEMA.PRIVACY ← PRIVACY.BASES_LEGAIS` (+1) | G01 | D10-DOC-PRD-001 segue com premissa; revisar quando D02-DOC-DGRC-001 for aprovado | DERIVED | não |
| DEP-045 | D02-DOC-DGRC-001 | D20-DOC-PPR-001 | Permissões seguem os controles de conformidade: `PERMISSIONS.ACESSO ← COMPLIANCE.CONTROLES` | G01 | D20-DOC-PPR-001 segue com premissa; revisar quando D02-DOC-DGRC-001 for aprovado | DERIVED | não |
| DEP-047 | D02-DOC-DGRC-001 | D05-DOC-EPGD-001 | Finalidade, retenção e acesso a dados seguem o enquadramento jurídico: `PRIVACY.FINALIDADE ← PRIVACY.FINALIDADES` (+2) | G01 | D05-DOC-EPGD-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-051 | D02-DOC-DGRC-001 | D02-DOC-PPT-001 | Bases legais, retenção e direitos da política vêm da governança jurídica: `PURPOSES.BASE_LEGAL ← PRIVACY.BASES_LEGAIS` (+2) | G01 | D02-DOC-PPT-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-057 | D02-DOC-DGRC-001 | D18-DOC-PCE-001 | Inventário de contratos inclui os contratos jurídicos: `CONTRACT_INVENTORY.CONTRATO ← CONTRACTS.CONTRATOS_EXISTENTES` | G01 | D18-DOC-PCE-001 segue com premissa; revisar quando D02-DOC-DGRC-001 for aprovado | DERIVED | não |
| DEP-060 | D01-DOC-MRE-001 | D18-DOC-PCE-001 | Contratos de handoff formalizam os handoffs do mapa de relações: `HANDOFF_CONTRACTS.ORIGEM ← INTERFACES.HANDOFFS` | G01 | D18-DOC-PCE-001 segue com premissa; revisar quando D01-DOC-MRE-001 for aprovado | DERIVED | não |
| DEP-065 | D07-DOC-PEX-001 | D07-DOC-PIM-001 | Pacotes, gates e recursos da implementação vêm do plano de execução: `WORK_PACKAGES.ENTREGAVEL ← DELIVERABLES.ENTREGAVEL` (+2) | G01 | D07-DOC-PIM-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-069 | D01-DOC-MNE-001 | D08-DOC-MOP-001 | Serviços e processos operados são os do modelo de negócio: `OPERATING_MODEL.SERVICOS ← OFFERINGS.SERVICOS` (+1) | G01 | D08-DOC-MOP-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-070 | D04-DOC-PPC-001 | D08-DOC-MOP-001 | Executores dos processos são papéis definidos em pessoas: `ROLES.EXECUTOR ← ROLES.PAPEL` | G01 | D08-DOC-MOP-001 segue com premissa; revisar quando D04-DOC-PPC-001 for aprovado | DERIVED | não |
| DEP-071 | D02-DOC-DGRC-001 | D08-DOC-MOP-001 | Controles operacionais implementam controles de conformidade: `CONTROLS.CONTROLE ← COMPLIANCE.CONTROLES` | G01 | D08-DOC-MOP-001 segue com premissa; revisar quando D02-DOC-DGRC-001 for aprovado | DERIVED | não |
| DEP-075 | D13-DOC-DRM-001 | D14-DOC-PCV-001 | ICP, qualificação e objeções de vendas vêm do mercado: `CUSTOMER.ICP ← ICP.PERFIL` (+2) | G01 | D14-DOC-PCV-001 não pode fechar os campos consumidores (39 campos no artefato) | DERIVED | sim |
| DEP-076 | D03-DOC-PFO-001 | D14-DOC-PCV-001 | Preço, desconto e quota vêm do plano financeiro (valor em CONFLICT: D22-DEC-CFL-03): `PRICING.PRECO ← PRICING.PRECOS` (+2) | G01 | D14-DOC-PCV-001 não pode fechar os campos consumidores (39 campos no artefato) | DERIVED | sim |
| DEP-077 | D01-DOC-MNE-001 | D14-DOC-PCV-001 | Pacotes de venda seguem os planos do modelo de negócio: `OFFERS.PACOTE ← OFFERINGS.PLANOS` | G01 | D14-DOC-PCV-001 segue com premissa; revisar quando D01-DOC-MNE-001 for aprovado | DERIVED | não |
| DEP-081 | D01-DOC-MNE-001 | D15-DOC-PASC-001 | O modelo de atendimento segue relacionamento e suporte do modelo de negócio: `SERVICE_MODEL.MODELO ← RELATIONSHIPS.RELACIONAMENTO_COM_CLIENTE` (+1) | G01 | D15-DOC-PASC-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-085 | D13-DOC-DRM-001 | D13-DOC-GTM-001 | ICP, posicionamento e mensagem de lançamento vêm do mercado: `AUDIENCE.ICP ← ICP.PERFIL` (+2) | G01 | D13-DOC-GTM-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-086 | D03-DOC-PFO-001 | D13-DOC-GTM-001 | Preço da oferta e investimento do lançamento vêm do plano financeiro: `OFFER.PRECO ← PRICING.PRECOS` (+1) | G01 | D13-DOC-GTM-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-096 | D13-DOC-DRM-001 | D16-DOC-PEM-001 | Públicos e teses editoriais vêm do mercado: `AUDIENCE.PUBLICOS ← SEGMENTS.SEGMENTO` (+1) | G01 | D16-DOC-PEM-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-097 | D09-DOC-DEB-001 | D16-DOC-PEM-001 | Claims publicados exigem evidência no dossiê: `BRAND_COMPLIANCE.CLAIMS ← SCHEMA.CLAIM` (+1) | G01 | D16-DOC-PEM-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-103 | D09-DOC-DEB-001 | D17-DOC-PEP-001 | Evidências de cases citam o dossiê: `CASE_STUDIES.EVIDENCIA ← SCHEMA.CITATION` | G01 | D17-DOC-PEP-001 segue com premissa; revisar quando D09-DOC-DEB-001 for aprovado | DERIVED | não |

### G02 PRODUCT_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-030 | D10-DOC-DRP-001 | D11-DOC-EEP-001 | Jornadas e personas da experiência detalham as do produto: `JOURNEYS.ETAPA ← JOURNEYS.JORNADAS` (+2) | G02 | D11-DOC-EEP-001 não pode fechar os campos consumidores (31 campos no artefato) | DERIVED | sim |
| DEP-031 | D11-DOC-EEP-001 | D10-DOC-DRP-001 | Pesquisa de usuários refina as jornadas do produto (informativa: quebra o ciclo DRP↔EEP): `JOURNEYS.JORNADAS ← USER_RESEARCH.NECESSIDADES` | G02 | D10-DOC-DRP-001 segue com premissa; revisar quando D11-DOC-EEP-001 for aprovado | PROPOSED | não |
| DEP-032 | D11-DOC-DSI-001 | D11-DOC-EEP-001 | Microcopy e feedback usam voz e padrões do design system: `CONTENT.MICROCOPY ← CONTENT_DESIGN.VOZ` (+1) | G02 | D11-DOC-EEP-001 segue com premissa; revisar quando D11-DOC-DSI-001 for aprovado | DERIVED | não |
| DEP-034 | D10-DOC-DRP-001 | D10-DOC-PRD-001 | Os requisitos integrados por produto detalham o documento de requisitos: `SCHEMA.PROBLEM ← PROBLEM.PROBLEMA` (+5) | G02 | D10-DOC-PRD-001 não pode fechar os campos consumidores (23 campos no artefato) | DERIVED | sim |
| DEP-035 | D11-DOC-EEP-001 | D10-DOC-PRD-001 | Fluxos, estados e acessibilidade por produto vêm da especificação de experiência: `SCHEMA.USER_FLOWS ← FLOWS.DECISAO` (+2) | G02 | D10-DOC-PRD-001 não pode fechar os campos consumidores (23 campos no artefato) | DERIVED | sim |
| DEP-061 | D10-DOC-PRD-001 | D23-DOC-PBL-001 | Problema, escopo e aceite do blueprint vêm dos requisitos integrados: `PROBLEM.PROBLEMA ← SCHEMA.PROBLEM` (+2) | G02 | D23-DOC-PBL-001 não pode fechar os campos consumidores (40 campos no artefato) | DERIVED | sim |
| DEP-064 | D11-DOC-EEP-001 | D23-DOC-PBL-001 | Fluxo de usuário do blueprint segue as jornadas: `USER_FLOW.ACAO ← JOURNEYS.ACAO` | G02 | D23-DOC-PBL-001 segue com premissa; revisar quando D11-DOC-EEP-001 for aprovado | DERIVED | não |
| DEP-083 | D10-DOC-PRD-001 | D15-DOC-PASC-001 | Base de conhecimento cobre os casos de uso do produto: `KNOWLEDGE_BASE.ARTIGOS ← SCHEMA.USE_CASES` | G02 | D15-DOC-PASC-001 segue com premissa; revisar quando D10-DOC-PRD-001 for aprovado | DERIVED | não |
| DEP-087 | D10-DOC-PRD-001 | D13-DOC-GTM-001 | Produto ofertado e objetivo do lançamento vêm dos requisitos integrados: `OFFER.PRODUTO ← SCHEMA.PRODUCT_NAME` (+1) | G02 | D13-DOC-GTM-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-094 | D11-DOC-DSI-001 | D19-DOC-PAC-001 | Visual e legibilidade dos assets seguem o design system: `CONTENT.VISUAL ← TOKENS.COR` (+1) | G02 | D19-DOC-PAC-001 segue com premissa; revisar quando D11-DOC-DSI-001 for aprovado | DERIVED | não |
| DEP-100 | D11-DOC-DSI-001 | D16-DOC-PEM-001 | Voz e visual de marca seguem o design system: `BRAND_COMPLIANCE.VISUAL ← TOKENS.COR` (+1) | G02 | D16-DOC-PEM-001 segue com premissa; revisar quando D11-DOC-DSI-001 for aprovado | DERIVED | não |

### G03 DEVELOPMENT_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-038 | D10-DOC-PRD-001 | D12-DOC-ETE-001 | Transição A03: arquitetura, integrações, dados e testes derivam dos requisitos integrados: `ARCHITECTURE.VISAO_GERAL ← SCHEMA.FUNCTIONAL_REQUIREMENTS` (+4) | G03 | D12-DOC-ETE-001 não pode fechar os campos consumidores (48 campos no artefato) | DERIVED | sim |
| DEP-039 | D11-DOC-DSI-001 | D12-DOC-ETE-001 | Transição A03: pacotes de UI da engenharia vêm do handoff do design system: `PACKAGES.PACKAGE ← ENGINEERING_HANDOFF.PACKAGE` (+1) | G03 | D12-DOC-ETE-001 não pode fechar os campos consumidores (48 campos no artefato) | DERIVED | sim |
| DEP-040 | D11-DOC-EEP-001 | D12-DOC-ETE-001 | Transição A03: responsabilidades das apps seguem a arquitetura de informação: `APPLICATIONS.RESPONSABILIDADE ← INFORMATION_ARCHITECTURE.NAVEGACAO` | G03 | D12-DOC-ETE-001 segue com premissa; revisar quando D11-DOC-EEP-001 for aprovado | DERIVED | não |

### G04 ENGINEERING_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-037 | D05-DOC-DCM-001 | D10-DOC-PRD-001 | Analytics do produto usa as métricas catalogadas: `SCHEMA.ANALYTICS ← SCHEMA.METRIC_OR_FIELD_ID` | G04 | D10-DOC-PRD-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-041 | D20-DOC-PPR-001 | D12-DOC-ETE-001 | Repositórios, ambientes e hosting da engenharia são os inventariados nas plataformas: `REPOSITORIES.REPOSITORIO ← REPOSITORIES.REPO` (+2) | G04 | D12-DOC-ETE-001 não pode fechar os campos consumidores (48 campos no artefato) | DERIVED | sim |
| DEP-042 | D05-DOC-EPGD-001 | D12-DOC-ETE-001 | Banco e schemas da engenharia seguem a estratégia de dados: `DATA.BANCO ← STORAGE.BANCO` (+1) | G04 | D12-DOC-ETE-001 não pode fechar os campos consumidores (48 campos no artefato) | DERIVED | sim |
| DEP-046 | D20-DOC-PPR-001 | D05-DOC-EPGD-001 | Fontes e armazenamento de dados são os sistemas e repositórios existentes: `SOURCES.SISTEMA ← SYSTEMS.PLATAFORMA` (+1) | G04 | D05-DOC-EPGD-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-048 | D05-DOC-EPGD-001 | D02-DOC-DGRC-001 | O inventário de dados pessoais refina a seção de privacidade (informativa: quebra o ciclo DGRC↔EPGD): `PRIVACY.DADOS_PESSOAIS ← PRIVACY.DADOS_PESSOAIS` | G04 | D02-DOC-DGRC-001 segue com premissa; revisar quando D05-DOC-EPGD-001 for aprovado | PROPOSED | não |
| DEP-049 | D05-DOC-EPGD-001 | D05-DOC-DCM-001 | Fonte, dataset, classificação e retenção de cada métrica vêm da estratégia de dados: `SCHEMA.FONTE ← SOURCES.FONTE` (+3) | G04 | D05-DOC-DCM-001 não pode fechar os campos consumidores (18 campos no artefato) | DERIVED | sim |
| DEP-052 | D05-DOC-EPGD-001 | D02-DOC-PPT-001 | A política declara os dados efetivamente coletados: `COLLECTED_DATA.CATEGORIAS_DE_DADOS ← PRIVACY.DADOS_PESSOAIS` (+1) | G04 | D02-DOC-PPT-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-053 | D20-DOC-PPR-001 | D02-DOC-PPT-001 | Operadores da política são as plataformas usadas: `SHARING.OPERADORES ← SYSTEMS.PLATAFORMA` | G04 | D02-DOC-PPT-001 segue com premissa; revisar quando D20-DOC-PPR-001 for aprovado | DERIVED | não |
| DEP-054 | D05-DOC-DCM-001 | D02-DOC-PPT-001 | Cookies de analytics correspondem aos eventos catalogados: `COOKIES.ANALYTICS ← SCHEMA.CAMPO_EVENTO` | G04 | D02-DOC-PPT-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-055 | D12-DOC-ETE-001 | D18-DOC-PCE-001 | Contratos de API e eventos registram as interfaces da engenharia: `API_CONTRACTS.ENDPOINT ← INTERFACES.API` (+1) | G04 | D18-DOC-PCE-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-056 | D05-DOC-EPGD-001 | D18-DOC-PCE-001 | Contratos de dados registram schemas e linhagem: `DATA_CONTRACTS.PAYLOAD ← SCHEMAS.SCHEMA` (+2) | G04 | D18-DOC-PCE-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |
| DEP-059 | D05-DOC-DCM-001 | D18-DOC-PCE-001 | Propriedades de eventos seguem as dimensões catalogadas: `EVENT_CONTRACTS.PROPRIEDADES ← SCHEMA.DIMENSOES` | G04 | D18-DOC-PCE-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-062 | D12-DOC-ETE-001 | D23-DOC-PBL-001 | Arquitetura, interfaces e implementação do blueprint vêm da especificação técnica: `ARCHITECTURE.COMPONENTES ← ARCHITECTURE.VISAO_GERAL` (+3) | G04 | D23-DOC-PBL-001 não pode fechar os campos consumidores (40 campos no artefato) | DERIVED | sim |
| DEP-063 | D18-DOC-PCE-001 | D23-DOC-PBL-001 | Contratos do blueprint referenciam o registro de contratos: `CONTRACTS.SCHEMAS ← DOCUMENT_SCHEMAS.SCHEMA` (+1) | G04 | D23-DOC-PBL-001 segue com premissa; revisar quando D18-DOC-PCE-001 for aprovado | DERIVED | não |
| DEP-066 | D12-DOC-ETE-001 | D07-DOC-PIM-001 | Pacotes, rollback e verificação da implementação vêm da especificação técnica: `WORK_PACKAGES.PACOTE ← PACKAGES.PACKAGE` (+2) | G04 | D07-DOC-PIM-001 não pode fechar os campos consumidores (27 campos no artefato) | DERIVED | sim |
| DEP-068 | D18-DOC-PCE-001 | D07-DOC-PIM-001 | Handoffs da implementação usam os contratos de handoff: `HANDOFF.CONTRATO ← HANDOFF_CONTRACTS.REQUISITOS` | G04 | D07-DOC-PIM-001 segue com premissa; revisar quando D18-DOC-PCE-001 for aprovado | DERIVED | não |
| DEP-073 | D20-DOC-PPR-001 | D08-DOC-RUN-001 | Sistemas e credenciais do runbook são os inventariados: `SCHEMA.SISTEMAS ← SYSTEMS.PLATAFORMA` (+1) | G04 | D08-DOC-RUN-001 não pode fechar os campos consumidores (16 campos no artefato) | DERIVED | sim |
| DEP-074 | D12-DOC-ETE-001 | D08-DOC-RUN-001 | Rollback operacional segue o procedimento técnico: `SCHEMA.ROLLBACK ← ROLLBACK.PROCEDIMENTO` | G04 | D08-DOC-RUN-001 segue com premissa; revisar quando D12-DOC-ETE-001 for aprovado | DERIVED | não |
| DEP-079 | D20-DOC-PPR-001 | D14-DOC-PCV-001 | O CRM é uma das plataformas inventariadas: `CRM.SISTEMA ← SYSTEMS.PLATAFORMA` | G04 | D14-DOC-PCV-001 segue com premissa; revisar quando D20-DOC-PPR-001 for aprovado | DERIVED | não |
| DEP-091 | D05-DOC-DCM-001 | D13-DOC-GTM-001 | Métricas e eventos do lançamento usam o catálogo: `ANALYTICS.METRICAS ← SCHEMA.METRIC_OR_FIELD_ID` (+1) | G04 | D13-DOC-GTM-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-093 | D20-DOC-PPR-001 | D19-DOC-PAC-001 | Destinos dos CTAs são domínios publicados: `DESTINATION.URL ← DOMAINS.DOMINIO` | G04 | D19-DOC-PAC-001 segue com premissa; revisar quando D20-DOC-PPR-001 for aprovado | DERIVED | não |
| DEP-095 | D05-DOC-DCM-001 | D19-DOC-PAC-001 | Tracking dos assets usa os eventos catalogados: `TRACKING.EVENTO ← SCHEMA.CAMPO_EVENTO` | G04 | D19-DOC-PAC-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-101 | D05-DOC-DCM-001 | D16-DOC-PEM-001 | Conversão é medida pela fórmula catalogada: `MEASUREMENT.CONVERSAO ← SCHEMA.FORMULA` | G04 | D16-DOC-PEM-001 segue com premissa; revisar quando D05-DOC-DCM-001 for aprovado | DERIVED | não |
| DEP-106 | D20-DOC-PPR-001 | D06-DOC-RMI-001 | Repositório e localização do registro são os inventariados: `SCHEMA.REPOSITORY ← REPOSITORIES.REPO` (+1) | G04 | D06-DOC-RMI-001 segue com premissa; revisar quando D20-DOC-PPR-001 for aprovado | DERIVED | não |
| DEP-107 | D20-DOC-PPR-001 | D06-DOC-EGC-001 | Repositórios de conhecimento são os inventariados: `REPOSITORIES.REPOSITORIO ← REPOSITORIES.REPO` | G04 | D06-DOC-EGC-001 segue com premissa; revisar quando D20-DOC-PPR-001 for aprovado | DERIVED | não |
| DEP-110 | D05-DOC-DCM-001 | D21-DOC-PWB-001 | Campos, fórmulas e indicadores dos workbooks vêm do catálogo de métricas: `FIELDS.DEFINICAO ← SCHEMA.DEFINICAO` (+2) | G04 | D21-DOC-PWB-001 não pode fechar os campos consumidores (30 campos no artefato) | DERIVED | sim |
| DEP-111 | D05-DOC-EPGD-001 | D21-DOC-PWB-001 | Fontes dos workbooks são as fontes de dados: `SOURCE_DATA.FONTE ← SOURCES.FONTE` | G04 | D21-DOC-PWB-001 segue com premissa; revisar quando D05-DOC-EPGD-001 for aprovado | DERIVED | não |

### G05 RELEASE_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-088 | D07-DOC-PIM-001 | D13-DOC-GTM-001 | Data de lançamento depende dos marcos de implementação (valor em CONFLICT: D22-DEC-CFL-02): `LAUNCH.LAUNCH ← MILESTONES.MARCO` (+1) | G05 | D13-DOC-GTM-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |

### G06 GO_LIVE
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-072 | D08-DOC-MOP-001 | D08-DOC-RUN-001 | Cada runbook operacionaliza um processo/incidente do manual: `SCHEMA.OBJETIVO ← PROCESS_INVENTORY.OBJETIVO` (+3) | G06 | D08-DOC-RUN-001 não pode fechar os campos consumidores (16 campos no artefato) | DERIVED | sim |
| DEP-082 | D08-DOC-MOP-001 | D15-DOC-PASC-001 | Prazos de atendimento respeitam os SLAs operacionais: `SLA.PRAZO ← SLA.META` | G06 | D15-DOC-PASC-001 segue com premissa; revisar quando D08-DOC-MOP-001 for aprovado | DERIVED | não |

### G07 OPERATIONAL_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-084 | D15-DOC-PASC-001 | D03-DOC-MFO-001 | Churn da economia unitária vem da métrica de sucesso do cliente: `UNIT_ECONOMICS.CHURN ← METRICS.CHURN` | G07 | D03-DOC-MFO-001 segue com premissa; revisar quando D15-DOC-PASC-001 for aprovado | DERIVED | não |
| DEP-089 | D15-DOC-PASC-001 | D13-DOC-GTM-001 | Prontidão de suporte é critério do lançamento: `SUPPORT_READINESS.ATENDIMENTO ← SERVICE_MODEL.MODELO` (+1) | G07 | D13-DOC-GTM-001 não pode fechar os campos consumidores (32 campos no artefato) | DERIVED | sim |

### G08 GTM_READY
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-078 | D14-DOC-PCV-001 | D03-DOC-PFO-001 | Forecast comercial refina previsões de receita (informativa: quebra o ciclo PFO↔PCV): `REVENUE.PREVISOES ← FORECAST.RECEITA` | G08 | D03-DOC-PFO-001 segue com premissa; revisar quando D14-DOC-PCV-001 for aprovado | PROPOSED | não |
| DEP-080 | D14-DOC-PCV-001 | D15-DOC-PASC-001 | Onboarding recebe o handoff comercial (informativa: o CS desenha o onboarding antes do G08): `ONBOARDING.ETAPAS ← HANDOFF.ONBOARDING` (+1) | G08 | D15-DOC-PASC-001 segue com premissa; revisar quando D14-DOC-PCV-001 for aprovado | PROPOSED | não |
| DEP-090 | D13-DOC-GTM-001 | D14-DOC-PCV-001 | Etapas de vendas recebem o handoff de marketing: `PROCESS.ETAPAS ← SALES_HANDOFF.MARKETING_PARA_VENDAS` | G08 | D14-DOC-PCV-001 segue com premissa; revisar quando D13-DOC-GTM-001 for aprovado | DERIVED | não |
| DEP-092 | D13-DOC-GTM-001 | D19-DOC-PAC-001 | Campanha, produto e headline dos assets vêm do plano de lançamento: `PURPOSE.CAMPANHA ← CAMPAIGN.FASE` (+2) | G08 | D19-DOC-PAC-001 não pode fechar os campos consumidores (37 campos no artefato) | DERIVED | sim |
| DEP-098 | D19-DOC-PAC-001 | D16-DOC-PEM-001 | CTAs e destinos das peças vêm do catálogo de CTAs: `CTA.CTA ← CTA_CATALOG.CTA_ID` (+1) | G08 | D16-DOC-PEM-001 não pode fechar os campos consumidores (36 campos no artefato) | DERIVED | sim |
| DEP-099 | D13-DOC-GTM-001 | D16-DOC-PEM-001 | Calendário editorial acompanha as atividades de campanha: `EDITORIAL_CALENDAR.TEMA ← CAMPAIGN.ATIVIDADE` | G08 | D16-DOC-PEM-001 segue com premissa; revisar quando D13-DOC-GTM-001 for aprovado | DERIVED | não |
| DEP-104 | D19-DOC-PAC-001 | D17-DOC-PEP-001 | Portfólio publicado reutiliza assets: `ASSETS.PORTFOLIO ← ASSET_INVENTORY.ASSET_ID` | G08 | D17-DOC-PEP-001 segue com premissa; revisar quando D19-DOC-PAC-001 for aprovado | DERIVED | não |

### G11 DOCUMENTED
| ID | Origem | → Destino | Motivo (campos) | Gate | Impacto se faltar | Tag | Bloqueante? |
|---|---|---|---|---|---|---|---|
| DEP-043 | D22-DOC-DRL-001 | D12-DOC-ETE-001 | Links de ADR apontam para o log de decisões: `ADR_LINKS.DECISOES_ARQUITETURAIS ← SCHEMA.DECISION_ID` | G11 | D12-DOC-ETE-001 segue com premissa; revisar quando D22-DOC-DRL-001 for aprovado | DERIVED | não |
| DEP-058 | D06-DOC-EGC-001 | D18-DOC-PCE-001 | Registro e versionamento de contratos seguem o padrão de IDs e versões: `REGISTRY.ID ← IDENTITY.PADRAO_DE_IDS` (+1) | G11 | D18-DOC-PCE-001 segue com premissa; revisar quando D06-DOC-EGC-001 for aprovado | DERIVED | não |
| DEP-105 | D06-DOC-EGC-001 | D06-DOC-RMI-001 | IDs, tipos, domínios e supersedes do registro seguem a gestão do conhecimento: `SCHEMA.CANONICAL_ID ← IDENTITY.PADRAO_DE_IDS` (+3) | G11 | D06-DOC-RMI-001 não pode fechar os campos consumidores (19 campos no artefato) | DERIVED | sim |
| DEP-109 | D06-DOC-EGC-001 | D22-DOC-DRL-001 | Supersedes de decisões seguem a regra de versionamento: `SCHEMA.SUPERSEDES ← VERSIONING.SUPERSEDE` | G11 | D22-DOC-DRL-001 segue com premissa; revisar quando D06-DOC-EGC-001 for aprovado | DERIVED | não |
| DEP-112 | D06-DOC-EGC-001 | D21-DOC-PWB-001 | Versionamento dos workbooks segue a regra de versões: `VERSIONING.VERSAO ← VERSIONING.VERSAO` | G11 | D21-DOC-PWB-001 segue com premissa; revisar quando D06-DOC-EGC-001 for aprovado | DERIVED | não |

### Transição Produto → Engenharia (A03)
1. **A03 existe só como macroárea.** O 10_REG tem "A03 Handoff Produto → Engenharia", mas nenhum domínio do 11_REG aponta para A03 e nenhum artefato do 14_REG está nela. O formulário `01_Formulario_A03` não tem campos, e o G03 DEVELOPMENT_READY não tem artefato que o certifique (GAP-DEP-C).
2. **O que A03 recebe de Produto (A02):**
   - de D10-DOC-PRD-001: requisitos funcionais e não funcionais, integrações, requisitos de dados e critérios de aceite;
   - de D11-DOC-DSI-001: o pacote e os tokens do handoff de engenharia;
   - de D11-DOC-EEP-001: a arquitetura de informação.
3. **O que A03 entrega à Engenharia (A04):** a D12-DOC-ETE-001, nas seções de arquitetura, performance, integrações, dados, testes, pacotes e responsabilidades das apps.
   - A partir de ETE, o fluxo segue para PCE, PBL e PIM, e depois para GTM, PAC e PEM: 7 artefatos e **252 campos** a jusante.
4. **Gate:** G03 DEVELOPMENT_READY (PROPOSED). É o checkpoint da fase F7.
5. **Se a transição for antecipada:** a engenharia desenha sobre requisitos não aprovados, e o retrabalho se propaga pelos 252 campos citados.
6. **CONFLICT proposto (para o 22_REG).** O `TPL-DRP-001` (13_REG_Templates) é aplicável só à **A03**, mas o artefato D10-DOC-DRP-001 está na **A02** pela DEC-MACRO-D10, que é PROPOSED e ainda aguarda validação humana. Os templates `FUNCTIONAL_REQUIREMENTS` e `ACCEPTANCE_CRITERIA` também citam A03, e esse conteúdo hoje vive em campos do D10-DOC-PRD-001.
7. **Decisão mínima necessária (humana).** Macroáreas e domínios não foram alterados. As opções são:
   - (a) criar um artefato de handoff em A03 a partir desses templates;
   - (b) revisar a DEC-MACRO-D10 e mover D10-DOC-DRP-001 para A03;
   - (c) manter A03 como checkpoint sem artefato, com o G03 avaliado sobre PRD, DSI e EEP (é o que esta entrega assume).

### Ciclos e como foram resolvidos
A análise encontrou 7 ciclos de informação. Em cada um, o lado bloqueante segue o fluxo principal e o outro lado foi classificado como **informativo (PROPOSED)**, dependendo de validação humana. Não sobrou nenhum ciclo bloqueante.

| ID | Aresta informativa | Motivo |
|---|---|---|
| DEP-010 | D03-DOC-MFO-001 → D01-DOC-MNE-001 | Economia unitária do MNE resume o modelo financeiro (informativa: quebra o ciclo MNE↔MFO) |
| DEP-013 | D03-DOC-PFO-001 → D03-DOC-MFO-001 | Premissas gerais (período, moeda) do plano calibram o modelo (informativa: quebra o ciclo MFO↔PFO) |
| DEP-019 | D07-DOC-PEX-001 → D04-DOC-PPC-001 | Demanda de trabalho alimenta a carga de pessoas (informativa: quebra o ciclo PPC↔PEX) |
| DEP-031 | D11-DOC-EEP-001 → D10-DOC-DRP-001 | Pesquisa de usuários refina as jornadas do produto (informativa: quebra o ciclo DRP↔EEP) |
| DEP-048 | D05-DOC-EPGD-001 → D02-DOC-DGRC-001 | O inventário de dados pessoais refina a seção de privacidade (informativa: quebra o ciclo DGRC↔EPGD) |
| DEP-078 | D14-DOC-PCV-001 → D03-DOC-PFO-001 | Forecast comercial refina previsões de receita (informativa: quebra o ciclo PFO↔PCV) |
| DEP-080 | D14-DOC-PCV-001 → D15-DOC-PASC-001 | Onboarding recebe o handoff comercial (informativa: o CS desenha o onboarding antes do G08) |

### Camadas topológicas (bloqueantes)
Esta é a saída do validador. A camada 1 são os artefatos sem nenhuma dependência bloqueante de entrada.
- camada 1: D01-DOC-DDE-001, D06-DOC-EGC-001, D09-DOC-DEB-001, D11-DOC-DSI-001, D17-DOC-PEP-001
- camada 2: D01-DOC-MNE-001, D01-DOC-MRE-001, D01-DOC-TAP-001, D02-DOC-DGRC-001, D04-DOC-PPC-001, D06-DOC-RMI-001, D20-DOC-PPR-001, D22-DOC-DRL-001
- camada 3: D02-DOC-MRC-001, D03-DOC-MFO-001, D05-DOC-EPGD-001, D07-DOC-PEX-001, D08-DOC-MOP-001, D09-DOC-PPE-001, D13-DOC-DRM-001, D15-DOC-PASC-001
- camada 4: D02-DOC-PPT-001, D03-DOC-PFO-001, D05-DOC-DCM-001, D08-DOC-RUN-001, D10-DOC-DRP-001
- camada 5: D11-DOC-EEP-001, D14-DOC-PCV-001, D21-DOC-PWB-001
- camada 6: D10-DOC-PRD-001
- camada 7: D12-DOC-ETE-001
- camada 8: D07-DOC-PIM-001, D18-DOC-PCE-001, D23-DOC-PBL-001
- camada 9: D13-DOC-GTM-001
- camada 10: D19-DOC-PAC-001
- camada 11: D16-DOC-PEM-001

---

## PARTE 3 — ARQUITETURA DE PREENCHIMENTO
As fases são consequência das dependências reais. Elas não seguem a ordem A00–A12 nem D01–D23 nem o calendário. As prioridades aplicadas foram, em ordem:
1. dependência de informação;
2. contexto cognitivo;
3. macroárea e domínio;
4. ordem dos Gates.

A cobertura é de **1.125 de 1.125 campos**, e nenhuma fase vem antes de uma dependência bloqueante (validador com `--fases`).

| Fase | Contexto único | Escopo: macroáreas/domínios | Entregável 1 | Entregável 2 | Entregável 3 | Dependências de entrada | Saída da fase | Gate associado |
|---|---|---|---|---|---|---|---|---|
| F1 | Direção e abertura do ecossistema | A00/D01 | D01-DOC-DDE-001 | D01-DOC-TAP-001 | — | nenhuma (raiz) | 73 campos preenchidos; libera D01-DOC-MNE-001 (F2), D01-DOC-MRE-001 (F2), D02-DOC-DGRC-001 (F4), D04-DOC-PPC-001 (F5), D07-DOC-PEX-001 (F5), D10-DOC-DRP-001 (F6), D20-DOC-PPR-001 (F8), D22-DOC-DRL-001 (F13); G00 avaliável | G00 INITIATIVE_READY |
| F2 | Modelo de negócio e economia | A00/D01, A00/D03 | D01-DOC-MNE-001 | D03-DOC-MFO-001 | D03-DOC-PFO-001 | D01-DOC-DDE-001 (F1) | 124 campos preenchidos; libera D09-DOC-PPE-001 (F3), D13-DOC-DRM-001 (F3), D10-DOC-DRP-001 (F6), D08-DOC-MOP-001 (F10), D14-DOC-PCV-001 (F11), D15-DOC-PASC-001 (F11), D13-DOC-GTM-001 (F12); G01 avaliável | G01 BUSINESS_READY (parcial) |
| F3 | Mercado, pesquisa e evidências | A01/D13, A06/D09 | D09-DOC-DEB-001 | D13-DOC-DRM-001 | D09-DOC-PPE-001 | D01-DOC-MNE-001 (F2) | 67 campos preenchidos; libera D10-DOC-DRP-001 (F6), D14-DOC-PCV-001 (F11), D13-DOC-GTM-001 (F12), D16-DOC-PEM-001 (F12); G01 avaliável | G01 BUSINESS_READY (parcial) |
| F4 | Governança jurídica e riscos | A00/D02 | D02-DOC-DGRC-001 | D02-DOC-MRC-001 | — | D01-DOC-DDE-001 (F1) | 51 campos preenchidos; libera D02-DOC-PPT-001 (F8), D05-DOC-EPGD-001 (F8); G01 avaliável | G01 BUSINESS_READY (parcial) |
| F5 | Pessoas e capacidade de execução | A07/D04, A09/D07 | D04-DOC-PPC-001 | D07-DOC-PEX-001 | — | D01-DOC-DDE-001 (F1), D01-DOC-TAP-001 (F1) | 71 campos preenchidos; libera D07-DOC-PIM-001 (F10); G01 avaliável | G01 BUSINESS_READY (fecha) |
| F6 | Produto e experiência (A02) | A02/D10, A02/D11 | D11-DOC-DSI-001 | D10-DOC-DRP-001 | D11-DOC-EEP-001 | D01-DOC-DDE-001 (F1), D01-DOC-MNE-001 (F2), D13-DOC-DRM-001 (F3) | 113 campos preenchidos; libera D12-DOC-ETE-001 (F9), D23-DOC-PBL-001 (F9), D13-DOC-GTM-001 (F12); G02 avaliável | G02 PRODUCT_READY |
| F7 | Transição Produto → Engenharia (A03) | A03 (sem domínio) | — (sem artefato em 14_REG; GAP-DEP-C) | — | — | D10-DOC-PRD-001 (F6), D11-DOC-DSI-001 (F6), D11-DOC-EEP-001 (F6) | PRD, DSI e EEP aprovados e aceitos pela Engenharia; G03 DEVELOPMENT_READY avaliável; libera ETE (F9) | G03 DEVELOPMENT_READY |
| F8 | Plataformas, dados e privacidade | A00/D02, A06/D05, A11/D20 | D20-DOC-PPR-001 | D05-DOC-EPGD-001 | D05-DOC-DCM-001 | D01-DOC-DDE-001 (F1), D02-DOC-DGRC-001 (F4) | 120 campos preenchidos; libera D12-DOC-ETE-001 (F9), D18-DOC-PCE-001 (F9), D08-DOC-RUN-001 (F10), D21-DOC-PWB-001 (F13); G04 avaliável | G04 (parcial) · G05 (PPT) |
| F9 | Engenharia, contratos e blueprints (A04) | A00/D18, A04/D12, A10/D23 | D12-DOC-ETE-001 | D18-DOC-PCE-001 | D23-DOC-PBL-001 | D10-DOC-PRD-001 (F6), D11-DOC-DSI-001 (F6), D05-DOC-EPGD-001 (F8), D20-DOC-PPR-001 (F8) | 120 campos preenchidos; libera D07-DOC-PIM-001 (F10); G04 avaliável | G04 ENGINEERING_READY |
| F10 | Implementação e operação | A05/D08, A09/D07 | D07-DOC-PIM-001 | D08-DOC-MOP-001 | D08-DOC-RUN-001 | D01-DOC-MNE-001 (F2), D07-DOC-PEX-001 (F5), D20-DOC-PPR-001 (F8), D12-DOC-ETE-001 (F9) | 70 campos preenchidos; libera D13-DOC-GTM-001 (F12); G05 avaliável | G05 RELEASE_READY · G06 GO_LIVE |
| F11 | Comercial e sucesso do cliente | A01/D14, A01/D15 | D14-DOC-PCV-001 | D15-DOC-PASC-001 | — | D01-DOC-MNE-001 (F2), D03-DOC-PFO-001 (F2), D13-DOC-DRM-001 (F3) | 71 campos preenchidos; libera D13-DOC-GTM-001 (F12); G07 avaliável | G07 OPERATIONAL_READY · G08 (parcial) |
| F12 | Lançamento e conteúdo | A01/D13, A08/D16, A11/D19 | D13-DOC-GTM-001 | D19-DOC-PAC-001 | D16-DOC-PEM-001 | D03-DOC-PFO-001 (F2), D09-DOC-DEB-001 (F3), D13-DOC-DRM-001 (F3), D10-DOC-PRD-001 (F6), D07-DOC-PIM-001 (F10), D15-DOC-PASC-001 (F11) | 105 campos preenchidos; libera nenhum bloqueio a jusante; G08 avaliável | G08 GTM_READY |
| F13 | Conhecimento, registros e workbooks | A06/D06, A10/D21, A10/D22 | D06-DOC-EGC-001 | D06-DOC-RMI-001 | D22-DOC-DRL-001 | D01-DOC-DDE-001 (F1), D05-DOC-DCM-001 (F8) | 101 campos preenchidos; libera nenhum bloqueio a jusante; G09 avaliável | G09 MEASURED · G11 DOCUMENTED |
| F14 | Emprego e portfólio (A12) | A12/D17 | D17-DOC-PEP-001 | — | — | nenhuma (raiz) | 39 campos preenchidos; ramo independente | gate:tbd |

- **F1 — fronteira:** Raiz da rede: nenhum artefato bloqueia DDE; TAP depende só de DDE.
- **F2** — também nesta fase: D01-DOC-MRE-001.
- **F2 — fronteira:** Mudança de contexto (estratégia → economia); MNE bloqueia 8 artefatos, inclusive toda a F3.
- **F3 — fronteira:** Mesmo contexto comercial de F2, mas bloqueado por MNE; DRM e DEB bloqueiam produto e conteúdo.
- **F4 — fronteira:** Contexto jurídico; depende só de DDE; bloqueia privacidade/dados (F8).
- **F5 — fronteira:** Contexto de capacidade; PEX exige TAP e PPC; fecha o G01.
- **F6** — também nesta fase: D10-DOC-PRD-001.
- **F6 — fronteira:** Bloqueada por DDE, MNE e DRM; ordem interna DRP → EEP → PRD; DSI sem bloqueante (entra primeiro).
- **F7 — fronteira:** Checkpoint sem artefato: 14_REG não tem nenhum artefato em A03 (GAP-DEP-C). Avalia PRD/DSI/EEP para a engenharia.
- **F8** — também nesta fase: D02-DOC-PPT-001.
- **F8 — fronteira:** Contexto técnico-dados; PPR→EPGD→DCM/PPT; exige DGRC (F4). Precede a engenharia para evitar retrabalho em ETE.
- **F9 — fronteira:** Bloqueada por PRD, DSI (via G03), PPR e EPGD; ETE → PCE → PBL.
- **F10 — fronteira:** PIM exige PEX e ETE; RUN exige MOP e PPR; contexto de entrega e operação.
- **F11 — fronteira:** PCV exige DRM e PFO; PASC exige MNE; PASC bloqueia o lançamento.
- **F12 — fronteira:** GTM exige DRM, PFO, PRD, PIM e PASC; GTM → PAC → PEM; PEM exige DEB (claims).
- **F13** — também nesta fase: D21-DOC-PWB-001.
- **F13 — fronteira:** Contexto de governança do conhecimento; RMI recebe o próprio 16_REG (depends_on/blocks); PWB exige DCM.
- **F14 — fronteira:** Ramo independente: só dependências informativas; pode correr em paralelo desde F1.

---

## ANEXO — Proveniência epistêmica
- O `anexo.csv` tem uma linha por `dependency_id`, com `status_epistemico`, justificativa (todos os pares de campos) e o estado epistêmico do Gate.
- Resumo:
  - 105 DERIVED: dependência demonstrável por campo;
  - 7 PROPOSED: classificação informativa para quebrar ciclos, listada acima;
  - 0 DIRECT, porque nada está documentado na fonte;
  - 0 CONFLICT e 0 GAP no registro.
- O 16_REG não tem colunas para classe epistêmica nem para justificativa. Por isso o anexo fica separado, com a mesma `dependency_id` (GAP-DEP-F).

## Lacunas e conflitos
**GAP** (para o 21_REG_Gaps; os IDs são sugestão)
- **GAP-DEP-A:** o domínio de valores de `relation`, `required_status` e `status` do 16_REG não está definido. Os valores adotados estão na Parte 1 e precisam de confirmação.
- **GAP-DEP-B:**
  - `17_REG_Gates.required_artifact_types` está vazio nos 12 Gates;
  - `gate_id`, `lifecycle_stage_id`, `template_id` e `portfolio_id` estão vazios nos 37 artefatos;
  - por isso, o mapeamento artefato → Gate é PROPOSED.
- **GAP-DEP-C:** A03 não tem domínio nem artefato. O G03 e o G10 LEARNING_CAPTURED ficam sem artefato certificador.
- **GAP-DEP-D:** a aba obrigatória `README_MASTER_INDEX_EXECUTAR` está ausente.
- **GAP-DEP-E:** a coluna Resposta está vazia em 1.125 campos, e 1.013 deles são PROPOSED (UAR-04).
  - As dependências foram derivadas da estrutura dos campos. Quando o conteúdo for preenchido, cada DERIVED pode subir para DIRECT ou cair.
- **GAP-DEP-F:** o 16_REG não tem colunas `status_epistemico` nem `justificativa`. A proposta é acrescentá-las ou manter o anexo.
- **NA-03 e GAP-DEP-01:** podem ser fechados depois da validação humana desta entrega.

**CONFLICT** (para o 22_REG_Conflitos)
- **Novo (proposto):** TPL-DRP-001 (A03) × D10-DOC-DRP-001 (A02, pela DEC-MACRO-D10). Detalhe na subseção A03.
- **Existentes que afetam valores, não a existência das relações:**
  - D22-DEC-CFL-02, a data de lançamento, afeta DEP-067 (TAP→PIM) e DEP-088 (PIM→GTM);
  - D22-DEC-CFL-03, o preço, afeta DEP-009 (MNE→MFO), DEP-011 (MNE→PFO), DEP-076 (PFO→PCV) e DEP-086 (PFO→GTM).

**PROPOSED** (exigem validação humana)
- as 7 classificações informativas de ciclo;
- todo o mapeamento de `gate_id`;
- os valores escolhidos em GAP-DEP-A;
- a opção (c) da transição A03.

---

## Fechamento
`Dependências de entrada → Saída → Gate`
- **Entradas lidas:**
  - 00_Leia-me;
  - os formulários A00–A12;
  - as visões 02–09;
  - os registros 10–24, com peso em 14_REG_Artefatos, 15_REG_Campos, 17_REG_Gates, 13_REG_Templates, 20_REG_Decisoes, 21_REG_Gaps e 22_REG_Conflitos.
- **Saídas:**
  - `registro.csv` e `registro_para_colar.csv` (112 linhas);
  - `anexo.csv`;
  - `fases.json`;
  - `14_REG_depends_on_blocks.csv`;
  - `validacao.txt`;
  - `analise_pf24.py` (reprodutível);
  - este `ENTREGA.md`.
- **O que isso desbloqueia (depois da validação humana):**
  - preencher o 16_REG e as colunas `depends_on`/`blocks` do 14_REG;
  - recalcular a `06_Visao_Dependencias`;
  - alimentar `depends_on`/`blocks` do D06-DOC-RMI-001;
  - gerar o `estrutura.json` da `executar-arvore-roadmap` (CV-ARVORE-001) a partir das fases F1–F14;
  - fechar o NA-03 e o GAP-DEP-01.
- **Validador** (`validar_registro.py --control-plane --fases`): **0 erro(s), 20 aviso(s)**.
  - Os avisos são: GAP-DEP-A e D, os ciclos informativos já resolvidos e as 7 relações PROPOSED.
- Nada foi gravado na planilha. Colar as linhas e decidir A03, o domínio de valores e o mapeamento de Gates são passos humanos.
