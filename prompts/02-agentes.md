# Prompt 2 — Instrução de entrada
Alvo: executar-23/Copiloto-ops. Abra aqui as tarefas desta operação. Sas-Executar/Copiloto é fonte do schema; executar-Blog é contexto técnico, não destino automático.

Leia AGENTS.md, CLAUDE.md e docs/FONTES.md. Use título [TIPO] <ID> — <descrição>. Preserve IDs canônicos. M2 identifica Executar Blog e foi confirmado em manifest-03.json e Epic #37 do Copiloto; revalide sua aplicabilidade.

Escolha labels somente da lista canônica. Inclua type adequado, approval:pendente e gate confirmado ou gate:tbd; área quando comprovada e prioridade conforme política. Registre portfolio_id no corpo, sem criar label de portfólio por inferência.

Confirme Epic e capacidade de sub-issue antes de criar tarefa. Valide vínculo real; URL no corpo não basta. Epic #37 de outro repositório é referência, não prova de pai nativo. Pergunte se ID ou pai forem ambíguos.

Owner desconhecido: A_DEFINIR, sem assignee. WIP=1. Fechar é execução; aprovação só muda por ação humana explícita. Gate indefinido admite gate:tbd, mas não autoriza inventar relações enquanto GAP-DEP-01 impedir mapeamento.

A planilha canônica prevalece sobre GitHub; divergência exige type:conflict com ambas as versões e fontes. Preserve a hierarquia ao registrar conflitos. Nenhum segredo em arquivos, issues ou comentários.

Project organiza; Epic agrupa; issue define entrega; sub-issue divide; checklist detalha; milestone marca meta temporal; commit/PR implementa. Issue Types e labels não se confundem.

Responda em pt-BR, até 500 palavras: resultado, números/links reais, validações, bloqueios e próxima ação. Não afirme criação, dependência ou aprovação sem evidência.
