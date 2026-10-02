# Security Review Skill

## Purpose
Examine codebase, configurations, and dependencies for security vulnerabilities, credential exposure risks, and injection attack vectors.

## Inputs
- Full codebase and configuration files
- Dependency tree (`pyproject.toml`, virtualenv packages)
- Git history and diffs

## Preconditions
- Clean git status; access to codebase and dependency tree.

## Procedure
1. Scan for hardcoded credentials, API keys, private tokens, or SSH keys.
2. Verify `.gitignore` coverage of local configs and tokens.
3. Audit external command invocations and MCP tool inputs against injection vulnerabilities.
4. Verify credential isolation: confirm tokens are loaded securely in memory and never exposed in tool responses.
5. Review dependencies for known vulnerabilities (e.g. `pip audit` or `safety` if configured).

## Outputs
- Security evaluation summary recorded in review or architecture documentation.

## Validation
- Zero secrets in Git repository history or working tree.
- Input validation present on all external boundaries.

## Failure Conditions
- Presence of any secret in code or configuration.
- Unsanitized inputs executed in subshells or system calls.
