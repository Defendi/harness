# Specification Workflow (OpenSPEC)

## Trigger
Completion of PRD and initiation of technical specifications for a Jira card in `Backlog`.

## Preconditions (Mandatory)
- **Approved PRD**: Corresponding `docs/prds/PRD-NNN.md` approved by the Product Owner (P.O.) agent.
- **Synchronized TRD**: `docs/trd.md` created or updated by the Architect agent using `.agents/skills/escrever-trd/`.
- **HARD-GATE**: Agents are **STRICTLY FORBIDDEN** from authoring SPEC documents before both PRD and TRD are written and approved.

## Steps
1. **Technical Requirements Document (TRD) Synchronization**:
   - The **Architect Agent** executes `.agents/skills/escrever-trd/`.
   - Update `docs/trd.md` with global architecture, stack constraints, NFRs, external dependencies, and new ADRs in `docs/decisions/`.
2. **OpenSPEC Creation**:
   - The Architect Agent creates the formal OpenSPEC document: `docs/specs/<jira>-<slug>.md` using `.agents/templates/specification.md`.
   - Implement the OpenSPEC methodology:
     - Canonical YAML frontmatter (`type: openspec`, `prd_ref`, `trd_ref`, `jira`).
     - Map Functional Requirements (RFs) directly to the PRD User Stories.
     - Define technical schemas, contracts, endpoints, and data models adhering to the TRD.
     - Detail edge cases, error codes, and failure modes.
     - Specify concrete acceptance criteria and test scenarios using Given-When-Then syntax.
3. **Security & Zero Trust Validation**:
   - Validate that credentials, API tokens, and secrets are completely isolated from LLM output.
4. **Peer Review**:
   - Architect and P.O. validate that the OpenSPEC satisfies the PRD intent without violating TRD constraints.

## Artifacts Produced
- `docs/trd.md` (updated via `escrever-trd`)
- `docs/decisions/<number>-<slug>.md` (ADRs if applicable)
- `docs/specs/<jira>-<slug>.md` (OpenSPEC document)

## Quality Gates
- **OpenSPEC Gate**:
  - PRD and TRD confirmed present and approved.
  - 100% of Acceptance Criteria testable and formatted in Given-When-Then.
  - Zero credential exposure risks.

## Exit Conditions
- OpenSPEC approved and committed; card ready for Planning and Architecture design.
