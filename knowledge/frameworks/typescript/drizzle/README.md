# Drizzle ORM Knowledge

## Heuristics

- Keep schema definitions, queries, and migrations coherent.
- Review query performance for relation loading patterns.
- Treat migration strategy and schema versioning as architecture.
- Use the type-safe query builder to prevent runtime SQL errors.

## Common Risks

- Relation loading causing N+1 queries.
- Schema changes without proper migration planning.
- Raw SQL queries bypassing type safety.
