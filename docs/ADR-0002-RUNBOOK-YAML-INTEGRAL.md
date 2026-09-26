# ADR-0002 — Runbook editorial canônico em YAML integral

**Status:** Aceito  
**Data:** 2026-09-26  
**Escopo:** `Runbooks/RUN-F1-PRODUCAO-EDITORIAL-MULTIPLATAFORMA.yaml`

## Contexto

O Runbook F1 existente condensava o Process Document `PD-CLB-20260922-F01-DOC-V02` em um resumo Markdown. Isso removia detalhes operacionais necessários para execução e auditoria por agentes, incluindo campos Who/When/How/Output/Evidence/Done, matrizes completas, exceções, métricas e critérios.

## Decisão

O Runbook canônico passa a ser um arquivo YAML que transpõe integralmente o Process Document, preservando as seções 1–14 e os 22 passos detalhados. O arquivo Markdown anterior permanece apenas como ponte de compatibilidade para links históricos.

Novas referências operacionais devem apontar para o YAML.

## Consequências

- Agentes passam a consumir uma estrutura completa e parseável.
- O YAML não inventa owner, gate, aprovação ou dependência ausente no documento-fonte.
- Alterações futuras no processo devem preservar rastreabilidade com o documento-fonte e registrar decisão estrutural em ADR.
- O Markdown resumido deixa de ser fonte normativa.
