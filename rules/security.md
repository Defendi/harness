# Regras de Segurança

## 1. Gerenciamento de Segredos Zero Trust
- **Nunca faça commit de segredos no Git**: chaves de API, chaves privadas SSH, tokens de nuvem ou tokens de acesso pessoal nunca devem aparecer em arquivos do repositório.
- Garanta que todos os arquivos de credenciais, overrides locais e arquivos `.env*` estejam estritamente cobertos pelo `.gitignore`.
- Sanitize todas as strings antes de enviá-las para clientes MCP ou registrar em logs.

## 2. Princípio do Menor Privilégio
- Ferramentas MCP devem conceder aos clientes de IA a capacidade mínima necessária para a tarefa.
- Operações de leitura devem ser separadas de operações de escrita/execução.
- Operações destrutivas (excluir recursos, fazer push de atualizações forçadas) exigem confirmação explícita.

## 3. Sanitização de Entrada
- Valide todos os parâmetros de entrada das ferramentas contra ataques de injeção (command injection, path traversal, SQL injection).
- Ao invocar comandos SSH ou processos locais, evite interpolação de shell (`shell=True`); utilize sempre listas de argumentos parseadas.
