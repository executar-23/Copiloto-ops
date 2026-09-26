# Estado — arquitetura de duas plataformas
Data: 2026-09-26.

Decisão do usuário: **GitHub executar-23/Copiloto-ops** para operação; **Notion do projeto** como banco de informações. Referências a caminhos anteriores foram removidas das instruções ativas.

## Confirmado
- Este repositório contém instruções, prompts, modelo e mapa de páginas Notion.
- O workspace Notion conectado é o do projeto GTM-Blog; Runner, Master Index, Foundation, ADRs, Plano e Tasks foram lidos.
- GitHub e Notion possuem links cruzados documentados, sem sincronização automática.
- O usuário forneceu a URL `https://github.com/users/executar-23/projects/1` e a URL de workflow `https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616`.

## Política de commits
ADR de agentes em main aceito em 2026-09-26 e incorporado ao README/AGENTS/INSTRUCOES/CLAUDE e prompts. WIP=1 por agente, não exclusividade global. Locking/ownership de arquivos segue pendente; não presumir CI configurada.

Antes de escrever: sincronizar, inspecionar arquivos-alvo e HEAD remoto. Escrita deve ser fast-forward; conflito ou avanço concorrente exige interromper e reinspecionar.

## GitHub Project
A URL fornecida pelo usuário identifica o Project #1 do owner `executar-23`. A integração GitHub disponível neste agente não expõe GitHub Projects v2, então título, campos, workflow ativo e vínculos internos não estão independentemente verificados.

A documentação oficial do GitHub orienta configurar auto-add em **Project → Workflows → Auto-add to project → Edit → selecionar repositório/filtro → Save and turn on workflow**. Itens existentes não são adicionados retroativamente apenas por habilitar o workflow.

## Ainda não configurado/verificado
- Labels do inventário, milestones, Epic operacional e vínculos de sub-issues.
- Schema final de Issues e filtro do workflow auto-add.
- Estado efetivo do workflow do Project #1.
- O inventário `.github/labels.yml` é proposta local, não política aprovada nem labels aplicadas.

Próxima ação única: definir o schema de Issues/labels e o filtro do auto-add antes de criar Epics ou Issues.
