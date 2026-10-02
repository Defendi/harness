# Python Language Profile

## Language Specifications
- **Language**: Python
- **Version**: `>=3.12`
- **Framework**: FastMCP (`fastmcp` >= 2.0)
- **Execution Environment**: Local virtualenv at `.venv` (never committed to Git)

## Tooling Ecosystem
- **Package & Dependency Manager**: `pip` via PyPI into local `.venv`
- **Linter & Code Analyzer**: `ruff`
- **Code Formatter**: `ruff`
- **Type Checker**: `mypy` (strict mode encouraged)
- **Test Runner & Coverage**: `pytest`, `pytest-asyncio`, `pytest-cov`

## Directory Structure Standards
```text
/
├── pyproject.toml
├── src/
│   └── mcpsentinel/
│       ├── __init__.py
│       ├── server.py
│       └── providers/
│           ├── __init__.py
│           ├── aws.py
│           ├── gitlab.py
│           ├── azure.py
│           └── ssh.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_server.py
```
