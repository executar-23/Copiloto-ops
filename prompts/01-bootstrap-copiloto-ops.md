# Prompt 1 — Bootstrap de Issues em Copiloto-ops
## Objetivo
Configurar executar-23/Copiloto-ops conforme schema de Sas-Executar/Copiloto: labels, hierarquia, milestones e documentação. Não modificar executar-Blog nem Sas-Executar/OPS-COPILOTO.

## Regras
Leia instruções locais, fonte canônica e manifest. Revalide M2 e Epic #37, confirmados em 2026-09-26. Consulte a planilha quando o protocolo canônico exigir. WIP=1; IDs literais; aprovação somente humana; nenhuma issue nasce aprovada. Sem owner: A_DEFINIR e sem assignee. Gate indefinido: gate:tbd. Nenhum segredo.

## Execução
1. Verifique alvo, branch, permissões e regras locais.
2. Confirme portfólio, Epic, lacunas e gates. Se ID ou pai forem ambíguos, pergunte.
3. Descubra ferramentas de labels, milestones e sub-issues no catálogo/ToolSearch, quando disponível. Não invente capacidades.
4. Inventarie labels existentes e compare com fonte canônica. Crie somente faltantes, sem alterar semântica. Verifique nome, cor e descrição retornados. Sem criação disponível, use .github/labels.yml como inventário declarativo e registre passos manuais; não afirme aplicação.
5. Resolva a política de milestones: metas temporais ou checkpoints por gate. Não crie datas/mapeamentos fictícios.
6. Reutilize Epic correto; se for necessário Epic operacional local M2, defina escopo e referência ao #37. Aplique type:portfolio-epic, approval:pendente e gate confirmado ou gate:tbd. Não finja vínculo nativo entre repositórios.
7. Só crie tarefas com IDs e pai confirmados e capacidade real de vínculo. Valide sub-issues no retorno.
8. Atualize AGENTS.md, CLAUDE.md e README.md deste alvo preservando conteúdo; referencie lista canônica sem copiá-la nessas páginas.
9. Valide, faça commit/push conforme política efetiva e registre evidências.
10. Não migre tarefas #2–#7 do Blog por inferência.

## Saída e validação
Reporte labels criadas/existentes/pendentes; milestones e propósito; Epic local com número/link ou bloqueio; referência canônica, portfolio_id, gates, arquivos e commit.
Verifique labels exatas, approval:pendente inicial, vínculos reais e ausência de segredos.
Pare diante de bloqueios de permissão ou decisões materiais não resolvidas. Nunca declare configuração executada quando só houver proposta.
