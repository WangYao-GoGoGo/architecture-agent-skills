# jOOQ Knowledge

## Heuristics

- Keep generated code and custom SQL clearly separated.
- Review query complexity and execution plans.
- Treat transaction boundaries and batch operations as architecture.
- Use the DSL type safety to prevent SQL errors at compile time.

## Common Risks

- Complex queries that are hard to read and maintain.
- Transaction boundaries too broad or too narrow.
- Generated code not regenerated after schema changes.
