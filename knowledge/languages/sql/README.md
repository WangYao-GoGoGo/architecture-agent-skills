# SQL Architecture Idioms

## Use When

- Reviewing query structure, schema shape, constraints, indexes, migrations, and data ownership.

## Heuristics

- Treat constraints as architecture, not just validation.
- Start from access patterns before adding indexes.
- Prefer readable query stages, but verify CTEs and subqueries with plans.
- Use migrations as compatibility workflows.
- Keep business-critical invariants close to the data when appropriate.

## Common Risks

- Queries that accidentally fan out rows.
- Indexes added without query evidence.
- Schema changes that break rolling deployments.
- Application logic duplicating database constraints inconsistently.

