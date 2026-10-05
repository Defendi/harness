# Bootstrap Workflow

## Gatilho
Inicialização de um novo projeto ou onboarding inicial do Application Development Harness.

## Pré-condições
- Diretório de workspace estabelecido.
- Intenção do usuário de configurar ou adaptar o repositório.

## Etapas
1. Executar a Entrevista de Bootstrap do Projeto (Descrição do Projeto, Linguagem, Diretório, Jira, GitHub). Não presuma nenhuma linguagem ou framework.
2. Conduzir questionamento adaptativo ("Pergunte apenas o que for necessário") com base na stack escolhida pelo usuário.
3. Inspecionar o ambiente e as ferramentas do workspace (usando `harness-probe.py` opcionalmente).
4. Detectar o perfil de linguagem necessário, dependências e setup de ambiente.
5. Estabelecer conexão com o Jira e alinhamento de board/workflow do workspace.
6. Criar ou verificar repositório remoto no GitHub.
7. Gerar o core do harness: `AGENTS.md`, adapters (`CLAUDE.md`, `GEMINI.md`), `.agents/`, `docs/`.
8. Configurar `.gitignore` garantindo proteção estrita de secrets e ambientes virtuais.
9. Realizar commit inicial do git e push para o remoto.

## Artefatos
- `AGENTS.md`
- `CLAUDE.md`, `GEMINI.md`
- `.agents/config/harness.yaml`
- `.agents/config/language.yaml`
- Commit inicial do Git

## Quality Gates
- Harness Gate: configuração válida, secrets protegidos, repositório remoto sincronizado.

## Condições de Saída
- Repositório inicializado, perfil de linguagem ativo, projeto do Jira configurado.

## Tratamento de Falhas
- Se já existir um repositório remoto com código conflitante, interromper e solicitar orientação do usuário.
