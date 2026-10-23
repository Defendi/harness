---
name: jira-management
description: Manage Jira issue lifecycle, status transitions, itemized comments, and traceability links across project workflows. Use when updating Jira issue status, logging progress, adding comments, or managing work item transitions.
---

# Skill de Gerenciamento do Jira

## Objetivo
Gerenciar o ciclo de vida de issues do Jira, transições de status, comentários detalhados e links de rastreabilidade em todo o projeto `MCPS`.

## Entradas
- Chave da Issue do Jira (`MCPS-xxx`)
- ID de transição / status desejado
- Comentários de atualização de fase e artefatos

## Pré-condições
- Conexão ativa com o Atlassian MCP ou credenciais válidas da REST API.
- Conformidade com `.agents/rules/jira-card-lifecycle.md` e `.agents/rules/jira.md`.

## Regras para Abertura de Cards
- **Cards de História (Story)**: Destinados a contar a história do usuário. Somente podem ser abertos para agrupar épicos.
- **Cards de Épicos (Epic)**: Servem para agrupar as tarefas subdividindo por ação dentro da história.
- **Cards de Tarefas (Task)**: São os cards nos quais os agentes de execução vão se basear, podendo ser para Features ou Bugs.


## Procedimento
1. Verificar o status atual do card.
2. Determinar o ID de transição necessário de acordo com a state machine oficial:
   - `Backlog` (`10012`, transição `20`)
   - `A Fazer` (`10057`, transição `30`)
   - `Em Andamento` (`3`, transição `40`)
   - `Pronto para Review` (`10099`, transição `50`)
   - `Review` (`10100`, transição `60`)
   - `Pronto Para Testar` (`10101`, transição `70`)
   - `Testando` (`10102`, transição `80`)
   - `Concluído` (`10011`, transição `90`)
3. Executar a transição utilizando a ferramenta Atlassian MCP (`transitionJiraIssue`) ou REST API.
4. Adicionar comentário formatado descrevendo o resultado da fase, artefatos anexados e links.
   - **Ao transicionar para `Concluído` (Fechamento de Task de Feature ou Bug):** Incluir obrigatoriamente o **Resumo para Humanos Leigos** formatado conforme `.agents/templates/layperson-summary-comment.md`, detalhando o que foi feito, o benefício e as ações realizadas de forma acessível a stakeholders.
5. Se sugestões não bloqueantes forem registradas, criar novas tasks no Jira em `Backlog`.

## Saídas
- Status do card atualizado no Jira.
- Comentários documentados e trilha de auditoria no card.

## Validação
- Transição bem-sucedida sem erros de API.
- Status refletido com precisão no board do Jira.

## Condições de Falha
- Salto de status não autorizado violando a state machine do ciclo de vida.
- Falha de autenticação ou API do Jira inacessível.
