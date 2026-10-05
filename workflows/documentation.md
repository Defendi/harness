# Workflow de Documentação

## Gatilho
Conclusão dos testes ou mudanças comportamentais significativas que exijam sincronização de conhecimento.

## Pré-condições
- Testes passando; card próximo da conclusão ou recém-concluído.

## Passos
1. Escanear alterações em especificações, documentos de arquitetura e código-fonte.
2. Sincronizar contratos de API, seções de uso do README e quickstarts.
3. Validar todos os links internos de arquivos, títulos e diagramas.
4. Registrar retrospectiva de implementação ou resumos de execução em `docs/execution/`.
5. Fazer commit das atualizações de documentação seguindo o Conventional Commits (`docs(scope): ...`).

## Artefatos
- Documentação sincronizada em `docs/` e `README.md`.

## Quality Gates
- Documentation Gate: zero links quebrados, exemplos de código correspondem ao comportamento real.

## Condições de Saída
- Documentação atualizada e commitada no Git.

## Tratamento de Falhas
- Se for encontrada discrepância entre a documentação e a implementação, abra uma issue de documentação ou corrija imediatamente.
