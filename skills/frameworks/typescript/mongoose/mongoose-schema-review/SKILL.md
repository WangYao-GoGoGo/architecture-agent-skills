---
name: mongoose-schema-review
description: Use when reviewing Mongoose schemas, subdocuments, references, indexes, middleware, validation, and MongoDB access patterns.
---

# Mongoose Schema Review

## When To Use

- The main decision is about Mongoose schema design, document structure, indexing strategy, or middleware boundaries.
- Reviewing subdocument vs reference tradeoffs, validation rules, or query performance.

## Workflow

1. Identify the schema design — field types, validation, defaults, and indexes.
2. Review subdocuments vs references — embedding vs referencing tradeoffs.
3. Check indexing strategy — single field, compound, text, and TTL indexes.
4. Review middleware (pre/post hooks) — are side effects visible and testable?
5. Check query patterns — `populate`, `lean`, aggregation pipelines, and pagination.
6. Review document growth and unbounded array risks.
7. Recommend the smallest structural change that improves performance or data integrity.

## Output Format

```markdown
Mongoose review:
- Schema design:
- Subdocuments vs references:
- Indexing strategy:
- Middleware:
- Query patterns:
- Document growth:
- Recommended change:
- Verification:
```
