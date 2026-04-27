# Couchbase Knowledge

## Heuristics

- Model documents around access patterns; use N1QL for ad-hoc queries and key-value for fast paths.
- Design indexes carefully; each index consumes memory and write overhead.
- Use cross-datacenter replication (XDCR) for multi-region deployments.
- Treat bucket, scope, and collection hierarchy as the data organization boundary.
- Watch `ep_bg_fetched` ratio to detect working set exceeding memory.
- Use sub-document operations for partial updates to reduce network overhead.
