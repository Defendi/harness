# Testing Rules

## 1. Hermetic Testing Triad
All automated test executions must pass the complete quality triad:
1. **Linter Check:** Strict linting passes without warnings.
2. **Format Check:** Code formatting complies 100% with the standard.
3. **Automated Tests:** Unit and integration test suites run with 100% success.

## 2. Test Isolation & Determinism
- Unit tests must never make actual outbound network requests to live AWS, GitLab, Azure, or SSH hosts.
- Use mocks, stubs, and synthetic fixtures to isolate external systems.
- Tests must be deterministic: no reliance on global mutable state or execution order.

## 3. Test Coverage & Edge Cases
- Test both the happy path and error paths (credential failure, timeout, invalid parameters, permission denied).
- Fast execution: unit tests must execute in seconds.
- Every bug fix must include a reproducing regression test.
