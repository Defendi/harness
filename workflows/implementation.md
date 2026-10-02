# Implementation Workflow

## Trigger
Pickup of a card in `A Fazer` by developer subagent.

## Preconditions
- Card in `A Fazer`.
- Implementation plan approved.

## Steps
1. Transition Jira card from `A Fazer` to `Em Andamento` (status ID `3`, transition `40`).
2. Add Jira comment signaling start of development.
3. Create/checkout feature branch: `feature/<jira>-<short-description>`.
4. Implement unit tests and corresponding production code.
5. Execute local code formatting (`ruff format`) and linting (`ruff check --fix`).
6. Run local tests within the virtual environment (`.venv/bin/pytest`).
7. Once implementation and tests are 100% green, transition card to `Pronto para Review` (status ID `10099`, transition `50`).
8. Add comment on Jira with diff summary and readiness for review.

## Artifacts
- Production source code (`src/`)
- Unit tests (`tests/`)
- Passing test logs

## Quality Gates
- Implementation Gate: zero compilation/syntax errors, 100% passing unit tests, zero uncommitted debug code.

## Exit Conditions
- Card moved to `Pronto para Review`.

## Failure Handling
- If implementation encounters blocking architectural ambiguities, raise finding to architect and pause development.
