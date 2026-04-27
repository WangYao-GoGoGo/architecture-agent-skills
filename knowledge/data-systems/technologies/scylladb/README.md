# ScyllaDB Knowledge

## Heuristics

- Leverage shard-per-core architecture; each vCPU owns a shard with its own memory and CPU.
- Use workload prioritization to isolate critical queries from background workloads.
- Tune `memtable_flush_quiet_period` and `compaction_throughput_mb_per_sec` for write-heavy loads.
- Monitor `cache_hit_rate`, `disk_usage`, and `shard` balance across the cluster.
- Use the same CQL data modeling patterns as Cassandra for compatibility.
- Plan `nodetool cleanup` after topology changes to remove stale data.
