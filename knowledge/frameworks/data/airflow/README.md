# Airflow Knowledge

## Heuristics

- Keep DAGs as orchestration, not heavy business logic.
- Make retries, idempotency, backfills, and dependencies explicit.
- Separate task code into testable modules.
- Treat schedules, sensors, SLAs, and failure alerts as architecture.

## Common Risks

- Non-idempotent tasks.
- Business logic hidden in DAG files.
- Backfills causing production load surprises.

