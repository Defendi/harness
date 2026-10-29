---
name: testing
description: Execute hermetic quality verification, static analysis, coverage checks, and regression testing. Use when validating code changes, running linters/type checks, verifying test suites, or validating test coverage.
---

# Skill de Testes

## Objetivo
Executar verificação hermética de qualidade, análise estática, verificações de cobertura e testes de regressão.

## Entradas
- Código e testes implementados
- Plano de testes (`docs/execution/<jira>-test-plan.md`)

## Pré-condições
- Implementação concluída.
- Card do Jira movido para `Testando` (status ID `10102`).
- Arquivos de configuração e segurança de teste validados (ex.: `mcpsentinel_backup.conf` e `security_teste.yaml`).
- Garantia de preservação: nunca sobrescrever arquivos; backup prévio obrigatório caso qualquer alteração seja requerida para testes.

## Procedimento
1. Executar análise estática:
   ```bash
   .venv/bin/ruff check .
   .venv/bin/ruff format --check .
   .venv/bin/mypy src/
   ```
2. Executar suítes de testes automatizados hermeticamente com os arquivos dedicados de teste:
   ```bash
   SENTINEL_CONF_FILE=/mnt/home/alexandre/.config/mcpsentinel/mcpsentinel_backup.conf \
   SENTINEL_SECURITY_CONFIG=/mnt/home/alexandre/.config/mcpsentinel/security_teste.yaml \
   .venv/bin/pytest tests/ -v --cov=src
   ```
3. Verificar se a cobertura de testes atinge o threshold definido (>80%).
4. Verificar o isolamento de mocks: confirmar que nenhuma chamada de rede real foi iniciada.
5. Se algum arquivo de configuração/segurança foi manipulado: assegurar que o backup prévio foi mantido e o estado original restaurado sem sobrescrita destrutiva.
6. Gerar relatório de execução de testes.

## Saídas
- Relatório de execução de testes (`docs/execution/<jira>-test-report.md`)
- Status verde verificado em toda a tríade hermética.

## Validação
- Todas as verificações passam com exit code 0.
- Nenhum vazamento de rede durante a execução dos testes.

## Condições de Falha
- Qualquer falha de lint, formatação ou teste.
- Testes flaky ou dependências não controladas.
