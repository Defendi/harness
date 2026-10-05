# Regras Específicas de Python

## 1. Type Annotations & Assinaturas
- Use a sintaxe moderna do Python 3.12+: `list[str]`, `dict[str, Any]`, `X | None` em vez de `typing.Optional` / `typing.Union`.
- Type annotations são obrigatórias em todas as definições de função, atributos de classe e parâmetros de ferramentas.
- Evite usar `Any` onde um generic específico ou modelo Pydantic puder ser declarado.

## 2. Boas Práticas do FastMCP
- Defina descrições de ferramentas e docstrings claras; coding agents dependem de docstrings de ferramentas para descoberta de parâmetros.
- Use modelos Pydantic para validação estruturada de parâmetros.
- Todas as ferramentas FastMCP devem tratar exceções defensivamente e retornar mensagens de erro estruturadas em vez de tracebacks brutos e não tratados.

## 3. Código Assíncrono
- Prefira async/await para operações de rede ou I/O (conexões SSH, requisições HTTP para GitLab/AWS/Azure).
- Nunca bloqueie o event loop principal com leituras síncronas de arquivos ou instruções sleep; use `asyncio.sleep` ou I/O não bloqueante.

## 4. Linting e Formatação
- Conte com o `ruff` tanto para linting quanto para formatação.
- Respeite o limite de comprimento de linha de 100 caracteres configurado no `pyproject.toml`.
