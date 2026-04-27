---
name: dependency-boundary-review
description: Use when reviewing dependencies between modules, packages, services, layers, schemas, frontend components, or infrastructure boundaries to reduce coupling and clarify ownership.
---

# Dependency Boundary Review

Use this skill to check whether dependencies point in maintainable directions.

## When To Use

- A change crosses packages, layers, services, UI components, database access, or infrastructure.
- Business logic depends directly on frameworks, vendors, persistence, transport, or UI details.
- Tests are hard because dependencies cannot be substituted.
- Cycles or hidden dependencies make changes risky.

## Workflow

1. Map the current dependency direction.
2. Identify the stable core: domain rules, policies, contracts, or data ownership.
3. Identify volatile edges: frameworks, vendors, transport, persistence, UI, cache, external APIs.
4. Check whether volatile edges depend inward instead of the core depending outward.
5. Recommend boundary changes only where they reduce change cost or test friction.
6. Provide verification steps.

## Boundary Rules

- Domain rules should not know transport or persistence details unless the project deliberately chooses an active record style.
- UI state should not leak into domain or persistence logic.
- Database schemas should be owned by a clear service, module, or migration process.
- Cache access should sit behind a policy or repository boundary when consistency matters.
- Framework dependencies are acceptable at the edge; they are risky in reusable core logic.

## Output Format

```markdown
Boundary review:
- Current dependency shape:
- Boundary violations:
- Recommended direction:
- Minimal changes:
- Verification:
- Tradeoffs:
```
