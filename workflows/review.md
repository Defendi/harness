# Workflow de Review

## Gatilho
Card transicionado para `Pronto para Review` pelo agente desenvolvedor.

## Pré-condições
- Card em `Pronto para Review`.
- Implementação concluída, feature branch com push realizado ou diff local pronto.

## Etapas
1. Transicionar o card do Jira de `Pronto para Review` para `Review` (ID de status `10100`, transição `60`).
2. Adicionar comentário no Jira sinalizando o início do Code Review pelo agente Reviewer.
3. Realizar inspeção estática do diff de código:
   - Verificar conformidade com `.agents/rules/coding-standards.md`.
   - Verificar conformidade com `.agents/rules/security.md` (sem secrets, vazamento zero).
   - Verificar cobertura de testes e tipagem defensiva.
4. Preparar veredito do review:
   - **Se houver algum apontamento:** adicionar comentários individuais e itemizados ao card detalhando arquivo, linha, causa e recomendação. Transicionar o card de volta para `A Fazer` (ID de status `10057`, transição `30`) para reiniciar o desenvolvimento.
   - **Se estiver 100% aprovado com sugestões menores não bloqueantes:** transicionar o card para `Pronto Para Testar` (ID de status `10101`, transição `70`). Registrar comentário de aprovação do review e converter sugestões em novos cards de `Backlog`.

## Artefatos
- Resumo do review em `docs/execution/<jira>-review.md`
- Comentários itemizados no card do Jira
- Novos cards de Backlog para sugestões não bloqueantes (se houver)

## Quality Gates
- Review Gate: 100% de aprovação do agente reviewer; zero problemas bloqueantes.

## Condições de Saída
- Card movido para `Pronto Para Testar` (ou retornado para `A Fazer`).

## Tratamento de Falhas
- Em caso de rejeição: comentários detalhados e itemizados garantem que o agente desenvolvedor tenha orientações acionáveis imediatas.
