---
name: indexing-strategy-review
description: Use when reviewing database indexes for query access patterns, selectivity, sort order, write overhead, uniqueness, constraints, and operational risk.
---

# Indexing Strategy Review

## Workflow

1. Identify the slow or critical queries.
2. List filters, joins, sort order, grouping, and pagination behavior.
3. Check existing indexes and write volume.
4. Recommend indexes only when access patterns justify them.
5. Include verification with query plans or benchmark checks.

## Output Format

```markdown
Indexing review:
- Query patterns:
- Current indexes:
- Recommended indexes:
- Write/storage tradeoffs:
- Verification:
```
