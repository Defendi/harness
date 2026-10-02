# Plano de Testes e Validação: [PROJ-XXX] — [Título da Demanda]

## 1. Metadados
- **Jira Issue:** [PROJ-XXX](https://seu-dominio.atlassian.net/browse/PROJ-XXX)
- **Status:** DRAFT | EXECUTED | PASSED | FAILED
- **Versão:** 1.0.0
- **Responsável:** Tester
- **Data da Execução:** AAAA-MM-DD
- **Branch / Commit:** `feat/PROJ-XXX-descricao-curta` / `commit-hash`

---

## 2. Escopo dos Testes
- **O que está coberto:** Funcionalidades descritas em `docs/specs/PROJ-XXX.md`.
- **O que não está coberto:** Testes de estresse de longa duração (executados em pipeline noturno).

---

## 3. Matriz de Testes
| ID do Teste | Tipo (`Unitário` / `Integração` / `E2E`) | Cenário Avaliado | Resultado Esperado | Status (`PASS` / `FAIL`) |
| :--- | :--- | :--- | :--- | :--- |
| **TC-001** | Unitário | Criação de payload válido com campos obrigatórios | Retorna objeto com status 201 e ID gerado | PASS |
| **TC-002** | Unitário | Validação de payload sem campo mandatório | Retorna erro 422 com mensagem amigável | PASS |
| **TC-003** | Integração | Persistência real no banco de dados de teste | Registro consultável e idempotente | PASS |
| **TC-004** | Integração | Comportamento com timeout do gateway de pagamento | Retry com backoff e posterior fallback | PASS |
| **TC-005** | Segurança | Envio de caracteres de injeção em campos texto | Sanitização sem efeitos colaterais | PASS |

---

## 4. Evidências de Execução de Comandos
Registre a saída dos comandos do language profile:

```text
# Comando executado:
[comando de teste do language profile]

# Resumo da saída:
====== 42 passed in 1.34s ======
Coverage: 88.4%
```

---

## 5. Análise de Cobertura e Gaps
- **Cobertura Total Atingida:** XX.X%
- **Gaps Identificados:** Linhas não cobertas e justificativa técnica de aceitação de risco ou plano de teste complementar.

---

## 6. Parecer do Testing Gate
- **Decisão:** [ ] APROVADO (PASS) | [ ] REPROVADO (FAIL)
- **Bloqueadores / Falhas Abertas:** Nenhum.
- **Próximo Agente Recomendado:** Reviewer.
