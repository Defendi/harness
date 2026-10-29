# Regras de Teste

## 1. Tríade de Testes Herméticos
Todas as execuções de testes automatizados devem passar pela tríade completa de qualidade:
1. **Verificação de Linter:** O linting rigoroso passa sem avisos (`ruff check`).
2. **Verificação de Formatação:** A formatação do código cumpre 100% o padrão (`ruff format --check`).
3. **Testes Automatizados:** Suítes de testes unitários e de integração são executadas com 100% de sucesso e cobertura mínima de 80%.

---

## 2. Distinção Estrutural: Testes Unitários vs. Testes de Integração

### 2.1 Testes Unitários (Ciclo TDD Mandatório do Desenvolvedor)
- **Foco:** Lógica de domínio, validação de regras de negócio, transformações de dados e tratamento de exceções.
- **Hermetismo Absoluto:** Zero chamadas de I/O de rede, banco de dados real ou serviços externos. Uso obrigatório de mocks, stubs e fakes sintéticos.
- **Ciclo TDD Obrigatório (Red-Green-Refactor):**
  1. **Red:** O desenvolvedor escreve o teste unitário **antes** do código em `src/`, executando e garantindo que o teste falha deterministicamente pela ausência da implementação.
  2. **Green:** Escreve o código mínimo necessário em `src/` para fazer os testes passarem.
  3. **Refactor:** Limpa e otimiza o código com tipagem estrita e formatação, mantendo os testes 100% verdes.

### 2.2 Testes de Integração (Adaptadores e Infraestrutura)
- **Foco:** Validação de adaptadores com interfaces reais de teste (banco de dados isolado em memória, contêiner efêmero ou mocks de transporte HTTP em nível de socket).
- **Abordagem Estruturada:** Não são guiados por TDD unitário granular, para evitar acoplamento prematuro e mocks excessivamente frágeis de SDKs de terceiros. Focam em contratos de integração e fluxos ponta a ponta dos adaptadores descritos na arquitetura.

---

## 3. Necessidade de Contratos Prévios Claros
- **Proibição de Contratos Inventados:** O agente desenvolvedor é expressamente proibido de inventar ou inferir interfaces públicas, nomes de classes, métodos ou schemas durante a criação dos testes.
- **Rastreabilidade de Contratos:** Todo teste unitário criado deve validar um contrato (assinatura, tipos de entrada/saída e exceções esperadas) pré-estabelecido na especificação OpenSPEC ou no plano de implementação (`docs/execution/<jira>-plan.md`).
- **Tratamento de Ambiguidade:** Se um contrato não estiver claro ou contiver lacunas conceituais, o desenvolvedor deve pausar a tarefa e acionar o Arquiteto/Planner, impedindo a escrita de testes baseados em suposições.

---

## 4. O Papel do Agente Tester (QA): Validação Independente
- **Não Substituição pelo TDD:** O fato de o desenvolvedor adotar TDD e entregar testes unitários 100% verdes não elimina nem diminui o papel do Agente Tester.
- **Segunda Linha de Defesa (Quality Gate Independente):** O Agente Tester atua como auditor independente e adversário de qualidade:
  - **Auditoria de Testes:** Avalia se os testes unitários do desenvolvedor são significativos e não tautológicos (evitando asserts vazios ou testes que mockam a própria lógica a ser testada).
  - **Validação de Edge Cases e Testes de Falha:** Testa cenários adversos de borda não previstos pelo desenvolvedor, injeção de dados maliciosos, limites de estouro de memória/buffer, e condições de concorrência.
  - **Prevenção de Regressão e Cobertura Global:** Executa a suíte integrada completa e audita o limiar de cobertura global ($\ge 80\%$).
  - **Poder de Veto:** Possui autoridade para reprovar o Testing Gate e retornar o card para `A Fazer` caso identifique fragilidades, falta de isolamento ou cobertura deficiente.

---

## 5. Isolamento & Determinismo
- Testes unitários nunca devem fazer requisições de rede de saída reais para hosts ativos da AWS, GitLab, Azure ou SSH.
- Os testes devem ser estritamente determinísticos: independentes de timezone local, ordem de execução e variáveis de ambiente mutáveis.
- Todo bug fix deve incluir obrigatoriamente um teste de regressão que reproduza a falha antes da correção.

---

## 6. Ambiente de Configuração/Segurança de Teste e Regra de Backup Mandatório
- **Arquivos Dedicados de Teste:** O harness de testes deve utilizar arquivos de configuração e políticas de segurança dedicados e desacoplados dos arquivos de produção/operação (ex.: `mcpsentinel_backup.conf` via `SENTINEL_CONF_FILE` e `security_teste.yaml` via `SENTINEL_SECURITY_CONFIG`).
- **Proibição Estrita de Sobrescrita Sem Backup:** É expressamente proibido sobrescrever arquivos de configuração ou segurança durante os testes.
- **Backup Mandatório:** Se qualquer teste necessitar alterar ou manipular arquivos de configuração e/ou segurança, deve ser gerado impreterivelmente um backup prévio (ex.: `.bak` ou timestamp) antes da alteração, garantindo a integridade dos dados e restaurando o arquivo original ao término do teste.
