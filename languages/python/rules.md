# Python Specific Rules

## 1. Type Annotations & Signatures
- Use modern Python 3.12+ syntax: `list[str]`, `dict[str, Any]`, `X | None` instead of `typing.Optional` / `typing.Union`.
- Type annotations are required on all function definitions, class attributes, and tool parameters.
- Avoid using `Any` where a specific generic or Pydantic model can be declared.

## 2. FastMCP Best Practices
- Define clear tool descriptions and docstrings; coding agents rely on tool docstrings for parameter discovery.
- Use Pydantic models for structured parameter validation.
- All FastMCP tools must handle exceptions defensively and return structured error messages rather than raw unhandled tracebacks.

## 3. Asynchronous Code
- Prefer async/await for network or I/O operations (SSH connections, HTTP requests to GitLab/AWS/Azure).
- Never block the main event loop with synchronous file reads or sleep statements; use `asyncio.sleep` or non-blocking I/O.

## 4. Linting and Formatting
- Rely on `ruff` for both linting and formatting.
- Respect 100-character line length limit configured in `pyproject.toml`.
