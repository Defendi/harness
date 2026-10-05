# Regras de Arquitetura

## 1. Princípios
- **Separação de Preocupações:** Isolar claramente a camada de transporte/protocolo (MCP), a lógica de domínio e as integrações de provedores (AWS, GitLab, Azure, SSH).
- **Isolamento Hermético de Segredos:** O armazenamento e a resolução de credenciais nunca devem vazar tokens, chaves ou passphrases para saídas de ferramentas MCP, logs ou respostas de agentes LLM.
- **Design Defensivo:** Fail-closed por padrão. Se uma credencial não puder ser validada ou uma operação não for permitida, rejeite imediatamente com erros estruturados.
- **Architectural Decision Records (ADRs):** Mudanças significativas na estrutura, escolhas de bibliotecas ou postura de segurança devem ser registradas em `docs/decisions/` seguindo o template de ADR.

## 2. Modularidade & Interfaces
- Definir interfaces abstratas explícitas para provedores de serviços externos.
- Evitar acoplamento forte entre a configuração do servidor FastMCP e os clientes de provedores.
- Fornecer injeção de dependência ou factory patterns para facilitar testes unitários herméticos sem dependências de rede.

## 3. Arquitetura Evolutiva
- Novos provedores (ex.: provedores adicionais de VCS ou nuvem) devem ser adicionados como plugins/adapters sem modificar implementações funcionais existentes.
- Manter a compatibilidade retroativa para ferramentas MCP e recursos expostos a clientes de IA.
