# TiDB Knowledge

## Heuristics

- Design primary keys to avoid hot regions; use `AUTO_RANDOM` or shard bits for high-write tables.
- Use TiFlash replicas for analytical queries without impacting TP performance.
- Watch region size and scheduling with `pd-ctl` and TiDB Dashboard.
- Use `BATCH` and `COMMIT` size tuning for large data loads.
- Plan placement rules for data locality and isolation requirements.
- Monitor `KV` get/set latency, `TiKV` CPU, and gRPC message sizes.
