# Cassandra Knowledge

## Heuristics

- Design partition keys to distribute data evenly; avoid unbounded partition growth.
- Choose clustering columns for ordering and uniqueness within a partition.
- Model tables per query pattern; denormalization is expected.
- Use `QUORUM` for reads and writes when consistency matters; `ONE` for latency-sensitive paths.
- Watch compaction strategy: `SizeTieredCompactionStrategy` for write-heavy, `LeveledCompactionStrategy` for read-heavy.
- Monitor `pending_compactions`, `read_repair`, and `hinted_handoff` stats.
- Plan `nodetool repair` as a regular operational routine.
