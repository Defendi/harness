# Architecture Workflow

## Trigger
Approval of functional specification (`docs/specs/<jira>-<slug>.md`).

## Preconditions
- Specification Gate satisfied.
- Card remains in `Backlog`.

## Steps
1. Model structural components, provider adapters, and MCP server endpoints.
2. Verify zero-trust credential encapsulation (credentials reside solely in secure storage, never passed to agent tools).
3. If new technological decisions or structural shifts occur, author an ADR in `docs/decisions/`.
4. Document component architecture in `docs/architecture/<jira>-<slug>.md`.
5. Define interfaces, exception types, and dependency injection patterns.

## Artifacts
- `docs/architecture/<jira>-<slug>.md`
- `docs/decisions/<number>-<title>.md` (optional ADR)

## Quality Gates
- Architecture Gate: adheres to modularity rules and credential security standards.

## Exit Conditions
- Architecture approved and committed; ready for Planning.

## Failure Handling
- If security risks are detected in the architecture, pause and redesign credential boundaries.
