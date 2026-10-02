# Testing Skill

## Purpose
Execute hermetic quality verification, static analysis, coverage checks, and regression testing.

## Inputs
- Implemented code and tests
- Test plan (`docs/execution/<jira>-test-plan.md`)

## Preconditions
- Implementation completed.
- Jira card moved to `Testando` (status ID `10102`).

## Procedure
1. Execute static analysis:
   ```bash
   .venv/bin/ruff check .
   .venv/bin/ruff format --check .
   .venv/bin/mypy src/
   ```
2. Execute automated test suites hermetically:
   ```bash
   .venv/bin/pytest tests/ -v --cov=src
   ```
3. Verify test coverage meets defined threshold (>80%).
4. Verify mock isolation: confirm no live network calls were initiated.
5. Generate test execution report.

## Outputs
- Test execution report (`docs/execution/<jira>-test-report.md`)
- Verified green status across the hermetic triad.

## Validation
- All checks pass with exit code 0.
- No network leaks during test execution.

## Failure Conditions
- Any lint, formatting, or test failure.
- Flaky tests or uncontrolled dependencies.
