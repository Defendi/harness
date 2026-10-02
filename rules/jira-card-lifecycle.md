# Regras de Movimentação e Ciclo de Vida dos Cards no Jira

Este documento define as regras estritas e automáticas de movimentação de status dos cards no Jira, orientando todos os agentes, subagentes e desenvolvedores do projeto.

---

## 1. Mapeamento de Status e Transições

O ciclo de vida de qualquer card obedece rigorosamente à seguinte sequência:

```mermaid
flowchart TD
    Backlog["Backlog\n(Brainstorming -> PRD -> TRD -> OpenSPEC)"] -->|Planejamento Finalizado| AFazer["A Fazer\n(Aguardando Dev)"]
    AFazer -->|Início do Dev| EmAndamento["Em Andamento\n(Desenvolvimento e Testes Unitários)"]
    EmAndamento -->|Fim do Dev| ProntoParaReview["Pronto para Review"]
    ProntoParaReview -->|Início do Review| Review["Review\n(Code Reviewer)"]
    Review -->|Com Apontamentos\n(Diversos Comentários)| AFazer
    Review -->|Aprovado 100%\n(Sugestões -> Backlog)| ProntoParaTestar["Pronto Para Testar"]
    ProntoParaTestar -->|Início do QA| Testando["Testando\n(QA Tester)"]
    Testando -->|Com Apontamentos\n(Diversos Comentários)| AFazer
    Testando -->|Aprovado 100%\n(Sugestões -> Backlog)| Concluido["Concluído\n(Commit e Fechamento)"]
```

| Status Canônico no Jira | Responsável            | Condição e Ação                                                                 |
|:------------------------ |:---------------------- |:------------------------------------------------------------------------------- |
| **Backlog**              | Agente / Humano        | Card criado; mantido aqui durante todo o **ciclo Brainstorming, PRD, TRD e OpenSPEC**. |
| **A Fazer**              | Agente / Humano        | Finalização do planejamento sinalizada. Aguarda início do desenvolvimento.      |
| **Em Andamento**         | `developer-agent`      | Início do desenvolvimento sinalizado.                                           |
| **Pronto para Review**   | `developer-agent`      | Toda a implementação e testes unitários concluídos.                             |
| **Review**               | `reviewer-agent`       | Início da revisão de código sinalizado.                                         |
| **Pronto Para Testar**   | `reviewer-agent`       | Review aprovado 100%. Sugestões viram novos cards em Backlog.                   |
| **Testando**             | `tester-agent`         | Início das atividades de QA sinalizado.                                         |
| **Concluído**            | QA / Revisor           | Suíte de testes herméticos 100% aprovada. Commit semântico realizado.           |

> **Nota de Resolução de IDs de Transição:** Cada espaço e projeto no Jira possui IDs numéricos próprios de status e transições. O agente deve inspecionar as transições disponíveis dinamicamente via MCP Atlassian (`getTransitionsForJiraIssue`) ou REST API (`/rest/api/3/issue/{key}/transitions`) para resolver o ID correspondente ao status canônico desejado.

---

## 2. Regras Operacionais de Movimentação

### 2.1 Criação, Especificação e Planejamento (`Backlog`)

- Enquanto os agentes criam um card e esse card estiver sendo planejado, **deve-se manter o card em `Backlog`**.
- **Sequência Obrigatória em `Backlog`:**
  1. **Brainstorming:** Utilizar a skill `brainstorming` antes de qualquer ação técnica ou implementação, alinhando a intenção e aplicando Hard-Gates com o usuário.
  2. **PRD (Product Requirements Document):** O **agente de P.O.** elabora o PRD da feature em `docs/prds/PRD-NNN.md` utilizando a skill `escrever-prd`.
  3. **TRD (Technical Requirements Document):** Após a criação e aprovação do PRD, os agentes técnicos utilizam a skill `escrever-trd` para sincronizar `docs/trd.md` e registrar decisões de arquitetura (ADRs).
  4. **OpenSPEC:** **Somente após o TRD e o PRD estarem devidamente escritos e aprovados**, os agentes criam o documento de especificação executável em `docs/specs/` utilizando a metodologia **OpenSPEC**.
- Nenhum agente pode mudar o estado para "A Fazer" nessa fase sem a conclusão e aprovação desta esteira completa.

### 2.2 Conclusão do Planejamento (`A Fazer`)

- Assim que for sinalizada a **finalização do planejamento** (por definição de um agente ou pelo humano), **deve-se mover o card para `A Fazer`**.
- O card aguarda em `A Fazer` até o momento efetivo de início do desenvolvimento.

### 2.3 Desenvolvimento e Testes Unitários (`Em Andamento` → `Pronto para Review`)

- Assim que for sinalizado o **início do desenvolvimento**, **deve-se mudar o card para `Em Andamento`**.
- O desenvolvedor executa toda a implementação técnica, incluindo preparação de ambiente, código, tipagem defensiva e testes unitários herméticos.
- Assim que finalizada toda a implementação, **deve-se mudar o card para `Pronto para Review`**.

### 2.4 Code Review (`Review` → `A Fazer` ou `Pronto Para Testar`)

- Assim que sinalizado o **início do Review** pelo agente revisor, **deve-se mudar o card para `Review`** (status `Revisar`).
- O agente executa a inspeção detalhada conforme `.agents/rules/coding-standards.md` e `.agents/skills/code-review/SKILL.md`.
- **Tratamento de Resultados do Review:**
  - **Se houver qualquer tipo de apontamento:** deve-se anotar ponto a ponto em **diversos comentários** separados no card e mover o card para **`A Fazer`** para recomeçar o processo de desenvolvimento.
  - **Se passar 100% com apenas algumas sugestões:** deve-se mover o card para **`Pronto Para Testar`**. As sugestões apontadas no review **devem ser criadas como novos cards em `Backlog`**.

### 2.5 Testes de QA (`Testando` → `A Fazer` ou `Concluído`)

- Assim que for sinalizado pelo testador QA o **início da atividade**, **mova o card para `Testando`**.
- O testador executa a suíte hermética completa definida para a linguagem do projeto em `.agents/config/language.yaml` (comandos de `quality_gates.testing` e `quality_gates.implementation`).
- **Tratamento de Resultados do QA:**
  - **Se houver qualquer tipo de apontamento / falha:** deve-se anotar ponto a ponto em **diversos comentários** separados no card e mover o card para **`A Fazer`** para recomeçar o processo.
  - **Se passar 100% com apenas algumas sugestões:** move-se o card para **`Concluído`** (com commit semântico realizado). As sugestões apontadas no teste **devem ser criadas como novos cards em `Backlog`**.

---

## 3. Diretrizes de Comentários e Novos Cards

1. **Comentários Pontuais e Diversos:** Em caso de rejeição (seja no Review ou no QA), cada inconsistência ou apontamento deve ser registrado em um comentário individual no card, com contexto exato (arquivo, linha, causa raiz e recomendação).
2. **Desdobramento de Sugestões:** Sugestões e melhorias não bloqueantes nunca atrasam o card em andamento; são convertidas imediatamente em novos cards em `Backlog` com referência ao card de origem.
