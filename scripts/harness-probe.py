#!/usr/bin/env python3
"""
Harness Probe — Sonda Automática de Detecção de Ambiente e Toolchain.
Descobre interpretadores, gerenciadores de pacotes, CLI e credenciais disponíveis.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def probe_python_versions() -> list[dict[str, str]]:
    versions = []
    candidates = [
        "python3.13",
        "python3.12",
        "python3.11",
        "python3.10",
        "python3",
        "python",
    ]
    seen_paths = set()

    for cmd in candidates:
        path = shutil.which(cmd)
        if path and path not in seen_paths:
            seen_paths.add(path)
            try:
                out = subprocess.check_output(
                    [path, "--version"], stderr=subprocess.STDOUT, text=True
                ).strip()
                versions.append({"command": cmd, "path": path, "version": out})
            except Exception:
                pass
    return versions


def probe_tool(name: str, version_arg: str = "--version") -> dict[str, str | bool]:
    path = shutil.which(name)
    if not path:
        return {"installed": False, "path": "", "version": ""}
    try:
        out = subprocess.check_output(
            [path, version_arg], stderr=subprocess.STDOUT, text=True
        ).strip().split("\n")[0]
        return {"installed": True, "path": path, "version": out}
    except Exception:
        return {"installed": True, "path": path, "version": "unknown"}


def probe_github() -> dict[str, str | bool]:
    gh_probe = probe_tool("gh")
    if not gh_probe["installed"]:
        return {"installed": False, "authenticated": False, "user": ""}

    try:
        out = subprocess.check_output(
            ["gh", "auth", "status"], stderr=subprocess.STDOUT, text=True
        )
        authenticated = "Logged in to" in out
        user = ""
        for line in out.split("\n"):
            if "Logged in to" in line and "account" in line:
                parts = line.split("account")
                if len(parts) > 1:
                    user = parts[1].split()[0]
                    break
        return {"installed": True, "authenticated": authenticated, "user": user, "raw": out.strip()}
    except subprocess.CalledProcessError as e:
        return {"installed": True, "authenticated": False, "user": "", "error": e.output.strip()}
    except Exception as e:
        return {"installed": True, "authenticated": False, "user": "", "error": str(e)}


def probe_jira() -> dict[str, str | bool]:
    env_token = bool(os.environ.get("JIRA_API_TOKEN"))
    env_user = os.environ.get("JIRA_USER", "")
    env_domain = os.environ.get("JIRA_DOMAIN", "")

    token_file = Path("token_jira.txt")
    has_token_file = token_file.is_file()

    return {
        "has_env_token": env_token,
        "env_user": env_user,
        "env_domain": env_domain,
        "has_token_file": has_token_file,
    }


def main() -> None:
    data = {
        "python_versions": probe_python_versions(),
        "tooling": {
            "uv": probe_tool("uv"),
            "pip": probe_tool("pip"),
            "poetry": probe_tool("poetry"),
            "pdm": probe_tool("pdm"),
            "node": probe_tool("node", "-v"),
            "pnpm": probe_tool("pnpm", "-v"),
            "npm": probe_tool("npm", "-v"),
            "yarn": probe_tool("yarn", "-v"),
            "go": probe_tool("go", "version"),
            "rustc": probe_tool("rustc", "--version"),
            "cargo": probe_tool("cargo", "--version"),
            "java": probe_tool("java", "-version"),
            "mvn": probe_tool("mvn", "-version"),
            "gradle": probe_tool("gradle", "--version"),
            "php": probe_tool("php", "-v"),
            "composer": probe_tool("composer", "--version"),
            "dotnet": probe_tool("dotnet", "--version"),
            "git": probe_tool("git"),
            "gh": probe_tool("gh"),
            "docker": probe_tool("docker", "--version"),
        },
        "github": probe_github(),
        "jira": probe_jira(),
    }

    if "--json" in sys.argv or not sys.stdout.isatty():
        print(json.dumps(data, indent=2))
        return

    # Visual Output
    print("\n\033[1m\033[94m=== Sonda de Ambiente do Harness ===\033[0m\n")
    print("\033[1mPython Disponíveis:\033[0m")
    for py in data["python_versions"]:
        print(f"  • {py['version']} ({py['path']})")

    print("\n\033[1mGerenciadores e Ferramentas:\033[0m")
    for tool_name, info in data["tooling"].items():
        if info["installed"]:
            print(f"  ✔ \033[92m{tool_name}\033[0m: {info['version']}")
        else:
            print(f"  ✖ \033[90m{tool_name}: não encontrado\033[0m")

    print("\n\033[1mIntegrações:\033[0m")
    gh = data["github"]
    if gh.get("authenticated"):
        print(f"  ✔ \033[92mGitHub CLI\033[0m: Autenticado como \033[1m{gh['user']}\033[0m")
    else:
        print("  ⚠ \033[93mGitHub CLI\033[0m: Não autenticado ou ausente")

    jira = data["jira"]
    if jira["has_env_token"] or jira["has_token_file"]:
        print(f"  ✔ \033[92mJira\033[0m: Token detectado (arquivo={jira['has_token_file']}, env={jira['has_env_token']})")
    else:
        print("  ⚠ \033[93mJira\033[0m: Nenhuma credencial encontrada no ambiente imediato")
    print()


if __name__ == "__main__":
    main()
