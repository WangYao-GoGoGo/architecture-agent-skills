---
name: lit-component-architecture-review
description: Use when reviewing Lit web component architecture, reactive properties, shadow DOM, events, and component boundaries.
---

# Lit Component Architecture Review

## When To Use

- The main decision is about Lit web component organization, reactive property design, shadow DOM usage, or event communication patterns.
- Reviewing component boundaries or cross-component communication.

## Workflow

1. Identify component organization — are components organized by domain or UI role?
2. Review reactive property design — are properties scoped correctly (public vs internal)?
3. Check shadow DOM usage — is shadow DOM used for encapsulation or creating accessibility issues?
4. Review event communication — are events used for parent-child or cross-component communication?
5. Check component boundaries — do components mix data loading, business logic, and rendering?
6. Review lifecycle usage — are lifecycle callbacks used appropriately?
7. Recommend the smallest change that clarifies component boundaries.

## Output Format

```markdown
Lit architecture review:
- Component organization:
- Reactive properties:
- Shadow DOM usage:
- Event communication:
- Component boundaries:
- Lifecycle usage:
- Recommended change:
- Verification:
```
