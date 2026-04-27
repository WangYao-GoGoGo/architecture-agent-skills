---
name: axum-app-architecture-review
description: Use when reviewing Axum application architecture, routing, extractors, middleware, tower service composition, and error handling.
---

# Axum App Architecture Review

## When To Use

- The main decision is about Axum project structure, route organization, extractor design, middleware composition, or error handling patterns.
- Reviewing tower service layers or async request boundaries.

## Workflow

1. Identify project structure — are handlers, middleware, services, and domain separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check middleware composition — are tower layers ordered logically?
4. Review extractor usage — are extractors handling request parsing or business logic?
5. Check error handling — are errors mapped to consistent HTTP responses?
6. Review async boundaries — are blocking operations wrapped in `spawn_blocking`?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Axum architecture review:
- Project structure:
- Route organization:
- Middleware composition:
- Extractor usage:
- Error handling:
- Async boundaries:
- Recommended change:
- Verification:
```
