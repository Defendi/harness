# Workflow de Arquitetura

## Gatilho
Aprovação da especificação funcional (`docs/specs/<jira>-<slug>.md`).

## Pré-condições
- Specification Gate satisfeito.
- Card permanece no `Backlog`.

## Passos
1. Modelar componentes estruturais, provider adapters e endpoints do MCP server.
2. Verificar o encapsulamento de credenciais zero-trust (as credenciais residem unicamente em armazenamento seguro, nunca passadas para agent tools).
3. Se novas decisões tecnológicas ou mudanças estruturais ocorrerem, redigir um ADR em `docs/decisions/`.
4. Documentar a arquitetura de componentes em `docs/architecture/<jira>-<slug>.md`.
5. Definir interfaces, tipos de exceção e padrões de dependency injection.

## Artefatos
- `docs/architecture/<jira>-<slug>.md`
- `docs/decisions/<number>-<title>.md` (ADR opcional)

## Quality Gates
- Architecture Gate: adere às regras de modularidade e aos padrões de segurança de credenciais.

## Condições de Saída
- Arquitetura aprovada e commitada; pronta para Planning.

## Tratamento de Falhas
- Se riscos de segurança forem detectados na arquitetura, pause e reprojete as fronteiras de credenciais.
