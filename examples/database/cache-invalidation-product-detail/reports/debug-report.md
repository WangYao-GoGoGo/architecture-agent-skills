# Debug Report: Cache Invalidation Product Detail

## 1. Original Problem

Product detail pages are cached but not invalidated when product data changes. Users see stale product information (price, description, availability).

## 2. Root Cause

Missing cache invalidation strategy — the cache is write-only (set on read) with no mechanism to clear or update cached entries when the underlying data changes.

## 3. Fix Summary

Added a cache invalidation strategy:

- Cache-aside pattern with explicit invalidation on product updates.
- TTL-based expiration as a safety net.
- Write-through cache update for critical fields (price, stock).

## 4. Files Changed

| File | Change |
|---|---|
| `before/` | Original — no cache invalidation |
| `after/` | Refactored — cache invalidation strategy |

## 5. Validation Commands

```bash
redis-cli < tests/test_cache_invalidation.redis
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a cache server.

- Cache is invalidated when product data is updated.
- Stale data TTL is bounded by explicit invalidation + TTL safety net.
- Read-after-write consistency for critical fields.

## 7. Behavior Preservation Notes

✅ Behavior preserved — cache still serves product detail pages. Added invalidation ensures data freshness.

## 8. Remaining Risks

- Race conditions between concurrent reads and writes.
- Cache stampede if many requests arrive after invalidation.

## 9. Follow-up Recommendations

- Add a distributed lock for cache stampede prevention.
- Consider using Redis Streams for cache invalidation events.
