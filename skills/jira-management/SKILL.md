# Jira Management Skill

## Purpose
Manage Jira issue lifecycle, status transitions, itemized comments, and traceability links across project `MCPS`.

## Inputs
- Jira Issue Key (`MCPS-xxx`)
- Desired transition / status ID
- Phase update comments and artifacts

## Preconditions
- Active Atlassian MCP connection or valid REST API credentials.
- Compliance with `.agents/rules/jira-card-lifecycle.md`.

## Procedure
1. Verify current status of the card.
2. Determine required transition ID according to the official state machine:
   - `Backlog` (`10012`, transition `20`)
   - `A Fazer` (`10057`, transition `30`)
   - `Em Andamento` (`3`, transition `40`)
   - `Pronto para Review` (`10099`, transition `50`)
   - `Review` (`10100`, transition `60`)
   - `Pronto Para Testar` (`10101`, transition `70`)
   - `Testando` (`10102`, transition `80`)
   - `Concluído` (`10011`, transition `90`)
3. Execute transition using Atlassian MCP tool (`transitionJiraIssue`) or REST API.
4. Add formatted comment describing the phase outcome, attached artifacts, and links.
5. If non-blocking suggestions are recorded, create new Jira tasks in `Backlog`.

## Outputs
- Updated card status in Jira.
- Documented comments and audit trail on the card.

## Validation
- Transition succeeded with no API errors.
- Status reflected accurately on Jira board.

## Failure Conditions
- Unauthorized status jump violating the lifecycle state machine.
- Failed authentication or unreachable Jira API.
