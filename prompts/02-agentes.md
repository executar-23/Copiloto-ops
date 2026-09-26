# Prompt 2 — Entrada de agentes
O sistema atual tem duas plataformas: Notion como banco de informações e GitHub executar-23/Copiloto-ops como operação. Leia AGENTS.md, INSTRUCOES.md e docs/NOTION-ROTA.md.

Entre pelo Agent Runner, consulte o Master Index e a página Notion pertinente. Confirme URL, ID, objetivo e decisão antes de promover uma Task a Issue. Não invente ID, gate, owner ou Epic.

Abra Issues apenas no Copiloto-ops. Use título `[TIPO] <ID> — <descrição>` quando os campos forem confirmados. Inclua fonte Notion, critérios de aceite, dependências e aprovação pendente. Sem owner, registre A_DEFINIR; sem gate, gate:tbd. Confirme labels existentes e pai local antes de criar; vínculo textual não é sub-issue nativa.

WIP=1 por agente; agentes podem atuar simultaneamente com inspeção de mudanças concorrentes. Para arquivos, use main diretamente com sync → inspect → change → validate → commit → sync, sem force-push. Fechar uma Issue é execução, não aprovação. Só humano altera aprovação para aprovado. Após Issue/commit, registre o backlink e o resultado no Master Index. Decisões relevantes vão para ADRs.

Não coloque segredos no GitHub público. Permissões são independentes e links não sincronizam estado. Responda em pt-BR com números e links reais, validação, pendências e próxima ação única.
