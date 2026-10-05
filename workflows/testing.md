# Workflow de Testes (QA)

## Gatilho
Card transicionado para `Pronto Para Testar` pelo agente revisor.

## Pré-condições
- Card em `Pronto Para Testar`.
- Code review totalmente aprovado.

## Passos
1. Transicionar o card do Jira de `Pronto Para Testar` para `Testando` (status ID `10102`, transição `80`).
2. Adicionar comentário no Jira sinalizando o início das atividades de QA pelo agente testador.
3. Executar a tríade hermética completa:
   - `ruff check .`
   - `ruff format --check .`
   - `pytest tests/ -v --cov=src`
4. Avaliar o resultado do QA:
   - **Se qualquer falha ou defeito for encontrado:** adicionar comentários individuais e detalhados no card especificando o passo exato, a falha e o stack trace. Transicionar o card de volta para `A Fazer` (status ID `10057`, transição `30`) para reiniciar o desenvolvimento.
   - **Se 100% aprovado com sugestões menores não bloqueantes:** executar commit semântico/merge, transicionar o card para `Concluído` (status ID `10011`, transição `90`), registrar comentário de aprovação e converter as sugestões em novos cards no `Backlog`.

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
