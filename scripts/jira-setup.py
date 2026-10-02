#!/usr/bin/env python3
"""
Jira Setup — Provisionador Idempotente de Projetos e Workflows no Jira Cloud.
Suporta REST API v3 e mapeamento oficial do ciclo de vida do Application Development Harness.
"""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path


class JiraClient:
    def __init__(self, domain: str, user: str, token: str):
        self.domain = domain.rstrip("/")
        if not self.domain.startswith("http"):
            self.base_url = f"https://{self.domain}.atlassian.net"
        else:
            self.base_url = self.domain
        self.auth = base64.b64encode(f"{user}:{token}".encode()).decode()

    def request(self, method: str, endpoint: str, data: dict | list | None = None) -> tuple[int, dict | list | str]:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Basic {self.auth}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        body = json.dumps(data).encode("utf-8") if data is not None else None
        req = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req) as resp:
                status = resp.status
                text = resp.read().decode("utf-8")
                if text:
                    try:
                        return status, json.loads(text)
                    except json.JSONDecodeError:
                        return status, text
                return status, {}
        except urllib.error.HTTPError as e:
            err_text = e.read().decode("utf-8")
            try:
                err_json = json.loads(err_text)
                return e.code, err_json
            except Exception:
                return e.code, err_text


def get_current_user_account_id(client: JiraClient) -> str:
    status, data = client.request("GET", "/rest/api/3/myself")
    if status == 200 and isinstance(data, dict):
        return data.get("accountId", "")
    return ""


def ensure_project(client: JiraClient, key: str, name: str, lead_account_id: str) -> dict:
    status, data = client.request("GET", f"/rest/api/3/project/{key}")
    if status == 200:
        print(f"  ✔ Projeto {key} ({name}) já existe no Jira (ID: {data.get('id')}).")
        return data

    payload = {
        "key": key,
        "name": name,
        "projectTypeKey": "software",
        "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic",
        "leadAccountId": lead_account_id,
    }
    status, data = client.request("POST", "/rest/api/3/project", payload)
    if status in (200, 201):
        print(f"  ✔ Projeto {key} criado com sucesso (ID: {data.get('id')})!")
        return data
    else:
        raise RuntimeError(f"Falha ao criar projeto no Jira ({status}): {data}")


def setup_lifecycle_workflow(client: JiraClient, project_key: str, project_id: str) -> None:
    print(f"Configurando ciclo de vida e workflow para o projeto {project_key}...")

    # 1. Obter status existentes globais
    status, all_statuses = client.request("GET", "/rest/api/3/status")
    existing_by_name = {}
    if status == 200 and isinstance(all_statuses, list):
        for s in all_statuses:
            if s.get("scope") is None or s.get("scope", {}).get("type") == "GLOBAL":
                existing_by_name[s["name"].lower()] = s["id"]

    # 2. Assegurar status globais necessários
    required = [
        ("Backlog", "TODO", "10012"),
        ("A fazer", "TODO", "10057"),
        ("Em andamento", "IN_PROGRESS", "3"),
        ("Pronto para Review", "IN_PROGRESS", None),
        ("Revisar", "IN_PROGRESS", None),
        ("Pronto Para Testar", "IN_PROGRESS", None),
        ("Testando", "IN_PROGRESS", None),
        ("Concluído", "DONE", "10011"),
    ]

    resolved_statuses = []
    to_create = []

    for name, cat, default_id in required:
        sid = existing_by_name.get(name.lower()) or default_id
        if sid:
            resolved_statuses.append({"id": str(sid), "name": name, "statusCategory": cat})
        else:
            to_create.append({"name": name, "statusCategory": cat, "description": name})

    if to_create:
        status, res = client.request(
            "POST",
            "/rest/api/3/statuses",
            {"scope": {"type": "GLOBAL"}, "statuses": to_create},
        )
        if status in (200, 201) and isinstance(res, list):
            for s in res:
                resolved_statuses.append(
                    {"id": str(s["id"]), "name": s["name"], "statusCategory": s["statusCategory"]}
                )

    # 3. Criar workflow oficial
    workflow_name = f"{project_key} Lifecycle Workflow"
    status, search_res = client.request(
        "GET",
        f"/rest/api/3/workflow/search?workflowName={urllib.parse.quote(workflow_name)}",
    )
    already_has_wf = (
        status == 200
        and isinstance(search_res, dict)
        and search_res.get("values")
    )

    if not already_has_wf:
        for s in resolved_statuses:
            s["statusReference"] = str(uuid.uuid4())

        statuses_payload = [
            {
                "id": s["id"],
                "name": s["name"],
                "statusCategory": s["statusCategory"],
                "statusReference": s["statusReference"],
            }
            for s in resolved_statuses
        ]

        transitions = [
            {
                "id": "1",
                "name": "Create",
                "toStatusReference": resolved_statuses[0]["statusReference"],
                "type": "INITIAL",
                "actions": [],
                "links": [],
                "properties": {},
                "triggers": [],
                "validators": [],
            }
        ]

        for i, s in enumerate(resolved_statuses, start=2):
            transitions.append(
                {
                    "id": str(i * 10),
                    "name": s["name"],
                    "toStatusReference": s["statusReference"],
                    "type": "GLOBAL",
                    "actions": [],
                    "links": [],
                    "properties": {},
                    "triggers": [],
                    "validators": [],
                }
            )

        wf_payload = {
            "scope": {"type": "GLOBAL"},
            "statuses": statuses_payload,
            "workflows": [
                {
                    "name": workflow_name,
                    "description": f"Workflow oficial de ciclo de vida para o projeto {project_key}",
                    "statuses": [
                        {"statusReference": s["statusReference"], "properties": {}}
                        for s in resolved_statuses
                    ],
                    "transitions": transitions,
                }
            ],
        }

        status, wf_res = client.request("POST", "/rest/api/3/workflows/create", wf_payload)
        if status in (200, 201):
            print(f"  ✔ Workflow '{workflow_name}' criado com sucesso!")
        else:
            print(f"  ⚠ Alerta ao criar workflow ({status}): {wf_res}")

    # 4. Criar e associar Workflow Scheme
    scheme_name = f"{project_key} Workflow Scheme"
    status, schemes = client.request("GET", "/rest/api/3/workflowscheme")
    scheme_id = None
    if status == 200 and isinstance(schemes, dict):
        for s in schemes.get("values", []):
            if s.get("name") == scheme_name:
                scheme_id = s.get("id")
                break

    if not scheme_id:
        status, new_scheme = client.request(
            "POST",
            "/rest/api/3/workflowscheme",
            {
                "name": scheme_name,
                "description": f"Esquema de fluxo para {project_key}",
                "defaultWorkflow": workflow_name,
            },
        )
        if status in (200, 201) and isinstance(new_scheme, dict):
            scheme_id = new_scheme.get("id")
            print(f"  ✔ Workflow Scheme '{scheme_name}' criado (ID: {scheme_id}).")

    if scheme_id:
        status, _ = client.request(
            "PUT",
            "/rest/api/3/workflowscheme/project",
            {"projectId": str(project_id), "workflowSchemeId": str(scheme_id)},
        )
        if status in (200, 204):
            print(f"  ✔ Workflow Scheme associado ao projeto {project_key} com sucesso!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Provisionador Automático de Projetos no Jira Cloud")
    parser.add_argument("--domain", required=True, help="Domínio Atlassian (ex: meu-dominio.atlassian.net)")
    parser.add_argument("--user", required=True, help="Email do usuário Jira")
    parser.add_argument("--token-file", help="Caminho do arquivo com o API Token")
    parser.add_argument("--token", help="API Token em texto plano")
    parser.add_argument("--project-key", required=True, help="Chave do projeto (ex: MCPS)")
    parser.add_argument("--project-name", required=True, help="Nome do projeto (ex: McpSentinel)")

    args = parser.parse_args()

    token = args.token or os.environ.get("JIRA_API_TOKEN")
    if not token and args.token_file:
        t_path = Path(args.token_file)
        if t_path.is_file():
            token = t_path.read_text(encoding="utf-8").strip()

    if not token:
        print("Erro: API Token não fornecido (use --token, --token-file ou JIRA_API_TOKEN).", file=sys.stderr)
        sys.exit(1)

    client = JiraClient(args.domain, args.user, token)
    account_id = get_current_user_account_id(client)
    if not account_id:
        print("Erro: Não foi possível autenticar no Jira Cloud. Verifique credenciais.", file=sys.stderr)
        sys.exit(1)

    print(f"\n✔ Autenticado no Jira como {args.user} (Account ID: {account_id})")
    proj = ensure_project(client, args.project_key, args.project_name, account_id)
    setup_lifecycle_workflow(client, args.project_key, proj["id"])
    print("\n\033[92m✔ Setup do Jira concluído com sucesso!\033[0m\n")


if __name__ == "__main__":
    main()
