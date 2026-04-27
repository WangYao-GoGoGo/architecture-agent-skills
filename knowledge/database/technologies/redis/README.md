# Redis Knowledge

## Heuristics

- Choose data structures from access patterns: strings, hashes, sets, sorted sets, streams, bitmaps, HyperLogLog.
- Define whether Redis is cache, queue, lock, session store, rate limiter, or source of truth.
- Use TTLs intentionally and monitor memory growth.
- Use atomic operations or Lua where multi-step consistency matters.
- Keep key naming namespaced by environment, tenant, and feature where relevant.

