# Workflow de Planejamento

## Gatilho
Aprovação do OpenSPEC e do design de arquitetura para um card do Jira no `Backlog`.

## Pré-condições
- OpenSPEC Gate e Architecture Gate satisfeitos.
- PRD, TRD e OpenSPEC aprovados e commitados.
- Card pronto para sair do `Backlog`.

## Etapas
1. Decompor a implementação técnica em tarefas pequenas, atômicas e verificáveis, derivadas diretamente dos critérios de aceite do OpenSPEC.
2. Formular `docs/execution/<jira>-plan.md` utilizando `.agents/templates/implementation-plan.md`.
3. Criar plano de testes delineando testes unitários herméticos, configurações de mock e edge cases.
4. Transicionar o card do Jira de `Backlog` para `A Fazer` (sinalizando a finalização do planejamento).
5. Adicionar comentário com resumo do planejamento no card do Jira referenciando o PRD, TRD e OpenSPEC.

## Artefatos Produzidos
- `docs/execution/<jira>-plan.md`
- `docs/execution/<jira>-test-plan.md`
- Card do Jira transicionado para `A Fazer`

## Quality Gates
- **Planning Gate**: tarefas são atômicas, dependências mapeadas, cenários de teste do OpenSPEC cobertos.

## Condições de Saída
- Card em `A Fazer`, pronto para ser assumido imediatamente pelo developer agent.
