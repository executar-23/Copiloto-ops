# Schema operacional — Epic, Issue, Sub-issue e evidência

**Status:** definido em 2026-09-26 para `executar-23/Copiloto-ops`.  
**Fonte de decisão:** ADR-002 no Notion.

## Hierarquia
```text
Project #1
└── Epic
    ├── Issue de entrega/ciclo
    │   └── Sub-issue de etapa ou grupo
    │       └── Checklist + evidência
    └── Issue de entrega/ciclo
```

## Tipos

### Epic
Resultado agregado com duas ou mais entregas verificáveis.
- Título: `[EPIC] <ID confirmado> — <resultado>`
- Fecha quando todas as Issues-filhas atingem seu aceite.
- Não contém execução granular.

### Issue
Unidade executável, demonstrável e verificável.
- Título: `[ISSUE] <ID pai, se houver> — <entrega>`
- Deve apontar para Epic e Runbook quando aplicável.
- Para F1-3X, cada Issue representa um ciclo editorial completo.

### Sub-issue
Etapa delimitada de uma única Issue.
- Título: `[SUB] #<issue-pai> — <etapa>`
- Usa o número GitHub como identificador local; não inventar novo ID.
- Criar apenas quando a etapa precisar de execução/evidência independente.
- Se a integração não suportar vínculo nativo, registrar `Parent: #N` e não chamar isso de sub-issue nativa.

### Checklist
Passo atômico que não exige objeto próprio.
- Deve registrar evidência na Issue/Sub-issue.
- Promover a Issue apenas se houver owner/dependência própria, bloqueio relevante ou necessidade de rastreabilidade independente.

## Campos obrigatórios no corpo
- Fonte Notion URL/ID e/ou documento-fonte.
- ID confirmado, quando existir.
- Epic pai.
- Runbook.
- Owner: `A_DEFINIR` quando ausente.
- Aprovação: `pendente` por padrão.
- Gate: `gate:tbd` quando indefinido.
- Estado operacional.
- Objetivo e escopo.
- Critérios de aceite.
- Dependências.
- Evidências.
- Decisões humanas pendentes.

## Estados de execução editorial
`PLANNED → STRUCTURED → IMPLEMENTED → PRODUCED → VERIFIED`

Aprovação humana é eixo separado do estado de execução.

## Labels — estado desejado
Ver `.github/labels.yml`. O arquivo documenta o schema, mas não comprova que as labels existem no GitHub. As labels `state/*` e `type/*` do Copiloto Operacional e a equivalência com os estados acima estão pendentes de decisão; ver `docs/NOTION-ROTA.md` (Copiloto Operacional como conector).

## Milestones
Usar para janela/release compartilhada, não como substituto de Epic. Só criar quando datas e escopo temporal estiverem confirmados. F1-3X não recebe milestone enquanto a divergência 15d × 17d não for resolvida.

## Project #1
Quando o Project estiver verificável, campos desejados:
- Status
- Type
- Epic/Parent
- Cycle
- Owner
- Approval
- Gate
- Evidence
- Notion Source

Não declarar esses campos como configurados sem evidência.

## F1-3X
- Epic: `F1-3X`.
- 3 Issues de ciclo editorial, em sequência.
- Cada ciclo usa `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.yaml`.
- Sub-issues recomendadas por ciclo: Entrada+Topic Pack; Peça-mãe; Derivados; Coerência+governança; Handoff.
- Os 22 passos do Runbook permanecem checklist/evidência dentro desses grupos.
- WIP=1 por agente.
