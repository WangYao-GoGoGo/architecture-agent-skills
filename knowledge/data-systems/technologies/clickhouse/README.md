# ClickHouse Knowledge

## Heuristics

- Choose `MergeTree` engine family for production; `ReplicatedMergeTree` for HA.
- Design `ORDER BY` key as the primary sort key; it determines partition pruning and index granularity.
- Use `PARTITION BY` for time-based data management and retention.
- Use materialized views for pre-aggregated rollups; they push compute to insert time.
- Watch `max_part_size` and number of parts; merge debt causes `Too many parts` errors.
- Use `ALTER TABLE ... DELETE` sparingly; prefer TTL-based expiration.
- Keep `max_memory_usage` and `max_bytes_before_external_group_by` tuned for large queries.
