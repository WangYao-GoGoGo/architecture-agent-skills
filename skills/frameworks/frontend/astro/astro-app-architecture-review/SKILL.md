---
name: astro-app-architecture-review
description: Use when reviewing Astro application architecture, islands architecture, content collections, server/client boundaries, integrations, and data loading.
---

# Astro App Architecture Review

## When To Use

- The main decision is about Astro project structure, islands architecture, content collection design, or server/client component boundaries.
- Reviewing integration usage or data loading strategy.

## Workflow

1. Identify project structure — are pages, components, layouts, and content collections organized by domain?
2. Review islands architecture — are interactive islands scoped to specific UI behaviors?
3. Check server/client boundaries — is server-only code leaking into client bundles?
4. Review content collection design — are collections organized by content type and schema?
5. Check integration usage — are integrations adding unnecessary complexity?
6. Review data loading strategy — is data fetched at the right level (page vs component)?
7. Recommend the smallest change that clarifies architecture.

## Output Format

```markdown
Astro architecture review:
- Project structure:
- Islands architecture:
- Server/client boundaries:
- Content collections:
- Integration usage:
- Data loading:
- Recommended change:
- Verification:
```
