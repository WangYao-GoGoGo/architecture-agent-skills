---
name: phoenix-app-architecture-review
description: Use when reviewing Phoenix application architecture, context boundaries, LiveView, PubSub, Ecto schemas, channels, and real-time features.
---

# Phoenix App Architecture Review

## When To Use

- The main decision is about Phoenix project structure, context boundaries, LiveView design, PubSub topology, or Ecto schema organization.
- Reviewing channel design, real-time data flow, or migration strategies.

## Workflow

1. Identify context boundaries — do contexts follow domain ownership or technical layers?
2. Review LiveView design — are LiveViews handling presentation or business logic?
3. Check PubSub topology — are topics organized by domain and subscription scope?
4. Review Ecto schema design — are schemas representing persistence or domain concepts?
5. Check channel design — are channels handling real-time events or RPC-style calls?
6. Review migration strategy — are large migrations planned for zero-downtime?
7. Recommend the smallest change that clarifies context boundaries.

## Output Format

```markdown
Phoenix architecture review:
- Context boundaries:
- LiveView design:
- PubSub topology:
- Ecto schemas:
- Channel design:
- Migration strategy:
- Recommended change:
- Verification:
```
