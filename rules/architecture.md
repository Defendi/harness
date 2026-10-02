# Architecture Rules

## 1. Principles
- **Separation of Concerns:** Clearly isolate transport/protocol layer (MCP), domain logic, and provider integrations (AWS, GitLab, Azure, SSH).
- **Hermetic Isolation of Secrets:** Credential storage and resolution must never leak tokens, keys or passphrases to MCP tool outputs, logs, or LLM agent responses.
- **Defensive Design:** Fail-closed by default. If a credential cannot be validated or an operation is unpermitted, reject immediately with structured errors.
- **Architectural Decision Records (ADRs):** Significant changes to structure, library choices, or security posture must be recorded in `docs/decisions/` following the ADR template.

## 2. Modularity & Interfaces
- Define explicit abstract interfaces for external service providers.
- Avoid tight coupling between the FastMCP server setup and the provider clients.
- Provide dependency injection or factory patterns to facilitate hermetic unit testing without network dependencies.

## 3. Evolutionary Architecture
- New providers (e.g. additional VCS or cloud providers) should be added as plugins/adapters without modifying existing working implementations.
- Maintain backward compatibility for MCP tools and resources exposed to AI clients.
