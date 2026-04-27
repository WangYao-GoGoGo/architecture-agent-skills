# Peewee Knowledge

## Heuristics

- Keep model definitions, queries, and migrations coherent.
- Review query performance for N+1 patterns.
- Treat transaction scope and connection management as architecture.
- Use model methods for reusable query logic.

## Common Risks

- N+1 queries in serialization or templates.
- Connection management not handled properly.
- Migrations not tested against production-like data.
