# Code Review Skill

## Purpose
Perform thorough, objective peer code review validating code quality, specification adherence, architecture compliance, and security posture.

## Inputs
- Git diff between working branch and `main`
- Approved specification and architecture documents
- Coding standards (`.agents/rules/coding-standards.md`)

## Preconditions
- Jira card transitioned to `Review` (status ID `10100`).

## Procedure
1. Inspect the diff against specification requirements.
2. Verify absence of leaked tokens, hardcoded credentials, or insecure patterns.
3. Check code style, error handling, defensive typing, and test coverage.
4. Prepare review feedback using `.agents/templates/review.md`.
5. Determine review outcome:
   - **If any blocking findings exist**: add specific, itemized comments to Jira and return card to `A Fazer` (status ID `10057`).
   - **If 100% approved with minor non-blocking suggestions**: approve review, transition card to `Pronto Para Testar` (status ID `10101`), and create separate Backlog cards for the suggestions.

## Outputs
- Review report: `docs/execution/<jira>-review.md`
- Itemized feedback comments on Jira card.

## Validation
- Every finding includes file, line number, root cause, and concrete recommendation.
- Clear verdict: Approved or Returned to Dev.

## Failure Conditions
- Superficial review missing security flaws or specification gaps.
- Unactionable or ambiguous feedback comments.
