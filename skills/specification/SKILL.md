# Specification Skill

## Purpose
Formalize analyzed requirements into complete, version-controlled specifications under `docs/specs/`.

## Inputs
- Requirements analysis outputs
- Jira issue key (`MCPS-xxx`)

## Preconditions
- Requirements analysis completed and validated.

## Procedure
1. Create `docs/specs/<jira>-<slug>.md` using `.agents/templates/specification.md`.
2. Define metadata header (jira key, status, version, date).
3. Specify user stories, functional behavior, error conditions, and API contracts.
4. Define testable Acceptance Criteria using Given/When/Then format where applicable.
5. Review the specification against architecture and security guardrails.

## Outputs
- Persisted specification file: `docs/specs/<jira>-<slug>.md`.

## Validation
- Specification follows standard template.
- All acceptance criteria are testable.
- Linked to the corresponding Jira card.

## Failure Conditions
- Incomplete specifications missing error paths.
- Unspecified data models or interfaces.
