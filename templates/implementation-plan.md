# Plano de Implementação: [PROJ-XXX] — [Título da Demanda]

## 1. Metadados
- **Jira Issue:** [PROJ-XXX](https://seu-dominio.atlassian.net/browse/PROJ-XXX)
- **Status:** DRAFT | APPROVED | IN_PROGRESS | COMPLETED
- **Versão:** 1.0.0
- **Responsável:** Developer / Architect
- **Data:** AAAA-MM-DD
- **Branch:** `feat/PROJ-XXX-descricao-curta`

---

## 2. Rastreabilidade com a Especificação
- **Documento de Especificação:** `docs/specs/PROJ-XXX.md`
- **Documento de Arquitetura:** `docs/architecture/PROJ-XXX.md`
- **ADRs Vinculadas:** `docs/decisions/ADR-XXXX.md`

---

## 3. Arquivos e Módulos Afetados
| Arquivo | Ação (`Criar` / `Modificar` / `Excluir`) | Descrição da Mudança |
| :--- | :--- | :--- |
| `src/domain/entities/...` | Criar | Nova entidade com validações de regra de negócio |
| `src/services/...` | Modificar | Integração do novo fluxo de processamento |
| `tests/unit/...` | Criar | Suíte de testes unitários para a nova funcionalidade |

---

## 4. Etapas Sequenciais de Implementação
Execute estritamente passo a passo em pequenas alterações atômicas:

### Etapa 1: Preparação de Tipos e Modelos
- [ ] Criar interfaces / structs / classes em `src/domain/...`
- [ ] Implementar validações estáticas e invariantes

### Etapa 2: Implementação da Regra de Negócio e Testes Unitários (TDD)
- [ ] Escrever casos de teste unitários cobrindo cenários felizes e de borda
- [ ] Implementar o serviço de domínio até todos os testes passarem
- [ ] Verificar linter e tipagem estática

### Etapa 3: Integração com Infraestrutura / Persistência
- [ ] Implementar repositório ou adaptador de saída
- [ ] Adicionar testes de integração herméticos com mocks ou banco efêmero

### Etapa 4: Exposição do Endpoint / Interface Pública
- [ ] Implementar handler/controller com validação de payload
- [ ] Conectar ao roteador e documentação de API

---

## 5. Estratégia de Migração e Compatibilidade
- Há alterações no schema de banco de dados? (`Sim` / `Não`)
- Se sim: migration idempotente em `db/migrations/...`
- Há risco de quebra de contrato retrocompatível? Como mitigar?

---

## 6. Estratégia de Rollback
- Em caso de falha crítica em produção:
  - Reverter merge commit ou desativar feature flag `FEATURE_PROJ_XXX`.
  - Script ou comando de rollback de migration se aplicável.

---

## 7. Critérios de Conclusão para Handoff (Implementation Gate)
- [ ] Todos os arquivos planejados foram criados/alterados.
- [ ] Testes unitários executados e com cobertura satisfatória (`tests_pass: true`).
- [ ] Linter e formatador sem avisos ou erros.
- [ ] Nenhuma credencial ou secret presente no diff.
- [ ] Handoff gerado para o subagente **Tester**.
