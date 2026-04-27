# Caching

## Use When

- Adding or reviewing caches, Redis keys, materialized views, CDN behavior, or application-level memoization.

## Core Idea

A cache is derived state. It needs a source of truth, a refresh or invalidation strategy, and a failure behavior.

## Agent Heuristics

- Name the source of truth.
- Map read path, write path, invalidation path, and fallback path.
- Choose TTL based on stale-data tolerance, not guesswork.
- Protect hot keys and expensive recomputation from stampedes.
- Avoid caching data whose consistency requirements are not understood.

## Verification

- Writes cannot leave critical stale data indefinitely.
- Cache miss and cache failure behavior are tested.
- Key design avoids accidental collisions and unbounded growth.

