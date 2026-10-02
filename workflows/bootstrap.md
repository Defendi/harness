# Bootstrap Workflow

## Trigger
New project initialization or initial onboarding of the Application Development Harness.

## Preconditions
- Workspace directory established.
- User intent to configure or adapt the repository.

## Steps
1. Execute Project Bootstrap Interview (Project Description, Language, Directory, Jira, GitHub). Do not assume any language or framework.
2. Conduct adaptive questioning ("Ask only what is necessary") based on user's chosen stack.
3. Inspect workspace environment and tooling (using `harness-probe.py` optionally).
4. Detect required language profile, dependencies, and environment setup.
5. Establish Jira connection and workspace board/workflow alignment.
6. Create or verify remote GitHub repository.
7. Generate harness core: `AGENTS.md`, adapters (`CLAUDE.md`, `GEMINI.md`), `.agents/`, `docs/`.
8. Configure `.gitignore` ensuring strict protection of secrets and virtual environments.
9. Perform initial git commit and push to remote.

## Artifacts
- `AGENTS.md`
- `CLAUDE.md`, `GEMINI.md`
- `.agents/config/harness.yaml`
- `.agents/config/language.yaml`
- Initial Git commit

## Quality Gates
- Harness Gate: configuration valid, secrets protected, remote repo synchronized.

## Exit Conditions
- Repository initialized, language profile active, Jira project configured.

## Failure Handling
- If existing remote repository exists with conflicting code, halt and request user guidance.
