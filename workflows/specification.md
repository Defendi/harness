# Workflow de Especificação (OpenSPEC)

## Gatilho
Conclusão do PRD e início das especificações técnicas para um card do Jira em `Backlog`.

## Pré-condições (Obrigatórias)
- **PRD Aprovado**: `docs/prds/PRD-NNN.md` correspondente aprovado pelo agente Product Owner (P.O.).
- **TRD Sincronizado**: `docs/trd.md` criado ou atualizado pelo agente Arquiteto usando `.agents/skills/escrever-trd/`.
- **HARD-GATE**: Os agentes são **ESTRITAMENTE PROIBIDOS** de criar documentos de SPEC antes que tanto o PRD quanto o TRD estejam escritos e aprovados.

## Etapas
1. **Sincronização do Documento de Requisitos Técnicos (TRD)**:
   - O **Agente Arquiteto** executa `.agents/skills/escrever-trd/`.
   - Atualizar `docs/trd.md` com arquitetura global, restrições de stack, NFRs, dependências externas e novas ADRs em `docs/decisions/`.
2. **Criação do OpenSPEC**:
   - O Agente Arquiteto cria o documento formal OpenSPEC: `docs/specs/<jira>-<slug>.md` usando `.agents/templates/specification.md`.
   - Implementar a metodologia OpenSPEC:
     - YAML frontmatter canônico (`type: openspec`, `prd_ref`, `trd_ref`, `jira`).
     - Mapear Requisitos Funcionais (RFs) diretamente para as User Stories do PRD.
     - Definir schemas técnicos, contratos, endpoints e modelos de dados aderentes ao TRD.
     - Detalhar edge cases, códigos de erro e modos de falha.
     - Especificar critérios de aceitação concretos e cenários de teste usando a sintaxe Given-When-Then.
3. **Validação de Segurança & Zero Trust**:
   - Validar que credenciais, tokens de API e secrets estejam completamente isolados do output do LLM.
4. **Peer Review**:
   - Arquiteto e P.O. validam se o OpenSPEC atende à intenção do PRD sem violar as restrições do TRD.

## Artefatos Produzidos
- `docs/trd.md` (atualizado via `escrever-trd`)
- `docs/decisions/<number>-<slug>.md` (ADRs, se aplicável)
- `docs/specs/<jira>-<slug>.md` (documento OpenSPEC)

## Quality Gates
- **OpenSPEC Gate**:
  - PRD e TRD confirmados como presentes e aprovados.
  - 100% dos Critérios de Aceitação testáveis e formatados em Given-When-Then.
  - Zero risco de exposição de credenciais.

## Condições de Saída
- OpenSPEC aprovado e commitado; card pronto para Planejamento e design de Arquitetura.
