# Full-Cycle Workflow

## Trigger
End-to-end execution of a software work item from initial inception to completed release.

## Preconditions
- Jira card created in `Backlog`.
- Atlassian MCP connection verified.

## Sequence of Execution
```text
BRAINSTORMING (Backlog - Mandatório antes de qualquer ação pelos agentes via skill brainstorming)
   ↓
PRD DEFINITION (Backlog - P.O. Agent via skill escrever-prd em docs/prds/)
   ↓
TRD SYNCHRONIZATION (Backlog - Architect Agent via skill escrever-trd em docs/trd.md)
   ↓
OPENSPEC SPECIFICATION (Backlog - Architect Agent via metodologia OpenSPEC em docs/specs/)
   ↓
ARCHITECTURE & ADRs (Backlog - Desenho de módulos e registros de decisão)
   ↓
PLANNING (Backlog → A Fazer - Plano atômico de execução e handoff)
   ↓
IMPLEMENTATION (A Fazer → Em Andamento → Pronto para Review - Developer Agent)
   ↓
REVIEW (Review → Pronto Para Testar OU volta para A Fazer com comentários - Reviewer Agent)
   ↓
TESTING (Pronto Para Testar → Testando → Concluído OU volta para A Fazer com comentários - Tester Agent)
   ↓
DOCUMENTATION (Concluído - Sincronização técnica contínua)
   ↓
RELEASE (Tagged & Delivered - Release Agent)
```

## Quality Gates Sequence
1. **Brainstorming Gate**: Intenção, limites e restrições alinhados colaborativamente com o humano.
2. **PRD Gate**: Regras de negócio, personas e User Stories formalizadas pelo agente de P.O.
3. **TRD Gate**: Restrições técnicas globais, stack e NFRs consolidados em `docs/trd.md`.
4. **OpenSPEC Gate**: Somente após PRD e TRD aprovados; critérios de aceitação Given-When-Then 100% testáveis.
5. **Architecture Gate**: Modularidade verificada, ADRs registradas, Zero Trust em segredos.
6. **Implementation Gate**: Zero erros de sintaxe, tipagem estrita, testes unitários herméticos passando.
7. **Review Gate**: 100% aprovado pelo revisor; comentários pontuais abertos para ajustes.
8. **Testing Gate**: Tríade hermética 100% verde (`ruff check`, `ruff format`, `pytest` ou equivalente).
9. **Documentation Gate**: Documentação técnica sincronizada com o código real entregue.
10. **Release Gate**: Tag semântica gerada e enviada ao GitHub.

## Exit Conditions
- Feature entregue, card fechado em `Concluído`, branch mesclada na `main`, PRD marcado como `concluido` e documentação sincronizada.
