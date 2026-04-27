# Column-Family Databases

## Use When

- Reviewing HBase, Cassandra-like, Bigtable-like, or wide-column data models.

## Heuristics

- Start from access patterns and row key design.
- Avoid hot partitions and unbounded wide rows.
- Keep time-series ordering and retention explicit.
- Treat denormalization as a write-path responsibility.
- Understand compaction, TTL, and scan behavior.

## Common Risks

- Row keys that concentrate writes.
- Query patterns that require broad scans.
- Column families split without access-pattern reason.
- Updates duplicated across many rows without ownership rules.

