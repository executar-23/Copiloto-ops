# GTM-Blog

Projeto operacional do lançamento do GTM-Blog no repositório `executar-23/Copiloto-ops`.

## Estado

**Status:** Bootstrap  
**Fonte de verdade informacional:** Notion — GTM-Blog Launch Control  
**Execução e rastreabilidade:** GitHub — Copiloto-ops  
**GitHub Project nativo:** GTM-Blog — Project #1  
**Branch operacional:** `main`

## GitHub Project canônico

- Project: https://github.com/users/executar-23/projects/1
- Workflow informado: https://github.com/users/executar-23/projects/1/workflows/21a1dc6e-8b27-46e0-893d-178005569616
- Owner: `executar-23`
- Project number: `1`

O Project #1 foi confirmado pelo usuário como o Project nativo a ser usado para o GTM-Blog. O repositório operacional vinculado ao trabalho continua sendo `executar-23/Copiloto-ops`.

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
GitHub Project #1 — GTM-Blog
└── Epics
    └── Issues
        └── Sub-issues
```

A criação de Epics, Issues, labels, milestones e vínculos nativos deve ocorrer somente após confirmação do schema operacional e da capacidade de vínculo no GitHub.

## Regras

1. Toda execução deve apontar para a fonte Notion correspondente.
2. Nenhum ID, owner, gate, Epic ou dependência pode ser inventado.
3. Issues novas começam com aprovação pendente quando o schema de labels estiver configurado.
4. Decisões estruturais devem ser registradas em ADR.
5. Agentes autorizados trabalham diretamente em `main`, seguindo `sync → inspect → change → validate → commit → sync`.
6. O Master Index recebe backlinks de Issues, commits e resultados.
7. O Project #1 é o quadro canônico de acompanhamento do GTM-Blog.

## Próxima decisão

Definir o schema operacional do GitHub para o GTM-Blog:

- tipos de Epic e Issue;
- labels obrigatórias;
- status;
- milestones;
- campos do Project;
- convenção de IDs;
- regras de parent/child e sub-issues;
- critérios de aprovação e fechamento.
