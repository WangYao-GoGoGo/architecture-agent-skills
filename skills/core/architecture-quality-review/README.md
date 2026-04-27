# Architecture Quality Review

Evaluates whether generated or existing code meets architecture quality standards — maintainability, readability, testability, dependency direction, and appropriate abstraction level.

## When To Use This Skill

- After generating code with `architecture-before-coding` or `new-project-scaffolding`.
- After completing a refactoring with `refactoring-planner`.
- When reviewing AI-generated code for architecture quality.
- Before merging a pull request that touches architecture-significant code.

## How It Works

1. **Check dependency direction** — domain must not depend on infrastructure.
2. **Check responsibility boundaries** — no god classes, long methods, large conditionals.
3. **Check testability** — domain logic testable without infrastructure.
4. **Check abstraction level** — every abstraction is justified.
5. **Check readability** — names reflect domain, functions are focused.
6. **Assign quality score** — 🟢 Pass / 🟡 Minor / 🟠 Major / 🔴 Critical.

## Knowledge Used

- [`knowledge/principles/`](../../knowledge/principles/README.md) — SOLID, GRASP, dependency inversion.
- [`knowledge/smells/`](../../knowledge/smells/README.md) — symptom identification.
- [`knowledge/refactoring/`](../../knowledge/refactoring/README.md) — refactoring moves to fix issues.
- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — expected structure.

## Output

A structured quality review with findings table, category scores, and action items.

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — to design code that passes review.
- [`refactoring-planner`](../refactoring-planner/README.md) — to plan fixes for quality issues.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check abstraction justification.
