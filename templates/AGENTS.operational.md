# Manual Operacional do Harness

Este documento define a mecânica operacional do Application Development Harness sob `.agents/`.

## 1. Como Usar o Harness

O harness fornece uma infraestrutura de engenharia de software automatizada e orientada por especificações. Sempre que um agente atuar em um item de trabalho:

1. Validar pré-condições e conectividade com o Jira.
2. Identificar o workflow necessário em `.agents/workflows/`.
3. Carregar o perfil de papel relevante de `.agents/agents/`.
4. Carregar apenas as regras específicas de `.agents/rules/` e skills de `.agents/skills/` necessárias para a etapa atual.
5. Aplicar o perfil de linguagem de `.agents/languages/<language>/`.
6. Aplicar os Quality Gates antes da transição de estado.

## 2. Protocolo de Seleção de Regras

Não carregue todas as regras no contexto simultaneamente. Selecione as regras com base na atividade:
- Arquitetura / Design: `architecture.md`, `security.md`
- Implementação / Codificação: `coding-standards.md`, `security.md`, `<language>/rules.md`
- Testes / Verificação: `testing.md`
- Gestão de Trabalho & Rastreamento: `jira.md`, `jira-card-lifecycle.md`
- Controle de Versão: `git.md`
- Documentação: `documentation.md`

## 3. Protocolo de Seleção de Skills

Skills são capacidades funcionais modulares localizadas sob `.agents/skills/`.
Carregue uma skill apenas ao executar seu procedimento específico:
- Brainstorming & Ideação: `.agents/skills/brainstorming/SKILL.md` (obrigatório antes do trabalho criativo)
- Product Requirements Document (PRD): `.agents/skills/escrever-prd/SKILL.md`
- Technical Requirements Document (TRD): `.agents/skills/escrever-trd/SKILL.md`
- Análise de Requisitos: `.agents/skills/requirements-analysis/SKILL.md`
- Escrita de Especificação OpenSPEC: `.agents/skills/specification/SKILL.md`
- Design de Arquitetura: `.agents/skills/architecture-design/SKILL.md`
- Implementação: `.agents/skills/implementation/SKILL.md`
- Testes Herméticos: `.agents/skills/testing/SKILL.md`
- Code Review: `.agents/skills/code-review/SKILL.md`
- Security Review: `.agents/skills/security-review/SKILL.md`
- Gestão do Ciclo de Vida de Cards no Jira: `.agents/skills/jira-management/SKILL.md`
- Sincronização de Documentação: `.agents/skills/documentation/SKILL.md`

## 4. Protocolo de Seleção de Workflows

Execute tarefas estritamente de acordo com os workflows de ciclo de vida definidos em `.agents/workflows/`:
- Onboarding de projeto: `bootstrap.md`
- Exploração do espaço do problema & Brainstorming: `discovery.md`
- Formalização de requisitos OpenSPEC: `specification.md`
- Modelagem de sistemas & ADRs: `architecture.md`
- Decomposição de tarefas: `planning.md`
- Desenvolvimento: `implementation.md`
- Verificação hermética: `testing.md`
- Inspeção multifacetada: `review.md`
- Sincronização de conhecimento: `documentation.md`
- Empacotamento para entrega: `release.md`
- Fluxo contínuo ponta a ponta: `full-cycle.md`

## 5. Especialização & Delegação de Agentes

As tarefas devem seguir o gate estrito de papéis:
- **Orchestrator (Main Agent)**: Coordena, despacha subagentes, gerencia o status e as transições do Jira. Proibido de editar código diretamente.
- **Product Owner (P.O.)**: Lidera a descoberta de problemas, regras de negócio, User Stories e elabora PRDs em `docs/prds/`.
- **Architect**: Elabora o Technical Requirements Document (`docs/trd.md`), ADRs, arquitetura de sistemas e especificações formais do OpenSPEC (`docs/specs/`).
- **Developer**: Implementa código e testes unitários estritamente baseados nas especificações OpenSPEC.
- **Tester**: Executa suítes de testes herméticos, testes de regressão e validação de cobertura.
- **Reviewer**: Realiza code review estático, checagens de aderência e feedback construtivo.
- **Security**: Valida isolamento de credenciais, scans de vulnerabilidades e controle de acesso.
- **Documentation**: Sincroniza especificações, documentos de arquitetura e referências técnicas.
- **Release**: Prepara tags de versão, release notes e pacotes de entrega.

## 6. Carregamento do Perfil de Linguagem

O perfil de linguagem ativo é determinado por `.agents/config/harness.yaml` e `.agents/config/language.yaml`.
Carregue:
- Definições de perfil: `.agents/languages/<selected-language>/PROFILE.md`
- Regras específicas da linguagem: `.agents/languages/<selected-language>/rules.md`
- Comandos de execução da toolchain: `.agents/languages/<selected-language>/toolchain.md`

## 7. Precedência de Configuração

Quando existirem diretivas conflitantes, resolva-as nesta ordem:
1. `AGENTS.md` (Contrato Raiz Canônico)
2. `.agents/rules/jira-card-lifecycle.md` (Máquina de Estados Estrita do Jira)
3. `.agents/rules/` (Regras Fundamentais de Disciplina)
4. `.agents/languages/<language>/rules.md` (Especificidades da Linguagem)
5. Arquivos individuais de workflow e skill.

## 8. Protocolo de Handoff

As transições de estado entre agentes devem produzir artefatos persistentes e rastreáveis utilizando templates de `.agents/templates/`:
- Brainstorming → PRD: `docs/prds/PRD-<number>-<slug>.md` (elaborado pelo agente P.O.)
- PRD → TRD: `docs/trd.md` + `docs/decisions/<number>-<title>.md` (elaborado pelo agente Architect)
- TRD & PRD → OpenSPEC: `docs/specs/<jira>-<slug>.md` (metodologia OpenSPEC)
- OpenSPEC → Arquitetura: `docs/architecture/<jira>-<slug>.md`
- Arquitetura → Planejamento: `docs/execution/<jira>-plan.md`
- Implementação → Review: Código-fonte + Testes + Resumo de diff
- Review → Testes / Handoff: `docs/execution/<jira>-review.md`
- Testes → Release / Done: Relatório de execução de testes + Quality gates verificados
