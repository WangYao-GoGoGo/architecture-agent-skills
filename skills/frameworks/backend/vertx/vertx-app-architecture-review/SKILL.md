---
name: vertx-app-architecture-review
description: Use when reviewing Vert.x application architecture, verticle design, event bus topology, reactive streams, shared data, and async request handling.
---

# Vert.x App Architecture Review

## When To Use

- The main decision is about Vert.x project structure, verticle boundaries, event bus topology, or reactive stream design.
- Reviewing shared data access, async coordination, or failure handling patterns.

## Workflow

1. Identify verticle design — are verticles organized by domain or by technical concern?
2. Review event bus topology — are addresses organized by domain and event type?
3. Check reactive stream design — are streams properly backpressured and error-handled?
4. Review shared data access — is shared data accessed through appropriate data structures?
5. Check async coordination — are complex async flows using `Future`, `Promise`, or RxJava?
6. Review failure handling — are verticle failure and restart behaviors clear?
7. Recommend the smallest change that clarifies verticle boundaries.

## Output Format

```markdown
Vert.x architecture review:
- Verticle design:
- Event bus topology:
- Reactive streams:
- Shared data:
- Async coordination:
- Failure handling:
- Recommended change:
- Verification:
```
