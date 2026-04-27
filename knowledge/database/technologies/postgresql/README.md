# PostgreSQL Knowledge

## Heuristics

- Use constraints, indexes, partial indexes, expression indexes, and JSONB deliberately.
- Review query plans with representative data.
- Treat migrations and lock behavior as deployment concerns.
- Prefer database-native features when they simplify correctness without over-coupling.
- Use full-text search and extensions only with clear operational ownership.

