# Requirements Analysis Skill

## Purpose
Analyze incoming problem statements, user requests, or high-level goals and extract clear, unambiguous functional and non-functional requirements.

## Inputs
- Jira card summary and description
- User prompts or stakeholder feedback
- Existing system context

## Preconditions
- Active Jira connection or access to the problem statement.
- Clean working directory.

## Procedure
1. Parse the request to extract user roles, primary objectives, and constraints.
2. Identify dependencies on external systems (AWS, GitLab, Azure, SSH).
3. Map potential security, credential, and compliance risks.
4. Formulate explicit questions for any ambiguous items.
5. Produce a structured requirement draft.

## Outputs
- Structured requirements inventory formatted according to the specification template.

## Validation
- Every requirement has a verifiable acceptance criterion.
- Security constraints for credentials are explicitly declared.

## Failure Conditions
- Ambiguous or conflicting requirements left unresolved.
- Unverifiable acceptance criteria.
