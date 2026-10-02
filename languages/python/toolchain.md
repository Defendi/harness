# Python Toolchain & Execution Commands

All commands must be executed using the local virtual environment `.venv/`.

## 1. Environment Setup & Dependency Installation
```bash
# Create virtual environment if missing
python3.12 -m venv .venv

# Upgrade pip
.venv/bin/pip install --upgrade pip

# Install project and development dependencies in editable mode
.venv/bin/pip install -e ".[dev]"
```

## 2. Formatting & Linting
```bash
# Format code
.venv/bin/ruff format .

# Check formatting without modifying
.venv/bin/ruff format --check .

# Lint and auto-fix safe rules
.venv/bin/ruff check --fix .

# Static type checking
.venv/bin/mypy src/
```

## 3. Test Execution
```bash
# Run full unit test suite
.venv/bin/pytest tests/ -v

# Run with test coverage report
.venv/bin/pytest tests/ -v --cov=src --cov-report=term-missing
```

## 4. Server Execution
```bash
# Run FastMCP server locally
.venv/bin/python -m mcpsentinel.server
```
