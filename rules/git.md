# Regras de Git & Controle de Versão

## 1. Estratégia de Branches
- Branch principal: `main` (código verificado e pronto para produção).
- Branches de trabalho: `feature/<issue-key>-<short-description>`, `fix/<issue-key>-<short-description>`, `chore/<issue-key>-<short-description>`.
- Branches devem ser criadas a partir da `main` atualizada.

## 2. Padrões de Commit
- Siga o Conventional Commits:
  - `feat(scope): adiciona nova funcionalidade`
  - `fix(scope): corrige bug ou defeito`
  - `test(scope): adiciona ou modifica suítes de teste`
  - `docs(scope): atualiza a documentação`
  - `refactor(scope): refatora sem alteração de comportamento`
  - `chore(scope): build, tooling, dependências`
- Sempre referencie a issue do Jira na mensagem ou no corpo.
- **Anonimato de IA (Ghostwriting):** É ESTRITAMENTE PROIBIDO incluir referências a IA, Claude, Claude Code, Antigravity, LLMs, ChatGPT, bots ou prompts nas mensagens de commit. O histórico de commits deve refletir autoria 100% humana.

## 3. Guardrails de Segurança
- **NUNCA execute operações destrutivas do Git automaticamente**:
  - `git reset --hard` é proibido sem autorização explícita.
  - `git push --force` ou `--force-with-lease` é proibido em branches protegidas.
- Sempre verifique `git status` e `git diff` antes de fazer o commit.
