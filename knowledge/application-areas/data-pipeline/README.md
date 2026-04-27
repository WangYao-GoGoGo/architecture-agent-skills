# Data Pipeline Architecture Knowledge

## Heuristics

- Define source, transformation, sink, schedule, and owner for every pipeline.
- Treat schemas and data contracts as public boundaries.
- Make idempotency, retries, backfills, ordering, and late data explicit.
- Add quality checks near the stage that can explain the failure.
- Keep observability around freshness, volume, errors, and lag.

## Common Risks

- Non-idempotent jobs that cannot be safely retried.
- Backfills that reuse production paths without capacity planning.
- Silent schema drift.
- Transformations that mix business rules with operational cleanup.

