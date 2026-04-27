# MariaDB Knowledge

## Heuristics

- Review storage engine choice: InnoDB for transactions, Aria for caching, MyRocks for compression.
- Use Galera clustering for synchronous multi-master replication.
- Watch `wsrep` flow control under write-heavy workloads.
- Prefer MariaDB-specific optimizations over MySQL compatibility when not migrating.
- Use `EXPLAIN` and optimizer trace for query tuning.
- Keep `innodb_buffer_pool_size` and `aria_pagecache_buffer_size` tuned to workload.
