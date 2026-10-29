# Workflow de Testes (QA)

## Gatilho
Card transicionado para `Pronto Para Testar` pelo agente revisor.

## Pré-condições
- Card em `Pronto Para Testar`.
- Code review totalmente aprovado.

## Passos
1. Transicionar o card do Jira de `Pronto Para Testar` para `Testando` (status ID `10102`, transição `80`).
2. Adicionar comentário no Jira sinalizando o início das atividades de validação independente de QA pelo agente testador.
3. **Auditoria Independente dos Testes do Desenvolvedor:**
   - Inspecionar os testes unitários e de integração criados pelo desenvolvedor para garantir que testam o comportamento real do contrato (e não testes tautológicos com mocks viciosos ou sem asserções efetivas).
   - Elaborar e executar testes complementares de edge cases, dados adversos, concorrência e regressão.
4. Executar a tríade hermética completa:
   - `ruff check .`
   - `ruff format --check .`
   - `mypy src/`
   - `SENTINEL_CONF_FILE=/mnt/home/alexandre/.config/mcpsentinel/mcpsentinel_backup.conf SENTINEL_SECURITY_CONFIG=/mnt/home/alexandre/.config/mcpsentinel/security_teste.yaml pytest tests/ -v --cov=src`
   - **Regra de Backup:** se qualquer arquivo de configuração ou segurança for alterado para teste, efetuar backup prévio obrigatório; nunca sobrescrever arquivos originais. Restabelecer arquivos originais ao final.
5. Avaliar o resultado do QA:
   - **Se qualquer falha for encontrada, a cobertura for < 80% ou os testes forem insuficientes/superficiais:** adicionar comentários individuais e detalhados no card especificando o passo exato, a falha, o gap de cobertura e o stack trace. Transicionar o card de volta para `A Fazer` (status ID `10057`, transição `30`) para saneamento pelo desenvolvedor.
   - **Se 100% aprovado com critérios plenamente atendidos:** executar commit semântico/merge, transicionar o card para `Concluído` (status ID `10011`, transição `90`), registrar relatório de QA aprovado e converter eventuais sugestões menores em novos cards no `Backlog`.

## Artefatos
- Relatório de execução de testes em `docs/execution/<jira>-test-report.md`
- Commit semântico na branch `main`
- Comentários no Jira e transição de status para `Concluído`

## Quality Gates
- Testing Gate: tríade hermética passa 100%, zero regressão, código mergeado de forma limpa.

## Condições de Saída
- Card movido para `Concluído` (ou retornado para `A Fazer`).

## Tratamento de Falhas
- Em caso de falha nos testes: logs de teste precisos anexados aos comentários do Jira para rápido debugging.
