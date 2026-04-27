# Memcached Knowledge

## Heuristics

- Use Memcached as a distributed cache, not a persistent store.
- Design key namespaces consistently with application context and tenant isolation.
- Watch slab allocation and eviction stats to tune `-f` growth factor.
- Use consistent hashing on the client side for cache node changes.
- Keep value sizes small; large values waste slab memory.
- Plan for cache misses; always have a fallback data source.
