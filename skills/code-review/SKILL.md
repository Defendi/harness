# Skill de Code Review

## Objetivo
Realizar code review por pares minucioso e objetivo, validando a qualidade do código, a aderência à especificação, a conformidade arquitetural e a postura de segurança.

## Entradas
- Git diff entre a branch de trabalho e a `main`
- Documentos aprovados de especificação e arquitetura
- Padrões de código (`.agents/rules/coding-standards.md`)

## Pré-condições
- Card do Jira transicionado para `Review` (status ID `10100`).

## Procedimento
1. Inspecionar o diff em relação aos requisitos da especificação.
2. Verificar a ausência de vazamento de tokens, credenciais hardcoded ou padrões inseguros.
3. Checar estilo de código, tratamento de erros, tipagem defensiva e cobertura de testes.
4. Preparar o feedback da revisão utilizando `.agents/templates/review.md`.
5. Determinar o resultado da revisão:
   - **Se houver algum apontamento bloqueante**: adicionar comentários específicos e itemizados no Jira e retornar o card para `A Fazer` (status ID `10057`).
   - **Se estiver 100% aprovado com sugestões menores não bloqueantes**: aprovar a revisão, transicionar o card para `Pronto Para Testar` (status ID `10101`) e criar cards separados no Backlog para as sugestões.

## Saídas
- Relatório de revisão: `docs/execution/<jira>-review.md`
- Comentários de feedback itemizados no card do Jira.

## Validação
- Cada apontamento inclui arquivo, número da linha, causa raiz e recomendação concreta.
- Veredito claro: Aprovado ou Retornado para Dev.

## Condições de Falha
- Revisão superficial que não identifique falhas de segurança ou lacunas de especificação.
- Comentários de feedback ambíguos ou não acionáveis.
