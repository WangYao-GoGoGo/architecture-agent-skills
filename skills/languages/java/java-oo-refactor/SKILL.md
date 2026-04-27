---
name: java-oo-refactor
description: Use when refactoring Java object-oriented code for responsibilities, packages, interfaces, dependency injection, design patterns, SOLID, GRASP, and testability.
---

# Java OO Refactor

## Workflow

1. Inspect packages, public APIs, constructors, dependency injection style, and tests.
2. Identify responsibility, coupling, inheritance, or conditional complexity.
3. Prefer package-private helpers and small interfaces where possible.
4. Use design patterns only when Java callers gain clarity or substitution.
5. Keep behavior stable and verify with existing tests.

## Java Rules

- Prefer constructor injection for required dependencies.
- Keep interfaces meaningful; avoid one interface per implementation by default.
- Use packages to express architecture boundaries.
- Avoid static global state for replaceable services.

## Output Format

```markdown
Java refactor:
- Design pressure:
- Target packages/classes:
- Recommended structure:
- Steps:
- Verification:
```
