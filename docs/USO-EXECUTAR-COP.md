# Como usar o plugin executar-cop (v0.3.0)

## 1. Instalar

### Claude Code (terminal)
```text
/plugin marketplace add executar-23/Copiloto-ops
/plugin install executar-cop@copiloto-ops
```
Depois rode `/reload-plugins`, ou abra uma sessão nova. Para atualizar, use `/plugin marketplace update copiloto-ops`.

### Pelo zip (sem marketplace)
Descompacte `executar-cop-v0.3.0.zip` e rode `claude --plugin-dir <pasta>/executar-cop`.

### claude.ai / Cowork
Vá em Settings → Plugins → Add marketplace → `executar-23/Copiloto-ops` e instale o `executar-cop`.

Conecte as ferramentas em Settings → Connectors (Notion, Gmail, GitHub, Slack etc.). As categorias estão em `plugins/executar-cop/CONNECTORS.md`.

## 2. Como falar com ele
Existem três formas equivalentes de pedir a mesma coisa:
- **Slash:** `/bomdia`.
- **Frase:** "Bom dia, copiloto".
- **Agente de entrada:** `claude --agent executar-cop:orquestrador-cop`, para que toda conversa passe pelo orquestrador.

Você não precisa informar o módulo. O orquestrador resolve o ID verbal (`CV-XXX-NNN`), faz o **pré-voo de dependências** e só então executa. Se algo depende de outra etapa, ele avisa antes, por exemplo: "`/arvore` depende de `/dependencias`".

## 3. Os 40 comandos

| Grupo | Comandos |
|---|---|
| Rotina do dia | `/bomdia` `/agora` `/estado` `/fechardia` `/replanejamento` `/mapa` `/evidencia` `/bloqueio` |
| Produtividade | `/iniciar` `/tarefas` `/atualizar` `/atualizar-abrangente` `/contexto` `/memoria` |
| Operações | `/capacidade` `/mudanca` `/processo` `/procedimento` `/situacao` `/fornecedor` `/risco` `/conformidade` `/otimizar` |
| Produto | `/roadmap` `/spec` `/pesquisa` `/concorrencia` `/metricas` `/brainstorm` `/sprint` `/stakeholders` `/produto-codigo` |
| Cadeia proprietária | `/dependencias` → `/arvore` → `/arvore-visual` → `/editorial` |
| Setup e execução | `/personalizar-plugin` `/criar-plugin` `/plano` `/execucao` |

A lista completa, com IDs, sinônimos e aliases (`ARVOREKIT`, `/planejar-capacidade` etc.), está em `plugins/executar-cop/references/cmd-cop-index.md`.

## 4. Roteiros de uso
- **Começar o dia:** `/bomdia`, depois `/agora`. Ao terminar, `/fechardia`. Se algo travar, use `/bloqueio`. Se o plano mudar, use `/replanejamento`.
- **Primeira vez com tarefas:** `/iniciar` cria `TASKS.md`, `memory/` e o dashboard. Depois use `/tarefas` e `/atualizar`.
- **Preencher o Control Plane:**
  1. `/dependencias <caminho>/EXECUTAR_HUB_Control_Plane_v2.xlsx` entrega o 16_REG, o mapa e as fases.
  2. Valide as decisões pendentes (seção "Lacunas" da entrega).
  3. Cole `registro_para_colar.csv` no 16_REG.
  4. Rode `/arvore kit`, `/arvore-visual` e `/editorial`.

  A primeira execução está em `projects/EXECUTAR-HUB/control-plane/PF-24/`.
- **Da ideia ao código:** `/brainstorm` → `/spec` → `/roadmap` → `/sprint` → `/produto-codigo`.
- **Planejar antes de executar qualquer tarefa grande:** `/plano`.

## 5. O que esperar das respostas
- As respostas vêm em português do Brasil, com uma ação principal.
- Toda resposta fecha com `Dependências de entrada → Saída → Gate`.
- Saídas visuais seguem o token do calendário: branco, preto, e vermelho só para hoje, prioridade ou item atual.
- Quando o assunto depende de fato externo, a resposta passa por busca web e cita fontes.
- O plugin nunca simula o que não tem:
  - skill da conta ausente (`copiloto-executar`, `executar-mapa-os`) ou arquivo que falta: `bloqueado-externo`;
  - etapa anterior não concluída: `bloqueado-interno`;
  - dado sem fonte: `GAP`.

## 6. Manutenção
```bash
python3 plugins/executar-cop/scripts/validar_plugin.py      # índice, grafo, cobertura total de IDs
claude plugin validate plugins/executar-cop --strict
claude plugin eval plugins/executar-cop --runs 1 --trust-plugin --no-publish
```
Regra: todo componente novo entra primeiro no índice (`cmd-cop-index.md`) e no grafo, e só depois vira arquivo.
