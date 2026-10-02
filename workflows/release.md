# Release Workflow

## Trigger
Milestone completion, batch of completed cards in `Concluído`, or explicit release trigger.

## Preconditions
- All associated Jira cards in `Concluído`.
- All quality gates satisfied on `main`.

## Steps
1. Verify `main` branch status and CI/CD results.
2. Determine new semantic version (SemVer: Major.Minor.Patch).
3. Generate release notes from completed Jira cards and commit log using `.agents/templates/release-notes.md`.
4. Create release tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
5. Push commit and tag to GitHub remote (`git push origin main --tags`).
6. Notify stakeholders and close Jira release version.

## Artifacts
- `docs/execution/release-vX.Y.Z.md`
- Git release tag `vX.Y.Z`
- GitHub Release entry

## Quality Gates
- Release Gate: all predecessor gates satisfied, clean working tree, verified build.

## Exit Conditions
- Release published, version tagged, Jira milestone closed.

## Failure Handling
- If release build fails, do not publish tag. Revert or patch on a new release branch.
