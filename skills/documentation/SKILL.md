# Documentation Skill

## Purpose
Maintain, organize, and synchronize all technical documentation under `docs/` with ongoing code changes and architectural evolutions.

## Inputs
- Implemented code, test results, and ADRs
- Existing documentation in `docs/`

## Preconditions
- Implementation and testing steps completed.

## Procedure
1. Identify all documentation impacted by the change (README, specs, architecture, API guides).
2. Update interface definitions, usage instructions, and configuration parameters.
3. Validate all internal file links and code references.
4. Record execution summary in `docs/execution/` if required.
5. Ensure Markdown documents adhere to formatting standards.

## Outputs
- Synchronized documentation in `docs/` and `README.md`.

## Validation
- No broken links.
- Code examples and schemas match actual behavior.

## Failure Conditions
- Inconsistencies between documented behavior and real implementation.
- Broken markdown links or incomplete sections.
