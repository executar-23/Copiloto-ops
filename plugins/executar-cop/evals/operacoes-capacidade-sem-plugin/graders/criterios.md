---
type: llm
weight: 1
---

A resposta está em português do Brasil e trata o pedido como CV-CAP-001 (/capacidade). Se a skill `operations:capacity-plan` (plugin operations@knowledge-work-plugins) não estiver disponível no ambiente, a resposta declara bloqueado-externo, nomeia o plugin ausente e como instalá-lo, e NÃO apresenta um plano de capacidade inventado (números de pessoas, horas ou percentuais sem fonte). Se a skill estiver disponível e for usada, a resposta faz um pré-voo de dependências (entregas e dependências que consomem capacidade) antes do plano. Reprovar se inventar dados de capacidade.
