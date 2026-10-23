#!/usr/bin/env python3
"""
Harness Doctor — Verificador de Sanidade e Conformidade do Application Development Harness
Projeto: Padrão de Engenharia Defendi
"""

import sys
from pathlib import Path

# Cores para terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


class HarnessDoctor:
    def __init__(self, root_dir: Path):
        self.root = root_dir
        self.passed = 0
        self.warnings = 0
        self.failures = 0

    def check(self, condition: bool, title: str, details: str = "", is_warning: bool = False) -> None:
        if condition:
            print(f"  {GREEN}✔ [OK]{RESET} {title}")
            self.passed += 1
        elif is_warning:
            print(f"  {YELLOW}⚠ [WARN]{RESET} {title}")
            if details:
                print(f"        {YELLOW}↳ {details}{RESET}")
            self.warnings += 1
        else:
            print(f"  {RED}✖ [FAIL]{RESET} {title}")
            if details:
                print(f"        {RED}↳ {details}{RESET}")
            self.failures += 1

    def validate_skill_frontmatter(self, skill_file: Path, expected_name: str = "") -> tuple[bool, str]:
        """Valida se o arquivo SKILL.md possui frontmatter YAML válido com name e description."""
        if not skill_file.is_file():
            return False, f"Arquivo {skill_file.name} não encontrado."

        try:
            content = skill_file.read_text(encoding="utf-8")
        except Exception as e:
            return False, f"Erro ao ler arquivo: {e}"

        if not content.startswith("---"):
            return False, "Ausência do delimitador inicial '---' do YAML frontmatter."

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "Delimitadores do YAML frontmatter malformatados (necessário fechar com '---')."

        fm_text = parts[1].strip()
        if not fm_text:
            return False, "Bloco YAML frontmatter vazio."

        try:
            import yaml
            data = yaml.safe_load(fm_text)
        except Exception as e:
            return False, f"Sintaxe YAML inválida no frontmatter: {e}"

        if not isinstance(data, dict):
            return False, "Frontmatter YAML deve ser um mapeamento/dicionário chave-valor."

        name = data.get("name")
        if not name or not isinstance(name, str) or not name.strip():
            return False, "Campo obrigatório 'name' ausente ou vazio no frontmatter YAML."

        if expected_name and name.strip() != expected_name:
            return False, f"Campo 'name' ('{name}') diverge do nome do diretório ('{expected_name}')."

        desc = data.get("description")
        if not desc or not isinstance(desc, str) or not desc.strip():
            return False, "Campo obrigatório 'description' ausente ou vazio no frontmatter YAML."

        return True, ""

    def run(self) -> int:
        print(f"\n{BOLD}{BLUE}=== Verificando Sanidade do Application Development Harness ==={RESET}")
        print(f"Diretório Raiz: {self.root.resolve()}\n")

        # Detectar modo de execução: Projeto Consumidor (.agents/) vs Repositório Base do Harness
        is_harness_framework = not (self.root / ".agents").is_dir() and (self.root / "skills").is_dir() and (self.root / "rules").is_dir()
        agents_dir = self.root if is_harness_framework else (self.root / ".agents")

        if is_harness_framework:
            print(f"{BLUE}Modo detectado: Repositório Base do Harness Framework (Origem){RESET}\n")
        else:
            print(f"{BLUE}Modo detectado: Projeto Consumidor do Harness (.agents/){RESET}\n")

        # 1. Contratos e Adaptadores Raiz
        print(f"{BOLD}1. Contratos e Adaptadores Raiz:{RESET}")
        if is_harness_framework:
            self.check((self.root / "README.md").is_file(), "README.md do repositório base presente")
            self.check((self.root / "adapters").is_dir(), "Diretório adapters/ presente")
            self.check((self.root / "templates").is_dir(), "Diretório templates/ presente")
            self.check((self.root / "scripts").is_dir(), "Diretório scripts/ presente")
        else:
            self.check((self.root / "AGENTS.md").is_file(), "Contrato canônico AGENTS.md presente na raiz", "AGENTS.md é mandatório como contrato principal.")
            self.check((self.root / "README.md").is_file(), "README.md do projeto presente na raiz", "README.md deve apresentar o projeto e instruções básicas.")
            self.check((self.root / "CLAUDE.md").is_file(), "Adaptador CLAUDE.md presente", "Necessário para integração com Claude Code.", is_warning=True)
            self.check((self.root / "GEMINI.md").is_file(), "Adaptador GEMINI.md presente", "Necessário para integração com Gemini/Antigravity.", is_warning=True)
            self.check((self.root / ".gitignore").is_file(), "Arquivo .gitignore presente", "Proteção essencial para isolamento de credenciais e venv.")

        # 2. Infraestrutura do Harness
        infra_label = "Infraestrutura do Harness (Raiz do Framework)" if is_harness_framework else "Infraestrutura do Harness (.agents/)"
        print(f"\n{BOLD}2. {infra_label}:{RESET}")
        if not is_harness_framework:
            self.check(agents_dir.is_dir(), "Diretório .agents/ existe", "Toda a infraestrutura do harness deve residir sob .agents/.")
            self.check((agents_dir / "AGENTS.md").is_file(), ".agents/AGENTS.md operacional presente", "Define como interpretar e carregar recursos do harness.")

        config_dir = agents_dir / "config"
        harness_yaml = config_dir / "harness.yaml"
        self.check(harness_yaml.is_file(), f"{config_dir.relative_to(self.root)}/harness.yaml presente", "Configuração central do harness e dos quality gates.")
        if not is_harness_framework:
            self.check((config_dir / "language.yaml").is_file(), ".agents/config/language.yaml presente", "Configuração do ecossistema e comandos da linguagem.")

        # 3. Regras Modulares
        rules_label = "rules/" if is_harness_framework else ".agents/rules/"
        print(f"\n{BOLD}3. Regras Modulares ({rules_label}):{RESET}")
        rules_dir = agents_dir / "rules"
        self.check(rules_dir.is_dir(), f"Diretório {rules_label} presente")
        self.check((rules_dir / "jira-card-lifecycle.md").is_file(), f"Regra obrigatória de ciclo de vida ({rules_label}jira-card-lifecycle.md)")
        self.check((rules_dir / "architecture.md").is_file(), "Regras de arquitetura presentes", is_warning=True)
        self.check((rules_dir / "coding-standards.md").is_file(), "Regras de coding standards presentes", is_warning=True)
        self.check((rules_dir / "security.md").is_file(), "Regras de segurança presentes", is_warning=True)
        self.check((rules_dir / "testing.md").is_file(), "Regras de testes herméticos presentes", is_warning=True)
        self.check((rules_dir / "git.md").is_file(), "Regras de Git presentes", is_warning=True)
        self.check((rules_dir / "jira.md").is_file(), "Regras de Jira presentes", is_warning=True)

        # 4. Habilidades Especializadas e Frontmatter YAML
        skills_label = "skills/" if is_harness_framework else ".agents/skills/"
        print(f"\n{BOLD}4. Skills Especializadas e Frontmatter YAML ({skills_label}):{RESET}")
        skills_dir = agents_dir / "skills"
        skills_exist = skills_dir.is_dir() and any(skills_dir.iterdir())
        self.check(skills_exist, f"Diretório {skills_label} populado")

        self.check((skills_dir / "brainstorming").is_dir(), "Skill 'brainstorming' presente para alinhamento inicial", is_warning=True)
        self.check((skills_dir / "escrever-prd").is_dir(), "Skill 'escrever-prd' presente para definição de PRDs", is_warning=True)
        self.check((skills_dir / "escrever-trd").is_dir(), "Skill 'escrever-trd' presente para definição de TRDs", is_warning=True)

        if skills_exist:
            for skill_dir in sorted(skills_dir.iterdir()):
                if skill_dir.is_dir() and not skill_dir.name.startswith("."):
                    skill_md = skill_dir / "SKILL.md"
                    valid, err = self.validate_skill_frontmatter(skill_md, expected_name=skill_dir.name)
                    self.check(
                        valid,
                        f"Skill '{skill_dir.name}': frontmatter YAML válido (name e description)",
                        err
                    )

        # 5. Workflows de Processo
        workflows_label = "workflows/" if is_harness_framework else ".agents/workflows/"
        print(f"\n{BOLD}5. Workflows de Processo ({workflows_label}):{RESET}")
        workflows_dir = agents_dir / "workflows"
        self.check(workflows_dir.is_dir() and any(workflows_dir.iterdir()), f"Diretório {workflows_label} populado")
        self.check((workflows_dir / "full-cycle.md").is_file(), "Workflow full-cycle.md presente", is_warning=True)

        # 6. Agentes Especializados
        agents_sub_label = "agents/" if is_harness_framework else ".agents/agents/"
        print(f"\n{BOLD}6. Agentes Especializados ({agents_sub_label}):{RESET}")
        subagents_dir = agents_dir / "agents"
        self.check(subagents_dir.is_dir() and any(subagents_dir.iterdir()), f"Diretório {agents_sub_label} com papéis especializados")
        self.check((subagents_dir / "po").is_dir(), f"Papel de Product Owner ({agents_sub_label}po/) presente", is_warning=True)

        # 7. Language Profile
        lang_label = "languages/" if is_harness_framework else ".agents/languages/"
        print(f"\n{BOLD}7. Language Profile ({lang_label}):{RESET}")
        lang_dir = agents_dir / "languages"
        has_languages = lang_dir.is_dir() and any(lang_dir.iterdir())
        self.check(has_languages, f"Perfil de linguagem configurado em {lang_label}", "O projeto deve possuir ao menos um language profile definido.")

        # 8. Estrutura de Documentação Persistente (docs/) - Apenas em Projetos Consumidores
        if not is_harness_framework:
            print(f"\n{BOLD}8. Documentação Persistente (docs/):{RESET}")
            docs_dir = self.root / "docs"
            self.check(docs_dir.is_dir(), "Diretório docs/ existe", "Estado e documentação devem ser persistidos em docs/.")
            self.check((docs_dir / "prds").is_dir(), "Diretório docs/prds/ existe", "Local para Product Requirements Documents (PRDs).", is_warning=True)
            self.check((docs_dir / "specs").is_dir(), "Diretório docs/specs/ existe", "Local para especificações de requisitos (OpenSPEC).")
            self.check((docs_dir / "architecture").is_dir(), "Diretório docs/architecture/ existe", "Local para desenhos arquiteturais.")
            self.check((docs_dir / "decisions").is_dir(), "Diretório docs/decisions/ existe", "Local para Architecture Decision Records (ADRs).")
            self.check((docs_dir / "execution").is_dir(), "Diretório docs/execution/ existe", "Local para planos de implementação e handoffs.")
            self.check((docs_dir / "references").is_dir(), "Diretório docs/references/ existe", "Local para documentações técnicas de referência.")

        # Resumo Final
        print(f"\n{BOLD}=== Resumo da Auditoria ==={RESET}")
        print(f"Sucessos: {GREEN}{self.passed}{RESET} | Alertas: {YELLOW}{self.warnings}{RESET} | Falhas: {RED}{self.failures}{RESET}\n")

        if self.failures > 0:
            print(f"{RED}{BOLD}✖ O repositório NÃO está em conformidade com a especificação do Harness!{RESET}\n")
            return 1
        elif self.warnings > 0:
            print(f"{YELLOW}{BOLD}⚠ O repositório está funcional, mas possui avisos de conformidade.{RESET}\n")
            return 0
        else:
            print(f"{GREEN}{BOLD}✔ Repositório plenamente em conformidade com o Padrão de Engenharia Defendi!{RESET}\n")
            return 0


def main() -> None:
    root = Path.cwd()
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    doctor = HarnessDoctor(root)
    sys.exit(doctor.run())


if __name__ == "__main__":
    main()
