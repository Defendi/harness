# Skill de Design de Arquitetura

## Propósito
Projetar a arquitetura do sistema, diagramas de componentes, interfaces e Architectural Decision Records (ADRs), garantindo segurança, isolamento de credenciais e modularidade.

## Entradas
- Especificação validada (`docs/specs/<jira>-<slug>.md`)
- Contexto de arquitetura existente em `docs/architecture/`

## Pré-condições
- Specification Gate satisfeito.

## Procedimento
1. Modelar os componentes do sistema e os caminhos de comunicação.
2. Garantir limite estrito de credenciais: as credenciais nunca saem do servidor nem passam para respostas de ferramentas.
3. Projetar interfaces/classes abstratas para provedores externos.
4. Registrar as principais decisões de design como ADRs em `docs/decisions/` usando o template.
5. Criar ou atualizar a documentação de arquitetura em `docs/architecture/`.

## Saídas
- `docs/architecture/<jira>-<slug>.md`
- `docs/decisions/<number>-<title>.md` (se as decisões justificarem uma ADR)

## Validação
- A arquitetura está em conformidade com o gerenciamento de segredos Zero Trust.
- Princípios de modularidade e desacoplamento respeitados.

## Condições de Falha
- Comprometimento de segurança na manipulação de segredos.
- Componentes fortemente acoplados violando a separação de responsabilidades.
