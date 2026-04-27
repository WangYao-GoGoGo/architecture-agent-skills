---
name: express-app-architecture-review
description: Use when reviewing Express application architecture, middleware pipeline, routing, error handling, async patterns, validation, and application structure.
---

# Express App Architecture Review

## When To Use

- The main decision is about Express project structure, middleware organization, error handling patterns, or async request management.
- Reviewing route handler responsibilities, validation boundaries, or middleware ordering.

## Workflow

1. Identify project structure — are routes, middleware, controllers, and services separated?
2. Review middleware pipeline — is ordering logical and are side effects visible?
3. Check route handler responsibilities — do they handle HTTP only or also business logic?
4. Review async error handling — are unhandled promise rejections caught?
5. Check validation boundaries — is request validation at the API boundary or scattered?
6. Review error middleware and consistent error response contracts.
7. Recommend the smallest change that clarifies structure or reduces risk.

## Output Format

```markdown
Express architecture review:
- Project structure:
- Middleware pipeline:
- Route handler responsibilities:
- Async error handling:
- Validation boundaries:
- Error contracts:
- Recommended change:
- Verification:
```
