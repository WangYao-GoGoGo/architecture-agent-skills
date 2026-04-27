---
name: solidjs-component-architecture-review
description: Use when reviewing Solid.js component architecture, signals, effects, stores, reactive primitives, and component boundaries.
---

# Solid.js Component Architecture Review

## When To Use

- The main decision is about Solid.js component organization, signal/store design, effect boundaries, or reactive primitive usage.
- Reviewing component boundaries or state ownership patterns.

## Workflow

1. Identify component roles — page, feature, shared, and primitive components.
2. Review signal and store design — are signals scoped to component or global state?
3. Check effect boundaries — are effects used for synchronization or general control flow?
4. Review derived state — are computed values using `createMemo` appropriately?
5. Check component boundaries — do components mix data loading, business logic, and rendering?
6. Review resource management — are async resources handled with `createResource`?
7. Recommend the smallest change that clarifies component or state ownership.

## Output Format

```markdown
Solid.js architecture review:
- Component roles:
- Signal/store design:
- Effect boundaries:
- Derived state:
- Component boundaries:
- Resource management:
- Recommended change:
- Verification:
```
