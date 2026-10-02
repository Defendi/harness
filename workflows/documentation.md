# Documentation Workflow

## Trigger
Completion of Testing or significant behavioral changes requiring knowledge synchronization.

## Preconditions
- Tests passing; card approaching completion or newly completed.

## Steps
1. Scan changes across specifications, architecture docs, and source code.
2. Synchronize API contracts, README usage sections, and quickstarts.
3. Validate all internal file links, headings, and diagrams.
4. Record implementation retrospective or execution summaries in `docs/execution/`.
5. Commit documentation updates following Conventional Commits (`docs(scope): ...`).

## Artifacts
- Synchronized documentation in `docs/` and `README.md`.

## Quality Gates
- Documentation Gate: zero broken links, code examples match real behavior.

## Exit Conditions
- Documentation up to date and committed to Git.

## Failure Handling
- If discrepancy between docs and implementation is found, open a documentation issue or fix immediately.
