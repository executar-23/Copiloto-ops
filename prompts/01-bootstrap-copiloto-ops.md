# Prompt 1 — Configuração de Issues no Copiloto-ops
## Objetivo
Configurar exclusivamente executar-23/Copiloto-ops para transformar tarefas confirmadas do Notion em Issues rastreáveis.

## Entrada
Leia AGENTS.md, INSTRUCOES.md, docs/NOTION-ROTA.md e o Agent Runner/Master Index do Notion. Confirme com o usuário IDs, hierarquia, labels, milestones e gate antes de aplicar um esquema ainda não aprovado. WIP=1 por agente, com concorrência segura conforme ADR aceito no README; nenhuma Issue nasce aprovada.

## Execução
1. Inventarie o estado real do GitHub: permissões, branch, labels, Issues, Epic, Project e milestones.
2. Compare o inventário local .github/labels.yml com a decisão atual do usuário. É proposta, não configuração aplicada. Não crie labels automaticamente.
3. Defina com o usuário o Epic local, tipos, labels e milestones que serão usados. Não invente IDs ou prazos.
4. Descubra ferramentas reais de criação/vinculação. Se não houver capacidade de vínculo, não crie sub-issues órfãs; registre pendência.
5. Para cada tarefa aprovada para execução, registre URL/ID Notion, objetivo, aceite, owner, gate e vínculo; depois registre backlink no Master Index.
6. Valide mudanças, ausência de segredos e aprovação inicial pendente. Faça commits pequenos diretamente em main, sem force-push; sincronize, inspecione diff, valide e acompanhe CI conforme ADR aceito no README.

## Saída
Reporte objetos realmente criados, números/links, validação e decisões pendentes. Não confunda documentação com configuração aplicada nem fechamento com aprovação humana.
