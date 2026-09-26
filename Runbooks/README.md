# Runbooks

Runbooks operacionais do Copiloto. Um Runbook descreve **como executar** um processo repetível; Epics e Issues descrevem **qual resultado entregar**.

O formato canônico dos Runbooks é YAML para permitir leitura estrutural por agentes e validação automatizada. Arquivos Markdown podem existir apenas como ponte de compatibilidade.

## Disponíveis
- [RUN-F1 — Produção Editorial Multiplataforma](RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.yaml)
  - [Overlay operacional F1-3X](RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.operational.yaml)

## Regra
1. A Issue aponta para o Runbook aplicável.
2. Cada execução registra evidência e estado.
3. Alteração estrutural do Runbook exige registro em ADR.
4. O Runbook não cria aprovação humana, owner, gate, Project ou vínculo nativo por si só.
