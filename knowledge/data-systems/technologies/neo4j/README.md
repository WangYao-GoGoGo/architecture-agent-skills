# Neo4j Knowledge

## Heuristics

- Model domains as labeled property graphs; use nodes for entities and relationships for connections.
- Use `PROFILE` and `EXPLAIN` to analyze Cypher query performance.
- Create indexes on properties used in `WHERE` and `JOIN` predicates.
- Use `MERGE` for idempotent create-or-match patterns.
- Watch for fan-out patterns that produce large intermediate result sets.
- Use `apoc` procedures for advanced operations and data import.
- Plan index and constraint creation before data loading for large imports.
