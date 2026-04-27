# InfluxDB Knowledge

## Heuristics

- Design measurements around data sources; use tags for metadata and fields for values.
- Choose tag cardinality carefully; high tag cardinality degrades write and query performance.
- Use retention policies and continuous queries for automatic data lifecycle management.
- Use `EXPLAIN` to analyze query execution and verify index usage.
- Watch series cardinality; it's the most common scaling bottleneck.
- Use InfluxDB 2.x tasks (Flux) or 3.x (SQL) for data processing pipelines.
