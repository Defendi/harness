---
name: implementation
description: Translate approved specifications and architectural models into clean, maintainable, type-annotated code and unit tests. Use when implementing new features, components, or fixing bugs according to specifications.
---

# Skill de Implementação

## Propósito
Traduzir especificações e modelos arquiteturais aprovados em código limpo, manutenível, com anotações de tipo e testes unitários.

## Entradas
- Plano de Implementação (`docs/execution/<jira>-plan.md`)
- Documentos aprovados de Especificação e Arquitetura
- Perfil de linguagem (`.agents/languages/python/`)

## Pré-condições
- Gates de Arquitetura e Planejamento satisfeitos.
- Card do Jira movido para `Em Andamento` (status ID `3`).

## Procedimento
1. Criar ou fazer checkout da feature branch da tarefa (`feature/MCPS-xxx-...`).
2. **Verificar Contratos Prévios:** Confirmar que interfaces, classes, métodos e schemas estão explicitamente descritos no plano de implementação. Pausar caso haja contratos ausentes ou ambíguos (proibido inventar contratos).
3. **Ciclo TDD Mandatório (Testes Unitários):**
   - **Fase RED:** Escrever testes unitários herméticos em `tests/unit/` com base nos contratos pré-definidos e critérios Given-When-Then. Executar e comprovar a falha inicial.
   - **Fase GREEN:** Implementar o código mínimo estritamente necessário em `src/` para fazer os testes passarem.
   - **Fase REFACTOR:** Refatorar código, aplicar tipagem estrita (`mypy`) e formatação/lint (`ruff check --fix`, `ruff format`) mantendo os testes 100% verdes.
4. **Testes de Integração de Adaptadores (se aplicável):** Implementar testes em `tests/integration/` para validar adaptadores contra fixtures herméticas.
5. Executar a suíte completa de testes para garantir 100% de sucesso local.
6. Verificar se não há segredos ou dados sensíveis hardcoded ou registrados em logs.

## Saídas
- Código-fonte em `src/`
- Testes unitários em `tests/`
- Resultados limpos da execução dos testes

## Validação
- 100% dos testes unitários passando.
- Zero violações de linting e formatação.
- Anotações de tipo completas em assinaturas públicas.

## Condições de Falha
- Testes unitários falhando.
- Código divergindo das especificações aprovadas.
- Credenciais expostas ou tratamento inadequado de erros.
