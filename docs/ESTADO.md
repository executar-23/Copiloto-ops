# Estado — arquitetura de duas plataformas
Data: 2026-09-26.

Decisão do usuário: **GitHub executar-23/Copiloto-ops** para operação; **Notion do projeto** como banco de informações. Referências a caminhos anteriores foram removidas das instruções ativas.

## Confirmado
- Este repositório contém instruções, prompts, modelo e mapa de páginas Notion.
- O workspace Notion conectado é o do projeto GTM-Blog; Runner, Master Index, Foundation, ADRs, Plano e Tasks foram lidos.
- GitHub e Notion possuem links cruzados documentados, sem sincronização automática.
- O usuário forneceu a URL `https://github.com/users/executar-23/projects/1` e a URL de workflow `https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616`.
- A documentação local AIKB fornecida em 2026-09-26 foi versionada em `projects/GTM-Blog/knowledge/`.
- A árvore real está em `docs/ARVORE-REPOSITORIO.md`; a arquitetura-alvo está em `docs/ARVORE-PROJETO-ALVO.txt`.
- A subissue operacional #6 foi criada com `Parent: #3` para concentrar a preparação e a submissão do hardcode de 2026-09-27.

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
- Subissue documental/operacional: #6, parent textual #3. A integração não expõe vínculo nativo; não declarar vínculo nativo aplicado.
- O arquivo `.github/labels.yml` registra o estado desejado do schema; não comprova criação/aplicação das labels no GitHub.

## Ainda não configurado/verificado
- Labels efetivamente criadas no repositório.
- Milestone do F1-3X.
- Estado efetivo do workflow/auto-add do Project #1.
- Campos/vínculos internos do Project #1.
- Cadência final do F1-3X: 15 dias/ciclo no Process Document versus 17 dias/pack na ficha da iniciativa.
- Fonte Notion específica e owner/gate da subissue #6.

## Próxima ação única
Em **2026-09-27**, executar #6: inventariar todo hardcode local disponível, validar segredos/credenciais, mapear cada artefato para a árvore-alvo, versionar somente artefatos concretos em `main`, validar o resultado e registrar evidências. Após #6, retomar o Topic Pack do Ciclo 1 (#3).
