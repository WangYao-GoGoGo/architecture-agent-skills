---
name: redis-cache-design-review
description: Use when reviewing Redis-backed cache design, key naming, TTLs, invalidation, atomic operations, memory growth, eviction, and source-of-truth boundaries.
---

# Redis Cache Design Review

## Workflow

1. Identify keys, values, TTLs, and access patterns.
2. Check whether Redis is cache, queue, lock, session store, or source of truth.
3. Review invalidation, atomicity, memory growth, eviction, and fallback behavior.
4. Recommend structure and operational safeguards.
5. Include verification and monitoring signals.

## Output Format

```markdown
Redis cache review:
- Role:
- Key design:
- Data structure:
- Invalidation and TTL:
- Operational risks:
- Verification:
```
