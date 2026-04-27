# Dependency Boundary Review

Reviews whether dependencies between modules, services, schemas, UI components, caches, and infrastructure point in maintainable directions.

## When To Use This Skill

- A module or service imports infrastructure, framework, or vendor code directly.
- Cyclic dependencies exist between packages, modules, or services.
- Tests are slow or hard to set up because of tangled dependencies.
- A code review shows unclear ownership or responsibility boundaries.
- Domain logic is mixed with transport, persistence, or UI code.

## How It Works

1. **Map** the dependency graph between modules, services, or components.
2. **Identify** inward-pointing vs outward-pointing dependencies.
3. **Check** whether domain or policy code depends on volatile details.
4. **Look for** cycles, excessive fan-out, and implicit dependencies.
5. **Recommend** the smallest boundary change that improves dependency direction.
6. **Verify** that the change does not break existing behavior.

## Knowledge Used

- [`knowledge/core/dependency-boundary-review/`](../../knowledge/core/dependency-boundary-review/README.md) — dependency direction rules, stable vs volatile dependencies.
- [`knowledge/principles/dependency-inversion.md`](../../knowledge/principles/dependency-inversion.md) — high-level policy should not depend on low-level details.
- [`knowledge/principles/coupling-and-cohesion.md`](../../knowledge/principles/coupling-and-cohesion.md) — signals of harmful coupling.

## Boundary Rules

- Domain logic must not import framework, database driver, or HTTP client code directly.
- Public interfaces should be owned by the consumer, not the implementor.
- Cyclic dependencies between modules must be broken by extracting shared policy.
- Infrastructure code may depend on domain abstractions, not the reverse.

## Output

```markdown
Dependency boundary review:
- Dependency map:
- Violations:
- Recommended change:
- Verification:
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — to design boundaries before implementing.
- [`refactoring-planner`](../refactoring-planner/README.md) — to plan incremental boundary changes.
