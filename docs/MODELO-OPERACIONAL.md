# Modelo operacional — duas plataformas

| Plataforma | Responsabilidade | Estado |
|---|---|---|
| [Notion](https://app.notion.com/p/3e7d1d673fb381899d77e41b766525ac) | Banco de informações; Foundation, ADRs, Plano, Tasks e Master Index | Páginas do projeto acessíveis |
| [GitHub Copiloto-ops](https://github.com/executar-23/Copiloto-ops) | Agentes, Issues operacionais, commits e evidências | Instruções versionadas; objetos de planejamento ainda pendentes |

## Fluxo
Notion: Agent Runner → Foundation → ADR → Plano de Implementação → Tasks.
Master Index registra transversalmente a entrada e a saída.
GitHub: Task confirmada → Issue vinculada quando houver Epic/capacidade → execução → evidência.
Issue aponta para página Notion; Master Index aponta para Issue/commit. Isso não é integração automática.

Project, Epic, labels e milestone são opções de organização no GitHub, mas sua existência deve ser verificada antes de uso. Gate e aprovação dependem de decisões e configuração efetiva; não inferir.
