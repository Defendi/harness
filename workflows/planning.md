# Planning Workflow

## Trigger
Approval of Architecture and completion of specification phase.

## Preconditions
- Specification Gate and Architecture Gate satisfied.
- Card ready to leave `Backlog`.

## Steps
1. Break down technical implementation into small, verifiable tasks.
2. Formulate `docs/execution/<jira>-plan.md` using `.agents/templates/implementation-plan.md`.
3. Create test plan outlining unit tests, mock configurations, and edge cases.
4. Transition Jira card from `Backlog` to `A Fazer` (status ID `10057`, transition `30`).
5. Add planning summary comment to Jira card.

## Artifacts
- `docs/execution/<jira>-plan.md`
- `docs/execution/<jira>-test-plan.md`
- Jira card transitioned to `A Fazer`

## Quality Gates
- Planning Gate: tasks are atomic, dependencies mapped, test plan defined.

## Exit Conditions
- Card in `A Fazer`, ready for immediate pickup by developer agent.

## Failure Handling
- If tasks are too large or ambiguous, break them into smaller sub-tasks on Jira.
