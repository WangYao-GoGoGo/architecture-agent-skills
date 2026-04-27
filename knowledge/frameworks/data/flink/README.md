# Flink Knowledge

## Heuristics

- Treat event time, watermarks, state, checkpoints, and exactly-once semantics as architecture.
- Keep stream transformations and sinks idempotent or transactional.
- Define recovery, backpressure, and late data behavior.
- Make state ownership and schema evolution explicit.

## Common Risks

- Stateful operators without migration strategy.
- Late events handled inconsistently.
- Checkpoint failures not observable.

