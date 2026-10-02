# Harness Operational Manual

This document defines the operational mechanics of the Application Development Harness under `.agents/`.

## 1. How to Use the Harness

The harness provides an automated, specification-driven software engineering infrastructure. Whenever an agent engages with a work item:

1. Validate preconditions and Jira connectivity.
2. Identify the required workflow in `.agents/workflows/`.
3. Load the relevant role profile from `.agents/agents/`.
4. Load only the specific rules from `.agents/rules/` and skills from `.agents/skills/` needed for the current step.
5. Apply the language profile from `.agents/languages/<language>/`.
6. Enforce Quality Gates before transitioning state.

## 2. Rule Selection Protocol

Do not load all rules into context simultaneously. Select rules based on activity:
- Architecture / Design: `architecture.md`, `security.md`
- Implementation / Coding: `coding-standards.md`, `security.md`, `<language>/rules.md`
- Testing / Verification: `testing.md`
- Work Management & Tracking: `jira.md`, `jira-card-lifecycle.md`
- Version Control: `git.md`
- Documentation: `documentation.md`

## 3. Skill Selection Protocol

Skills are modular functional capabilities located under `.agents/skills/`.
Load a skill only when executing its specific procedure:
- Requirements Analysis: `.agents/skills/requirements-analysis/SKILL.md`
- Specification Writing: `.agents/skills/specification/SKILL.md`
- Architecture Design: `.agents/skills/architecture-design/SKILL.md`
- Implementation: `.agents/skills/implementation/SKILL.md`
- Hermetic Testing: `.agents/skills/testing/SKILL.md`
- Code Review: `.agents/skills/code-review/SKILL.md`
- Security Review: `.agents/skills/security-review/SKILL.md`
- Jira Card Lifecycle Management: `.agents/skills/jira-management/SKILL.md`
- Documentation Sync: `.agents/skills/documentation/SKILL.md`

## 4. Workflow Selection Protocol

Execute tasks strictly according to the defined lifecycle workflows in `.agents/workflows/`:
- Project onboarding: `bootstrap.md`
- Problem space exploration: `discovery.md`
- Requirement formalization: `specification.md`
- System modeling & ADRs: `architecture.md`
- Task breakdown: `planning.md`
- Development: `implementation.md`
- Hermetic verification: `testing.md`
- Multi-faceted inspection: `review.md`
- Knowledge synchronization: `documentation.md`
- Delivery packaging: `release.md`
- End-to-end continuous flow: `full-cycle.md`

## 5. Agent Specialization & Delegation

Tasks must follow the strict gate of roles:
- **Orchestrator (Main Agent)**: Coordinates, dispatches subagents, manages Jira status and transitions. Prohibited from editing code directly.
- **Architect**: Produces system architecture, ADRs, interface contracts.
- **Developer**: Implements code and unit tests based on specifications.
- **Tester**: Executes hermetic test suites, regression tests, and coverage validation.
- **Reviewer**: Performs static code review, adherence checks, and constructive feedback.
- **Security**: Validates credential isolation, vulnerability scans, and access control.
- **Documentation**: Synchronizes specs, architecture docs, and technical references.
- **Release**: Prepares version tags, release notes, and delivery packages.

## 6. Language Profile Loading

The active language profile is determined by `.agents/config/harness.yaml` and `.agents/config/language.yaml`.
Load:
- Profile definitions: `.agents/languages/<selected-language>/PROFILE.md`
- Language-specific rules: `.agents/languages/<selected-language>/rules.md`
- Toolchain execution commands: `.agents/languages/<selected-language>/toolchain.md`

## 7. Configuration Precedence

When conflicting directives exist, resolve them in this order:
1. `AGENTS.md` (Canonical Root Contract)
2. `.agents/rules/jira-card-lifecycle.md` (Strict Jira State Machine)
3. `.agents/rules/` (Core Discipline Rules)
4. `.agents/languages/<language>/rules.md` (Language Specifics)
5. Individual workflow and skill files.

## 8. Handoff Protocol

State transitions between agents must produce persistent, traceable artifacts using templates from `.agents/templates/`:
- Discovery → Specification: `docs/specs/<jira>-<slug>.md`
- Specification → Architecture: `docs/architecture/<jira>-<slug>.md`
- Architecture → Planning: `docs/execution/<jira>-plan.md`
- Implementation → Review: Source code + Tests + Diff summary
- Review → Testing / Handoff: `docs/execution/<jira>-review.md`
- Testing → Release / Done: Test execution report + Verified quality gates
