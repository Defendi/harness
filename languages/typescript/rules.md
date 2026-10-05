# Regras de Engenharia para Projetos TypeScript

## 1. Toolchain Padrão
- **Gerenciador de Pacotes:** `pnpm` (rápido, determinístico e econômico em disco).
- **Compilador & Type Checker:** `tsc` com `tsconfig.json` rigoroso (`"strict": true`, `"noImplicitAny": true`).
- **Linter & Formatter:** `biome` para linting e formatação unificada e instantânea.
- **Test Runner:** `vitest` com suporte nativo a ESM e TypeScript sem overhead de transpilação.

## 2. Padrões de Código
- **Proibição de `any`:** O uso de `any` é estritamente proibido. Em casos de incerteza, utilizar `unknown` com type guards explícitos.
- **Validação em Runtime:** Para dados externos (requisições HTTP, variáveis de ambiente, mensagens), utilizar schemas com `zod` ou `valibot`.
- **Tratamento de Erros:** Favorecer o padrão Result (`Result<T, E>`) ou classes de erro customizadas estendendo `Error`, sem lançar literais de string ou objetos soltos.
- **Módulos:** Utilizar ESM nativo (`import` / `export`), imports absolutos configurados com path aliases (`@/domain/...`).

## 3. Estrutura de Diretórios
```text
src/
├── domain/             # Entidades, value objects e interfaces puras
├── application/        # Use cases e serviços de aplicação
├── infrastructure/     # Banco de dados, clientes HTTP externos, repositórios
└── presentation/       # Rotas HTTP, handlers e controllers
tests/
├── unit/               # Testes unitários com mocks
└── integration/        # Testes de integração end-to-end com supertest/testcontainers
