# Copiloto-ops
Operação do GTM-Blog em duas plataformas: **Notion como banco de informações** e **GitHub executar-23/Copiloto-ops como execução e rastreabilidade**.

## Entrada
- [AGENTS.md](AGENTS.md) — regras dos agentes.
- [CLAUDE.md](CLAUDE.md) e [INSTRUCOES.md](INSTRUCOES.md) — protocolo.
- [Notion ↔ GitHub](docs/NOTION-ROTA.md) — páginas e fluxo.
- [Modelo operacional](docs/MODELO-OPERACIONAL.md), [schema de trabalho](docs/SCHEMA-TRABALHO.md), [fontes](docs/FONTES.md) e [estado](docs/ESTADO.md).
- [Runbooks](Runbooks/README.md) — execução operacional repetível.
- [Prompt de configuração](prompts/01-bootstrap-copiloto-ops.md), [orientação de agentes](prompts/02-agentes.md) e [modelo de tarefa](templates/tarefa.md).

## Rota única
1. Entrar no [GTM-Blog — Launch Control](https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac), ler [00 — Agent Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) e consultar [01 — Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62).
2. Consultar a página Notion pertinente. Registrar a URL e o ID na Issue do [Copiloto-ops](https://github.com/executar-23/Copiloto-ops/issues).
3. Registrar no Master Index o número/link da Issue e a evidência de execução.

Links cruzados dão rastreabilidade; **não há sincronização automática**. Cada plataforma exige permissão própria.

## Criar tarefa
Confirme ID, fonte, escopo, aceite e Epic local. Título: `[TIPO] <ID> — <descrição>`. Se dados ou capacidade de vínculo faltarem, não crie issue órfã. Nenhuma issue nasce aprovada. Consulte o estado real: labels, milestones, Epic e Project ainda não estão configurados por esta documentação.

## Política de agentes
A instrução operacional obrigatória para agentes está em [AGENTS.md](AGENTS.md), inclusive trabalho direto em `main`, WIP=1, concorrência segura e o ciclo `sync → inspect → change → validate → commit → sync`. O README não é a fonte normativa dessa regra.

O contexto, a decisão e as consequências estão registrados em [ADR-0001 — Agentes de IA diretamente em main](docs/ADR-0001-AGENTES-DIRETO-MAIN.md).
