# Copiloto-ops
Repositório-alvo: **executar-23/Copiloto-ops**. Operação e governança do GTM-Blog, com instruções para agentes e execução rastreável.

## Comece aqui
- [AGENTS.md](AGENTS.md): regras permanentes.
- [CLAUDE.md](CLAUDE.md): entrada para Claude.
- [INSTRUCOES.md](INSTRUCOES.md): protocolo operacional.
- [Modelo de operação](docs/MODELO-OPERACIONAL.md).
- [Fontes verificadas](docs/FONTES.md) e [estado](docs/ESTADO.md).
- [Prompt 1: configurar este repositório](prompts/01-bootstrap-copiloto-ops.md).
- [Prompt 2: orientar agentes](prompts/02-agentes.md).
- [Modelo de tarefa](templates/tarefa.md).

## Como abrir uma tarefa
Use [Issues deste repositório](https://github.com/executar-23/Copiloto-ops/issues).
Confirme ID e Epic, depois use `[TIPO] <ID> — <descrição>`. Informe objetivo, escopo, aceite, fontes, owner e dependências.
Selecione somente labels da [lista canônica](https://github.com/Sas-Executar/Copiloto/blob/claude/gifted-brown-7u1e5d/CLAUDE.md#labels-use-somente-estas). Toda issue nasce com approval:pendente. Owner desconhecido: A_DEFINIR, sem assignee. Gate desconhecido: gate:tbd.
Confirme o vínculo ao Epic; um link no corpo não substitui sub-issue. Se não houver ID ou Epic seguro, pergunte antes de criar.

## Limites
Copiloto é fonte do schema; executar-Blog é referência técnica. Não modificar esses repositórios nem Sas-Executar/OPS-COPILOTO neste bootstrap.
M2 identifica a iniciativa Executar Blog, não um novo ID inventado para este repositório.
Documentação pronta não significa labels, milestones ou hierarquia configurados; consulte o estado real.
