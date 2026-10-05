# Workflow de Discovery & Requisitos

## Gatilho
Nova solicitação de funcionalidade (feature), exploração de iniciativa ou definição de problema complexo.

## Pré-condições
- Issue do Jira em `Backlog`.
- Nenhuma ação de código ou implementação pode ser realizada antes deste workflow.

## Etapas
1. **Brainstorming Obrigatório (Hard-Gate)**:
   - Invocar `.agents/skills/brainstorming/` antes de QUALQUER ação dos agentes.
   - Conduzir diálogo colaborativo para descobrir intenção, persona, limites do problema e restrições.
   - Respeitar os Hard-Gates: estabelecer entendimento compartilhado e obter alinhamento humano antes de prosseguir.
2. **Elaboração do Product Requirements Document (PRD)**:
   - O **Agente Product Owner (P.O.)** executa `.agents/skills/escrever-prd/`.
   - Elaborar `docs/prds/PRD-<number>-<slug>.md` definindo contexto de negócio, user stories (US01, US02...), critérios de aceitação e edge cases.
   - Manter o PRD focado estritamente na intenção de negócio (*o que* e *por que*), deixando a viabilização técnica para o TRD.
3. **Validação e Aprovação do PRD**:
   - Verificar se todos os critérios de aceitação estão claramente declarados sob a perspectiva de produto.
   - Transicionar o status do PRD de `rascunho` para `pronto`.

## Artefatos Produzidos
- `docs/prds/PRD-<number>-<slug>.md` (elaborado pelo agente P.O.)

## Quality Gates
- **Brainstorming Gate**: Intenção do usuário, restrições e critérios de sucesso acordados mutuamente.
- **PRD Gate**: Regras de negócio completas, IDs de US estáveis, critérios de aceitação de produto testáveis.

## Condições de Saída
- PRD aprovado em `docs/prds/` pronto para ser repassado ao Arquiteto para a elaboração do TRD e do OpenSPEC.
