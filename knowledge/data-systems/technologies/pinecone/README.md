# Pinecone Knowledge

## Heuristics

- Choose index metric type (`cosine`, `dotproduct`, `euclidean`) based on embedding model.
- Use namespaces to isolate vectors by tenant or environment within one index.
- Use metadata filtering to narrow search scope before vector comparison.
- Monitor pod utilization and scale horizontally with replicas for higher throughput.
- Use `upsert` for incremental updates; batch inserts for initial loading.
- Plan index dimension to match the embedding model output dimension.
