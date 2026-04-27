---
name: echo-app-architecture-review
description: Use when reviewing Echo (Go) application architecture, routing, middleware, handler responsibilities, data binding, validation, and error handling.
---

# Echo App Architecture Review

## When To Use

- The main decision is about Echo project structure, route organization, middleware pipeline, handler responsibilities, or validation boundaries.
- Reviewing error handling patterns or data binding design.

## Workflow

1. Identify project structure — are handlers, middleware, services, and domain separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check middleware pipeline — is ordering logical and are side effects visible?
4. Review handler responsibilities — do handlers handle HTTP only or also business logic?
5. Check data binding and validation — are bindings at API boundaries or scattered?
6. Review error handling — are errors mapped to consistent HTTP responses?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Echo architecture review:
- Project structure:
- Route organization:
- Middleware pipeline:
- Handler responsibilities:
- Data binding & validation:
- Error handling:
- Recommended change:
- Verification:
```
