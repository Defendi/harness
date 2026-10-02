---
type: specification
id: SPEC-HARNESS-001
status: approved
version: 2.0
domain: software-engineering
---

# Application Development Harness

## 1. Objetivo

O **Application Development Harness** é uma infraestrutura de engenharia de software orientada a agentes de IA, projetada para controlar e padronizar o ciclo de desenvolvimento de aplicações.

O harness deve permitir que diferentes coding agents conduzam atividades de:

```text
Discovery
→ Specification
→ Architecture
→ Planning
→ Implementation
→ Testing
→ Review
→ Documentation
→ Validation
→ Release
```

O harness deve ser:

* independente de linguagem;
* independente de LLM;
* independente de coding agent;
* orientado a especificações;
* rastreável;
* modular;
* extensível;
* compatível com múltiplos ambientes de desenvolvimento.

A primeira implementação não deve assumir nenhuma linguagem. A linguagem do projeto será definida durante o bootstrap.

---

# 2. Problema

Coding agents normalmente operam diretamente sobre o código, utilizando instruções dispersas em prompts, arquivos de configuração e memória da conversa.

Esse modelo gera problemas como:

* ausência de processo consistente;
* perda de contexto entre agentes;
* duplicação de instruções;
* divergência entre documentação e código;
* pouca rastreabilidade entre requisito e implementação;
* forte dependência de uma ferramenta específica;
* dificuldade para trocar de linguagem ou stack;
* dificuldade para reutilizar processos de engenharia;
* ausência de quality gates explícitos.

O harness deve resolver esses problemas criando uma camada persistente de controle da engenharia.

---

# 3. Escopo

O harness deverá controlar:

### 3.1 Contexto do projeto

* descrição;
* linguagem;
* versão;
* framework;
* toolchain;
* estrutura do projeto.

### 3.2 Processo de engenharia

* discovery;
* especificação;
* arquitetura;
* planejamento;
* implementação;
* testes;
* revisão;
* documentação;
* validação;
* release.

### 3.3 Agentes

* architect;
* developer;
* tester;
* reviewer;
* security;
* documentation;
* release.

### 3.4 Artefatos

* specifications;
* architecture documents;
* ADRs;
* implementation plans;
* test plans;
* review reports;
* release notes.

### 3.5 Integrações

* Jira;
* Git;
* coding agents.

---

# 4. Fora do Escopo

O harness não deverá:

* substituir o Git;
* substituir o Jira;
* substituir um CI/CD;
* impor uma linguagem;
* impor uma IDE;
* impor um fornecedor de LLM;
* implementar o produto do projeto;
* obrigar um framework específico;
* impor uma única estratégia de branching;
* manter toda a informação exclusivamente na memória da conversa.

---

# 5. Princípios Arquiteturais

## 5.1 Contrato separado da implementação

O arquivo:

```text
AGENTS.md
```

é o contrato principal de operação.

A implementação do harness fica em:

```text
.agents/
```

Portanto:

```text
AGENTS.md
    ↓
define o contrato

.agents/
    ↓
implementa o harness
```

---

## 5.2 Language Agnostic

O core não deve conter regras específicas de Python, Go, Java, PHP, C ou C++.

O conhecimento específico deve ser isolado em:

```text
.agents/languages/<language>/
```

---

## 5.3 Agent Agnostic

O core também não deve depender de Claude, Gemini ou OpenCode.

As diferenças entre ferramentas devem ser encapsuladas em:

```text
.agents/adapters/
```

---

## 5.4 Persistent State

Informações importantes do processo devem existir em arquivos persistentes.

A execução não deve depender somente da memória da sessão do agente.

---

## 5.5 Specification Driven

Mudanças significativas devem ser derivadas de uma specification.

A cadeia preferencial é:

```text
Jira
 ↓
Specification
 ↓
Architecture
 ↓
Implementation Plan
 ↓
Code
 ↓
Tests
 ↓
Review
```

---

# 6. Arquitetura Conceitual

```text
                         ┌──────────────────┐
                         │      Jira        │
                         │ Work Management  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Specification   │
                         │      docs/       │
                         └────────┬─────────┘
                                  │
                                  ▼
                 ┌──────────────────────────────────┐
                 │       Application Harness         │
                 │                                  │
                 │ AGENTS.md                        │
                 │                                  │
                 │ .agents/                         │
                 │ ├── rules                        │
                 │ ├── skills                       │
                 │ ├── workflows                    │
                 │ ├── agents                       │
                 │ ├── templates                    │
                 │ ├── languages                    │
                 │ ├── adapters                     │
                 │ └── config                       │
                 └───────────────┬──────────────────┘
                                 │
                  ┌──────────────┴───────────────┐
                  │                              │
                  ▼                              ▼
           Agent Adapters                  Language Profile
                  │                              │
        ┌─────────┼──────────┐          ┌────────┼─────────┐
        ▼         ▼          ▼          ▼        ▼         ▼
      Claude    Gemini    OpenCode    Python     Go       Java
```

---

# 7. Estrutura do Harness

A estrutura mínima deve ser:

```text
/
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── README.md
│
├── .agents/
│   ├── AGENTS.md
│   │
│   ├── agents/
│   │   ├── architect/
│   │   ├── developer/
│   │   ├── tester/
│   │   ├── reviewer/
│   │   ├── security/
│   │   ├── documentation/
│   │   └── release/
│   │
│   ├── rules/
│   │   ├── architecture.md
│   │   ├── coding-standards.md
│   │   ├── testing.md
│   │   ├── security.md
│   │   ├── documentation.md
│   │   ├── jira.md
│   │   └── git.md
│   │
│   ├── skills/
│   │   ├── requirements-analysis/
│   │   ├── specification/
│   │   ├── architecture-design/
│   │   ├── implementation/
│   │   ├── testing/
│   │   ├── code-review/
│   │   ├── security-review/
│   │   ├── jira-management/
│   │   └── documentation/
│   │
│   ├── workflows/
│   │   ├── bootstrap.md
│   │   ├── discovery.md
│   │   ├── specification.md
│   │   ├── architecture.md
│   │   ├── planning.md
│   │   ├── implementation.md
│   │   ├── testing.md
│   │   ├── review.md
│   │   ├── documentation.md
│   │   ├── release.md
│   │   └── full-cycle.md
│   │
│   ├── templates/
│   │   ├── specification.md
│   │   ├── architecture.md
│   │   ├── adr.md
│   │   ├── implementation-plan.md
│   │   ├── test-plan.md
│   │   ├── review.md
│   │   └── release-notes.md
│   │
│   ├── languages/
│   │   └── <language>/
│   │
│   ├── adapters/
│   │   ├── claude/
│   │   ├── gemini/
│   │   └── opencode/
│   │
│   └── config/
│       ├── harness.yaml
│       └── language.yaml
│
└── docs/
    ├── specs/
    ├── architecture/
    ├── decisions/
    ├── execution/
    └── references/
```

A estrutura específica do código do aplicativo deve ser determinada pela linguagem e toolchain selecionadas.

---

# 8. Bootstrap

## 8.1 Objetivo

O bootstrap é a primeira etapa executada pelo harness.

Seu objetivo é compreender o projeto antes de criar o skeleton.

---

## 8.2 Entrevista obrigatória

Antes de criar qualquer estrutura, o agente deve perguntar:

### Projeto

```text
Qual é a descrição do projeto?

Explique:
- o que o sistema fará;
- quem utilizará;
- qual problema pretende resolver.
```

### Linguagem

```text
Qual linguagem será utilizada?
```

Exemplos:

```text
Python
Go
Java
PHP
C
C++
Rust
TypeScript
etc.
```

O agente nunca deve assumir Python.

### Pasta do Projeto

```text
Qual é o caminho da pasta onde ficará o projeto?
```

Exemplos:

```text
/caminho/absoluto/do/projeto
./ (diretório atual)
```

---

## 8.3 Coleta adicional

Após receber descrição e linguagem, o harness deve inspecionar o projeto.

Deve identificar:

* versão da linguagem;
* framework;
* package manager;
* build system;
* estrutura de diretórios;
* testes;
* lint;
* formatter;
* type checker;
* CI/CD;
* documentação;
* configuração existente.

O agente deve perguntar somente informações que não possam ser determinadas de maneira confiável por inspeção.

---

# 9. Language Profile

Cada projeto possui um Language Profile.

Formato:

```text
.agents/languages/<language>/
```

O profile deve conter:

```text
language
version
framework
tooling
commands
project conventions
testing strategy
build strategy
```

Exemplo conceitual:

```yaml
language:
  id: python
  version: ">=3.12"

tooling:
  package_manager: uv
  test_runner: pytest
  linter: ruff
  formatter: ruff
  type_checker: mypy
```

Essas configurações são defaults e devem ser adaptáveis ao projeto existente.

---

# 10. AGENTS.md

O `AGENTS.md` deve conter apenas o contrato operacional.

Ele deve indicar:

* identidade do projeto;
* princípios;
* localização do harness;
* localização da documentação;
* existência do Jira;
* localização do language profile;
* regras gerais de operação.

Não deve conter implementação detalhada do harness.

---

# 11. `.agents/AGENTS.md`

Esse arquivo define como interpretar o próprio harness.

Deve especificar:

* seleção de rules;
* seleção de skills;
* seleção de workflows;
* seleção de agents;
* seleção do language profile;
* precedência;
* contexto necessário;
* handoff.

---

# 12. Rules

Rules são regras operacionais reutilizáveis.

Exemplos:

```text
architecture
coding-standards
testing
security
documentation
jira
git
```

Rules devem ser:

* pequenas;
* independentes;
* versionáveis;
* reutilizáveis.

---

# 13. Skills

Skills representam capacidades específicas.

Exemplos:

```text
requirements-analysis
specification
architecture-design
implementation
testing
code-review
security-review
jira-management
documentation
```

Cada skill deve definir:

```text
Purpose
Inputs
Preconditions
Procedure
Outputs
Validation
Failure Conditions
```

---

# 14. Agents

O harness deverá possuir agentes especializados.

## Architect

Responsável por:

* análise de requisitos;
* arquitetura;
* componentes;
* dependências;
* riscos;
* ADRs.

## Developer

Responsável por:

* implementação;
* testes unitários;
* aderência à specification.

## Tester

Responsável por:

* estratégia de testes;
* testes;
* execução;
* análise de falhas.

## Reviewer

Responsável por:

* revisão;
* bugs;
* regressões;
* aderência à specification;
* problemas arquiteturais.

## Security

Responsável por:

* vulnerabilidades;
* autenticação;
* autorização;
* secrets;
* exposição de dados;
* dependências.

## Documentation

Responsável por:

* documentação;
* specifications;
* ADRs;
* release notes.

## Release

Responsável por:

* validação final;
* release;
* versionamento;
* documentação de release.

---

# 15. Workflows

Workflows representam processos executáveis.

Cada workflow deve conter:

```text
Trigger
Preconditions
Steps
Artifacts
Quality Gates
Exit Conditions
Failure Handling
```

Workflows mínimos:

```text
bootstrap
discovery
specification
architecture
planning
implementation
testing
review
documentation
release
full-cycle
```

---

# 16. Full Cycle

O workflow completo deverá seguir:

```text
Discovery
↓
Specification
↓
Architecture
↓
Planning
↓
Implementation
↓
Testing
↓
Review
↓
Documentation
↓
Validation
↓
Release
```

---

# 17. State Machine

O estado de uma tarefa deverá poder ser representado por:

```text
NEW
↓
DISCOVERY
↓
SPECIFICATION
↓
ARCHITECTURE
↓
PLANNED
↓
IMPLEMENTING
↓
TESTING
↓
REVIEW
↓
DOCUMENTATION
↓
READY
↓
DONE
```

A conclusão do código não implica conclusão do trabalho.

---

# 18. Quality Gates

Deverão existir gates independentes e executáveis:

```text
Specification Gate
Architecture Gate
Implementation Gate
Testing Gate
Review Gate
Release Gate
```

Cada gate deve possuir critérios verificáveis e vinculados a comandos determinísticos da stack tecnológica do projeto.

Exemplo de mapeamento executável:

```yaml
quality_gates:
  implementation_gate:
    commands:
      - "uv run ruff check ."
      - "uv run mypy src/"
  testing_gate:
    min_coverage_percent: 80
    commands:
      - "uv run pytest -v --cov=src --cov-fail-under=80"
  security_gate:
    commands:
      - "uv run pip-audit"
```

A transição de status no Jira é estritamente condicionada ao exit code `0` de todos os comandos obrigatórios do gate correspondente.

---

# 19. Jira

Jira é o sistema de gestão e controle do trabalho.

O harness deve utilizar identificadores Jira para rastreabilidade.

Exemplo:

```text
PROJ-123
```

Um item Jira pode estar relacionado a:

```text
Specification
Architecture
ADR
Implementation Plan
Code
Tests
Review
Release
```

---

# 20. Documentação

A documentação persistente deve ficar em:

```text
docs/
```

Organização:

```text
docs/
├── specs/
├── architecture/
├── decisions/
├── execution/
└── references/
```

---

# 21. Specification

Uma specification deve possuir:

```markdown
# Specification

## Metadata

## Objective

## Context

## Functional Requirements

## Non-Functional Requirements

## Business Rules

## User Flows

## Edge Cases

## Acceptance Criteria

## Technical Constraints

## Dependencies

## Risks

## Open Questions

## References
```

Metadata mínima:

```yaml
jira: PROJ-123
type: specification
status: draft
version: 1
```

---

# 22. Architecture

Arquitetura deve ser armazenada em:

```text
docs/architecture/
```

Decisões arquiteturais significativas devem utilizar ADR:

```text
docs/decisions/
```

Formato mínimo:

```markdown
# ADR-XXXX — Title

## Context

## Problem

## Decision

## Alternatives

## Consequences

## Status

## References
```

---

# 23. Implementation Plan

O implementation plan deve permitir relacionar:

```text
Requirement
→ component
→ source files
→ implementation step
→ tests
```

Deve conter:

```text
Requirements
Files
Components
Dependencies
Steps
Testing Strategy
Migration Strategy
Rollback Strategy
Validation
```

---

# 24. Traceability

O harness deve permitir rastrear:

```text
Jira Issue
     ↓
Specification
     ↓
Architecture
     ↓
ADR
     ↓
Implementation Plan
     ↓
Code
     ↓
Tests
     ↓
Review
     ↓
Release
```

Nenhuma etapa deve depender exclusivamente da memória do agente.

---

# 25. Agent Handoff

O handoff entre agentes deverá ser explícito e estruturado via manifesto persistente em arquivo:

```text
docs/execution/handoff-[PROJ-XXX].yaml
```

Esse manifesto garante que a troca de agentes ou de sessões não dependa da memória volátil da conversa.

Estrutura canônica do manifesto de handoff:

```yaml
schema_version: "1.0"
jira_issue: "PROJ-123"
lifecycle:
  phase: "TESTING"
  previous_agent: "developer"
  next_agent: "tester"
artifacts:
  specification: "docs/specs/PROJ-123.md"
  architecture: "docs/architecture/PROJ-123.md"
  implementation_plan: "docs/execution/PROJ-123-plan.md"
quality_gates:
  implementation_gate: "PASSED"
  testing_gate: "PENDING"
instructions_for_next_agent:
  - "Executar suíte de testes com cobertura."
  - "Validar casos de erro e edge cases."
```

O agente receptor lê primordialmente o arquivo de handoff e os artefatos apontados, preservando a janela de contexto.

---

# 26. Context Loading

O agente não deve carregar todo o repositório conceitual indiscriminadamente.

A ordem geral será:

```text
AGENTS.md
↓
.agents/AGENTS.md
↓
relevant rules
↓
relevant workflow
↓
relevant skills
↓
language profile
↓
project specification
↓
implementation plan
↓
source code
```

Somente o contexto necessário deve ser carregado.

---

# 27. Agent Adapters

O harness deverá suportar inicialmente:

```text
Claude Code
Gemini / Antigravity
OpenCode
```

Adapters devem somente traduzir o contrato do harness para cada ferramenta.

---

# 28. Claude Adapter

Deverá existir:

```text
CLAUDE.md
```

Preferencialmente apontando para:

```text
AGENTS.md
```

Sem duplicar regras.

---

# 29. Gemini Adapter

Deverá existir:

```text
GEMINI.md
```

Também apontando para o contrato canônico.

---

# 30. OpenCode Adapter

OpenCode deverá utilizar:

```text
AGENTS.md
```

como contrato principal.

Qualquer configuração específica deverá permanecer isolada do core.

---

# 31. Safe Change Policy

Toda alteração deverá seguir:

```text
READ
↓
UNDERSTAND
↓
PLAN
↓
MODIFY
↓
TEST
↓
REVIEW
```

Operações destrutivas devem exigir autorização explícita.

---

# 32. Git

O harness deve definir regras para:

* branches;
* commits;
* pull requests;
* review;
* tags;
* release.

Não executar automaticamente:

```text
git reset --hard
git push --force
```

---

# 33. Security

É proibido:

* armazenar secrets;
* expor tokens;
* copiar credenciais para documentação;
* inserir credenciais reais em exemplos;
* remover controles de segurança para fazer testes passarem.

---

# 34. Configuração

O arquivo principal deverá ser:

```text
.agents/config/harness.yaml
```

Estrutura conceitual:

```yaml
harness:
  version: 1

project:
  name: ""
  description: ""
  language: ""
  language_version: ""
  framework: ""

jira:
  enabled: true
  project_key: ""
  base_url: ""

documentation:
  root: docs

quality_gates:
  specification: true
  architecture: true
  implementation: true
  testing: true
  review: true
  release: true
```

---

# 35. Extensibilidade

O harness deve permitir adicionar:

### Linguagens

```text
Python
Go
Java
PHP
C
C++
Rust
TypeScript
Kotlin
C#
```

### Coding agents

```text
Claude
Gemini
OpenCode
Codex
Cursor
Copilot
outros
```

A adição de uma linguagem não deve exigir alteração do core.

A adição de um agent não deve exigir alteração do core.

---

# 36. Requisitos Funcionais

## RF-001 — Bootstrap

O sistema deve realizar uma entrevista inicial antes de criar o skeleton.

## RF-002 — Project Description

O sistema deve armazenar a descrição do projeto.

## RF-003 — Language Selection

O sistema deve solicitar explicitamente a linguagem.

## RF-004 — Language Profile

O sistema deve carregar ou criar o profile da linguagem escolhida.

## RF-005 — Repository Inspection

O sistema deve inspecionar o projeto existente antes de modificar sua estrutura.

## RF-006 — Harness Generation

O sistema deve criar o skeleton do harness após o bootstrap.

## RF-007 — Agent Compatibility

O sistema deve gerar adapters para Claude, Gemini/Antigravity e OpenCode.

## RF-008 — Documentation

O sistema deve manter documentação persistente em `docs/`.

## RF-009 — Jira Traceability

O sistema deve permitir relacionar artefatos ao Jira.

## RF-010 — Workflow Execution

O sistema deve possuir workflows explícitos.

## RF-011 — Quality Gates

O sistema deve possuir quality gates configuráveis.

## RF-012 — Agent Handoff

O sistema deve permitir handoff explícito entre agentes.

## RF-013 — Persistent Artifacts

O estado relevante deve ser persistido em arquivos.

## RF-014 — Extensibility

O sistema deve permitir adição de linguagens e agentes.

---

# 37. Requisitos Não Funcionais

## RNF-001 — Portabilidade

O harness deve ser utilizável em diferentes sistemas operacionais e ambientes de desenvolvimento.

## RNF-002 — Modularidade

Rules, skills, workflows e language profiles devem ser independentes.

## RNF-003 — Manutenibilidade

Cada responsabilidade deve possuir localização única.

## RNF-004 — Rastreabilidade

Mudanças relevantes devem ser associáveis a requisitos e issues.

## RNF-005 — Não acoplamento

O core não deve depender de um LLM ou coding agent específico.

## RNF-006 — Extensibilidade

Novas linguagens devem ser adicionadas sem modificar o core.

## RNF-007 — Segurança

O harness não deve incentivar operações destrutivas ou exposição de credenciais.

---

# 38. Critérios de Aceitação

O harness será considerado inicializado corretamente quando:

1. `AGENTS.md` existir.
2. O projeto possuir descrição.
3. A linguagem estiver explicitamente definida.
4. O Language Profile correspondente existir.
5. `.agents/AGENTS.md` existir.
6. Rules relevantes estiverem presentes.
7. Skills básicas estiverem presentes.
8. Workflows básicos estiverem presentes.
9. Agents especializados estiverem definidos.
10. Templates estiverem presentes.
11. `CLAUDE.md` existir.
12. `GEMINI.md` existir.
13. Adapter do OpenCode estiver definido.
14. `docs/` estiver estruturado.
15. configuração do harness existir.
16. nenhuma configuração existente relevante tiver sido sobrescrita silenciosamente.
17. o projeto continuar executável após a inicialização.
18. a estrutura do projeto respeitar a linguagem selecionada.

---

# 39. Critérios de Qualidade

O harness deverá ser avaliado pela capacidade de responder:

```text
Qual é o projeto?
Qual é a linguagem?
Qual é a specification?
Qual Jira originou a mudança?
Qual arquitetura foi adotada?
Qual agente realizou a etapa?
Quais testes foram executados?
Quem realizou a revisão?
Qual documentação foi atualizada?
O que falta para DONE?
```

Todas essas respostas devem ser obtidas a partir de artefatos persistentes, sem depender exclusivamente da memória da sessão do agente.

---

# 40. Princípio Fundamental

O harness deve obedecer à seguinte regra:

> **Primeiro entender o projeto. Depois construir o harness.**

Portanto:

```text
Project Description
        +
Programming Language
        ↓
Bootstrap
        ↓
Language Profile
        ↓
Harness Generation
        ↓
Development Lifecycle
```

O harness não deve assumir Python como linguagem padrão.

Python é apenas um dos Language Profiles canônicos disponíveis (junto a TypeScript, Go e outros).

---

# 41. Harness Doctor (Auditoria de Sanidade)

O harness deve disponibilizar um mecanismo automatizado de verificação de sanidade (`scripts/harness-doctor.py`), capaz de auditar:

* presença e integridade de `AGENTS.md` e adaptadores de fornecedor;
* presença e validade de `.agents/config/harness.yaml`;
* existência e consistência do Language Profile selecionado;
* estrutura obrigatória de persistência em `docs/`;
* integridade dos diretórios de rules e workflows;
* retorno determinístico de códigos de saída (`0` para sucesso, `1` para falha) para integração com CI/CD.

---

# 42. Harness Upgrade Path

Quando o padrão de engenharia corporativo evoluir, projetos existentes devem ser atualizados através do workflow formal de upgrade:

* preservação integral do código de negócio da aplicação (`src/`, `cmd/`, etc.);
* reconciliação (merge) sem sobrescrita destrutiva de configurações customizadas em `harness.yaml`;
* atualização das regras universais (`.agents/rules/`), workflows e templates;
* revalidação obrigatória de sanidade via `harness-doctor`.

---

# 43. Automação de Scaffolding e Ferramental de Engenharia

Para eliminar latência e riscos de falhas manuais durante o bootstrap em ambientes assistidos por IA, o harness deve incorporar utilitários executáveis em `scripts/`:

* **`scripts/harness-probe.py` (Sonda de Ambiente):** Autodescoberta de interpretadores instalados (Python, Node, Go), gerenciadores de pacotes (`uv`, `pip`, `pnpm`), e estados de autenticação (`gh`, `jira`), evitando suposições ou perguntas redundantes.
* **`scripts/harness-init.py` (Scaffolding em Lote):** Gerador determinístico que popula a árvore completa (`.agents/`, `docs/`, contratos, templates e perfis) em menos de 1 segundo.
* **`scripts/jira-setup.py` (Provisionador Jira):** Provisionamento idempotente de projetos, workflows canônicos e status de ciclo de vida via Jira Cloud REST API v3.
* **`scripts/harness-doctor.py` (Auditor de Sanidade):** Auditoria estrita com 28 checagens para garantir conformidade antes de qualquer commit inicial.


