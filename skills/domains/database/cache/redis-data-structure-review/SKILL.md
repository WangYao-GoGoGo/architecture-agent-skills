---
name: redis-data-structure-review
description: Use when choosing Redis data structures such as string, hash, list, set, sorted set, stream, bitmap, or HyperLogLog based on access patterns and consistency needs.
---

# Redis Data Structure Review

## Workflow

1. Identify access pattern: point lookup, counter, membership, ranking, queue, stream, session, lock, or rate limit.
2. Choose the simplest Redis structure that matches operations.
3. Review key naming, TTL, memory growth, atomicity, and eviction behavior.
4. Check whether Redis is source of truth or derived cache.
5. Define verification and monitoring.

## Output Format

```markdown
Redis structure review:
- Access pattern:
- Recommended structure:
- Key and TTL:
- Consistency and memory risks:
- Verification:
```
