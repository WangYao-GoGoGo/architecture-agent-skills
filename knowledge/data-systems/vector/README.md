# Vector Databases

## Use When

- Reviewing semantic search, retrieval-augmented generation, embeddings, chunking, metadata filters, and vector index freshness.

## Heuristics

- Define document ownership and embedding refresh path.
- Design chunking around retrieval quality, not fixed size alone.
- Store metadata needed for filtering, authorization, and citation.
- Evaluate recall, precision, freshness, and latency.
- Keep vector search paired with lexical or structured filters when needed.

## Common Risks

- Embeddings stale after source content changes.
- Missing tenant or permission filters.
- Chunking that destroys context.
- No evaluation set for retrieval quality.

