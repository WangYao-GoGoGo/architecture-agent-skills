---
name: cache-strategy-review
description: Use when reviewing or designing cache strategy, including cache-aside, write-through, write-behind, TTLs, consistency, stampede prevention, key design, and failure behavior.
---

# Cache Strategy Review

## Workflow

1. Identify what is cached, who owns the source of truth, and why caching is needed.
2. Map read path, write path, invalidation path, and fallback behavior.
3. Check consistency requirements, TTL, key design, stampede prevention, and cache size.
4. Review failure behavior when cache is unavailable or stale.
5. Recommend the simplest cache pattern that meets the need.

## Output Format

```markdown
Cache strategy review:
- Source of truth:
- Read/write path:
- Invalidation:
- Consistency risk:
- Recommended strategy:
- Verification:
```
