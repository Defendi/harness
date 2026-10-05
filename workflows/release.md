# Workflow de Release

## Gatilho
Conclusão de milestone, lote de cards finalizados em `Concluído` ou gatilho explícito de release.

## Pré-condições
- Todos os cards associados do Jira em `Concluído`.
- Todos os quality gates satisfeitos na `main`.

## Passos
1. Verifique o status da branch `main` e os resultados de CI/CD.
2. Determine a nova versão semântica (SemVer: Major.Minor.Patch).
3. Gere as release notes a partir dos cards concluídos do Jira e do commit log utilizando `.agents/templates/release-notes.md`.
4. Crie a release tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
5. Faça push do commit e da tag para o remoto do GitHub (`git push origin main --tags`).
6. Notifique os stakeholders e feche a versão de release no Jira.

## Artefatos
- `docs/execution/release-vX.Y.Z.md`
- Release tag do Git `vX.Y.Z`
- Registro de GitHub Release

## Quality Gates
- Release Gate: todos os gates predecessores satisfeitos, working tree limpa, build verificado.

## Condições de Saída
- Release publicada, versão com tag criada, milestone do Jira fechado.

## Tratamento de Falhas
- Se o build de release falhar, não publique a tag. Reverta ou aplique patch em uma nova branch de release.
