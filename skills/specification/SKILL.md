# Skill de Especificação

## Propósito
Formalizar os requisitos analisados em especificações completas e versionadas sob `docs/specs/`.

## Entradas
- Saídas da análise de requisitos
- Chave da issue do Jira (`MCPS-xxx`)

## Pré-condições
- Análise de requisitos concluída e validada.

## Procedimento
1. Criar `docs/specs/<jira>-<slug>.md` utilizando `.agents/templates/specification.md`.
2. Definir o cabeçalho de metadados (jira key, status, versão, data).
3. Especificar user stories, comportamento funcional, condições de erro e contratos de API.
4. Definir Critérios de Aceitação testáveis utilizando o formato Given/When/Then onde aplicável.
5. Revisar a especificação em relação aos guardrails de arquitetura e segurança.

## Saídas
- Arquivo de especificação persistido: `docs/specs/<jira>-<slug>.md`.

## Validação
- A especificação segue o template padrão.
- Todos os critérios de aceitação são testáveis.
- Vinculada ao card correspondente do Jira.

## Condições de Falha
- Especificações incompletas sem caminhos de erro.
- Modelos de dados ou interfaces não especificados.
