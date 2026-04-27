---
name: backbone-app-architecture-review
description: Use when reviewing Backbone.js application architecture, models, views, collections, routers, events, and application structure.
---

# Backbone.js App Architecture Review

## When To Use

- The main decision is about Backbone.js project structure, model/collection design, view responsibilities, router organization, or event management.
- Reviewing data flow or state ownership patterns.

## Workflow

1. Identify project structure — are models, views, collections, and routers organized by domain?
2. Review model/collection design — do models represent domain concepts or UI state?
3. Check view responsibilities — do views handle rendering or also business logic?
4. Review router organization — do routes map to application states?
5. Check event management — are events namespaced and scoped appropriately?
6. Review data flow — is data passed through models or global events?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Backbone.js architecture review:
- Project structure:
- Model/collection design:
- View responsibilities:
- Router organization:
- Event management:
- Data flow:
- Recommended change:
- Verification:
```
