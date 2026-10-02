# Workflow de Execução de Quality Gates

## 1. Objetivo
Garantir que nenhuma demanda transicione de status no Jira ou avance no ciclo de engenharia sem que os critérios e comandos definidos nos **Quality Gates Executáveis** tenham sido satisfeitos com comprovação objetiva (exit code `0` e artefatos gerados).

---

## 2. Mapa dos Quality Gates no Ciclo de Vida

```text
[SPECIFICATION] ───> Gate 1: Specification Gate
      │
[ARCHITECTURE]  ───> Gate 2: Architecture Gate
      │
[IMPLEMENTATION]───> Gate 3: Implementation Gate (Linter, Typecheck, Formatter)
      │
[TESTING]       ───> Gate 4: Testing Gate (Unit, Integration, Coverage >= 80%)
      │
[REVIEW]        ───> Gate 5: Review Gate (Code Review Report Aprovado)
      │
[RELEASE]       ───> Gate 6: Release Gate (Build, Clean Git, SemVer)
```

---

## 3. Protocolo de Validação de Cada Gate

### Gate 1: Specification Gate
- **Responsável:** Architect
- **Critérios Obrigatórios:**
  1. Arquivo `docs/specs/{JIRA_ISSUE}.md` criado com metadados preenchidos.
  2. Todos os Requisitos Funcionais, Não-Funcionais e Critérios de Aceitação definidos.
  3. Ausência de termos ambíguos ("rápido", "intuitivo", "etc.") sem métrica.

### Gate 2: Architecture Gate
- **Responsável:** Architect
- **Critérios Obrigatórios:**
  1. Arquivo `docs/architecture/{JIRA_ISSUE}.md` criado e alinhado com a spec.
  2. Decisões arquiteturais fundamentais registradas em `docs/decisions/ADR-XXXX.md`.
  3. Diagrama estrutural atualizado.

### Gate 3: Implementation Gate
- **Responsável:** Developer
- **Critérios Obrigatórios:**
  1. Execução obrigatória dos comandos definidos em `language.yaml:quality_gates.implementation`.
  2. Todos os comandos devem retornar código de saída `0`.
  3. Linter sem warnings bloqueantes, formatador verificado e tipagem estática 100% satisfeita.
  4. Nenhuma credencial ou secret identificada no diff.

### Gate 4: Testing Gate
- **Responsável:** Tester
- **Critérios Obrigatórios:**
  1. Execução dos comandos definidos em `language.yaml:quality_gates.testing`.
  2. Cobertura de código superior ao limiar estipulado (mínimo de 80%).
  3. Testes executados com detecção de concorrência/race conditions se aplicável.
  4. Relatório gerado em `docs/execution/{JIRA_ISSUE}-test-plan.md`.

### Gate 5: Review Gate
- **Responsável:** Reviewer
- **Critérios Obrigatórios:**
  1. Subagente Reviewer não pode ser o mesmo que implementou o código.
  2. Verificação de checklist em `docs/execution/{JIRA_ISSUE}-review.md`.
  3. Decisão final explicitamente marcada como `APPROVED`.

### Gate 6: Release Gate
- **Responsável:** Release Agent
- **Critérios Obrigatórios:**
  1. Comando de build (`language.yaml:commands.build`) executado com sucesso.
  2. Árvore Git limpa (sem arquivos não commitados ou não rastreados).
  3. `docs/execution/release-notes-vX.Y.Z.md` criado e tag Git anotada.

---

## 4. Tratamento de Falhas em Gates
- Se qualquer comando ou critério falhar:
  1. O gate emite status `FAILED`.
  2. A transição no Jira é bloqueada.
  3. O card é mantido no status atual e recebe comentário de erro com o log resumido.
  4. O trabalho retorna ao agente responsável para saneamento.
