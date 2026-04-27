---
name: mithril-app-architecture-review
description: Use when reviewing Mithril application architecture, components, routing, XHR requests, redraw system, and application structure.
---

# Mithril App Architecture Review

## When To Use

- The main decision is about Mithril project structure, component design, route organization, or XHR request patterns.
- Reviewing redraw management or state ownership.

## Workflow

1. Identify project structure — are components, models, and services organized by domain?
2. Review component design — are components focused on UI or owning business logic?
3. Check route organization — do routes follow the application's URL structure?
4. Review XHR request patterns — are API calls at the right level (component vs model)?
5. Check redraw management — are manual redraws minimized and predictable?
6. Review state ownership — is state in components, models, or services?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Mithril architecture review:
- Project structure:
- Component design:
- Route organization:
- XHR patterns:
- Redraw management:
- State ownership:
- Recommended change:
- Verification:
```
