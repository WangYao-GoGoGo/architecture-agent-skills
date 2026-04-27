---
name: remix-app-architecture-review
description: Use when reviewing Remix application architecture, routing, loaders, actions, nested routes, error boundaries, and data loading strategy.
---

# Remix App Architecture Review

## When To Use

- The main decision is about Remix project structure, route organization, loader/action design, nested route data dependencies, or error boundary placement.
- Reviewing caching and revalidation strategy or progressive enhancement patterns.

## Workflow

1. Identify route organization — do routes follow the application's domain structure?
2. Review loader design — are loaders fetching only the data needed by the route?
3. Check action design — are actions handling mutations or also business logic?
4. Review nested route data dependencies — are parent/child data dependencies clear?
5. Check error boundary placement — are boundaries at appropriate route levels?
6. Review caching and revalidation strategy — is it explicit and predictable?
7. Recommend the smallest change that clarifies route or data boundaries.

## Output Format

```markdown
Remix architecture review:
- Route organization:
- Loader design:
- Action design:
- Nested route dependencies:
- Error boundaries:
- Caching strategy:
- Recommended change:
- Verification:
```
