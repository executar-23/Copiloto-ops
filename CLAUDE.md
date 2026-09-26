# Entrada para Claude
Leia [AGENTS.md](AGENTS.md), [INSTRUCOES.md](INSTRUCOES.md) e [docs/NOTION-ROTA.md](docs/NOTION-ROTA.md).

## Operação
Notion é o banco de informações; executar-23/Copiloto-ops é o único GitHub operacional desta arquitetura. Comece no Agent Runner, consulte o Master Index e registre fonte Notion ↔ Issue GitHub nos dois sentidos.
WIP=1 por agente, com concorrência segura e commit direto em main conforme a regra 9 de AGENTS.md. IDs devem estar confirmados na fonte. Issue nasce com approval:pendente quando disponível; aprovação é ato humano. Gate desconhecido: gate:tbd. Não criar issue órfã nem alegar sincronização automática.
