# Discovery & Requirements Workflow

## Trigger
New feature request, initiative exploration, or complex problem statement.

## Preconditions
- Jira issue in `Backlog`.
- No code or implementation action may be taken prior to this workflow.

## Steps
1. **Mandatory Brainstorming (Hard-Gate)**:
   - Invoke `.agents/skills/brainstorming/` before ANY action by agents.
   - Conduct collaborative dialogue to discover intent, persona, problem boundaries, and constraints.
   - Respect Hard-Gates: establish shared understanding and obtain human alignment before proceeding.
2. **Product Requirements Document (PRD) Authoring**:
   - The **Product Owner (P.O.) Agent** executes `.agents/skills/escrever-prd/`.
   - Author `docs/prds/PRD-<number>-<slug>.md` defining business context, user stories (US01, US02...), acceptance criteria, and edge cases.
   - Keep PRD focused strictly on business intent (*what* and *why*), leaving technical realization to TRD.
3. **PRD Validation & Approval**:
   - Verify that all acceptance criteria are clearly stated from a product perspective.
   - Transition PRD status from `rascunho` to `pronto`.

## Artifacts Produced
- `docs/prds/PRD-<number>-<slug>.md` (authored by P.O. agent)

## Quality Gates
- **Brainstorming Gate**: User intent, constraints, and success criteria mutually agreed upon.
- **PRD Gate**: Complete business rules, stable US IDs, testable product acceptance criteria.

## Exit Conditions
- Approved PRD in `docs/prds/` ready to be handed off to the Architect for TRD and OpenSPEC authoring.
