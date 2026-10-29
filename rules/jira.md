# Regras de Governança do Jira

## 1. Rastreabilidade
- Todo código de produção, documentos de arquitetura, especificações e planos de teste devem ser rastreáveis a uma issue do Jira (`MCPS-xxx`).
- Branches, commits e pull requests devem conter o prefixo ou referenciar a chave da issue: `feat(MCPS-123): ...`.

## 2. Governança de Status
- As transições devem refletir estritamente o progresso real de acordo com `.agents/rules/jira-card-lifecycle.md`.
- Sem pular etapas: os cards devem passar por Review e Testing antes de chegar a Concluído.
- Comentários devem acompanhar cada transição de etapa, fornecendo links para artefatos e diffs.

## 3. Regras para Abertura de Cards e Hierarquia
- **Cards de História (Story)**: Destinados a contar a história do usuário. Somente podem ser abertos para agrupar épicos.
- **Cards de Épicos (Epic)**: Servem para agrupar as tarefas subdividindo por ação dentro da história.
- **Cards de Tarefas (Task)**: São os cards nos quais os agentes de execução vão se basear, podendo ser para Features ou Bugs.
- **Subtask**: Unidade atômica de execução técnica dentro de uma tarefa.

## 4. Preenchimento Obrigatório e Manutenção dos Cards (Nunca Deixar Vazio)
- **Proibição de Cards Vazios**: Nenhum card deve ser criado ou mantido com descrição em branco (`description: null` ou apenas o `summary`).
- **Estrutura Obrigatória da Descrição**:
  - **Contexto e Problema**: Descrição detalhada da dor do usuário, necessidade de negócio ou relato de bug em produção.
  - **Escopo e Requisitos**: Funcionalidades e requisitos técnicos que delimitam a entrega.
  - **Critérios de Aceite**: Itens verificáveis e objetivos que definem a entrega concluída.
  - **Rastreabilidade**: Links para documentos do harness vinculados (`PRD`, `TRD`, `OpenSPEC`).
- **Manutenção Contínua**: O orquestrador e subagentes devem manter a descrição do card atualizada e refinada ao longo de todo o ciclo de vida.

## 5. Resumo para Humanos Leigos ao Finalizar Cards (Obrigatório)
Ao finalizar qualquer card de tarefa (Task de Feature ou Bug) e transicioná-lo para `Concluído`, o agente responsável deve **obrigatoriamente publicar um comentário de encerramento em linguagem clara e acessível para humanos leigos** (seguindo `.agents/templates/layperson-summary-comment.md`), contendo:
- **O que foi feito:** Explicação direta e sem jargões técnicos sobre a funcionalidade ou correção.
- **Benefício Prático:** O que muda na experiência do usuário, na operação ou no negócio.
- **Ações Realizadas (Bastidores):** Resumo amigável das alterações e validações de qualidade executadas.
- **Como Validar:** Roteiro simples de verificação visual ou funcional.


