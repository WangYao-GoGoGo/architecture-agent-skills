---
name: relational-performance-review
description: Use when reviewing relational database performance, indexes, query plans, joins, locks, pagination, connection usage, and read/write scaling.
---

# Relational Performance Review

## Workflow

1. Identify slow paths, critical queries, write volume, and data size.
2. Review query plans, indexes, joins, pagination, and lock behavior.
3. Check connection pooling, transaction scope, and N+1 query risks.
4. Recommend targeted changes before adding new infrastructure.
5. Verify with explain plans or benchmark checks.

## Output Format

```markdown
Relational performance review:
- Hot path:
- Plan/index risks:
- Transaction/lock risks:
- Recommendation:
- Verification:
```
