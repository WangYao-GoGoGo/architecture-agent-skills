# Architecture Before Coding

Guides an agent to sketch responsibilities, boundaries, patterns, files, verification, and overengineering risks before implementing a non-trivial change.

## When To Use This Skill

- The user asks for a new feature with multiple responsibilities.
- The change touches domain logic, persistence, APIs, workflows, or integrations.
- The code may need extension points later.
- The implementation could become a long method, god class, large conditional, or tangled dependency graph.

Do **not** use this skill for tiny edits, simple bug fixes, formatting, or one-line changes.

## How It Works

1. **Inspect** the existing codebase and identify local conventions.
2. **State** the feature goal in one or two sentences.
3. **Identify** responsibilities and assign an owner for each one.
4. **Define** boundaries: public interfaces, internal helpers, data models, external services, persistence, and side effects.
5. **Decide** whether a known pattern is justified. If unsure, prefer the simpler structure.
6. **Propose** the smallest implementation sequence that keeps behavior verifiable.
7. **Implement** in small steps and verify with existing tests or focused checks.

## Knowledge Used

- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — in-process application structure.
- [`knowledge/architecture/integration-patterns/`](../../knowledge/architecture/integration-patterns/README.md) — events, async workflows, gateways.
- [`knowledge/architecture/distributed-systems/`](../../knowledge/architecture/distributed-systems/README.md) — service boundaries, deployment units.
- [`knowledge/principles/`](../../knowledge/principles/README.md) and [`knowledge/patterns/`](../../knowledge/patterns/README.md) — responsibility and pattern decisions.

## Output

A concise design sketch before editing:

```markdown
Design sketch:
- Goal:
- Responsibilities:
- Boundaries:
- Pattern, if any:
- Files likely to change:
- Verification:
- Overengineering check:
```

## Related Skills

- [`design-pattern-selector`](../design-pattern-selector/README.md) — when you need to pick a specific pattern.
- [`refactoring-planner`](../refactoring-planner/README.md) — when working with existing code that needs restructuring first.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check whether the proposed design is too large.
