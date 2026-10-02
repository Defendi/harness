#!/usr/bin/env python3
"""
Harness Doctor — Verificador de Sanidade e Conformidade do Application Development Harness
Projeto: Padrão de Engenharia Defendi
"""

import sys
import os
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

    def check(self, condition: bool, title: str, details: str = "", is_warning: bool = False):
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

        # 1. Contratos Raiz
        print(f"{BOLD}1. Contratos e Adaptadores Raiz:{RESET}")
        self.check((self.root / "AGENTS.md").is_file(), "Contrato canônico AGENTS.md presente na raiz", "AGENTS.md é mandatório como contrato principal.")
        self.check((self.root / "README.md").is_file(), "README.md do projeto presente na raiz", "README.md deve apresentar o projeto e instruções básicas.")
        self.check((self.root / "CLAUDE.md").is_file(), "Adaptador CLAUDE.md presente", "Necessário para integração com Claude Code.", is_warning=True)
        self.check((self.root / "GEMINI.md").is_file(), "Adaptador GEMINI.md presente", "Necessário para integração com Gemini/Antigravity.", is_warning=True)

        # 2. Estrutura Interna .agents/
        print(f"\n{BOLD}2. Infraestrutura do Harness (.agents/):{RESET}")
        agents_dir = self.root / ".agents"
        self.check(agents_dir.is_dir(), "Diretório .agents/ existe", "Toda a infraestrutura do harness deve residir sob .agents/.")
        self.check((agents_dir / "AGENTS.md").is_file(), ".agents/AGENTS.md operacional presente", "Define como interpretar e carregar recursos do harness.")

        config_dir = agents_dir / "config"
        harness_yaml = config_dir / "harness.yaml"
        self.check(harness_yaml.is_file(), ".agents/config/harness.yaml presente", "Configuração central do projeto e dos quality gates.")

        # 3. Language Profile
        print(f"\n{BOLD}3. Language Profile:{RESET}")
        lang_dir = agents_dir / "languages"
        has_languages = lang_dir.is_dir() and any(lang_dir.iterdir())
        self.check(has_languages, "Perfil de linguagem configurado em .agents/languages/", "O projeto deve possuir ao menos um language profile definido.")

        # 4. Estrutura de Documentação Persistente
        print(f"\n{BOLD}4. Documentação Persistente (docs/):{RESET}")
        docs_dir = self.root / "docs"
        self.check(docs_dir.is_dir(), "Diretório docs/ existe", "Estado e documentação devem ser persistidos em docs/.")
        self.check((docs_dir / "specs").is_dir(), "Diretório docs/specs/ existe", "Local para especificações de requisitos.")
        self.check((docs_dir / "architecture").is_dir(), "Diretório docs/architecture/ existe", "Local para desenhos arquiteturais.")
        self.check((docs_dir / "decisions").is_dir(), "Diretório docs/decisions/ existe", "Local para Architecture Decision Records (ADRs).")
        self.check((docs_dir / "execution").is_dir(), "Diretório docs/execution/ existe", "Local para planos de implementação e handoffs.")

        # 5. Regras e Workflows
        print(f"\n{BOLD}5. Regras e Workflows:{RESET}")
        rules_dir = agents_dir / "rules"
        self.check(rules_dir.is_dir(), "Diretório .agents/rules/ presente")
        self.check((rules_dir / "git.md").is_file(), "Regras de Git (.agents/rules/git.md) presentes", is_warning=True)
        self.check((rules_dir / "jira.md").is_file(), "Regras de Jira (.agents/rules/jira.md) presentes", is_warning=True)

        workflows_dir = agents_dir / "workflows"
        self.check(workflows_dir.is_dir(), "Diretório .agents/workflows/ presente")

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


def main():
    root = Path.cwd()
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    doctor = HarnessDoctor(root)
    sys.exit(doctor.run())


if __name__ == "__main__":
    main()
