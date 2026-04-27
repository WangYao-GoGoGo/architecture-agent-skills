# ArangoDB Knowledge

## Heuristics

- Choose the right data model: documents, graphs, or key-value per access pattern.
- Use AQL for cross-model queries; it supports document, graph, and join operations.
- Create indexes on fields used in `FILTER`, `SORT`, and `JOIN` operations.
- Use graph traversals with `GRAPH` or edge collections for relationship-heavy queries.
- Watch `smart_graphs` for distributed graph sharding in cluster mode.
- Use `db.<collection>.ensureIndex()` for index creation; review with `db.<collection>.indexes()`.
