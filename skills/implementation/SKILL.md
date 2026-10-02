# Implementation Skill

## Purpose
Translate approved specifications and architectural models into clean, maintainable, type-annotated code and unit tests.

## Inputs
- Implementation Plan (`docs/execution/<jira>-plan.md`)
- Approved Specification and Architecture docs
- Language profile (`.agents/languages/python/`)

## Preconditions
- Architecture & Planning Gates satisfied.
- Jira card moved to `Em Andamento` (status ID `3`).

## Procedure
1. Create or checkout the task feature branch (`feature/MCPS-xxx-...`).
2. Write unit tests defining expected behavior (TDD preferred).
3. Implement business logic and provider adapters conforming strictly to specifications.
4. Run formatting and linting tools locally (`ruff check --fix`, `ruff format`).
5. Run local test suite using the virtual environment to ensure all tests pass.
6. Verify no secrets or sensitive data are hardcoded or logged.

## Outputs
- Source code in `src/`
- Unit tests in `tests/`
- Clean test run results

## Validation
- 100% passing unit tests.
- Zero linting and formatting violations.
- Full type annotations on public signatures.

## Failure Conditions
- Failing unit tests.
- Code diverging from approved specifications.
- Exposed credentials or improper error handling.
