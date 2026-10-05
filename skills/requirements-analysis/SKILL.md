# Skill de Análise de Requisitos

## Propósito
Analisar declarações de problemas recebidas, solicitações de usuários ou metas de alto nível e extrair requisitos funcionais e não funcionais claros e inequívocos.

## Entradas
- Resumo e descrição do card do Jira
- Prompts do usuário ou feedback de stakeholders
- Contexto do sistema existente

## Pré-condições
- Conexão ativa com o Jira ou acesso à declaração do problema.
- Working directory limpo.

## Procedimento
1. Fazer o parse da solicitação para extrair papéis de usuário, objetivos principais e restrições.
2. Identificar dependências em sistemas externos (AWS, GitLab, Azure, SSH).
3. Mapear potenciais riscos de segurança, credenciais e compliance.
4. Formular perguntas explícitas para quaisquer itens ambíguos.
5. Produzir um draft estruturado de requisitos.

## Saídas
- Inventário estruturado de requisitos formatado de acordo com o template de especificação.

## Validação
- Cada requisito possui um critério de aceitação verificável.
- Restrições de segurança para credenciais são declaradas explicitamente.

## Condições de Falha
- Requisitos ambíguos ou conflitantes deixados sem resolução.
- Critérios de aceitação não verificáveis.
