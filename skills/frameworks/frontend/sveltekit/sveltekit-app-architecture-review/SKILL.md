---
name: sveltekit-app-architecture-review
description: Use when reviewing SvelteKit application architecture, routing, load functions, form actions, server/client boundaries, endpoints, and data loading strategy.
---

# SvelteKit App Architecture Review

## When To Use

- The main decision is about SvelteKit project structure, route organization, load function design, form action design, or server/client boundaries.
- Reviewing caching and invalidation strategy or endpoint design.

## Workflow

1. Identify route organization — do routes follow the application's domain structure?
2. Review load function design — are load functions fetching only needed data?
3. Check form action design — are actions handling mutations or also business logic?
4. Review server/client boundaries — is server-only code leaking into client bundles?
5. Check endpoint design — are API routes organized by domain?
6. Review caching and invalidation strategy — is it explicit and predictable?
7. Recommend the smallest change that clarifies route or data boundaries.

## Output Format

```markdown
SvelteKit architecture review:
- Route organization:
- Load functions:
- Form actions:
- Server/client boundaries:
- Endpoints:
- Caching strategy:
- Recommended change:
- Verification:
```
