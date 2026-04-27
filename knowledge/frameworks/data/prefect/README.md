# Prefect Knowledge

## Heuristics

- Separate flow design, task decomposition, retry logic, caching, and concurrency.
- Keep task side effects idempotent and independently retryable.
- Treat flow parameters, caching keys, and result persistence as architecture.
- Add monitoring for flow runs, task failures, and latency.

## Common Risks

- Tasks with hidden dependencies on shared state.
- Caching without proper invalidation strategy.
- Flow parameters not versioned with deployment.
