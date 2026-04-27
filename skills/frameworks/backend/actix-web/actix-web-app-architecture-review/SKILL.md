---
name: actix-web-app-architecture-review
description: Use when reviewing Actix-web application architecture, routing, middleware, extractors, error handling, and async request processing.
---

# Actix-web App Architecture Review

## When To Use

- The main decision is about Actix-web project structure, route organization, middleware pipeline, extractor design, or error handling patterns.
- Reviewing actor-based state management or async request boundaries.

## Workflow

1. Identify project structure — are handlers, middleware, services, and domain separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check middleware pipeline — is ordering logical and are side effects visible?
4. Review extractor usage — are extractors handling request parsing or business logic?
5. Check error handling — are errors mapped to consistent HTTP responses?
6. Review async boundaries — are blocking operations wrapped in appropriate thread pools?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Actix-web architecture review:
- Project structure:
- Route organization:
- Middleware pipeline:
- Extractor usage:
- Error handling:
- Async boundaries:
- Recommended change:
- Verification:
```
