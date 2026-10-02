# Architecture Design Skill

## Purpose
Design system architecture, component diagrams, interfaces, and Architectural Decision Records (ADRs) ensuring security, credential isolation, and modularity.

## Inputs
- Validated specification (`docs/specs/<jira>-<slug>.md`)
- Existing architecture context in `docs/architecture/`

## Preconditions
- Specification Gate satisfied.

## Procedure
1. Model system components and communication paths.
2. Ensure strict credential boundary: credentials never leave the server or pass into tool responses.
3. Design interfaces/abstract classes for external providers.
4. Record major design choices as ADRs in `docs/decisions/` using the template.
5. Create or update architecture documentation in `docs/architecture/`.

## Outputs
- `docs/architecture/<jira>-<slug>.md`
- `docs/decisions/<number>-<title>.md` (if decisions warrant an ADR)

## Validation
- Architecture conforms to Zero Trust secret management.
- Modularity and decoupling principles respected.

## Failure Conditions
- Security compromise in secret handling.
- Tightly coupled components violating separation of concerns.
