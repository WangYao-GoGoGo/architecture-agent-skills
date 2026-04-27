# Spark Knowledge

## Heuristics

- Separate data contracts, transformations, actions, and output writes.
- Treat partitioning, shuffles, caching, and joins as architecture.
- Keep business transformations testable outside cluster execution where possible.
- Make job idempotency and backfill behavior explicit.

## Common Risks

- Hidden wide shuffles.
- Non-idempotent writes.
- Schema drift and weak data quality checks.

