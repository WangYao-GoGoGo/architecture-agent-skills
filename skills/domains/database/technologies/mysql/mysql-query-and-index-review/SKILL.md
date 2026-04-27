---
name: mysql-query-and-index-review
description: Use when reviewing MySQL queries, indexes, EXPLAIN plans, joins, pagination, locks, transactions, and InnoDB-specific performance risks.
---

# MySQL Query And Index Review

## Workflow

1. Identify critical queries and table sizes.
2. Review `EXPLAIN`, join order, indexes, covering indexes, and pagination.
3. Check transaction scope, lock risks, and write overhead.
4. Recommend query or index changes with migration impact.
5. Verify with query plans and representative data.

## Output Format

```markdown
MySQL review:
- Query/access pattern:
- Plan/index issues:
- Lock/write risks:
- Recommendation:
- Verification:
```
