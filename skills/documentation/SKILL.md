# Skill de Documentação

## Propósito
Manter, organizar e sincronizar toda a documentação técnica sob `docs/` com as alterações contínuas de código e evoluções arquiteturais.

## Entradas
- Código implementado, resultados de testes e ADRs
- Documentação existente em `docs/`

## Pré-condições
- Etapas de implementação e testes concluídas.

## Procedimento
1. Identificar toda a documentação impactada pela alteração (README, specs, arquitetura, guias de API).
2. Atualizar definições de interface, instruções de uso e parâmetros de configuração.
3. Validar todos os links internos de arquivos e referências de código.
4. Registrar o resumo da execução em `docs/execution/`, se necessário.
5. Garantir que os documentos Markdown sigam os padrões de formatação.

## Saídas
- Documentação sincronizada em `docs/` e `README.md`.

## Validação
- Nenhum link quebrado.
- Exemplos de código e schemas correspondem ao comportamento real.

## Condições de Falha
- Inconsistências entre o comportamento documentado e a implementação real.
- Links markdown quebrados ou seções incompletas.
