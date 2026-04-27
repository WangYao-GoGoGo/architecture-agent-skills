---
name: rocket-app-architecture-review
description: Use when reviewing Rocket (Rust) application architecture, routing, request guards, form/data handling, templating, and error handling.
---

# Rocket App Architecture Review

## When To Use

- The main decision is about Rocket project structure, route organization, request guard design, or data handling boundaries.
- Reviewing error handling patterns or template usage.

## Workflow

1. Identify project structure — are routes, guards, services, and domain separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check request guard design — are guards handling auth/validation or business logic?
4. Review form/data handling — are data types at API boundaries or leaking into domain?
5. Check error handling — are errors mapped to consistent HTTP responses using `Responder`?
6. Review template usage — are templates presentation-only or owning logic?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Rocket architecture review:
- Project structure:
- Route organization:
- Request guards:
- Form/data handling:
- Error handling:
- Template usage:
- Recommended change:
- Verification:
```
