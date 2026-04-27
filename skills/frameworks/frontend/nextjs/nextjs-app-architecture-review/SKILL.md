---
name: nextjs-app-architecture-review
description: Use when reviewing Next.js application architecture, server/client components, routing, data fetching, caching, server actions, API routes, and bundle boundaries.
---

# Next.js App Architecture Review

## When To Use

- The main decision is about Next.js project structure, server/client component boundaries, data fetching strategy, caching and revalidation, or server action design.
- Reviewing route organization, middleware placement, or bundle size concerns.

## Workflow

1. Identify server/client component boundaries — is server-only code leaking into client bundles?
2. Review routing structure — do routes follow the application's domain organization?
3. Check data fetching strategy — are fetching, caching, and revalidation strategies explicit?
4. Review server action design — are actions handling orchestration or leaking into UI concerns?
5. Check API route responsibilities — are routes thin or owning business logic?
6. Review middleware placement — is middleware handling cross-cutting concerns at the right level?
7. Recommend the smallest change that clarifies boundaries or improves performance.

## Output Format

```markdown
Next.js architecture review:
- Server/client boundaries:
- Routing structure:
- Data fetching & caching:
- Server actions:
- API routes:
- Middleware:
- Recommended change:
- Verification:
```
