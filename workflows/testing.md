# Testing Workflow (QA)

## Trigger
Card transitioned to `Pronto Para Testar` by reviewer agent.

## Preconditions
- Card in `Pronto Para Testar`.
- Code review fully approved.

## Steps
1. Transition Jira card from `Pronto Para Testar` to `Testando` (status ID `10102`, transition `80`).
2. Add Jira comment signaling start of QA activities by tester agent.
3. Execute the complete hermetic triad:
   - `ruff check .`
   - `ruff format --check .`
   - `pytest tests/ -v --cov=src`
4. Evaluate QA outcome:
   - **If any failure or defect is found:** add individual itemized comments on the card detailing exact step, failure, and stack trace. Transition card back to `A Fazer` (status ID `10057`, transition `30`) to restart development.
   - **If 100% approved with minor non-blocking suggestions:** execute semantic commit/merge, transition card to `Concluído` (status ID `10011`, transition `90`), record approval comment, and convert suggestions into new `Backlog` cards.

## Artifacts
- Test execution report in `docs/execution/<jira>-test-report.md`
- Semantic commit on `main` branch
- Jira comments and status transition to `Concluído`

## Quality Gates
- Testing Gate: hermetic triad passes 100%, zero regression, code merged cleanly.

## Exit Conditions
- Card moved to `Concluído` (or returned to `A Fazer`).

## Failure Handling
- On test failure: precise test logs attached to Jira comments for rapid debugging.
