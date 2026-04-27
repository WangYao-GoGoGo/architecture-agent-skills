# Database Technologies

Technology-specific database cards live here when behavior depends on one database engine.

## Relational Databases

- [`mysql/`](./mysql/) — MySQL: InnoDB indexes, locks, transactions, isolation, EXPLAIN, pagination, covering indexes, charset/collation.
- [`postgresql/`](./postgresql/) — PostgreSQL: constraints, indexes, JSONB, query plans, migrations, lock behavior, full-text search.
- [`oracle/`](./oracle/) — Oracle: execution plans, partitions, PL/SQL, undo/redo, RAC, optimizer statistics.
- [`sql-server/`](./sql-server/) — SQL Server: query plans, clustered/nonclustered indexes, isolation levels, lock escalation, tempdb.
- [`sqlite/`](./sqlite/) — SQLite: WAL mode, schema migrations, EXPLAIN QUERY PLAN, rowid, PRAGMA tuning.
- [`mariadb/`](./mariadb/) — MariaDB: storage engines, Galera clustering, wsrep flow control, optimizer trace.
- [`cockroachdb/`](./cockroachdb/) — CockroachDB: geo-partitioning, SERIALIZABLE isolation, range splits, changefeeds.
- [`tidb/`](./tidb/) — TiDB: AUTO_RANDOM, TiFlash, region scheduling, placement rules, batch tuning.
- [`timescaledb/`](./timescaledb/) — TimescaleDB: hypertables, continuous aggregates, compression, retention policies, chunk sizing.

## Document Databases

- [`mongodb/`](./mongodb/) — MongoDB: aggregates, embedding vs references, document growth, indexes, shard keys.
- [`couchbase/`](./couchbase/) — Couchbase: N1QL, key-value access, XDCR, sub-document operations, memory management.
- [`couchdb/`](./couchdb/) — CouchDB: replication, MapReduce views, _changes feed, conflict resolution, eventual consistency.
- [`firestore/`](./firestore/) — Firestore: collection design, composite indexes, security rules, real-time queries, write limits.

## Key-Value Databases

- [`redis/`](./redis/) — Redis: data structures, TTLs, atomic operations, Lua, key naming, memory monitoring.
- [`memcached/`](./memcached/) — Memcached: slab allocation, eviction, consistent hashing, cache miss handling.
- [`rocksdb/`](./rocksdb/) — RocksDB: LSM-tree tuning, compaction, bloom filters, block cache, rate limiting.
- [`dynamodb/`](./dynamodb/) — DynamoDB: partition keys, sort keys, GSIs, LSIs, capacity planning, streams.

## Wide-Column Databases

- [`hbase/`](./hbase/) — HBase: row key design, column families, hot regions, TTL, compaction, scans.
- [`cassandra/`](./cassandra/) — Cassandra: partition keys, clustering columns, CQL, consistency levels, compaction, repair.
- [`scylladb/`](./scylladb/) — ScyllaDB: shard-per-core, workload prioritization, memtable tuning, cache hit rate.

## Graph Databases

- [`neo4j/`](./neo4j/) — Neo4j: labeled property graphs, Cypher, indexes, fan-out patterns, apoc procedures.
- [`dgraph/`](./dgraph/) — Dgraph: schema, DQL, reverse edges, sharding, transaction conflicts.

## Search & Analytics Databases

- [`elasticsearch/`](./elasticsearch/) — Elasticsearch: mappings, analyzers, shards, index lifecycle, relevance, aggregations.
- [`clickhouse/`](./clickhouse/) — ClickHouse: MergeTree, ORDER BY keys, partitions, materialized views, TTL, memory tuning.
- [`trino/`](./trino/) — Trino: query federation, connector pushdown, distributed execution, memory limits.
- [`influxdb/`](./influxdb/) — InfluxDB: measurements, tags vs fields, retention policies, continuous queries, series cardinality.

## Cloud Data Warehouses

- [`snowflake/`](./snowflake/) — Snowflake: warehouse sizing, clustering, materialized views, zero-copy cloning, cost monitoring.
- [`bigquery/`](./bigquery/) — BigQuery: partitioning, clustering, slot management, INFORMATION_SCHEMA, cost control.
- [`redshift/`](./redshift/) — Redshift: distribution keys, sort keys, compression, WLM, VACUUM, ANALYZE, COPY.

## Multi-Model Databases

- [`arangodb/`](./arangodb/) — ArangoDB: multi-model, AQL, graph traversals, smart graphs, indexing.

## Vector Databases

- [`pinecone/`](./pinecone/) — Pinecone: index configuration, namespaces, metadata filtering, pod scaling.
- [`weaviate/`](./weaviate/) — Weaviate: schema classes, hybrid search, modules, multi-tenancy, sharding.
- [`milvus/`](./milvus/) — Milvus: collections, index types, partitions, consistency levels, bulk insert.
- [`qdrant/`](./qdrant/) — Qdrant: collections, payload indexing, quantization, optimizers, sharding.
