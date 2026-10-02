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

    def run(self) -> int:
        print(f"\n{BOLD}{BLUE}=== Verificando Sanidade do Application Development Harness ==={RESET}")
        print(f"Diretório Raiz: {self.root.resolve()}\n")

        # 1. Contratos e Adaptadores Raiz
        print(f"{BOLD}1. Contratos e Adaptadores Raiz:{RESET}")
        self.check((self.root / "AGENTS.md").is_file(), "Contrato canônico AGENTS.md presente na raiz", "AGENTS.md é mandatório como contrato principal.")
        self.check((self.root / "README.md").is_file(), "README.md do projeto presente na raiz", "README.md deve apresentar o projeto e instruções básicas.")
        self.check((self.root / "CLAUDE.md").is_file(), "Adaptador CLAUDE.md presente", "Necessário para integração com Claude Code.", is_warning=True)
        self.check((self.root / "GEMINI.md").is_file(), "Adaptador GEMINI.md presente", "Necessário para integração com Gemini/Antigravity.", is_warning=True)
        self.check((self.root / ".gitignore").is_file(), "Arquivo .gitignore presente", "Proteção essencial para isolamento de credenciais e venv.")

        # 2. Infraestrutura do Harness (.agents/)
        print(f"\n{BOLD}2. Infraestrutura do Harness (.agents/):{RESET}")
        agents_dir = self.root / ".agents"
        self.check(agents_dir.is_dir(), "Diretório .agents/ existe", "Toda a infraestrutura do harness deve residir sob .agents/.")
        self.check((agents_dir / "AGENTS.md").is_file(), ".agents/AGENTS.md operacional presente", "Define como interpretar e carregar recursos do harness.")

        config_dir = agents_dir / "config"
        harness_yaml = config_dir / "harness.yaml"
        self.check(harness_yaml.is_file(), ".agents/config/harness.yaml presente", "Configuração central do projeto e dos quality gates.")
        self.check((config_dir / "language.yaml").is_file(), ".agents/config/language.yaml presente", "Configuração do ecossistema e comandos da linguagem.")

        # 3. Regras Modulares (.agents/rules/)
        print(f"\n{BOLD}3. Regras Modulares (.agents/rules/):{RESET}")
        rules_dir = agents_dir / "rules"
        self.check(rules_dir.is_dir(), "Diretório .agents/rules/ presente")
        self.check((rules_dir / "jira-card-lifecycle.md").is_file(), "Regra obrigatória de ciclo de vida (.agents/rules/jira-card-lifecycle.md)")
        self.check((rules_dir / "architecture.md").is_file(), "Regras de arquitetura presentes", is_warning=True)
        self.check((rules_dir / "coding-standards.md").is_file(), "Regras de coding standards presentes", is_warning=True)
        self.check((rules_dir / "security.md").is_file(), "Regras de segurança presentes", is_warning=True)
        self.check((rules_dir / "testing.md").is_file(), "Regras de testes herméticos presentes", is_warning=True)
        self.check((rules_dir / "git.md").is_file(), "Regras de Git presentes", is_warning=True)
        self.check((rules_dir / "jira.md").is_file(), "Regras de Jira presentes", is_warning=True)

        # 4. Habilidades Especializadas (.agents/skills/)
        print(f"\n{BOLD}4. Skills Especializadas (.agents/skills/):{RESET}")
        skills_dir = agents_dir / "skills"
        self.check(skills_dir.is_dir() and any(skills_dir.iterdir()), "Diretório .agents/skills/ populado")
        self.check((skills_dir / "brainstorming").is_dir(), "Skill 'brainstorming' presente para alinhamento inicial", is_warning=True)
        self.check((skills_dir / "escrever-prd").is_dir(), "Skill 'escrever-prd' presente para definição de PRDs", is_warning=True)
        self.check((skills_dir / "escrever-trd").is_dir(), "Skill 'escrever-trd' presente para definição de TRDs", is_warning=True)

        # 5. Workflows de Processo (.agents/workflows/)
        print(f"\n{BOLD}5. Workflows de Processo (.agents/workflows/):{RESET}")
        workflows_dir = agents_dir / "workflows"
        self.check(workflows_dir.is_dir() and any(workflows_dir.iterdir()), "Diretório .agents/workflows/ populado")
        self.check((workflows_dir / "full-cycle.md").is_file(), "Workflow full-cycle.md presente", is_warning=True)

        # 6. Agentes Especializados (.agents/agents/)
        print(f"\n{BOLD}6. Agentes Especializados (.agents/agents/):{RESET}")
        subagents_dir = agents_dir / "agents"
        self.check(subagents_dir.is_dir() and any(subagents_dir.iterdir()), "Diretório .agents/agents/ com papéis especializados")
        self.check((subagents_dir / "po").is_dir(), "Papel de Product Owner (.agents/agents/po/) presente", is_warning=True)

        # 7. Language Profile
        print(f"\n{BOLD}7. Language Profile:{RESET}")
        lang_dir = agents_dir / "languages"
        has_languages = lang_dir.is_dir() and any(lang_dir.iterdir())
        self.check(has_languages, "Perfil de linguagem configurado em .agents/languages/", "O projeto deve possuir ao menos um language profile definido.")

        # 8. Estrutura de Documentação Persistente (docs/)
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
