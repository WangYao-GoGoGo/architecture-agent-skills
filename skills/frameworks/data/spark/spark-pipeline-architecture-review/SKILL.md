---
name: spark-pipeline-architecture-review
description: Use when reviewing Apache Spark pipeline architecture, DataFrame/Dataset transformations, partitioning, shuffles, caching, and production job design.
---

# Spark Pipeline Architecture Review

## When To Use

- The main decision is about Spark job structure, partitioning strategy, shuffle boundaries, caching, or idempotent writes.
- Reviewing data contracts, transformation logic, or cluster resource usage.

## Workflow

1. Identify the data contracts — input schema, transformation steps, and output schema.
2. Review partitioning strategy — is it aligned with data volume and cluster resources?
3. Check shuffle boundaries — wide transformations, join strategies, and data skew.
4. Review caching and checkpoint usage — is it justified and cleaned up?
5. Check idempotency of output writes — overwrite mode, partition discovery, and retry behavior.
6. Review job structure for testability — can transformations be tested outside the cluster?
7. Recommend the smallest structural change that improves performance or reliability.

## Output Format

```markdown
Spark pipeline review:
- Data contracts:
- Partitioning strategy:
- Shuffle & join boundaries:
- Caching & checkpointing:
- Write idempotency:
- Testability:
- Recommended change:
- Verification:
```
