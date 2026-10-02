# Jira Governance Rules

## 1. Traceability
- All production code, architecture docs, specifications, and test plans must trace back to a Jira issue (`MCPS-xxx`).
- Branches, commits, and pull requests should prefix or reference the issue key: `feat(MCPS-123): ...`.

## 2. Status Governance
- Transitions must strictly mirror real-world progress according to `.agents/rules/jira-card-lifecycle.md`.
- No skipping stages: cards must travel through Review and Testing before reaching Concluído.
- Comments must accompany each stage transition, providing links to artifacts and diffs.

## 3. Issue Hierarchy
- **Initiative / Epic**: Strategic capability or major subsystem.
- **Story / Task**: Deliverable unit of value or technical setup.
- **Bug**: Fix for defect or unexpected behavior.
- **Subtask**: Atomic unit of execution within a task.
