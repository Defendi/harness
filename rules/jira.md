# Regras de Governança do Jira

## 1. Rastreabilidade
- Todo código de produção, documentos de arquitetura, especificações e planos de teste devem ser rastreáveis a uma issue do Jira (`MCPS-xxx`).
- Branches, commits e pull requests devem conter o prefixo ou referenciar a chave da issue: `feat(MCPS-123): ...`.

## 2. Governança de Status
- As transições devem refletir estritamente o progresso real de acordo com `.agents/rules/jira-card-lifecycle.md`.
- Sem pular etapas: os cards devem passar por Review e Testing antes de chegar a Concluído.
- Comentários devem acompanhar cada transição de etapa, fornecendo links para artefatos e diffs.

## 3. Hierarquia de Issues
- **Initiative / Epic**: Capacidade estratégica ou subsistema principal.
- **Story / Task**: Unidade entregável de valor ou setup técnico.
- **Bug**: Correção para defeito ou comportamento inesperado.
- **Subtask**: Unidade atômica de execução dentro de uma task.
