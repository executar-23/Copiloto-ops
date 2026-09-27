# Estado — arquitetura de duas plataformas
Data: 2026-09-26 (atualizado em 2026-09-27 com o plugin executar-cop).

Decisão do usuário: **GitHub executar-23/Copiloto-ops** para operação; **Notion do projeto** como banco de informações. Referências a caminhos anteriores foram removidas das instruções ativas.

## Confirmado
- Este repositório contém instruções, prompts, modelo e mapa de páginas Notion.
- O workspace Notion conectado é o do projeto GTM-Blog; Runner, Master Index, Foundation, ADRs, Plano e Tasks foram lidos.
- GitHub e Notion possuem links cruzados documentados, sem sincronização automática.
- O usuário forneceu a URL `https://github.com/users/executar-23/projects/1` e a URL de workflow `https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616`.
- A documentação local AIKB fornecida em 2026-09-26 foi versionada em `projects/GTM-Blog/knowledge/`.
- A árvore real está em `docs/ARVORE-REPOSITORIO.md`; a arquitetura-alvo está em `docs/ARVORE-PROJETO-ALVO.txt`.
- A subissue operacional #6 foi criada com `Parent: #3` para concentrar a preparação e a submissão do hardcode de 2026-09-27.
- O scaffold creator-led foi materializado diretamente na raiz do `executar-23/Copiloto-ops`: 143 caminhos `.gitkeep`, commit `48653d8a13374bb9f9efec9323d9193b0bbeeabc`, validação 143/143.
- `SETUP-001` está concluído na Issue #7; o repositório separado `executar-23/creator-led-platform` não existe e não deve ser usado como destino.

- Plugin `executar-cop` versionado em `plugins/executar-cop/` com marketplace `copiloto-ops` em `.claude-plugin/marketplace.json`. Ele contém:
  - o Orquestrador CMD-COP;
  - 28 commands (IDs verbais);
  - 4 agentes;
  - 4 skills proprietárias;
  - o núcleo transversal de dependências;
  - o grafo;
  - o token do calendário.

  Rastreio: Issue #24. Decisão: [ADR-0003](ADR-0003-PLUGIN-EXECUTAR-COP.md). Fonte: [HANDOFF-AGENTES-001](architecture/HANDOFF-AGENTES-001.md).
- A regra 8 do AGENTS.md foi atualizada em 2026-09-27: conteúdo proprietário do EXECUTAR é permitido, e segredos, credenciais, tokens e dados pessoais continuam proibidos.

## Política de commits
ADR de agentes em main aceito em 2026-09-26. A regra operacional está em AGENTS.md e é repetida nos pontos de entrada necessários; o racional está em `docs/ADR-0001-AGENTES-DIRETO-MAIN.md`. O README apenas aponta para essas fontes. WIP=1 por agente, não exclusividade global. Locking/ownership de arquivos segue pendente; não presumir CI configurada.

Antes de escrever: sincronizar, inspecionar arquivos-alvo e HEAD remoto. Escrita deve ser fast-forward; conflito ou avanço concorrente exige interromper e reinspecionar.

## GitHub Project
A URL fornecida pelo usuário identifica o Project #1 do owner `executar-23`. A integração GitHub disponível neste agente não expõe GitHub Projects v2, então título, campos, workflow ativo e vínculos internos não estão independentemente verificados.

A documentação oficial do GitHub orienta configurar auto-add em **Project → Workflows → Auto-add to project → Edit → selecionar repositório/filtro → Save and turn on workflow**. Itens existentes não são adicionados retroativamente apenas por habilitar o workflow.

## Estrutura operacional definida
- Schema de Epic → Issue → Sub-issue → checklist: `docs/SCHEMA-TRABALHO.md`.
- Runbook editorial: `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.yaml`.
- Overlay operacional do F1-3X: `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.operational.yaml`.
- Epic criado: #2 — `F1-3X`.
- Issues de ciclo: #3, #4 e #5.
- Subissue documental/operacional: #6, parent textual #3. A integração não expõe vínculo nativo; não declarar vínculo nativo aplicado.
- O arquivo `.github/labels.yml` registra o estado desejado do schema; não comprova criação/aplicação das labels no GitHub.

## Plugin executar-cop — pendências
- A planilha `EXECUTAR_HUB_Control_Plane_v2.xlsx` real não foi recebida. O especialista `executar-dependency-architect` foi validado só com uma fixture fictícia.
- A definição do PF-24 (reconciliação cruzada) não foi fornecida.
- As skills da conta `copiloto-executar` e `executar-mapa-os` são dependências externas, com fonte fora deste repositório.
- Os plugins `operations`, `productivity` e `product-management` (`knowledge-work-plugins`) são pré-requisitos documentados, não `dependencies`. Quando faltam, o resultado é bloqueado-externo.
- Aprovação da Issue #24, Gate (`gate:tbd`) e owner (`A_DEFINIR`) dependem de decisão humana.

## Ainda não configurado/verificado
- Labels efetivamente criadas no repositório.
- Milestone do F1-3X.
- Estado efetivo do workflow/auto-add do Project #1.
- Campos/vínculos internos do Project #1.
- Cadência final do F1-3X: 15 dias/ciclo no Process Document versus 17 dias/pack na ficha da iniciativa.
- Gate da subissue #6 permanece `gate:tbd`; fonte Notion e owner já estão registrados.

## Próxima ação única
Continuar #6 em **2026-09-27** apenas para hardcode/artefatos concretos ainda não versionados; o scaffold estrutural já foi concluído em #7. Depois, retomar o Topic Pack do Ciclo 1 (#3).
