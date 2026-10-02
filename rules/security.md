# Security Rules

## 1. Zero Trust Secret Management
- **Never commit secrets to Git**: API keys, SSH private keys, cloud tokens, or personal access tokens must never appear in repository files.
- Ensure all credential files, local overrides, and `.env*` files are strictly covered by `.gitignore`.
- Sanitize all strings before outputting to MCP clients or logging.

## 2. Principle of Least Privilege
- MCP tools must grant AI clients the minimum capability required for the task.
- Read operations should be separated from write/execute operations.
- Destructive operations (deleting resources, pushing forced updates) require explicit confirmation.

## 3. Input Sanitization
- Validate all incoming tool parameters against injection attacks (command injection, path traversal, SQL injection).
- When invoking SSH commands or local processes, avoid shell interpolation (`shell=True`); always use parsed argument lists.
