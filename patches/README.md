# Patches pendentes
`executar-blog-copiloto-conector-remoto.patch` contém 4 commits para `Sas-Executar/executar-Blog`: (1) conector MCP remoto no Worker, `OPS_REPO` apontando para este repositório e a rota Notion/Gmail na skill; (2) o novo status report "processo" (DOC-0066) com placeholders; (3) o id real do D1 `copiloto-ledger`, já criado no Cloudflare com a migration aplicada; (4) a convenção de labels deste repositório (schema aprovado).

`exemplo-status-real-copiloto-ops.html` é o status report "processo" gerado com as issues reais #9–#12, a partir de um instantâneo lido pelo conector GitHub, sem escrita.

`exemplo-status-processo.html` é um render do novo status report com dados simulados (campanha WF-CAMP-001, instância RC-F01), só para conferência visual. Esta sessão não tem push naquele repositório, por isso o patch está aqui.

Para aplicar (em um clone de `Sas-Executar/executar-Blog` com permissão de escrita):
```
git am /caminho/executar-blog-copiloto-conector-remoto.patch
npm ci && npm run check
```
Depois de aplicado lá, apague esta pasta.
