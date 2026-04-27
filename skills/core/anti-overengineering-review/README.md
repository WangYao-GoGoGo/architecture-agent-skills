# Anti-Overengineering Review

Checks whether a proposed architecture or abstraction is larger than the current problem needs.

## When To Use This Skill

- A design includes patterns, abstractions, or layers that may not be justified yet.
- The team is debating whether to introduce a framework, pattern, or service boundary.
- A code review shows abstraction that adds complexity without clear benefit.
- Before or after using `architecture-before-coding` or `design-pattern-selector`.

## How It Works

1. **Identify** the abstraction or pattern being proposed.
2. **Assess** the current problem size: how many variations, how often it changes, how many callers.
3. **Compare** the cost of the abstraction (complexity, indirection, testing burden) against the benefit.
4. **Recommend** the simplest structure that solves the current problem.
5. **Flag** abstractions that make future changes harder rather than easier.

## Knowledge Used

- [`knowledge/core/anti-overengineering-review/`](../../knowledge/core/anti-overengineering-review/README.md) — YAGNI, abstraction rent, complexity cost heuristics.
- [`knowledge/principles/`](../../knowledge/principles/README.md) — to check whether principles are being applied mechanically.

## Decision Rules

- If the abstraction solves a future problem that may never happen, remove it.
- If the abstraction makes the common path harder to read, remove it.
- If the abstraction can be introduced later without rewriting callers, defer it.
- If the abstraction reduces duplication for truly independent variations, keep it.

## Output

```markdown
Overengineering check:
- Abstraction or pattern proposed:
- Current problem size:
- Cost of abstraction:
- Recommendation:
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — to design with the right level of abstraction.
- [`design-pattern-selector`](../design-pattern-selector/README.md) — to pick the smallest pattern that fits.
