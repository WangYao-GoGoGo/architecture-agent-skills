---
name: nuxt-app-architecture-review
description: Use when reviewing Nuxt application architecture, auto-imports, modules, SSR/SSG, middleware, composables, server routes, and application structure.
---

# Nuxt App Architecture Review

## When To Use

- The main decision is about Nuxt project structure, auto-import organization, module usage, server/client boundaries, or composable design.
- Reviewing middleware placement, plugin side effects, or data fetching strategy.

## Workflow

1. Identify project structure — are pages, composables, server routes, plugins, and middleware organized by domain?
2. Review auto-import usage — are imports predictable or creating hidden dependencies?
3. Check server/client boundaries — is server-only code leaking into client bundles?
4. Review composable design — are composables reusable or creating hidden global state?
5. Check plugin side effects — are plugin initializations traceable and scoped?
6. Review data fetching and caching strategy — is it explicit and predictable?
7. Recommend the smallest change that clarifies structure or boundaries.

## Output Format

```markdown
Nuxt architecture review:
- Project structure:
- Auto-import usage:
- Server/client boundaries:
- Composable design:
- Plugin side effects:
- Data fetching:
- Recommended change:
- Verification:
```
