# Regras Universais de Versionamento e Ciclo Git

## 1. Nomenclatura Obrigatória de Branches
Todo branch de desenvolvimento deve obrigatoriamente estar vinculado a uma chave do Jira:

```text
<tipo>/<CHAVE-JIRA>-<slug-curto>
```

### Prefixos Aceitos:
- `feat/PROJ-123-autenticacao-jwt` (Novas funcionalidades)
- `fix/PROJ-124-corrigir-timeout-cache` (Correção de bugs)
- `refactor/PROJ-125-modularizar-repositorios` (Refatorações sem alteração de comportamento)
- `test/PROJ-126-adicionar-testes-e2e` (Apenas testes)
- `docs/PROJ-127-atualizar-openapi` (Apenas documentação)

## 2. Padrão de Mensagens de Commit (Conventional Commits + Jira)
Todas as mensagens de commit devem seguir rigorosamente o padrão:

```text
<tipo>(<escopo>): [CHAVE-JIRA] <descrição concisa no presente>

[Corpo opcional explicando motivação e detalhes técnicos]

[Rodapé opcional: Ref PROJ-XXX, Closes PROJ-XXX]
```

### Exemplos Válidos:
- `feat(auth): [PROJ-123] implementa validacao de tokens rsa`
- `fix(billing): [PROJ-124] previne divisao por zero no calculo de juros`
- `test(users): [PROJ-125] adiciona casos de borda para email duplicado`

## 3. Atomicidade e Qualidade dos Commits
- Cada commit deve representar uma alteração lógica única, coesa e com build passando.
- Não acumular centenas de arquivos sem commit intermediário.
- Nunca commitar arquivos sensíveis (`.env`, `.pem`, tokens, credenciais) ou temporários de build (`__pycache__`, `node_modules`, `dist/`).

## 4. Política Estrita de Comandos Destrutivos (Safe Change Policy)
O agente e os subagentes são ESTRITAMENTE PROIBIDOS de executar de forma autônoma:
- `git reset --hard`
- `git push --force` ou `git push -f`
- `git clean -fdx`
- `git branch -D` em branches compartilhados

Qualquer necessidade de reversão destrutiva deve ser solicitada explicitamente ao usuário com justificativa técnica.

## 5. Pull Requests e Integração
- PRs devem conter resumo, link para o Jira e referência ao plano de implementação.
- O branch principal (`main` ou `master`) é protegido: código só entra via PR revisado e aprovado pelo subagente `Reviewer` e com CI verde.
