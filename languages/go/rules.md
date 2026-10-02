# Regras de Engenharia para Projetos Go

## 1. Toolchain Padrão
- **Gerenciador de Dependências:** `go mod` com `go.mod` e `go.sum` versionados.
- **Linter:** `golangci-lint` habilitando linters essenciais (`errcheck`, `govet`, `staticcheck`, `unused`, `gosec`).
- **Formatter:** `gofmt` com flags padrão (`-s -w`).
- **Testes & Concorrência:** `go test -race` em todos os testes para prevenção de data races.
- **Auditoria de Vulnerabilidades:** `govulncheck`.

## 2. Padrões de Código
- **Tratamento Explícito de Erros:** Todo erro retornado deve ser verificado (`if err != nil`). Nunca ignorar erros com `_ = fn()`. Enriquecer erros contextualmente com `fmt.Errorf("falha ao consultar usuário %s: %w", id, err)`.
- **Context:** Toda função de I/O, rede ou banco de dados deve receber `ctx context.Context` como primeiro parâmetro.
- **Zero Allocations & Concorrência:** Não criar goroutines órfãs sem cancelamento coordenado por context ou `sync.WaitGroup`.
- **Interfaces Pequenas:** Definir interfaces no consumidor da dependência, não no pacote produtor. Preferir interfaces pequenas (1 ou 2 métodos).

## 3. Estrutura de Diretórios (Standard Go Project Layout)
```text
cmd/
└── app/                # Main entrypoint da aplicação
internal/
├── domain/             # Entidades de negócio e erros canônicos
├── service/            # Lógica de aplicação e casos de uso
├── repository/         # Implementação de acesso a dados (SQL, Redis)
└── handler/            # Handlers HTTP ou gRPC
pkg/                    # Pacotes utilitários públicos reutilizáveis (se houver)
tests/                  # Testes de integração de ponta a ponta
```
