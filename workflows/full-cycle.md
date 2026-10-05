# Workflow Full-Cycle

## Gatilho
Execução end-to-end de um item de trabalho de software desde a concepção inicial até o release concluído.

## Pré-condições
- Card do Jira criado em `Backlog`.
- Conexão do Atlassian MCP verificada.

## Sequência de Execução
```text
BRAINSTORMING (Backlog - Mandatório antes de qualquer ação pelos agentes via skill brainstorming)
   ↓
DEFINIÇÃO DE PRD (Backlog - Agente de P.O. via skill escrever-prd em docs/prds/)
   ↓
SINCRONIZAÇÃO DE TRD (Backlog - Agente de Arquitetura via skill escrever-trd em docs/trd.md)
   ↓
ESPECIFICAÇÃO OPENSPEC (Backlog - Agente de Arquitetura via metodologia OpenSPEC em docs/specs/)
   ↓
ARQUITETURA & ADRs (Backlog - Desenho de módulos e registros de decisão)
   ↓
PLANEJAMENTO (Backlog → A Fazer - Plano atômico de execução e handoff)
   ↓
IMPLEMENTAÇÃO (A Fazer → Em Andamento → Pronto para Review - Agente Desenvolvedor)
   ↓
REVISÃO (Review → Pronto Para Testar OU volta para A Fazer com comentários - Agente Revisor)
   ↓
TESTES (Pronto Para Testar → Testando → Concluído OU volta para A Fazer com comentários - Agente de Testes)
   ↓
DOCUMENTAÇÃO (Concluído - Sincronização técnica contínua)
   ↓
RELEASE (Tagged & Entregue - Agente de Release)
```

## Sequência de Quality Gates
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

## Condições de Saída
- Feature entregue, card fechado em `Concluído`, branch mesclada na `main`, PRD marcado como `concluido` e documentação sincronizada.
