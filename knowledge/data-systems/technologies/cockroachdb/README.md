# CockroachDB Knowledge

## Heuristics

- Design tables and indexes around geo-partitioning when latency matters globally.
- Use `SERIALIZABLE` isolation as the only isolation level; design for retries.
- Keep range splits even by choosing good primary keys; avoid monotonically increasing keys.
- Use `IMPORT INTO` for bulk loads and `CHANGEFEED` for streaming changes.
- Monitor `KV` latency, `SQL` latency, and replica balance as key health signals.
- Plan cluster topology with node and region survival goals.
