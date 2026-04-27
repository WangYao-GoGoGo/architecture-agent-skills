# Dagster Knowledge

## Heuristics

- Separate asset definitions, job composition, I/O managers, resources, and schedules.
- Keep asset dependencies explicit and acyclic where possible.
- Treat I/O manager boundaries and resource configuration as architecture.
- Add asset checks and data quality validation.

## Common Risks

- Assets with implicit dependencies not captured in the DAG.
- I/O managers that couple storage to business logic.
- Resource configuration not environment-aware.
