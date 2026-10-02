# Git & Version Control Rules

## 1. Branch Strategy
- Main branch: `main` (production-ready, verified code).
- Working branches: `feature/<issue-key>-<short-description>`, `fix/<issue-key>-<short-description>`, `chore/<issue-key>-<short-description>`.
- Branches must branch from up-to-date `main`.

## 2. Commit Standards
- Follow Conventional Commits:
  - `feat(scope): add new capability`
  - `fix(scope): fix bug or defect`
  - `test(scope): add or modify test suites`
  - `docs(scope): update documentation`
  - `refactor(scope): refactor without behavior change`
  - `chore(scope): build, tooling, dependencies`
- Always reference the Jira issue in the message or body.

## 3. Safety Guardrails
- **NEVER execute destructive Git operations automatically**:
  - `git reset --hard` is forbidden without explicit authorization.
  - `git push --force` or `--force-with-lease` is forbidden on protected branches.
- Always check `git status` and `git diff` before committing.
