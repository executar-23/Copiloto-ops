# ADR-0002 — Runbook editorial canônico em YAML integral

**Status:** Aceito  
**Data:** 2026-09-26  
**Escopo:** `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.yaml`

## Contexto

O Runbook F1 existente condensava o Process Document `PD-CLB-20260922-F01-DOC-V02` em um resumo Markdown. Isso removia detalhes operacionais necessários para execução e auditoria por agentes, incluindo campos Who/When/How/Output/Evidence/Done, matrizes completas, exceções, métricas e critérios.

## Decisão

O Runbook canônico passa a ser um arquivo YAML que transpõe integralmente o Process Document, preservando as seções 1–14 e os 22 passos detalhados. O arquivo Markdown anterior permanece apenas como ponte de compatibilidade para links históricos.

Novas referências ao processo devem apontar para o YAML canônico. Dados operacionais do F1-3X que não pertencem ao documento-fonte ficam separados em `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.operational.yaml`.

## Consequências

- Agentes passam a consumir uma estrutura completa e parseável.
- O YAML canônico não inventa owner, gate, aprovação ou dependência ausente no documento-fonte.
- O overlay operacional preserva owner, calendário, Issues e gates registrados fora do Process Document, inclusive a mudança concorrente do commit `0fe6430a2b8cf7e109376b4db3c9dbd04f4d8d38`.
- Alterações futuras no processo devem preservar rastreabilidade com o documento-fonte e registrar decisão estrutural em ADR.
- O Markdown resumido deixa de ser fonte normativa.
