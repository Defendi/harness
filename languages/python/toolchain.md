# Toolchain Python e Comandos de Execução

Todos os comandos devem ser executados usando o ambiente virtual local `.venv/`.

## 1. Configuração do Ambiente e Instalação de Dependências
```bash
# Criar ambiente virtual se não existir
python3.12 -m venv .venv

# Atualizar o pip
.venv/bin/pip install --upgrade pip

# Instalar dependências do projeto e de desenvolvimento em modo editável
.venv/bin/pip install -e ".[dev]"
```

## 2. Formatação e Linting
```bash
# Formatar código
.venv/bin/ruff format .

# Verificar formatação sem modificar
.venv/bin/ruff format --check .

# Executar lint e corrigir automaticamente regras seguras
.venv/bin/ruff check --fix .

# Checagem estática de tipos
.venv/bin/mypy src/
```

## 3. Execução de Testes
```bash
# Executar suíte completa de testes unitários
.venv/bin/pytest tests/ -v

# Executar com relatório de cobertura de testes
.venv/bin/pytest tests/ -v --cov=src --cov-report=term-missing
```

## 4. Execução do Servidor
```bash
# Executar servidor FastMCP localmente
.venv/bin/python -m mcpsentinel.server
