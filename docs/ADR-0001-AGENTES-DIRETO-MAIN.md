# ADR-0001 — Agentes de IA diretamente em main

**Status:** Aceito  
**Data:** 2026-09-26  
**Escopo:** `executar-23/Copiloto-ops`

## Regra normativa

A regra operacional obrigatória está em [AGENTS.md](../AGENTS.md). Este ADR registra a decisão e seu racional; agentes não devem depender deste documento nem do README para descobrir as regras de execução.

## Contexto

Branches e PRs concorrentes podem duplicar trabalho, divergir contexto e aumentar conflitos de integração. O repositório usa `main` como fonte única de verdade e adota ciclos curtos de integração.

## Decisão

Agentes autorizados trabalham diretamente em `main`, seguindo:

`sync → inspect → change → validate → commit → sync`

Cada agente mantém WIP=1, inspeciona mudanças recentes antes de editar, limita a alteração ao escopo recebido, valida o resultado, revisa o diff e produz commits pequenos, descritivos e reversíveis.

## Concorrência e segurança

- Estado obsoleto nunca deve sobrescrever trabalho recente.
- Edição concorrente exige sincronizar, reavaliar o diff e reaplicar apenas o que continuar válido.
- Conflito sem solução determinística interrompe a escrita automática.
- `push --force` em `main`, bypass de CI e alterações destrutivas sem recuperação explícita são proibidos.
- Mudanças de alto risco exigem validação adicional e mecanismo de recuperação apropriado.
- Ausência de CI não pode ser apresentada como CI aprovada.

## Consequências

O modelo reduz filas de merge e divergência de contexto, mas depende de validação rápida, observabilidade e rollback confiável.

**Pendente:** definir locking/ownership para casos em que agentes precisem modificar o mesmo módulo.
