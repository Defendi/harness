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
2. Escrever testes unitários definindo o comportamento esperado (preferência por TDD).
3. Implementar a lógica de negócio e adapters de provedor em estrita conformidade com as especificações.
4. Executar ferramentas de formatação e linting localmente (`ruff check --fix`, `ruff format`).
5. Executar a suíte de testes local usando o ambiente virtual para garantir que todos os testes passem.
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
