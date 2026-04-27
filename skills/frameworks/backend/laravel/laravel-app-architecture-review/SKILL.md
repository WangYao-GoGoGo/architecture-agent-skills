---
name: laravel-app-architecture-review
description: Use when reviewing Laravel application architecture, controller/model boundaries, service providers, events, queues, policies, and service container usage.
---

# Laravel App Architecture Review

## When To Use

- The main decision is about Laravel project structure, Eloquent model responsibilities, service container binding, event/queue design, or policy boundaries.
- Reviewing service providers, action classes, or when to extract domain layers.

## Workflow

1. Identify controller responsibilities — do controllers handle HTTP only or also business workflows?
2. Review Eloquent model design — do models own too many concerns (validation, events, accessors, relationships)?
3. Check service container bindings — are bindings creating hidden coupling?
4. Review event and queue design — are events appropriately scoped and jobs idempotent?
5. Check policy and authorization boundaries — are policies at the right level?
6. Review service providers for unintended side effects during boot.
7. Recommend the smallest change that clarifies boundaries.

## Output Format

```markdown
Laravel architecture review:
- Controller responsibilities:
- Eloquent model design:
- Service container bindings:
- Events & queues:
- Policy boundaries:
- Service providers:
- Recommended change:
- Verification:
```
