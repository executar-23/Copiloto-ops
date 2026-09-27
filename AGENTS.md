# Regras para agentes
Escopo: executar-23/Copiloto-ops.

1. A arquitetura atual tem somente Notion (banco de informações) e este GitHub (execução e rastreabilidade). Leia README.md, INSTRUCOES.md, docs/NOTION-ROTA.md, docs/ESTADO.md e, antes de criar ou decompor trabalho, docs/SCHEMA-TRABALHO.md. Para execução repetível, use o Runbook correspondente em Runbooks/.
2. Entre pelo Agent Runner e Master Index do Notion. Consulte apenas páginas do workspace conectado necessárias à tarefa. Registre URL/ID da página-fonte na Issue e backlink da Issue/commit no índice.
3. WIP=1 por agente: uma alteração ativa por agente, admitindo agentes simultâneos. Preserve IDs registrados no Notion; não invente ID, gate, Epic, owner ou dependência.
4. Sem owner confirmado, registre A_DEFINIR e não atribua assignee. Gate indefinido: gate:tbd. Se o esquema de labels ainda não estiver aprovado/configurado, registre a classificação no corpo e peça decisão antes de criar objeto que dependa dela.
5. Toda Issue nova começa com approval:pendente quando a label estiver disponível. Só ação humana explícita permite approval:aprovado. Fechar é execução, não aprovação.
6. Confirme Epic local e ferramenta de vínculo antes de criar sub-issue; link textual não é vínculo nativo. Não declare como aplicado o que existe só em documentação.
7. Decisões de produto, arquitetura, processo ou integração devem ser registradas em 03 — ADRs. O Master Index é registro transversal; não substitui a fonte.
8. Não publique segredos, credenciais, tokens nem dados pessoais de terceiros. Skills, agentes e documentação proprietária do EXECUTAR podem ser versionados aqui ([ADR-0003](docs/ADR-0003-PLUGIN-EXECUTAR-COP.md)). Acesso ao Notion e ao GitHub são independentes; bloqueio de permissão exige parar a ação afetada.
9. Agentes autorizados trabalham diretamente em main pelo ciclo sync → inspect → change → validate → commit → sync. Verifique alterações concorrentes, revise diff e execute validações pertinentes antes de commit. Sem force-push, PR/branch paralela rotineira, sobrescrita silenciosa ou bypass de CI. Conflito não determinístico interrompe a escrita. Preserve alterações alheias e reporte evidência. Saída humana em pt-BR, até 500 palavras.

A política de trabalho direto em `main` é obrigatória por este próprio `AGENTS.md`; o agente não deve depender do README para descobri-la. O racional e o histórico da decisão estão em [ADR-0001](docs/ADR-0001-AGENTES-DIRETO-MAIN.md). A política não autoriza criação automática de objetos GitHub nem alteração de aprovação humana. Prompts documentam procedimentos e não executam configuração automaticamente.
