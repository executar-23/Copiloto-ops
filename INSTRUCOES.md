# Protocolo operacional
## Entrada
Identifique objetivo, modo, alvo, fontes e aceite. Consulte estado real; escolha uma única tarefa.
Alvo confirmado pelo usuário: executar-23/Copiloto-ops. Sas-Executar/OPS-COPILOTO não recebe novas alterações.

## Execução
1. Leia instruções e fontes. Verifique permissões e branch atual.
2. Confirme IDs, pai, owner e gates. Use gate:tbd quando faltar correspondência; pergunte se ID ou pai forem ambíguos.
3. Reutilize objetos; não duplique Epics sem necessidade e escopo explícitos.
4. Confirme ferramentas antes de criar. Sem capacidade de vinculação, prepare proposta, não tarefa órfã.
5. Preserve fontes e registre evidência. Valide conteúdo e ausência de segredos antes do commit.
6. Consulte políticas reais do alvo; não herde autorização de push do Blog.

## Conflitos de especificação
- Labels técnicas sugeridas pelo usuário não ampliam automaticamente o conjunto canônico.
- Issue Type é distinto de label type:*; Task/Bug/Feature/Epic não são autorização para novas labels.
- Milestone temporal e gate de governança são conceitos diferentes. A escolha entre releases e milestones por gate precisa de decisão explícita; não criar G00–G11 automaticamente.
- #2–#7 são exemplos do Blog; não são Issues deste repositório e não devem ser migradas sem pedido específico.
- Epic #37 pertence ao Copiloto. É referência canônica; não alegar hierarquia nativa entre repositórios sem verificar suporte e política.

## Saída
Informe status, commit, arquivos/objetos, links, testes, limitações e próxima ação. Separar execução de aprovação e documentação de configuração aplicada.
