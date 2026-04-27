---
name: rails-app-architecture-review
description: Use when reviewing Rails application architecture, model/view/controller boundaries, service objects, background jobs, callbacks, and migration strategies.
---

# Rails App Architecture Review

## When To Use

- The main decision is about Rails project structure, model responsibilities, callback chains, background job design, or migration safety.
- Reviewing service objects, policy objects, or when to extract domain layers from Active Record models.

## Workflow

1. Identify model responsibilities — do models own validation, persistence, policy, and orchestration?
2. Review callback chains — are callbacks creating hidden workflow ordering and failure behavior?
3. Check controller responsibilities — are controllers thin or owning business logic?
4. Review background job design — are jobs idempotent and failure-tolerant?
5. Check migration strategy — are zero-downtime migrations planned for large tables?
6. Review service/domain objects — are they introduced when models become overloaded?
7. Recommend the smallest change that clarifies ownership without over-engineering.

## Output Format

```markdown
Rails architecture review:
- Model responsibilities:
- Callback chains:
- Controller responsibilities:
- Background jobs:
- Migration strategy:
- Service/domain objects:
- Recommended change:
- Verification:
```
