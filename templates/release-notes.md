# Release Notes — Versão [vX.Y.Z]

## Informações do Release
- **Versão:** vX.Y.Z
- **Data de Publicação:** AAAA-MM-DD
- **Responsável:** Release Agent
- **Changelog / Tag Git:** `refs/tags/vX.Y.Z`
- **Ambiente Alvo:** Staging / Production

---

## 🚀 Novas Funcionalidades (Features)
- **[PROJ-101]** Adiciona suporte à autenticação federada via OAuth2 e tokens JWT.
- **[PROJ-102]** Cria endpoint de reconciliação assíncrona de relatórios contábeis.

---

## 🐛 Correções de Erros (Bug Fixes)
- **[PROJ-103]** Corrige erro de concorrência na escrita simultânea de transações em cache.
- **[PROJ-104]** Ajusta validação de data limite para evitar timezone offset incorreto.

---

## ⚡ Melhorias de Performance e Refatorações
- **[PROJ-105]** Otimização da consulta de extrato bancário reduzindo tempo de resposta em 40%.

---

## 🔒 Segurança e Dependências
- Atualização da dependência `xyz` para versão segura mitigando CVE-XXXX-YYYY.

---

## ⚠️ Breaking Changes & Instruções de Migração
- **Atenção:** O campo `client_uuid` foi renomeado para `customer_id` no payload da API v2.
- **Instruções de Migração:**
  1. Executar a migration de banco: `[comando de migration]`
  2. Atualizar as variáveis de ambiente necessárias: `ENV_NOVA_CONFIG=true`

---

## 📋 Checklist de Validação do Release (Release Gate)
- [ ] Todos os testes automatizados passaram no branch de release.
- [ ] Artefatos compilados/empacotados e imagens publicadas com tag imutável.
- [ ] Tarefas relacionadas no Jira transicionadas para `DONE` / `RELEASED`.
- [ ] Documentação de API e manuais operacionais atualizados.
