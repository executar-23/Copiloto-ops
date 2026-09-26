# Rota Notion ↔ GitHub

Data da leitura: 2026-09-26. Este arquivo é um **espelho de navegação**, não cópia autoritativa do conteúdo nem sincronização automática.

## Entrada operacional
- Workspace Notion conectado: `hub.executar@gmail.com`, ID `a16d1d67-3fb3-819b-9a37-000340383a5d`.
- [GTM-Blog — Launch Control](https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac) → [00 — Agent Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) → [01 — Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62).
- Contexto: [02 — Foundation Doc](https://app.notion.com/p/3e7d1d673fb3815cb133cd8aeda89397); decisões: [03 — ADRs](https://app.notion.com/p/3e7d1d673fb381aeb3e4dda7c9f37b61); planejamento: [05 — Plano de Implementação](https://app.notion.com/p/3e7d1d673fb381368574fa687f7cf0eb); trabalho derivado: [04 — Tasks](https://app.notion.com/p/3e7d1d673fb381bd8f88e5c38979d403).
- Ao concluir, registrar no Master Index agente, IDs/fonte, resultado, Issue/PR/commit, aprovação e próxima ação. Decisões relevantes vão para ADRs.

## Corpus externo (rota declarada no Master Index do hub)
- Workspace-fonte: `sas.executar@gmail.com`, ID `70f07a81-4fc7-81d1-a772-0003881c098c`.
- [MASTER_INDEX — Ecossistema](https://app.notion.com/p/3d607a814fc78071a4b2d304443c31d3), ID `3d607a814fc78071a4b2d304443c31d3`.
- **Acesso não validado:** a conexão Notion atual retorna `object_not_found` (404) ao abrir esse MASTER_INDEX. Os IDs abaixo foram transcritos da rota do hub; não representam leitura direta das páginas externas nem permissão concedida a agentes.
- Modo padrão de consulta. Escrita no corpus externo exige autorização específica e conexão com acesso; não tentar contornar o bloqueio.

| Domínio | Diretório | Page ID declarado |
|---|---|---|
| D01 | gestao-empresarial | `3e207a814fc7819aa8baea30e951034c` |
| D02 | juridico-riscos-e-conformidade | `3e207a814fc78174a5dedb1bd7593240` |
| D03 | financas | `3e207a814fc78107aec9dacb50c7e1ff` |
| D04 | pessoas-e-recursos-humanos | `3e207a814fc7811197d8c5d603397b9f` |
| D05 | dados | `3e207a814fc78192bc73f3f42a6fa994` |
| D06 | conhecimento-e-busca-corporativa | `3e207a814fc78160b015ee0bc1d8a612` |
| D07 | produtividade-e-execucao | `3e207a814fc78172888bc2ec86526fda` |
| D08 | operacoes | `3e207a814fc781dbac69e9bf82a4559b` |
| D09 | pesquisa-e-inovacao | `3e207a814fc781d982fbdd5a82beb91e` |
| D10 | gestao-de-produto | `3e207a814fc781e5bc6cdd72f00898da` |
| D11 | experiencia-e-projeto | `3e207a814fc78152a537c5f3dc8d7d72` |
| D12 | engenharia | `3e207a814fc7810db055feed2718c5a3` |
| D13 | mercado-e-geracao-de-demanda | `3e207a814fc781f98f92dd0078ec258d` |
| D14 | vendas | `3e207a814fc7813d90fec9f185e278c4` |
| D15 | atendimento-e-sucesso-do-cliente | `3e207a814fc7813e85e7f98cdcc417f3` |
| D16 | midias-sociais-e-comunicacao-digital | `3e207a814fc78103b1fcc4dc40f71229` |
| D17 | emprego-e-portfolio | `3e207a814fc7813fa10cc6cd3eee4bfa` |
| D18 | contratos-e-esquemas | `3e207a814fc781b09152e470a92e2514` |
| D19 | assets-e-cta | `3e207a814fc781579fc6dc37ba09c1be` |
| D20 | plataformas-e-repositorios | `3e207a814fc781d3a02ce4f14e362f22` |
| D21 | workbook | `3e207a814fc7812387fbc3910056a819` |
| D22 | decision-and-register-log | `3e207a814fc78146a9dfdae87472380e` |
| D23 | blueprints | `3e207a814fc7815a921cf482e4143281` |

## Correlação operacional
1. O agente entra pelo Runner, consulta o Master Index e resolve a página-fonte necessária. Se o corpus externo estiver inacessível, registre a limitação e peça acesso; não trate a rota como leitura concluída.
2. Ao promover uma Task para Issue em [Copiloto-ops](https://github.com/executar-23/Copiloto-ops/issues), registre no corpo: URL Notion-fonte, workspace, domínio Dxx, ID canônico, Epic pai, gate, aceite e dependências. Preserve aprovação pendente.
3. Após Issue/PR/commit, registre backlinks e resultado no Master Index do hub. Link cruzado é rastreabilidade, não duplicação do documento nem sincronização automática.
4. O schema e IDs do Programa continuam na fonte canônica [Copiloto](https://github.com/Sas-Executar/Copiloto); execução técnica do produto, quando autorizada, em [executar-Blog](https://github.com/Sas-Executar/executar-Blog).
5. Cada plataforma exige sua própria autenticação e permissões. Acesso via GitHub não concede acesso ao Notion e vice-versa. Nunca copie segredos ou conteúdo privado para este repositório público.
