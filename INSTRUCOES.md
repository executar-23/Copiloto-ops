# Protocolo operacional
## Entrada
Identifique objetivo, modo, alvo, fontes e aceite. Consulte estado real; escolha uma única tarefa.
Alvo confirmado pelo usuário: executar-23/Copiloto-ops. Sas-Executar/OPS-COPILOTO não recebe novas alterações.

## Rota Notion ↔ GitHub
O hub Notion conectado é `hub.executar@gmail.com`: [Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) → [Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62). Consulte [docs/NOTION-ROTA.md](docs/NOTION-ROTA.md) para D01–D23 e o status do acesso externo. O Master Index do corpus `sas.executar@gmail.com` está mapeado, mas não acessível na conexão atual. Cada Issue deve apontar à fonte Notion confirmada; cada saída no índice deve apontar de volta à Issue/PR/commit. Permissão de uma plataforma não se transfere à outra.

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
