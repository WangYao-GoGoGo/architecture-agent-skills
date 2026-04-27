# SQLite Knowledge

## Heuristics

- Use WAL mode for concurrent reads without blocking writes.
- Keep schema migrations backward-compatible; SQLite has limited `ALTER TABLE`.
- Use `EXPLAIN QUERY PLAN` to verify index usage.
- Treat `INTEGER PRIMARY KEY` as the rowid alias for performance.
- Avoid excessive write concurrency; SQLite serializes writes.
- Use `PRAGMA` statements to tune journal mode, cache size, and synchronous behavior.
