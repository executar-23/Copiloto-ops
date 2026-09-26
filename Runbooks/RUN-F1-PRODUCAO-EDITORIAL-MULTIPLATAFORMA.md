# RUN-F1 — Produção Editorial Multiplataforma

**Fonte:** Process Document Produção Editorial Multiplataforma `PD-CLB-20260922-F01-DOC-V02`  
**Epic inicial:** `F1-3X`  
**Owner:** `executar-23`  
**Cadência documental:** 15 dias/ciclo no Process Document. A ficha F1-3X registra 17 dias/pack. O calendário operacional importado do ZIP cobre 15 unidades editoriais de 2026-09-28 a 2026-10-16; ele não substitui silenciosamente a cadência do ciclo completo.


## Rastreio operacional — F1-3X

- **Epic:** [#2 — F1-3X](https://github.com/executar-23/Copiloto-ops/issues/2)
- **Assignee/owner operacional:** `executar-23`
- **Preparação técnica:** [#6](https://github.com/executar-23/Copiloto-ops/issues/6)
- **SETUP-001:** [#7](https://github.com/executar-23/Copiloto-ops/issues/7) — 2026-09-27 — porta `G-SCAFFOLD`
- **Documento editorial mestre:** `DOC-20260926-0002`
- **Documento de arquitetura:** `DOC-20260926-0003`

### Ciclo 1 / Pilar 1 — Riscos Cognitivos
- Issue de ciclo: [#3](https://github.com/executar-23/Copiloto-ops/issues/3)
- Janela: **2026-09-28 → 2026-10-02**
- Unidades: #8–#12
- Porta final: `G-PILAR1`

### Ciclo 2 / Pilar 2 — Processos Neuroadaptativos
- Issue de ciclo: [#4](https://github.com/executar-23/Copiloto-ops/issues/4)
- Janela: **2026-10-05 → 2026-10-09**
- Unidades: #13–#17
- Porta final: `G-PILAR2`

### Ciclo 3 / Pilar 3 — Ferramentas e Soluções
- Issue de ciclo: [#5](https://github.com/executar-23/Copiloto-ops/issues/5)
- Janela: **2026-10-12 → 2026-10-16**
- Unidades: #18–#22
- Porta final: `G-PILAR3`

As janelas acima vêm de `blog-riscos-cognitivos-tres-pilares_DADOS.csv`. A associação ciclo↔pilar foi registrada como direção operacional e deve ser confirmada no Topic Pack de cada ciclo antes de promover o estado para `STRUCTURED`.

## Objetivo
Executar um ciclo editorial rastreável em que uma peça-mãe profunda e citável gera derivados nativos por canal, com governança, revisão e handoff controlado.

## Entrada mínima
- sinal de dor real;
- tema do ciclo com encaixe de nicho;
- fontes/evidências para claims;
- posição no roadmap/arco temático;
- Topic Pack com título, claim central, CTA e ferramenta associada.

## Saída por ciclo
- 1 artigo-mãe, 1.800–2.400 palavras;
- 1 roteiro de vídeo-mãe, 8–12 min;
- 4 vídeos verticais;
- 6 carrosséis;
- 6 imagens estáticas;
- 3 infográficos 16:9;
- 10–12 stories;
- 3 newsletters;
- 3 ebooks;
- 6 CTAs de ferramenta;
- pacote de handoff para a Fase 2, com briefings, specs, nomes e evidências.

## Estados
| Estado | Evidência mínima |
|---|---|
| 0% PLANNED | tema, objetivo e owner de ciclo registrados |
| 33% STRUCTURED | Topic Pack, fontes, outline e dependências estruturados |
| 66% IMPLEMENTED | peça-mãe funcional e derivados em produção |
| 99% PRODUCED | pacote organizado, aguardando revisão final/handoff |
| 100% VERIFIED | pacote revisado, evidenciado e aceito pela etapa seguinte |

## Execução — 22 passos

### Grupo A — Entrada + Topic Pack
1. Validar tema, dor e encaixe de nicho.
2. Pesquisar evidências e fontes citáveis.
3. Fechar Topic Pack, CTA e ferramenta associada.

### Grupo B — Peça-mãe
4. Estruturar outline com Claim/Evidência/Exemplo/Interpretação.
5. Redigir artigo-mãe de 1.800–2.400 palavras, com exemplos e tutorial.
6. Revisar estilo editorial.
7. Otimizar GEO/SEO e citabilidade.
8. Criar roteiro do vídeo-mãe de 8–12 min.
9. Marcar trechos/timestamps que originam derivados.

### Grupo C — Derivados
10. Produzir banco de textos curtos.
11. Roteirizar 4 vídeos verticais.
12. Criar copy/roteiro de 6 carrosséis.
13. Criar copy de 6 imagens estáticas.
14. Briefar 3 infográficos 16:9.
15. Criar sequência de 10–12 stories.
16. Criar 3 newsletters.
17. Criar outline e redação de 3 ebooks.
18. Mapear 6 CTAs de ferramenta.

### Grupo D — Coerência + governança
19. Checar coerência do arco temático.
20. Aplicar nomenclatura e indexação a todos os arquivos.
21. Executar checklist de conformidade pré-handoff.

### Grupo E — Handoff
22. Entregar pacote para a Fase 2 com specs por asset e confirmação de recebimento.

## Regras de qualidade
- Cada claim relevante deve ter fonte identificável.
- Derivado deve ser adaptação nativa; não iniciar do zero sem relação com a peça-mãe.
- Aprovação editorial ausente bloqueia handoff/publicação.
- Arquivo sem nomenclatura/índice permanece em 99% PRODUCED.
- Nova ideia durante WIP vai para fila do próximo ciclo.
- Automação parcial deve registrar efeitos produzidos e evitar duplicidade.

## Definition of Done do ciclo
- [ ] Tema nasce de dor/demanda registrada.
- [ ] Topic Pack completo.
- [ ] Peça-mãe atende profundidade, estilo e GEO.
- [ ] Derivados adaptados por canal.
- [ ] Assets nomeados, indexados e vinculados ao ciclo.
- [ ] Checklist de conformidade concluído.
- [ ] Handoff aceito pela Fase 2 com evidência.
- [ ] Estado `100% VERIFIED` somente com comprovação objetiva.

## Uso no F1-3X
Executar este Runbook três vezes em sequência. Cada execução é uma Issue de ciclo. O Epic fecha somente quando os três ciclos estiverem `100% VERIFIED`.
