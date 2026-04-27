# RocksDB Knowledge

## Heuristics

- Tune `write_buffer_size`, `max_write_buffer_number`, and `min_write_buffer_number_to_merge` for write workload.
- Choose compaction style: level compaction for read-heavy, universal for write-heavy.
- Use bloom filters on the last level to reduce read amplification.
- Monitor compaction debt; stalled writes indicate compaction falling behind.
- Use `rate_limiter` to control compaction I/O impact on foreground operations.
- Keep `block_cache` sized to fit the working set for read performance.
