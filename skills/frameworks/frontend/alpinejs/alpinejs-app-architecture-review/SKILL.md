---
name: alpinejs-app-architecture-review
description: Use when reviewing Alpine.js application architecture, component design, directives, stores, data flow, and application structure.
---

# Alpine.js App Architecture Review

## When To Use

- The main decision is about Alpine.js component organization, directive usage, store design, or data flow patterns.
- Reviewing component boundaries or state management approach.

## Workflow

1. Identify component organization — are components organized by domain or UI role?
2. Review directive usage — are `x-data`, `x-init`, `x-effect` used appropriately?
3. Check store design — are Alpine stores scoped by domain or becoming global dumps?
4. Review data flow — is data passed through `x-bind` or shared via stores?
5. Check component boundaries — do components mix data loading, business logic, and rendering?
6. Review AJAX and side effect patterns — are API calls at the right level?
7. Recommend the smallest change that clarifies component or data boundaries.

## Output Format

```markdown
Alpine.js architecture review:
- Component organization:
- Directive usage:
- Store design:
- Data flow:
- Component boundaries:
- AJAX/side effects:
- Recommended change:
- Verification:
```
