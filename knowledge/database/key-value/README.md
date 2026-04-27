# Key-Value Stores

## Use When

- Reviewing Redis-like, Dynamo-style, or simple key-value access patterns.

## Heuristics

- Design keys from exact lookup and partition needs.
- Keep value shape aligned with atomic update needs.
- Use TTLs deliberately and document source of truth.
- Watch hot keys and unbounded key cardinality.
- Avoid secondary-query expectations unless the store supports them.

## Common Risks

- Key naming without tenant/environment isolation.
- Cache data treated as source of truth accidentally.
- Hot partitions under popular keys.
- No cleanup or TTL strategy.

