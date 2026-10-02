# Specification Workflow

## Trigger
Completion of Discovery phase for a Jira card in `Backlog`.

## Preconditions
- Jira issue key assigned (`MCPS-xxx`).
- Clear problem statement identified.

## Steps
1. Create specification document: `docs/specs/<jira>-<slug>.md` using `.agents/templates/specification.md`.
2. Define functional requirements, boundaries, user stories, and error handling.
3. Formulate concrete, testable Acceptance Criteria.
4. Validate that credentials and secrets are isolated from LLM output.
5. Review specification with stakeholders or peer agents.

## Artifacts
- `docs/specs/<jira>-<slug>.md`

## Quality Gates
- Specification Gate: 100% of acceptance criteria are testable; zero credential exposure risks.

## Exit Conditions
- Specification approved and committed to Git; card ready for Architecture.

## Failure Handling
- If requirements cannot be made testable, return to Discovery for further refinement.
