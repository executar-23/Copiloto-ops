# Patches pendentes
`executar-blog-copiloto-conector-remoto.patch` contém a mudança de código do Copiloto Operacional em `Sas-Executar/executar-Blog`: conector MCP remoto no Worker, `OPS_REPO` apontando para este repositório e a rota Notion/Gmail na skill. Esta sessão não tem push naquele repositório, por isso o patch está aqui.

Para aplicar (em um clone de `Sas-Executar/executar-Blog` com permissão de escrita):
```
git am /caminho/executar-blog-copiloto-conector-remoto.patch
npm ci && npm run check
```
Depois de aplicado lá, apague esta pasta.
