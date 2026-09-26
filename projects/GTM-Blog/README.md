# GTM-Blog

Projeto operacional do lançamento do GTM-Blog no repositório `executar-23/Copiloto-ops`.

## Estado

**Status:** Bootstrap  
**Fonte de verdade informacional:** Notion — GTM-Blog Launch Control  
**Execução e rastreabilidade:** GitHub — Copiloto-ops  
**GitHub Project:** Project #1 — URL fornecida pelo usuário  
**Branch operacional:** `main`

## GitHub Project

- Project informado: https://github.com/users/executar-23/projects/1
- Workflow informado: https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616
- Owner indicado pela URL: `executar-23`
- Project number indicado pela URL: `1`

A URL do Project e a URL do workflow foram fornecidas explicitamente pelo usuário. A integração GitHub disponível neste agente não expõe leitura ou escrita de GitHub Projects v2; portanto, título, campos, estado do workflow e vínculos internos não devem ser declarados como verificados ou aplicados sem evidência adicional.

## Automação do Project

Segundo a documentação oficial do GitHub, a automação integrada de inclusão de itens é configurada no próprio Project:

1. abrir o Project;
2. abrir o menu e entrar em **Workflows**;
3. selecionar **Auto-add to project**;
4. clicar em **Edit**;
5. selecionar o repositório `executar-23/Copiloto-ops`;
6. definir o filtro;
7. usar **Save and turn on workflow**.

O auto-add adiciona itens quando são criados ou atualizados e passam a corresponder ao filtro; ele não faz backfill automático de itens existentes. O filtro definitivo deve ser definido somente após aprovação do schema de Issues/labels.

Referência: https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically

## Fonte canônica

- Launch Control: https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac
- Agent Runner: https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c
- Master Index: https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62
- Foundation Doc: https://app.notion.com/p/3e7d1d673fb3815cb133cd8aeda89397
- ADRs: https://app.notion.com/p/3e7d1d673fb381aeb3e4dda7c9f37b61
- Tasks: https://app.notion.com/p/3e7d1d673fb381bd8f88e5c38979d403
- Plano de Implementação: https://app.notion.com/p/3e7d1d673fb381368574fa687f7cf0eb

## Hierarquia operacional

```text
Project #1
└── Epics
    └── Issues
        └── Sub-issues
```

O schema operacional foi definido em [docs/SCHEMA-TRABALHO.md](../../docs/SCHEMA-TRABALHO.md). Vínculos nativos só podem ser declarados quando efetivamente aplicados por ferramenta compatível.

## Regras

1. Toda execução deve apontar para a fonte Notion correspondente.
2. Nenhum ID, owner, gate, Epic ou dependência pode ser inventado.
3. Issues novas começam com aprovação pendente quando o schema de labels estiver configurado.
4. Decisões estruturais devem ser registradas em ADR.
5. Agentes autorizados trabalham diretamente em `main`, seguindo `sync → inspect → change → validate → commit → sync`.
6. O Master Index recebe backlinks de Issues, commits e resultados.
7. Não declarar configuração de Project/workflow como aplicada sem verificação.

## Primeiro Epic

O primeiro resultado operacional é `F1-3X`: três ciclos editoriais executados pelo [Runbook de Produção Editorial Multiplataforma](../../Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.md), cada um concluído em `100% VERIFIED`.

A cadência ainda precisa de decisão: o Process Document registra 15 dias/ciclo, enquanto a ficha F1-3X registra 17 dias/pack e cerca de 45 dias para o arco. Não fixar datas até resolver essa divergência.
