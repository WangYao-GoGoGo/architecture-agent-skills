# Qdrant Knowledge

## Heuristics

- Configure collections with vector size, distance metric, and quantization options.
- Use payload indexing for efficient metadata filtering alongside vector search.
- Use scalar quantization (SQ) or product quantization (PQ) to reduce memory footprint.
- Use `optimizers_config` to tune segment optimization for write vs read performance.
- Use sharding for horizontal scaling; replication for high availability.
- Monitor segment count, optimized points, and disk usage per collection.
