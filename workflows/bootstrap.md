# Bootstrap Workflow

## Trigger
New project initialization or initial onboarding of the Application Development Harness.

## Preconditions
- Workspace directory established.
- User intent to configure or adapt the repository.

## Steps
1. Execute Project Bootstrap Interview (Project Description, Language, Directory, Jira, GitHub).
2. Inspect existing workspace environment, tooling, and repositories.
3. Detect required language profile, dependencies, and virtual environment.
4. Establish Jira connection and workspace board/workflow alignment.
5. Create or verify remote GitHub repository.
6. Generate harness core: `AGENTS.md`, adapters (`CLAUDE.md`, `GEMINI.md`), `.agents/`, `docs/`.
7. Configure `.gitignore` ensuring strict protection of secrets and virtual environments.
8. Perform initial git commit and push to remote.

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
