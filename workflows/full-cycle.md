# Full-Cycle Workflow

## Trigger
End-to-end execution of a software work item from initial inception to completed release.

## Preconditions
- Jira card created in `Backlog`.
- Atlassian MCP connection verified.

## Sequence of Execution
```text
DISCOVERY (Backlog)
   ↓
SPECIFICATION (Backlog)
   ↓
ARCHITECTURE (Backlog)
   ↓
PLANNING (Backlog → A Fazer)
   ↓
IMPLEMENTATION (A Fazer → Em Andamento → Pronto para Review)
   ↓
REVIEW (Review → Pronto Para Testar OU volta para A Fazer)
   ↓
TESTING (Pronto Para Testar → Testando → Concluído OU volta para A Fazer)
   ↓
DOCUMENTATION (Concluído)
   ↓
RELEASE (Tagged & Delivered)
```

## Quality Gates Sequence
1. **Specification Gate**: Acceptance criteria testable, secrets isolated.
2. **Architecture Gate**: Modularity verified, ADRs recorded, zero-trust secrets.
3. **Implementation Gate**: Zero syntax errors, unit tests written and passing.
4. **Review Gate**: 100% peer approval, zero blocking security or code flaws.
5. **Testing Gate**: Hermetic triad green (`ruff check`, `ruff format`, `pytest`).
6. **Documentation Gate**: Docs match actual code behavior, zero broken links.
7. **Release Gate**: Semantic versioning tag pushed to GitHub.

## Exit Conditions
- Feature delivered, card closed in `Concluído`, code merged to `main`, documentation synchronized.
