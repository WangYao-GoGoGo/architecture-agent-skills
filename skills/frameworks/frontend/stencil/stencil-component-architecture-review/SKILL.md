---
name: stencil-component-architecture-review
description: Use when reviewing Stencil web component architecture, decorators, reactive properties, shadow DOM, events, and component boundaries.
---

# Stencil Component Architecture Review

## When To Use

- The main decision is about Stencil component organization, decorator usage, reactive property design, or event communication patterns.
- Reviewing component boundaries or cross-component communication.

## Workflow

1. Identify component organization — are components organized by domain or UI role?
2. Review decorator usage — are `@Prop`, `@State`, `@Watch`, `@Event` used appropriately?
3. Check reactive property design — are properties scoped correctly (public vs internal)?
4. Review shadow DOM usage — is shadow DOM used for encapsulation?
5. Check event communication — are custom events used for parent-child communication?
6. Review component boundaries — do components mix data loading, business logic, and rendering?
7. Recommend the smallest change that clarifies component boundaries.

## Output Format

```markdown
Stencil architecture review:
- Component organization:
- Decorator usage:
- Reactive properties:
- Shadow DOM usage:
- Event communication:
- Component boundaries:
- Recommended change:
- Verification:
```
