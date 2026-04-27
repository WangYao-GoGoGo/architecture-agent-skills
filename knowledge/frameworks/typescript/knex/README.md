# Knex.js Knowledge

## Heuristics

- Keep query building, migration scripts, and seed files organized.
- Review transaction boundaries and query complexity.
- Treat migration versioning and rollback as architecture.
- Use query builder methods consistently for readability.

## Common Risks

- Raw SQL mixed inconsistently with query builder.
- Migrations without proper rollback definitions.
- Connection pooling not configured for production load.
