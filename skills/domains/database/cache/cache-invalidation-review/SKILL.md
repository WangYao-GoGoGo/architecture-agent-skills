---
name: cache-invalidation-review
description: Use when reviewing cache invalidation rules, stale data risk, TTLs, event-based invalidation, versioned keys, write paths, and consistency tradeoffs.
---

# Cache Invalidation Review

## Workflow

1. Identify all writes that can make cached data stale.
2. Map every cache key affected by each write.
3. Check invalidation timing: before write, after write, transaction commit, async event, or TTL only.
4. Review race conditions and partial failure behavior.
5. Recommend explicit invalidation or versioning rules.

## Output Format

```markdown
Cache invalidation review:
- Cached data:
- Write paths:
- Staleness risks:
- Invalidation strategy:
- Failure handling:
- Verification:
```
