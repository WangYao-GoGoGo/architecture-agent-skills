# Weaviate Knowledge

## Heuristics

- Define schema classes with properties and vectorizer module configuration.
- Use hybrid search (vector + keyword) for balanced relevance and recall.
- Use `nearText`, `nearVector`, `nearImage` for different query modalities.
- Configure modules (`text2vec-transformers`, `generative-openai`) for vectorization and generation.
- Use multi-tenancy for per-tenant data isolation within a single class.
- Monitor shard status and object count for cluster health.
