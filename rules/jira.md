# Regras Universais de Integração e Ciclo de Vida do Jira

## 1. Princípio Fundamental
O Jira é a autoridade central de gestão do trabalho e rastreabilidade nos projetos do Defendi.
Nenhum desenvolvimento ou alteração arquitetural deve ocorrer sem um identificador de card válido (ex.: `PROJ-123`).

## 2. Validação Obrigatória de Conexão MCP (Passo Zero)
Ao iniciar qualquer sessão de trabalho:
1. Validar a conexão ativa com o MCP do Atlassian (`atlassianUserInfo` ou `getAccessibleAtlassianResources`).
2. Se falhar, interromper imediatamente e alertar o usuário para renovação de token ou ajuste de configuração.

## 3. Comentários Estruturados a Cada Transição de Fase
A cada avanço no ciclo de vida (`Discovery → Specification → ... → Release`), o agente responsável DEVE adicionar um comentário no Jira com o seguinte padrão:

```markdown
🤖 **Harness AI Engineering Update**
* **Fase:** [NOME_DA_FASE] (ex.: IMPLEMENTATION -> TESTING)
* **Agente:** [Nome do Subagente]
* **Branch / Commit:** `[branch]` / `[hash]`
* **Artefatos Produzidos:**
  - `docs/specs/[PROJ-XXX].md`
  - `docs/execution/[PROJ-XXX]-plan.md`
* **Quality Gate:** [NOME_DO_GATE] -> ✅ PASSED
  - Evidência: `[resumo de comandos executados com exit code 0]`
* **Próximo Passo / Agente:** Delegado para subagente `[Tester/Reviewer/etc.]`
```

## 4. Rastreabilidade com Artefatos Locais
Todos os arquivos produzidos em `docs/` devem conter no cabeçalho o campo:
```yaml
jira_issue: PROJ-XXX
```
Nunca commitar documentos ou código com referências fictícias ou sem card associado.

## 5. Transições de Status
- O agente não deve pular etapas arbitrariamente.
- A transição para `IN REVIEW` só ocorre após a emissão de parecer favorável pelo subagente `Tester` (`testing_gate: PASSED`).
- A transição para `DONE` só é permitida após aprovação do `Reviewer` e conclusão da documentação pelo agente `Release`.
