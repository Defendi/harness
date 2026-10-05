# Security Review Skill

## Objetivo
Examinar codebase, configurações e dependências em busca de vulnerabilidades de segurança, riscos de exposição de credenciais e vetores de ataque de injeção.

## Entradas
- Codebase completa e arquivos de configuração
- Árvore de dependências (`pyproject.toml`, pacotes do virtualenv)
- Histórico do Git e diffs

## Pré-condições
- Git status limpo; acesso à codebase e à árvore de dependências.

## Procedimento
1. Fazer varredura em busca de credenciais hardcoded, API keys, tokens privados ou chaves SSH.
2. Verificar a cobertura do `.gitignore` para configurações locais e tokens.
3. Auditar invocações de comandos externos e inputs de ferramentas MCP contra vulnerabilidades de injeção.
4. Verificar o isolamento de credenciais: confirmar que os tokens são carregados com segurança na memória e nunca expostos em respostas de ferramentas.
5. Revisar dependências em busca de vulnerabilidades conhecidas (ex.: `pip audit` ou `safety`, se configurado).

## Saídas
- Resumo da avaliação de segurança registrado na documentação de revisão ou arquitetura.

## Validação
- Zero segredos no histórico do repositório Git ou working tree.
- Validação de entrada presente em todas as fronteiras externas.

## Condições de Falha
- Presença de qualquer segredo no código ou na configuração.
- Inputs não sanitizados executados em subshells ou chamadas de sistema.
