---
name: falcon-app-architecture-review
description: Use when reviewing Falcon application architecture, resource design, middleware, hooks, error handling, and application structure.
---

# Falcon App Architecture Review

## When To Use

- The main decision is about Falcon project structure, resource class design, hook usage, or middleware pipeline.
- Reviewing error handling patterns or content negotiation boundaries.

## Workflow

1. Identify project structure — are resources, hooks, services, and domain separated?
2. Review resource class design — do resources handle HTTP methods or also business logic?
3. Check hook usage — are hooks used for cross-cutting concerns or business logic?
4. Review middleware pipeline — is ordering logical and are side effects visible?
5. Check error handling — are errors mapped to consistent HTTP responses?
6. Review content negotiation — are media types handled at the right boundary?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Falcon architecture review:
- Project structure:
- Resource design:
- Hook usage:
- Middleware pipeline:
- Error handling:
- Content negotiation:
- Recommended change:
- Verification:
```
