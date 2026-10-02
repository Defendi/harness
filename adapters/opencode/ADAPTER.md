# OpenCode Adapter

## Integration Model
OpenCode agents interact with the repository using the canonical contract defined in:
`AGENTS.md`

## Configuration
- OpenCode agent runners should point to `.agents/` as the primary configuration repository.
- Avoid modifying core harness files or creating tool-specific variants of rules.
- Execute commands using the local environment `.venv/bin/`.
