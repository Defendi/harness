# Regras de Teste

## 1. Tríade de Testes Herméticos
Todas as execuções de testes automatizados devem passar pela tríade completa de qualidade:
1. **Verificação de Linter:** O linting rigoroso passa sem avisos.
2. **Verificação de Formatação:** A formatação do código cumpre 100% o padrão.
3. **Testes Automatizados:** Suítes de testes unitários e de integração são executadas com 100% de sucesso.

## 2. Isolamento & Determinismo de Testes
- Testes unitários nunca devem fazer requisições de rede de saída reais para hosts ativos da AWS, GitLab, Azure ou SSH.
- Use mocks, stubs e fixtures sintéticas para isolar sistemas externos.
- Os testes devem ser determinísticos: sem dependência de estado mutável global ou ordem de execução.

## 3. Cobertura de Testes & Edge Cases
- Teste tanto o happy path quanto os caminhos de erro (falha de credencial, timeout, parâmetros inválidos, permissão negada).
- Execução rápida: testes unitários devem ser executados em segundos.
- Todo bug fix deve incluir um teste de regressão que reproduza o problema.
