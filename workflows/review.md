# Review Workflow

## Trigger
Card transitioned to `Pronto para Review` by developer agent.

## Preconditions
- Card in `Pronto para Review`.
- Implementation complete, feature branch pushed or local diff ready.

## Steps
1. Transition Jira card from `Pronto para Review` to `Review` (status ID `10100`, transition `60`).
2. Add Jira comment signaling start of Code Review by Reviewer agent.
3. Perform static inspection of code diff:
   - Check compliance with `.agents/rules/coding-standards.md`.
   - Check compliance with `.agents/rules/security.md` (no secrets, zero leakage).
   - Check test coverage and defensive typing.
4. Prepare review verdict:
   - **If any findings exist:** add individual, itemized comments to the card detailing file, line, cause, and recommendation. Transition card back to `A Fazer` (status ID `10057`, transition `30`) to restart development.
   - **If 100% approved with minor non-blocking suggestions:** transition card to `Pronto Para Testar` (status ID `10101`, transition `70`). Record review approval comment, and convert suggestions into new `Backlog` cards.

## Artifacts
- Review summary in `docs/execution/<jira>-review.md`
- Itemized comments on Jira card
- New Backlog cards for non-blocking suggestions (if any)

## Quality Gates
- Review Gate: 100% approval from reviewer agent; zero blocking issues.

## Exit Conditions
- Card moved to `Pronto Para Testar` (or returned to `A Fazer`).

## Failure Handling
- On rejection: detailed itemized comments ensure developer agent has immediate actionable guidance.
