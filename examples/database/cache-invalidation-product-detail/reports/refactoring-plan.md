# Cache Invalidation Example: Product Detail

## Before

The application caches product detail responses by `product:{id}` with a 24-hour TTL. Product price, inventory, and description can be updated independently, but only description updates invalidate the cache.

## Design Pressure

- stale price can be shown to users
- write paths do not map to affected cache keys
- TTL is used as a substitute for ownership

## Recommended Direction

- define product detail cache as derived data
- invalidate or version `product:{id}` after price, inventory, or description changes
- keep source of truth in the product database
- consider shorter TTL only as backup, not primary correctness

## Verification

- changing price invalidates or refreshes product detail cache
- cache miss falls back to source of truth
- cache failure does not break product reads

