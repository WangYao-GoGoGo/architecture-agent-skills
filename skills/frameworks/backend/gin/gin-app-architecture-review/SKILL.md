---
name: gin-app-architecture-review
description: Use when reviewing Gin (Go) application architecture, handler responsibilities, middleware pipeline, routing, validation, and package boundaries.
---

# Gin App Architecture Review

## When To Use

- The main decision is about Gin project structure, handler organization, middleware ordering, or Go package boundaries.
- Reviewing validation placement, error handling patterns, or context propagation.

## Workflow

1. Identify project structure — are handlers, services, domain, and persistence in separate packages?
2. Review handler responsibilities — do handlers handle HTTP binding only or also business logic?
3. Check middleware pipeline — is ordering logical and are side effects visible?
4. Review validation boundaries — is request validation at the handler level or scattered?
5. Check error handling — are errors mapped to consistent HTTP responses?
6. Review context propagation — is `gin.Context` leaking into non-HTTP layers?
7. Recommend the smallest change that clarifies package boundaries.

## Output Format

```markdown
Gin architecture review:
- Project structure:
- Handler responsibilities:
- Middleware pipeline:
- Validation boundaries:
- Error handling:
- Context propagation:
- Recommended change:
- Verification:
```
