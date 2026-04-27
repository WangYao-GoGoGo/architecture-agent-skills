# Refactoring Planner Knowledge

## Use When

Planning a safe sequence of refactoring steps where behavior must remain stable — cleaning up, modularizing, or improving architecture across any language or domain.

## Heuristics

- Preserve external behavior first; improve shape second.
- Extract one responsibility at a time.
- Prefer moving code behind an existing boundary before changing callers.
- Keep compatibility adapters temporarily when many callers exist.
- Avoid renaming and behavior changes in the same step.
- For database or API changes, include migration and compatibility strategy.
- Add or identify verification before risky moves.
- Implement incrementally and check after each meaningful step.
- The smallest safe step is better than the perfect plan.

## Common Risks

- Refactoring and feature work mixed in the same step.
- No verification before the change, making it impossible to tell if behavior changed.
- Large-scale renames that create merge conflicts with no behavioral benefit.
- Over-abstracting before the new structure is proven.
