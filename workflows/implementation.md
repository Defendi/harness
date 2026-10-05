# Workflow de Implementação

## Gatilho
Coleta de um card em `A Fazer` pelo subagent desenvolvedor.

## Pré-condições
- Card em `A Fazer`.
- Plano de implementação aprovado.

## Etapas
1. Transicionar o card do Jira de `A Fazer` para `Em Andamento` (status ID `3`, transition `40`).
2. Adicionar comentário no Jira sinalizando o início do desenvolvimento.
3. Criar/fazer checkout da feature branch: `feature/<jira>-<short-description>`.
4. Implementar testes unitários e o código de produção correspondente.
5. Executar formatação local de código (`ruff format`) e linting (`ruff check --fix`).
6. Executar testes locais dentro do ambiente virtual (`.venv/bin/pytest`).
7. Assim que a implementação e os testes estiverem 100% verdes, transicionar o card para `Pronto para Review` (status ID `10099`, transition `50`).
8. Adicionar comentário no Jira com o resumo do diff e prontidão para review.

## Artefatos
- Código-fonte de produção (`src/`)
- Testes unitários (`tests/`)
- Logs de testes aprovados

## Quality Gates
- Implementation Gate: zero erros de compilação/sintaxe, 100% dos testes unitários passando, zero código de debug não commitado.

## Condições de Saída
- Card movido para `Pronto para Review`.

## Tratamento de Falhas
- Se a implementação encontrar ambiguidades arquiteturais bloqueantes, reportar o apontamento ao arquiteto e pausar o desenvolvimento.
