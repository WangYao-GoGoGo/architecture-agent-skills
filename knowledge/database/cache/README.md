# Cache Stores

## Use When

- Reviewing dedicated cache stores, application caches, Redis, CDN, or materialized read models.

## Heuristics

- Name the source of truth.
- Map read, write, invalidation, refresh, and fallback paths.
- Choose TTL from stale-data tolerance.
- Protect expensive misses from stampede.
- Make cache failure behavior explicit.

## Common Risks

- TTL-only correctness.
- Invalidation missing a write path.
- Cache keys without versioning or namespace.
- Cache outages breaking the source-of-truth path.

