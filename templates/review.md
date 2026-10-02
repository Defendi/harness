# Relatório de Code Review: [PROJ-XXX] — [Título da Demanda]

## 1. Metadados
- **Jira Issue:** [PROJ-XXX](https://seu-dominio.atlassian.net/browse/PROJ-XXX)
- **Status:** APPROVED | REQUEST_CHANGES | BLOCKED
- **Revisor:** Reviewer
- **Autor / Desenvolvedor:** Developer
- **Data:** AAAA-MM-DD
- **Pull Request / Branch:** PR #[000] / `feat/PROJ-XXX-descricao-curta`

---

## 2. Checklist de Validação do Revisor

### 2.1 Aderência à Especificação
- [ ] O código implementa todos os requisitos descritos em `docs/specs/PROJ-XXX.md`.
- [ ] Não há "scope creep" (funcionalidades extras não solicitadas).
- [ ] As regras de negócio e critérios de aceitação foram cumpridos integralmente.

### 2.2 Qualidade e Boas Práticas
- [ ] Arquitetura segue as convenções e camadas definidas em `docs/architecture/`.
- [ ] Nomes de funções, variáveis e módulos são expressivos e autoexplicativos.
- [ ] Tratamento adequado de erros sem supressão silenciosa (`except: pass` ou similar).
- [ ] Não há código duplicado ou lógica desnecessariamente convoluta.

### 2.3 Testes e Cobertura
- [ ] Testes unitários acompanham as alterações realizadas.
- [ ] Casos de borda (edge cases) e cenários de erro foram testados.
- [ ] A suíte de testes passou sem quebras ou dependências ocultas.

### 2.4 Segurança e Sanidade
- [ ] Nenhuma credencial, token, senha ou chave privada está no commit ou em logs.
- [ ] Entradas de dados são sanitizadas e validadas contra injeções.
- [ ] Não há operações destrutivas ou alterações de configuração sem justificativa.

---

## 3. Apontamentos e Comentários

| Arquivo e Linha | Severidade (`Bloqueador` / `Importante` / `Sugestão`) | Descrição do Apontamento | Resolução / Status |
| :--- | :--- | :--- | :--- |
| `src/domain/service.py:45` | Importante | Falta timeout explícito na chamada HTTP externa | Corrigido no commit `abc1234` |
| `src/domain/entities.py:12` | Sugestão | Adicionar docstring explicando invariante de data | Aceito e aplicado |

---

## 4. Parecer Final (Review Gate)
- **Resultado:** [ ] APROVADO | [ ] REQUER MUDANÇAS | [ ] REJEITADO
- **Justificativa:** O código atende plenamente aos critérios de aceitação e aos padrões de qualidade da organização.
- **Próximo Agente Recomendado:** Documentation / Release.
