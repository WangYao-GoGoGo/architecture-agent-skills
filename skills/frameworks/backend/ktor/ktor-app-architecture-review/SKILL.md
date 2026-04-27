---
name: ktor-app-architecture-review
description: Use when reviewing Ktor application architecture, routing, plugin pipeline, content negotiation, dependency injection, and async request handling.
---

# Ktor App Architecture Review

## When To Use

- The main decision is about Ktor project structure, route organization, plugin pipeline, or async request handling.
- Reviewing content negotiation, serialization, or client/server module boundaries.

## Workflow

1. Identify project structure — are routes, plugins, services, and persistence separated?
2. Review route organization — are routes grouped by domain or resource?
3. Check plugin pipeline — is plugin ordering logical and are side effects visible?
4. Review content negotiation and serialization boundaries.
5. Check dependency injection — are dependencies scoped correctly?
6. Review async request handling — are suspending functions used appropriately?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Ktor architecture review:
- Project structure:
- Route organization:
- Plugin pipeline:
- Content negotiation:
- Dependency injection:
- Async handling:
- Recommended change:
- Verification:
```
