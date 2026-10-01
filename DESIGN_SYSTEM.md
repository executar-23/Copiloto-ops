# DESIGN_SYSTEM

Apontador da fonte de verdade do design system deste repositório (ADR-DS-ROOT-MIGRATION-001).
O registro legível por máquina está em `design-system.manifest.json`.

| Campo | Valor |
| --- | --- |
| SOURCE_REPOSITORY | `executar-23/Risco-cognitivo-blog` |
| SOURCE_BRANCH | `main` (ver nota abaixo) |
| SOURCE_COMMIT | `530afe1708ed24111f9b6756948908ab7e9b3afe` |
| CANONICAL_TOKEN_FILE | n/a |
| COMPONENT_DIRECTORY | n/a |
| DESIGN_SYSTEM_ROUTE | n/a |
| CLASSIFICATION | `NON_UI` |
| INTEGRATION_STATUS | `VENDORED_REFERENCE_ONLY` |
| LAST_SYNC | 2026-10-01 |
| TARGET_COMMIT_BEFORE | `f70aa8631531b83eaaefd120f3a868ed99498c39` |

> Nota sobre a branch: em 2026-10-01 a default branch do GitHub da origem era
> `claude/youthful-archimedes-qksrsl` (`11f78e4`), ancestral direto da `main` (`530afe1`, 7 commits
> à frente). A `main` é a branch de integração declarada no `CLAUDE.md` da origem e traz a versão
> mais nova do design system (tokens `--area-*`, `ScrollArea` com `viewportProps`), por isso é a
> fonte usada aqui.

## Inventário

Repositório operacional (agentes, prompts, runbooks, plugins, conteúdo). `apps/web`, `apps/studio`,
`apps/event-collector` e `packages/design-system` existem só como diretórios reservados
(`.gitkeep`): ainda não há framework, `package.json`, CSS nem rota. Quando `apps/web` ou
`packages/design-system` ganharem código, a fonte de verdade é a indicada abaixo.
## Fonte canônica (na origem)

| Item | Caminho em `executar-23/Risco-cognitivo-blog` |
| --- | --- |
| Tokens (claro/escuro, `@theme inline`) | `src/styles/global.css` |
| Primitives (shadcn new-york + Radix) | `src/components/ui/` |
| Callouts (26 variantes) | `src/components/ui/callout.tsx`, `callout-registry.ts` |
| Plain text / ASCII | `src/components/plain/`, `src/lib/plain/` |
| Galerias | `src/components/design-system/` |
| Fontes | `public/fonts/dm-sans/` |
| Configuração | `components.json` |
| Normas | `docs/design-system/` |
| Catálogo | `src/pages/admin/design-system.astro` → `/admin/design-system` |

Implementações já integradas como default: `executar-23/react-router-hono-fullstack-template`
(`app/`) e `executar-23/workflows-starter-template` (`admin/`).

## Por que só o apontador

Este repositório não tem aplicação visual executável, então não há onde ativar o design system.
Nenhum componente ou token foi copiado: uma cópia sem consumidor só envelheceria. Quando surgir um
frontend aqui, ele deve partir da origem acima (ou de uma das implementações) e trocar
`INTEGRATION_STATUS` para `IMPLEMENTED_DEFAULT` no mesmo PR.
