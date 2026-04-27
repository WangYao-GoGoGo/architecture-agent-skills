# LlamaIndex Knowledge

## Heuristics

- Treat ingestion, chunking, indexing, retrieval, reranking, and synthesis as separate concerns.
- Keep source-of-truth ownership and refresh paths explicit.
- Evaluate retrieval quality with representative questions.
- Keep metadata filters and permissions close to retrieval boundaries.

## Common Risks

- Stale indexes.
- Chunking that destroys context.
- Missing permission filtering.

