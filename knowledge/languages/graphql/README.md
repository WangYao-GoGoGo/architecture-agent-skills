# GraphQL Architecture Idioms

## Use When

- Reviewing GraphQL schema design, resolver architecture, data loading patterns, or API gateway design.

## Heuristics

- Design schema around business capabilities, not database tables.
- Use `DataLoader` for batching and caching to prevent N+1 queries.
- Keep resolvers thin — delegate business logic to service layers.
- Use `Node` interface for relay-compatible pagination.
- Use `union` and `interface` for polymorphic return types.
- Prefer `Connection` pattern (with `PageInfo`, `edges`, `nodes`) for pagination.
- Use `@defer` and `@stream` (when available) for incremental delivery.
- Use `@deprecated` directive for schema evolution.

## Common Risks

- N+1 queries from field-level resolvers without batching.
- Over-fetching authorization data in every resolver instead of batching.
- Deeply nested queries causing database performance issues — use query depth limiting.
- Exposing internal implementation details through the schema.
- Circular type references without proper forward declaration.
