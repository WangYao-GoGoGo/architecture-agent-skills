# Redshift Knowledge

## Heuristics

- Choose distribution keys to minimize data movement during joins.
- Use sort keys for efficient range-restricted queries and `MIN`/`MAX` optimization.
- Use `ENCODE` appropriately: `RAW` for small tables, `ZSTD` for large, `AZ64` for numeric.
- Use workload management (WLM) queues to isolate ETL from reporting queries.
- Run `VACUUM` and `ANALYZE` regularly to maintain query performance.
- Monitor `stl_query`, `stl_scan`, and `svv_table_info` for performance troubleshooting.
- Use `COPY` for bulk loads; avoid single-row `INSERT`.
