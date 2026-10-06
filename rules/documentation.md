# Regras de Documentação

## 1. Documentação como Código
- Toda a documentação do projeto reside sob `docs/` e é versionada no Git junto ao código-fonte.
- Mantenha a documentação continuamente sincronizada com o comportamento do software.
- Documentação desatualizada deve ser atualizada ou sinalizada antes de concluir um card.
- **Anonimato de IA (Ghostwriting):** É ESTRITAMENTE PROIBIDO incluir referências a IA, Claude, Claude Code, Antigravity, LLMs, ChatGPT, bots ou prompts na documentação do projeto. A documentação deve refletir autoria 100% humana.

## 2. Taxonomia de Diretórios
- `docs/specs/`: Especificações funcionais e não funcionais detalhadas vinculadas a issues do Jira.
- `docs/architecture/`: Diagramas de sistema, limites de componentes, modelos de interface.
- `docs/decisions/`: Architectural Decision Records (ADRs).
- `docs/execution/`: Planos de execução, resumos de revisão, relatórios de testes.
- `docs/references/`: Notas de documentação de APIs externas, cheat sheets, guias.

## 3. Formatação e Links
- Use o padrão GitHub Flavored Markdown.
- Vincule símbolos de código e caminhos relativos de forma limpa usando links em Markdown.
- Mantenha um sumário claro para documentos com mais de 100 linhas.
