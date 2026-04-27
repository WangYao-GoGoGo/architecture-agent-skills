---
name: llamaindex-rag-architecture-review
description: Use when reviewing LlamaIndex RAG architecture, indexing strategy, retrieval pipeline, query engine design, document processing, and production readiness.
---

# LlamaIndex RAG Architecture Review

## When To Use

- The main decision is about LlamaIndex indexing strategy, chunking, retrieval, query engine composition, or document processing pipeline.
- Reviewing RAG quality, metadata filtering, or refresh strategy.

## Workflow

1. Identify the indexing strategy — document parsing, chunking, embedding, and storage.
2. Review the retrieval pipeline — retriever type, top-k, reranking, and metadata filtering.
3. Check query engine composition — sub-queries, routing, and synthesis.
4. Review document refresh and ingestion pipeline for staleness.
5. Check evaluation setup — retrieval quality metrics and representative queries.
6. Review permission and access control integration.
7. Recommend the smallest structural change that improves retrieval quality or maintainability.

## Output Format

```markdown
LlamaIndex architecture review:
- Indexing strategy:
- Retrieval pipeline:
- Query engine composition:
- Document refresh:
- Evaluation setup:
- Access control:
- Recommended change:
- Verification:
```
