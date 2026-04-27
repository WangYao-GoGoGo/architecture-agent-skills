# Refactoring Planner

Plans behavior-preserving refactors before code changes. Use for existing code with unclear ownership, duplication, coupling, or risky structure.

## When To Use This Skill

- Existing code has unclear ownership, duplicated logic, tight coupling, or risky structure.
- A feature change requires modifying code that is hard to understand or test.
- The codebase has god classes, long methods, large conditionals, or cyclic dependencies.
- The team wants to improve structure without changing behavior.

Do **not** use this skill for greenfield projects, simple bug fixes, or cosmetic formatting changes.

## How It Works

1. **Inspect** the current behavior and identify what must be preserved.
2. **Name** the design pressure: what makes the code hard to change.
3. **Identify** the invariant behavior that tests or characterization tests should protect.
4. **Choose** the smallest target structure that reduces the pressure.
5. **Split** the change into reversible steps.
6. **Add** verification at each step (tests, characterization tests, or manual checks).
7. **Implement** incrementally, verifying after each step.

## Knowledge Used

- [`knowledge/refactoring/`](../../knowledge/refactoring/README.md) — specific refactoring moves (extract function, extract class, move method, strangler fig).
- [`knowledge/smells/`](../../knowledge/smells/README.md) — symptom identification (long method, god class, large conditional, etc.).
- [`knowledge/principles/`](../../knowledge/principles/README.md) — to guide the target structure.
- [`knowledge/architecture/migration-strategies/`](../../knowledge/architecture/migration-strategies/README.md) — for large-scale migration approaches.

## Planning Heuristics

- Extract one responsibility at a time, not all at once.
- Move behavior with the data it needs.
- Keep the original interface stable while restructuring internally.
- Use characterization tests when existing tests are missing or inadequate.
- Prefer strangler fig for large, risky migrations.

## Output

```markdown
Refactoring plan:
- Current pressure:
- Behavior to preserve:
- Target structure:
- Steps:
  1. ...
  2. ...
- Verification:
- Risks:
- Overengineering check:
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — for designing new code with clean structure.
- [`dependency-boundary-review`](../dependency-boundary-review/README.md) — when refactoring involves dependency direction changes.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check that the refactoring target is not over-engineered.
