# Regras de Padrões de Código

## 1. Qualidade de Código e Formatação
- Conformidade estrita com formatadores e linters específicos da linguagem (ex.: `ruff check` e `ruff format` para Python).
- Sem código morto, imports não utilizados ou prints de debug remanescentes.
- Anotações explícitas de tipo em todas as funções públicas, métodos e assinaturas de classe.
- **Anonimato de IA (Ghostwriting):** É ESTRITAMENTE PROIBIDO adicionar comentários como "gerado por IA", "aqui está o código do Claude", ou qualquer outra referência a IAs/LLMs em comentários no código. Todo código deve transparecer autoria humana e profissional.

## 2. Tratamento de Erros e Logging
- Use tratamento de exceções estruturado. Capture exceções específicas; nunca use um `except:` genérico.
- Faça log com os níveis apropriados (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- **Nunca registre dados sensíveis no log**: mascare tokens, senhas, chaves privadas, headers de autorização.

## 3. Imutabilidade e Previsibilidade
- Prefira estruturas de dados imutáveis e schemas explícitos (ex.: modelos Pydantic / Dataclasses).
- Evite efeitos colaterais em getters de propriedades ou métodos de query.
- Valide entradas rigorosamente nos limites (parâmetros de ferramentas MCP).

## 4. Simplicidade de Código
- Mantenha funções concisas e focadas em uma única responsabilidade.
- Não faça over-engineering em abstrações antes que exista um segundo caso de uso.
