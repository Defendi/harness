# Claude Code Adapter

## Integration Model
Claude Code integrates with this project via the canonical root entrypoint:
`CLAUDE.md -> AGENTS.md`

## Discovery & Execution
- Claude Code discovers instructions via `CLAUDE.md`.
- Tool calls and command executions must use the virtual environment located at `.venv/bin/`.
- All guidelines, role separation, and Jira status transitions documented in `AGENTS.md` and `.agents/rules/` are canonical.
