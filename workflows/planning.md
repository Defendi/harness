# Planning Workflow

## Trigger
Approval of OpenSPEC and Architecture design for a Jira card in `Backlog`.

## Preconditions
- OpenSPEC Gate and Architecture Gate satisfied.
- PRD, TRD, and OpenSPEC approved and committed.
- Card ready to leave `Backlog`.

## Steps
1. Break down technical implementation into small, atomic, verifiable tasks derived directly from the OpenSPEC acceptance criteria.
2. Formulate `docs/execution/<jira>-plan.md` using `.agents/templates/implementation-plan.md`.
3. Create test plan outlining hermetic unit tests, mock configurations, and edge cases.
4. Transition Jira card from `Backlog` to `A Fazer` (sinalizando a finalização do planejamento).
5. Add planning summary comment to the Jira card referencing the PRD, TRD, and OpenSPEC.

## Artifacts Produced
- `docs/execution/<jira>-plan.md`
- `docs/execution/<jira>-test-plan.md`
- Jira card transitioned to `A Fazer`

## Quality Gates
- **Planning Gate**: tasks are atomic, dependencies mapped, OpenSPEC test scenarios covered.

## Exit Conditions
- Card in `A Fazer`, ready for immediate pickup by developer agent.
