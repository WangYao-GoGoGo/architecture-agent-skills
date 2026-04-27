# Milvus Knowledge

## Heuristics

- Design collections with primary keys, vector fields, and scalar fields for metadata.
- Choose index type: `IVF_FLAT` for balanced performance, `HNSW` for high recall, `DISKANN` for large-scale.
- Use partitions for time-based or category-based data segmentation.
- Use consistency levels: `Strong` for critical reads, `Bounded` for performance.
- Monitor segment status, index building progress, and query node memory.
- Use bulk insert (`bulk_insert`) for large initial data loads.
