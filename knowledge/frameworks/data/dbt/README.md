# dbt Knowledge

## Heuristics

- Separate staging, intermediate, and mart model layers.
- Keep transformations testable and documented.
- Treat materialization strategy and incremental logic as architecture.
- Add data quality tests for critical columns and relationships.

## Common Risks

- Models with too many direct upstream dependencies.
- Incremental models without proper unique key or merge logic.
- Documentation and tests treated as optional.
