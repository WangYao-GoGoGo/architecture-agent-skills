---
name: framework-boundary-review
description: Use when reviewing whether framework concepts, lifecycle objects, annotations, generated clients, or platform APIs are leaking into domain logic, application services, API contracts, or reusable modules.
---

# Framework Boundary Review

## Knowledge To Use

- `knowledge/frameworks/core/framework-boundaries.md`
- `knowledge/principles/dependency-inversion.md`
- `knowledge/principles/separation-of-concerns.md`

## Workflow

1. Identify framework-owned concepts, lifecycle hooks, annotations, generated types, and runtime requirements.
2. Map where those concepts appear: entry points, application logic, domain logic, persistence, UI, tests.
3. Decide which dependencies are acceptable edge dependencies and which cause harmful coupling.
4. Recommend adapters, ports, local contracts, or simpler direct use where appropriate.
5. Avoid wrapping stable framework features without a real coupling or testability problem.
6. Verify core logic can be tested without unnecessary framework boot.

## Output Format

```markdown
Framework boundary review:
- Framework dependencies:
- Boundary leaks:
- Recommended structure:
- What not to abstract:
- Verification:
```
