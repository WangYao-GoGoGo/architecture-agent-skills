# Trino Knowledge

## Heuristics

- Push down filters and aggregations to the source when the connector supports it.
- Use `EXPLAIN (TYPE DISTRIBUTED)` to understand query distribution across workers.
- Choose the right connector: Hive for data lakes, JDBC for relational sources, Elasticsearch for search.
- Use `query.max-memory-per-node` and `query.max-total-memory` to prevent OOM.
- Watch coordinator CPU and network I/O; the coordinator is a bottleneck for many small queries.
- Use `connector.name` properties to tune per-connector behavior.
