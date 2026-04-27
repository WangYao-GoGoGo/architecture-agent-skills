# SQL Server Knowledge

## Heuristics

- Review query plans with actual execution plans for critical queries.
- Use clustered and nonclustered indexes deliberately; watch key column order.
- Treat isolation levels and lock escalation as concurrency architecture.
- Use `MERGE`, window functions, and CTEs for set-based operations over cursors.
- Plan index maintenance and statistics updates as operational routines.
- Watch tempdb contention under high concurrency workloads.
