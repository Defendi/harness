# Coding Standards Rules

## 1. Code Quality & Formatting
- Strict compliance with language-specific formatters and linters (e.g. `ruff check` and `ruff format` for Python).
- No dead code, unused imports, or lingering debug print statements.
- Explicit type annotations on all public functions, methods, and class signatures.

## 2. Error Handling & Logging
- Use structured exception handling. Catch specific exceptions; never use bare `except:`.
- Log with appropriate levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- **Never log sensitive data**: redact tokens, passwords, private keys, authorization headers.

## 3. Immutability & Predictability
- Prefer immutable data structures and explicit schemas (e.g. Pydantic models / Dataclasses).
- Avoid side effects in property getters or query methods.
- Validate inputs rigorously at the boundaries (MCP tool parameters).

## 4. Code Simplicity
- Keep functions concise and focused on a single responsibility.
- Do not over-engineer abstractions before a second use case exists.
