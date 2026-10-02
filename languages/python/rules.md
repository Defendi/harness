# Regras de Engenharia para Projetos Python

## 1. Toolchain Padrão
- **Gerenciador de Pacotes:** `uv` é o padrão obrigatório para projetos modernos.
- **Configuração:** Todas as dependências e metadados devem residir em `pyproject.toml`.
- **Linter & Formatter:** `ruff` com regras configuradas (PEP 8, import sorting, bugs comuns).
- **Type Checker:** `mypy` em modo estrito (`strict = true`).
- **Test Runner:** `pytest` com fixtures organizadas em `conftest.py`.

## 2. Padrões de Código
- **Tipagem Obrigatória:** Todas as assinaturas de funções públicas e métodos devem ter type hints explícitos (`def process(user_id: str) -> User:`).
- **Tratamento de Exceções:** Nunca utilizar `except Exception: pass` ou `except:`. Sempre capturar exceções específicas e registrar com log estruturado.
- **Estruturas de Dados:** Preferir `dataclasses` (com `slots=True, frozen=True` para imutabilidade) ou `pydantic.BaseModel` para validação de borda.
- **Async/Await:** Em projetos assíncronos (FastAPI/AnyIO), nunca bloquear o event loop com chamadas I/O síncronas.

## 3. Estrutura de Diretórios
```text
src/
└── <package_name>/
    ├── domain/         # Entidades puras e regras de negócio
    ├── services/       # Casos de uso e orquestração
    ├── repositories/   # Acesso a banco de dados e persistência
    └── api/            # Rotas, controllers e schemas de entrada/saída
tests/
├── conftest.py         # Fixtures compartilhadas
├── unit/               # Testes unitários herméticos
└── integration/        # Testes com containers ou banco de teste
```
