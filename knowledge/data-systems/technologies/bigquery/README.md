# BigQuery Knowledge

## Heuristics

- Partition tables by date/time column for cost control and query pruning.
- Use clustering on columns frequently used in filters and aggregations.
- Use `SELECT * EXCEPT` and `LIMIT` to reduce data scanned.
- Use materialized views for pre-computed aggregations on streaming data.
- Slot reservations guarantee query performance; on-demand is simpler for variable workloads.
- Monitor `total_slot_ms`, `total_bytes_processed`, and `total_bytes_billed` per query.
- Use `INFORMATION_SCHEMA` views for query performance analysis.
