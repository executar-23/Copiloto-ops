# Copiloto-ops
Operação do GTM-Blog em duas plataformas: **Notion como banco de informações** e **GitHub executar-23/Copiloto-ops como execução e rastreabilidade**.

## Entrada
- [AGENTS.md](AGENTS.md) — regras dos agentes.
- [CLAUDE.md](CLAUDE.md) e [INSTRUCOES.md](INSTRUCOES.md) — protocolo.
- [Notion ↔ GitHub](docs/NOTION-ROTA.md) — páginas e fluxo.
- [Modelo operacional](docs/MODELO-OPERACIONAL.md), [fontes](docs/FONTES.md) e [estado](docs/ESTADO.md).
- [Prompt de configuração](prompts/01-bootstrap-copiloto-ops.md), [orientação de agentes](prompts/02-agentes.md) e [modelo de tarefa](templates/tarefa.md).

## Rota única
1. Entrar no [GTM-Blog — Launch Control](https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac), ler [00 — Agent Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) e consultar [01 — Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62).
2. Consultar a página Notion pertinente. Registrar a URL e o ID na Issue do [Copiloto-ops](https://github.com/executar-23/Copiloto-ops/issues).
3. Registrar no Master Index o número/link da Issue e a evidência de execução.

Links cruzados dão rastreabilidade; **não há sincronização automática**. Cada plataforma exige permissão própria.

## Criar tarefa
Confirme ID, fonte, escopo, aceite e Epic local. Título: `[TIPO] <ID> — <descrição>`. Se dados ou capacidade de vínculo faltarem, não crie issue órfã. Nenhuma issue nasce aprovada. Consulte o estado real: labels, milestones, Epic e Project ainda não estão configurados por esta documentação.

## ADR — Agentes de IA diretamente em main

**Status: Aceito em 2026-09-26 por autorização explícita do usuário.** Esta política vale para o repositório `executar-23/Copiloto-ops`; não concede permissões em outros sistemas. A branch `main` é a fonte única de verdade. Agentes autorizados trabalham diretamente nela em ciclos curtos, sem branches de longa duração ou PRs paralelos como fluxo rotineiro.

### Contexto e decisão
Branches e PRs concorrentes podem duplicar trabalho, divergir contexto e aumentar conflitos de integração. Adotamos trunk-based development com estado compartilhado e o ciclo:

`sync → inspect → change → validate → commit → sync`

Cada agente deve sincronizar e inspecionar mudanças recentes nos arquivos afetados antes de editar; alterar apenas o escopo recebido em unidades pequenas; executar validações pertinentes; revisar o diff; criar commits descritivos e reversíveis; sincronizar novamente e confirmar a integridade de `main`.

### Protocolo obrigatório
- **Antes:** sincronizar com `main`, verificar estado local/remoto e mudanças nos arquivos-alvo. Estado obsoleto nunca deve sobrescrever trabalho recente.
- **Durante:** preservar APIs e contratos não relacionados; evitar refactors oportunistas; separar mudanças independentes em commits próprios.
- **Antes do commit:** executar formatter, lint, typecheck, testes e build quando aplicáveis; revisar o diff completo. Se uma validação obrigatória falhar, não enviar o commit. Para mudanças exclusivamente documentais, conferir links, conteúdo, escopo e ausência de segredos.
- **Depois:** confirmar o commit em `main`, acompanhar CI quando existir e corrigir ou reverter imediatamente regressões introduzidas. Se não houver CI configurada, não alegar que passou.

### Concorrência e segurança
Agentes podem atuar simultaneamente, mas cada agente mantém **uma alteração ativa por vez**. Ninguém assume exclusividade do repositório. Ao detectar edição concorrente: `sync → reavaliar diff → reaplicar somente o que ainda é válido → validar`. Conflito sem solução determinística interrompe a escrita automática; não apague alterações desconhecidas.

`main` deve permanecer executável e recuperável. Mudanças de alto risco exigem validação adicional, feature flag ou mecanismo equivalente e recuperação comprovada. São proibidos `push --force` em `main`, ignorar CI obrigatória, misturar alterações independentes, ou executar mudanças destrutivas irreversíveis sem recuperação explícita. Proteções e bloqueios de permissão não devem ser contornados.

### Consequências e evolução
Benefícios esperados: menos filas de merge, menor divergência de contexto, integração contínua e feedback rápido. O modelo depende de validação rápida, observabilidade e rollback confiável. **Pendente:** definir locking/ownership de arquivos e regra para agentes que precisem modificar o mesmo módulo. Até lá, conflito sobreposto exige coordenação ou pausa.
