# Protocolo operacional
## Entrada
Identifique objetivo, aceite e dados necessários. Consulte o [Runner](https://app.notion.com/p/3e7d1d673fb3814bbe40d200227da25c) e [Master Index](https://app.notion.com/p/3e7d1d673fb381109e31eee5060e1b62) no Notion. Consulte [docs/NOTION-ROTA.md](docs/NOTION-ROTA.md).

## Duas plataformas
- Notion: banco de informações, contexto, decisões, plano, tarefas planejadas e registro de saída.
- GitHub executar-23/Copiloto-ops: Issues operacionais, implementação versionada, evidências e estado de execução.

## Procedimento
1. Confirme URL/ID da página Notion e os identificadores nela presentes. Não invente relações.
2. Antes de abrir Issue, confirme escopo, Epic local, labels efetivamente existentes, gate, owner e capacidade de vínculo. Ausência de dado material: pergunte.
3. Inclua URL/ID Notion e critérios de aceite na Issue. Ao executar, registre Issue/commit e resultado no Master Index. Decisão relevante vai para ADR.
4. WIP=1 por agente; agentes diferentes podem atuar simultaneamente. approval:pendente inicial se disponível e aprovação só humana. Sem owner: A_DEFINIR. Sem gate: gate:tbd.
5. Para arquivos deste repositório, siga a regra 9 de [AGENTS.md](AGENTS.md): sync → inspect → change → validate → commit → sync diretamente em main. O racional está em [ADR-0001](docs/ADR-0001-AGENTES-DIRETO-MAIN.md). Inspecione alterações concorrentes, execute validações aplicáveis, revise diff, não force-push e pare diante de conflito sem resolução inequívoca. Observe CI e corrija/reverta regressões introduzidas.
6. Valide resultado nas duas plataformas. Links não sincronizam estado nem transferem permissões.

## Plugin executar-cop
Para operar pelo Claude Code ou pelo claude.ai, instale o plugin `executar-cop@copiloto-ops` e siga [docs/USO-EXECUTAR-COP.md](docs/USO-EXECUTAR-COP.md). Todo comando faz um pré-voo de dependências antes de agir. Componentes novos entram primeiro no índice `plugins/executar-cop/references/cmd-cop-index.md`.

## Saída
Informe páginas consultadas, Issue/commit, validações, pendências e próxima ação única. Não declare como criados Project, labels, milestones ou Epics que ainda são propostas.
