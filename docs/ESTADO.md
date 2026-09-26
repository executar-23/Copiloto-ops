# Estado — arquitetura de duas plataformas
Data: 2026-09-26.

Decisão do usuário: **GitHub executar-23/Copiloto-ops** para operação; **Notion do projeto** como banco de informações. Referências a caminhos anteriores foram removidas das instruções ativas.

## Confirmado
- Este repositório contém instruções, prompts, modelo e mapa de páginas Notion.
- O workspace Notion conectado é o do projeto GTM-Blog; Runner, Master Index, Foundation, ADRs, Plano e Tasks foram lidos.
- GitHub e Notion possuem links cruzados documentados, sem sincronização automática.
- O usuário forneceu a URL `https://github.com/users/executar-23/projects/1` e a URL de workflow `https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616`.

## Política de commits
ADR de agentes em main aceito em 2026-09-26. A regra operacional está em AGENTS.md e é repetida nos pontos de entrada necessários; o racional está em `docs/ADR-0001-AGENTES-DIRETO-MAIN.md`. O README apenas aponta para essas fontes. WIP=1 por agente, não exclusividade global. Locking/ownership de arquivos segue pendente; não presumir CI configurada.

Antes de escrever: sincronizar, inspecionar arquivos-alvo e HEAD remoto. Escrita deve ser fast-forward; conflito ou avanço concorrente exige interromper e reinspecionar.

## GitHub Project
A URL fornecida pelo usuário identifica o Project #1 do owner `executar-23`. A integração GitHub disponível neste agente não expõe GitHub Projects v2, então título, campos, workflow ativo e vínculos internos não estão independentemente verificados.

A documentação oficial do GitHub orienta configurar auto-add em **Project → Workflows → Auto-add to project → Edit → selecionar repositório/filtro → Save and turn on workflow**. Itens existentes não são adicionados retroativamente apenas por habilitar o workflow.

## Estrutura operacional definida
- Schema de Epic → Issue → Sub-issue → checklist: `docs/SCHEMA-TRABALHO.md`.
- Runbook editorial: `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.md`.
- Epic criado: #2 — `F1-3X`.
- Issues de ciclo: #3, #4 e #5.
- O arquivo `.github/labels.yml` agora registra o estado desejado do schema; não comprova criação/aplicação das labels no GitHub.
- A integração disponível não expõe escrita de sub-issues nativas; os cinco grupos por ciclo estão estruturados, mas não devem ser declarados como vínculos nativos.

## Ainda não configurado/verificado
- Labels efetivamente criadas no repositório.
- Milestone do F1-3X.
- Estado efetivo do workflow/auto-add do Project #1.
- Campos/vínculos internos do Project #1.
- Cadência final do F1-3X: 15 dias/ciclo no Process Document versus 17 dias/pack na ficha da iniciativa.

Próxima ação única: definir tema/Topic Pack do Ciclo 1 (#3) e resolver a cadência antes de calendarizar.
