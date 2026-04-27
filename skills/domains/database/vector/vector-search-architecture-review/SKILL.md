---
name: vector-search-architecture-review
description: Use when reviewing vector search, embedding pipelines, chunking, metadata filters, vector indexes, hybrid search, freshness, retrieval quality, and RAG data boundaries.
---

# Vector Search Architecture Review

## Knowledge To Use

- `knowledge/data-systems/vector/`
- `knowledge/data-systems/search/`
- `knowledge/data-systems/core/access-patterns.md`

## Workflow

1. Identify source documents, chunking strategy, embedding model, vector index, metadata filters, and retrieval consumers.
2. Check source-of-truth ownership and embedding refresh path.
3. Review tenant, permission, and metadata filtering.
4. Evaluate retrieval quality with representative queries, not only index latency.
5. Consider hybrid search when lexical precision or structured filters matter.
6. Recommend index, chunking, metadata, or refresh changes with verification.

## Output Format

```markdown
Vector search review:
- Source and embedding flow:
- Chunking/index strategy:
- Metadata and permissions:
- Retrieval quality risks:
- Recommendation:
- Verification:
```
