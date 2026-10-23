---
name: escrever-req
description: |
  Escrever Documento de Requisitos (ERS/SRS) conforme ISO/IEC/IEEE 29148:2018, formatado segundo normas ABNT, a partir do título e da história principal (desejo) de um projeto ou card. Use quando o usuário ou agente pedir documento de requisitos, levantamento de requisitos, ERS, SRS ou norma 29148.
---

# Escrever Requisitos (ISO/IEC/IEEE 29148:2018 + ABNT)

Produz um **Documento de Requisitos** a partir de um **título** e de uma **história principal** (o desejo: o que se quer resolver). O conteúdo e a estrutura seguem a ISO/IEC/IEEE 29148:2018; a apresentação segue as normas ABNT.

## Papel no fluxo

- Executada pelo **subagente de P.O.** (ou pelo agente que o orquestrador designar). O agente principal **não** a executa diretamente quando houver código/projeto envolvido (ver `AGENTS.md`).
- Antecede o PRD (`escrever-prd`): o documento de requisitos é insumo para PRD, TRD e OpenSPEC. Não substitui nenhum deles.
- Não inventar requisitos: todo requisito deve rastrear a uma resposta do usuário, à história ou a uma premissa explicitamente marcada.

## Entrada

- `titulo` (obrigatório): título do projeto/história.
- `historia` (obrigatório): descrição do desejo/problema a resolver.
- `card` (opcional): chave do card Jira (ex.: `MCP-12`) onde a história está registrada.
- $ARGUMENTS — se fornecido, usar como título e história iniciais.

Se faltar título ou história, pedir ao chamador antes de prosseguir.

## Fluxo de Execução

### 1. Leitura e compreensão

1. Ler atentamente o título e a história. Se houver `card`, ler o card via MCP Atlassian (`getJiraIssue`), incluindo descrição e comentários.
2. Consultar, apenas em leitura, documentos existentes relevantes em `docs/` (PRDs, TRD) para evitar contradição.
3. Redigir internamente e **apresentar ao usuário** um resumo curto:
   - **Problema** entendido (quem sofre, qual dor, em que contexto);
   - **Resultado desejado**;
   - **Lacunas** percebidas.
4. Pedir confirmação ou correção do entendimento antes de continuar.

### 2. Perguntas sobre a solução do problema

Fazer perguntas **fechadas, com opções sempre que possível**, em pequenos lotes (máx. 3–5 por rodada), usando `ask_question`. Cobrir:

- Objetivo e critério de sucesso (como saber que o problema foi resolvido);
- Escopo: o que está dentro e fora;
- Fluxo/comportamento esperado, regras de negócio e exceções;
- Restrições (técnicas, legais, segurança, prazo, compatibilidade);
- Requisitos não funcionais relevantes (desempenho, disponibilidade, segurança, usabilidade);
- Premissas e dependências.

### 3. Perguntas sobre dados necessários

- Quais dados de entrada, processados e de saída existem;
- Origem, formato, volume e frequência de cada dado;
- Dados sensíveis/credenciais e requisitos de proteção (LGPD, sigilo, mascaramento);
- Retenção, integridade, auditoria e rastreabilidade;
- Interfaces e fontes externas (APIs, bancos, arquivos).

### 4. Perguntas sobre agentes (atores)

Entenda "agentes" em sentido amplo — todos os atores que interagem com a solução:

- Usuários humanos e seus papéis/permissões;
- Sistemas externos e serviços integrados;
- Agentes de IA / subagentes necessários, com responsabilidades e limites de autonomia;
- Quem aprova, quem opera e quem audita.

Para cada ator: nome, tipo (humano/sistema/agente), responsabilidade e interfaces.

Regra de condução das etapas 2–4: parar de perguntar quando não houver lacuna bloqueante. Lacunas menores devem virar **premissas** marcadas `*(premissa — confirme ou corrija)*` no documento, nunca ser omitidas.

### 5. Geração do documento (ISO 29148 + ABNT)

1. Ler o template em `references/template-req.md`.
2. Gerar o documento completo preenchendo todas as seções.
3. Aplicar as **características de qualidade da ISO 29148** a cada requisito: necessário, apropriado, não ambíguo, completo, singular (um requisito por sentença), viável, verificável, correto e conforme. Usar a forma **"O sistema deve …"**. Proibido termos vagos ("rápido", "amigável", "adequado") sem limiar mensurável.
4. Atribuir **IDs estáveis** e únicos: `RF-NNN` (funcional), `RNF-NNN` (não funcional), `RI-NNN` (interface), `RD-NNN` (dados), `RR-NNN` (restrição). Cada requisito leva prioridade (MoSCoW: Deve/Deveria/Poderia/Não terá), origem (história, resposta do usuário ou premissa), método de verificação (Inspeção, Análise, Demonstração, Teste) e critério de aceite.
5. Montar a **matriz de rastreabilidade** (necessidade → requisito → verificação).

**Formatação ABNT** (adaptada a Markdown):
- Estrutura: elementos pré-textuais (capa/identificação, resumo, lista de abreviaturas e siglas, sumário), textuais (seções numeradas) e pós-textuais (referências, apêndices) — NBR 14724.
- Numeração progressiva das seções (1, 1.1, 1.1.1) — NBR 6024.
- Resumo em parágrafo único, com palavras-chave — NBR 6028.
- Citações com sistema autor-data — NBR 10520.
- Referências no padrão NBR 6023, em ordem alfabética (incluir obrigatoriamente a ISO/IEC/IEEE 29148:2018).
- Títulos de tabelas e figuras acima, com fonte abaixo.
- Redação em português do Brasil, formal e impessoal.

### 6. Salvar o arquivo

1. Local: `docs/requisitos/` (criar se não existir).
2. Nome: `REQ-<CHAVE-DO-CARD>-<slug-kebab>.md` (ex.: `REQ-MCP-12-auditoria-de-acessos.md`); sem card: `REQ-NNN-<slug>.md` com NNN sequencial a partir de `001`.
3. Frontmatter: `titulo`, `card`, `versao` (`0.1`), `status: rascunho`, `data`, `norma: ISO/IEC/IEEE 29148:2018`.
4. Apresentar o documento ao usuário para revisão pontual; aplicar ajustes preservando os IDs já atribuídos. Em nova versão, incrementar `versao` e registrar no histórico de revisões.

### 7. Comentar no card Jira (se houver)

Se existir card da história:

1. Verificar a conexão com `atlassianUserInfo`; se falhar, avisar o usuário e registrar o documento só em arquivo.
2. Usar `addCommentToJiraIssue` com o **documento de requisitos completo** (consultar `getContentFormatGuide` para o formato) e, no topo, o caminho do arquivo no repositório. Se o documento exceder o limite do Jira, comentar o resumo, a tabela de requisitos e a matriz de rastreabilidade, indicando o arquivo para o texto integral.
3. **Não** alterar o status do card: ele permanece em `Backlog` (ver `.agents/rules/jira-card-lifecycle.md`).
4. Não incluir credenciais, tokens ou dados sensíveis no comentário.

Se não houver card, informar isso no retorno.

### 8. Comunicar o agente chamador

Ao final, enviar ao agente chamador (`send_message` quando for subagente, ou resposta final) um relatório conciso contendo:

- Caminho do documento gerado e versão;
- Resumo do problema e da solução documentada;
- Contagem de requisitos por tipo e lista dos IDs de maior prioridade;
- Atores/agentes identificados;
- **Premissas pendentes** de confirmação e perguntas em aberto;
- Se o comentário foi feito no card (chave e confirmação) ou o motivo de não ter sido;
- Próximo passo sugerido (ex.: `escrever-prd` → `escrever-trd` → OpenSPEC).

## Regras gerais

- Responder e entregar sempre em português do Brasil.
- Ler/gravar apenas dentro do workspace do projeto.
- Documento de requisitos descreve **o quê**, não **como** (sem decisões de projeto/arquitetura, que são TRD/ADR) — exceto restrições de projeto impostas.
- Não sobrescrever documento existente sem informar o usuário; em atualização, versionar.
