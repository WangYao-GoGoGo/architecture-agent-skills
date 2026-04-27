# Dgraph Knowledge

## Heuristics

- Design graph schema with types, predicates, and reverse edges explicitly.
- Use DQL (GraphQL+-) for flexible graph traversal and filtering.
- Create indexes on predicates used in `filter`, `order`, and `regexp` operations.
- Use `@reverse` directive for bidirectional edge traversal.
- Watch transaction conflicts under high write concurrency; design for retries.
- Plan sharding strategy; data is automatically sharded by predicate.
