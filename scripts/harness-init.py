#!/usr/bin/env python3
"""
Harness Init — Motor Gerador e Inicializador do Application Development Harness.
Cria o esqueleto completo em lote em segundos, evitando chamadas repetitivas de LLM.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

HARNESS_ROOT = Path(__file__).resolve().parent.parent


def render_template(content: str, variables: dict[str, str]) -> str:
    for key, value in variables.items():
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, str(value))
    return content


def init_harness(
    target_dir: Path,
    project_name: str,
    description: str,
    language: str,
    framework: str,
    jira_key: str,
    jira_domain: str,
    jira_user: str,
    github_repo: str,
    language_version: str = "",
) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)

    if not language_version:
        lang_defaults = {
            "python": ">=3.11",
            "typescript": ">=20",
            "javascript": ">=20",
            "go": "1.22",
            "java": "21",
            "rust": "1.75+",
        }
        language_version = lang_defaults.get(language.lower(), "latest")

    variables = {
        "PROJECT_NAME": project_name,
        "PROJECT_DESCRIPTION": description,
        "LANGUAGE": language,
        "LANGUAGE_VERSION": language_version,
        "FRAMEWORK": framework,
        "JIRA_KEY": jira_key,
        "JIRA_DOMAIN": jira_domain,
        "JIRA_USER": jira_user,
        "GITHUB_REPO": github_repo,
    }

    print(f"\n\033[1m\033[94m=== Inicializando Application Development Harness ===\033[0m")
    print(f"Destino: \033[1m{target_dir.resolve()}\033[0m")
    print(f"Projeto: {project_name} | Linguagem: {language} | Framework: {framework}\n")

    # 1. Estrutura de Documentação (docs/)
    print("1. Criando taxonomia de documentação persistente (docs/)...")
    for subdir in ["prds", "specs", "architecture", "decisions", "execution", "references"]:
        d = target_dir / "docs" / subdir
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        if not readme.exists():
            readme.write_text(f"# Docs: {subdir.capitalize()}\n\nArquivos versionados em docs/{subdir}/.\n", encoding="utf-8")
    print("  ✔ docs/prds, docs/specs, docs/architecture, docs/decisions, docs/execution, docs/references")

    # 2. Infraestrutura .agents/
    print("\n2. Instalando infraestrutura modular (.agents/)...")
    agents_dir = target_dir / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)

    # Copiar Rules
    target_rules = agents_dir / "rules"
    if (HARNESS_ROOT / "rules").is_dir():
        shutil.copytree(HARNESS_ROOT / "rules", target_rules, dirs_exist_ok=True)
        print("  ✔ .agents/rules/ (todas as regras canônicas)")

    # Copiar Skills
    target_skills = agents_dir / "skills"
    if (HARNESS_ROOT / "skills").is_dir():
        shutil.copytree(HARNESS_ROOT / "skills", target_skills, dirs_exist_ok=True)
        print("  ✔ .agents/skills/ (habilidades especializadas)")

    # Copiar Workflows
    target_workflows = agents_dir / "workflows"
    if (HARNESS_ROOT / "workflows").is_dir():
        shutil.copytree(HARNESS_ROOT / "workflows", target_workflows, dirs_exist_ok=True)
        print("  ✔ .agents/workflows/ (fluxos do ciclo de vida)")

    # Copiar Agents
    target_agents = agents_dir / "agents"
    if (HARNESS_ROOT / "agents").is_dir():
        shutil.copytree(HARNESS_ROOT / "agents", target_agents, dirs_exist_ok=True)
        print("  ✔ .agents/agents/ (papéis de subagentes)")

    # Copiar Templates
    target_templates = agents_dir / "templates"
    if (HARNESS_ROOT / "templates").is_dir():
        shutil.copytree(HARNESS_ROOT / "templates", target_templates, dirs_exist_ok=True)
        print("  ✔ .agents/templates/ (modelos de artefatos)")

    # Copiar Adapters
    target_adapters = agents_dir / "adapters"
    if (HARNESS_ROOT / "adapters").is_dir():
        shutil.copytree(HARNESS_ROOT / "adapters", target_adapters, dirs_exist_ok=True)
        print("  ✔ .agents/adapters/ (claude, gemini, opencode)")

    # Copiar Language Profile
    target_lang = agents_dir / "languages" / language
    src_lang = HARNESS_ROOT / "languages" / language
    if src_lang.is_dir():
        shutil.copytree(src_lang, target_lang, dirs_exist_ok=True)
        print(f"  ✔ .agents/languages/{language}/ (perfil da linguagem)")

    # 3. Arquivo Operacional .agents/AGENTS.md
    operational_agents_src = HARNESS_ROOT / "templates" / "AGENTS.operational.md"
    if operational_agents_src.is_file():
        content = operational_agents_src.read_text(encoding="utf-8")
        (agents_dir / "AGENTS.md").write_text(render_template(content, variables), encoding="utf-8")
        print("  ✔ .agents/AGENTS.md")

    # 4. Configurações (.agents/config/)
    print("\n3. Gerando configurações canônicas (.agents/config/)...")
    config_dir = agents_dir / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    harness_yaml_content = f"""harness:
  version: 1

project:
  name: "{project_name}"
  description: "{description}"
  language: "{language}"
  language_version: "{language_version}"
  framework: "{framework}"

jira:
  enabled: true
  project_key: "{jira_key}"
  base_url: "{jira_domain}"
  user: "{jira_user}"

github:
  repository: "{github_repo}"

documentation:
  root: docs

quality_gates:
  specification: true
  architecture: true
  implementation: true
  testing: true
  review: true
  release: true
"""
    (config_dir / "harness.yaml").write_text(harness_yaml_content, encoding="utf-8")
    print("  ✔ .agents/config/harness.yaml")

    lang_yaml_src = src_lang / "language.yaml"
    if lang_yaml_src.is_file():
        shutil.copy(lang_yaml_src, config_dir / "language.yaml")
        print("  ✔ .agents/config/language.yaml")

    # 5. Contratos e Adaptadores Raiz
    print("\n4. Criando contratos raiz e adapters...")

    root_agents_content = f"""# Project Agent Contract

## Project

{project_name}: {description}

## PROTOCOLO MANDATÓRIO DE ABERTURA DE SESSÃO (PASSO ZERO INEGOCIÁVEL)

Ao iniciar qualquer sessão ou receber qualquer demanda envolvendo cards, alterações ou código:

1. **Validação de Conexão MCP Atlassian:** Validar a conexão e autenticação com o MCP do Atlassian imediatamente (`atlassianUserInfo` ou `getAccessibleAtlassianResources`). Se falhar, interrompa o fluxo e avise o usuário.
2. Carregar ativamente via ferramenta de leitura os arquivos [`.agents/rules/jira-card-lifecycle.md`](./.agents/rules/jira-card-lifecycle.md) antes de qualquer ação.
3. **Gate Estrito de Papéis (Orquestrador vs. Subagentes):**
  - O **agente principal atua EXCLUSIVAMENTE como coordenador**, despachante de subagentes e gestor de status e comentários no Jira.
  - O agente principal é **ESTRITAMENTE PROIBIDO de inspecionar código para desenvolver ou implementar alterações diretamente**.
  - Toda concepção de produto, regras de negócio e escrita de PRD **DEVE ser delegada ao subagente de P.O.** (utilizando as skills `brainstorming` e `escrever-prd`).
  - Toda sincronização de TRD e elaboração de especificação formal **DEVE ser delegada ao subagente de arquitetura utilizando a metodologia OpenSPEC**.
  - Toda e qualquer implementação e testes unitários **DEVEM ser delegados imediatamente ao subagente desenvolvedor**.
  - Todo Code Review **DEVE ser delegado ao subagente de revisão**.
  - Toda etapa de Qualidade e Testes Herméticos **DEVE ser delegada ao subagente de tester**.
4. **Fluxo Contínuo como um Relógio:** O ciclo opera de ponta a ponta sem interrupções artificiais ou solicitações manuais de permissão, atualizando o card do Jira com comentários detalhados a cada transição de fase conforme o ciclo oficial.

- **Skills sob Demanda**: Carregue as skills oficiais em [`.agents/skills/`](./.agents/skills/) apenas quando a tarefa exigir seus detalhes operacionais.
- **Precedência**: Não duplique, reinterprete nem crie regras divergentes neste arquivo. Em qualquer caso de ambiguidade ou conflito, [`AGENTS.md`](./AGENTS.md) prevalece absolutamente.

## Harness

This project uses the Application Development Harness.

`AGENTS.md` is the canonical project agent contract.

The harness implementation lives under:

`.agents/`

## Core Principles

- Understand before modifying.
- Follow specifications.
- Preserve existing architecture unless explicitly changed.
- Prefer small, traceable changes.
- Tests are part of implementation.
- Documentation must remain synchronized with behavior.
- Relevant work must be traceable to Jira.
- Do not invent requirements.
- Do not perform destructive operations without authorization.

## Harness Structure

- `.agents/rules/`
- `.agents/skills/`
- `.agents/workflows/`
- `.agents/agents/`
- `.agents/templates/`
- `.agents/languages/`
- `.agents/config/`

## Documentation

Project documentation lives under:

`docs/`

## Jira

Jira is the work management and traceability system. Project key: `{jira_key}`.

## Execution

Follow the applicable workflow from `.agents/workflows/`.

## Language

Load the project language profile from:

`.agents/languages/{language}/`

## Agent Rule

Read this contract first.

Then load only the rules, skills, workflow and language profile relevant to the current task.
"""
    (target_dir / "AGENTS.md").write_text(root_agents_content, encoding="utf-8")
    print("  ✔ AGENTS.md (contrato canônico raiz)")

    claude_content = """# Claude Code Adapter

The canonical project instructions are defined in:

`AGENTS.md`

Harness implementation:

`.agents/`

- **Governança Canônica**: Toda diretriz de escopo, fluxo de execução contínuo, convenções técnicas e hermeticidade reside em [`AGENTS.md`](./AGENTS.md).
"""
    (target_dir / "CLAUDE.md").write_text(claude_content, encoding="utf-8")
    print("  ✔ CLAUDE.md")

    gemini_content = """# Gemini / Antigravity Adapter

The canonical project instructions are:

`AGENTS.md`

Harness implementation:

`.agents/`

Follow the applicable workflow, skills, rules and language profile.

- **Governança Canônica**: Toda diretriz de escopo, fluxo de execução contínuo, convenções técnicas e hermeticidade reside em [`AGENTS.md`](./AGENTS.md).
"""
    (target_dir / "GEMINI.md").write_text(gemini_content, encoding="utf-8")
    print("  ✔ GEMINI.md")

    # README.md do projeto
    readme_path = target_dir / "README.md"
    if not readme_path.exists():
        readme_content = f"""# {project_name}

[![Application Development Harness](https://img.shields.io/badge/Harness-Active-success)](./AGENTS.md)
[![Language](https://img.shields.io/badge/Language-{language}-blue)](./.agents/languages/{language}/)

{description}

---

## 🏛️ Application Development Harness

Este projeto opera sob a governança estrita do **Application Development Harness**.

- Contrato canônico: [`AGENTS.md`](./AGENTS.md)
- Infraestrutura e regras: [`.agents/`](./.agents/)
- Documentação persistente: [`docs/`](./docs/)
- Projeto Jira: `{jira_key}`

---

## 🚀 Execução e Testes

Consulte o guia de toolchain em [`.agents/languages/{language}/toolchain.md`](./.agents/languages/{language}/toolchain.md).
"""
        readme_path.write_text(readme_content, encoding="utf-8")
        print("  ✔ README.md")

    # .gitignore de segurança
    gitignore_content = """# Ambientes virtuais e dependências locais
.venv/
venv/
ENV/
env/
__pycache__/
*.py[cod]
node_modules/
dist/
build/
target/

# Segredos, tokens e credenciais
token_jira.txt
*.token
*.key
*.secret
.env
.env.*
!.env.example

# IDEs e caches
.idea/
.vscode/
*.swp
.pytest_cache/
.coverage
.mypy_cache/
.ruff_cache/
"""
    gitignore_path = target_dir / ".gitignore"
    if not gitignore_path.exists():
        gitignore_path.write_text(gitignore_content, encoding="utf-8")
        print("  ✔ .gitignore (proteção de segredos e ambientes)")

    # 6. Estrutura básica adaptativa para a linguagem selecionada
    if language == "python" and not (target_dir / "pyproject.toml").exists():
        # Dependências adaptativas com base no framework
        deps_list = []
        if framework:
            fw_clean = framework.lower().strip()
            if "fastmcp" in fw_clean:
                deps_list = ['"fastmcp>=0.4.0"', '"pydantic>=2.7.0"']
            elif "fastapi" in fw_clean:
                deps_list = ['"fastapi>=0.110.0"', '"uvicorn>=0.29.0"', '"pydantic>=2.7.0"']
            elif "django" in fw_clean:
                deps_list = ['"django>=5.0.0"']
            elif "flask" in fw_clean:
                deps_list = ['"flask>=3.0.0"']
            else:
                deps_list = [f'"{fw_clean}"']
        
        deps_str = ",\n    ".join(deps_list)
        if deps_str:
            deps_str = f"\n    {deps_str},\n"

        pyproject_content = f"""[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name.lower().replace(' ', '-').replace('_', '-')}"
version = "0.1.0"
description = "{description}"
readme = "README.md"
requires-python = "{language_version if language_version != 'latest' else '>=3.11'}"
license = {{text = "MIT"}}
dependencies = [{deps_str}]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=5.0.0",
    "ruff>=0.4.0",
    "mypy>=1.10.0",
]

[tool.ruff]
line-length = 100

[tool.mypy]
strict = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
"""
        (target_dir / "pyproject.toml").write_text(pyproject_content, encoding="utf-8")
        print("  ✔ pyproject.toml (adaptativo)")

        # Pastas de código
        pkg_name = project_name.lower().replace("-", "_").replace(" ", "_")
        src_pkg = target_dir / "src" / pkg_name
        src_pkg.mkdir(parents=True, exist_ok=True)
        (src_pkg / "__init__.py").write_text(f'"""Package {project_name}."""\n\n__version__ = "0.1.0"\n', encoding="utf-8")

        tests_dir = target_dir / "tests"
        tests_dir.mkdir(parents=True, exist_ok=True)
        (tests_dir / "__init__.py").write_text('"""Tests package."""\n', encoding="utf-8")
        print(f"  ✔ src/{pkg_name}/ e tests/")

    elif language in ("typescript", "javascript") and not (target_dir / "package.json").exists():
        pkg_json = f"""{{
  "name": "{project_name.lower().replace(' ', '-')}",
  "version": "0.1.0",
  "description": "{description}",
  "main": "dist/index.js",
  "scripts": {{
    "build": "tsc",
    "lint": "biome check .",
    "format": "biome format --write .",
    "test": "vitest run"
  }},
  "license": "MIT"
}}
"""
        (target_dir / "package.json").write_text(pkg_json, encoding="utf-8")
        (target_dir / "src").mkdir(parents=True, exist_ok=True)
        (target_dir / "src" / "index.ts").write_text(f"// {project_name}\nexport const version = '0.1.0';\n", encoding="utf-8")
        (target_dir / "tests").mkdir(parents=True, exist_ok=True)
        print("  ✔ package.json, src/ e tests/")

    elif language == "go" and not (target_dir / "go.mod").exists():
        go_mod = f"""module {github_repo if github_repo else project_name.lower()}

go {language_version if language_version != 'latest' else '1.22'}
"""
        (target_dir / "go.mod").write_text(go_mod, encoding="utf-8")
        (target_dir / "cmd" / project_name.lower()).mkdir(parents=True, exist_ok=True)
        (target_dir / "cmd" / project_name.lower() / "main.go").write_text(f"package main\n\nimport \"fmt\"\n\nfunc main() {{\n\tfmt.Println(\"{project_name}\")\n}}\n", encoding="utf-8")
        (target_dir / "pkg").mkdir(parents=True, exist_ok=True)
        print("  ✔ go.mod, cmd/ e pkg/")

    print(f"\n\033[92m\033[1m✔ Application Development Harness inicializado com sucesso em {target_dir.resolve()}!\033[0m\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inicializador e Scaffolder do Application Development Harness")
    parser.add_argument("--target-dir", default=".", help="Diretório de destino (padrão: .)")
    parser.add_argument("--project-name", required=True, help="Nome do projeto")
    parser.add_argument("--description", default="", help="Descrição do projeto")
    parser.add_argument("--language", default="python", help="Linguagem principal (python, go, typescript, java, rust, etc.)")
    parser.add_argument("--language-version", default="", help="Versão da linguagem (ex: 3.12, 1.22, 21, etc.)")
    parser.add_argument("--framework", default="", help="Framework principal")
    parser.add_argument("--jira-key", default="", help="Chave do projeto Jira (ex: PROJ)")
    parser.add_argument("--jira-domain", default="", help="Domínio do Jira Cloud")
    parser.add_argument("--jira-user", default="", help="E-mail do usuário do Jira")
    parser.add_argument("--github-repo", default="", help="Repositório GitHub (ex: org/repo)")

    args = parser.parse_args()

    init_harness(
        target_dir=Path(args.target_dir),
        project_name=args.project_name,
        description=args.description,
        language=args.language,
        framework=args.framework,
        jira_key=args.jira_key,
        jira_domain=args.jira_domain,
        jira_user=args.jira_user,
        github_repo=args.github_repo,
        language_version=args.language_version,
    )


if __name__ == "__main__":
    main()
