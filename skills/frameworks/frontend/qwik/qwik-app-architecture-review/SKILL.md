---
name: qwik-app-architecture-review
description: Use when reviewing Qwik application architecture, resumability, lazy loading, component design, stores, routes, and application structure.
---

# Qwik App Architecture Review

## When To Use

- The main decision is about Qwik project structure, component design for resumability, lazy loading boundaries, store design, or route organization.
- Reviewing `$` suffix conventions or serialization boundaries.

## Workflow

1. Identify component organization — are components designed for resumability and lazy loading?
2. Review `$` suffix usage — are `$` conventions followed correctly for lazy boundaries?
3. Check store design — are stores scoped by domain and serializable?
4. Review route organization — do routes follow the application's domain structure?
5. Check serialization boundaries — are only serializable data passed across lazy boundaries?
6. Review resource management — are resources fetched and cached appropriately?
7. Recommend the smallest change that clarifies resumability or component boundaries.

## Output Format

```markdown
Qwik architecture review:
- Component organization:
- `$` suffix usage:
- Store design:
- Route organization:
- Serialization boundaries:
- Resource management:
- Recommended change:
- Verification:
```
