---
name: fiber-app-architecture-review
description: Use when reviewing Fiber (Go) application architecture, routing, middleware, handler responsibilities, error handling, and project structure.
---

# Fiber App Architecture Review

## When To Use

- The main decision is about Fiber project structure, route organization, middleware pipeline, or handler responsibilities.
- Reviewing error handling patterns or validation boundaries.

## Workflow

1. Identify project structure — are handlers, middleware, services, and domain separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check middleware pipeline — is ordering logical and are side effects visible?
4. Review handler responsibilities — do handlers handle HTTP only or also business logic?
5. Check error handling — are errors mapped to consistent HTTP responses?
6. Review validation boundaries — is request validation at the handler level?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Fiber architecture review:
- Project structure:
- Route organization:
- Middleware pipeline:
- Handler responsibilities:
- Error handling:
- Validation boundaries:
- Recommended change:
- Verification:
```
