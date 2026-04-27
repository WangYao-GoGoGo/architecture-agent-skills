---
name: postgresql-query-and-index-review
description: Use when reviewing PostgreSQL queries, indexes, EXPLAIN plans, constraints, JSONB, full-text search, transactions, and performance risks.
---

# PostgreSQL Query And Index Review

## Workflow

1. Identify critical queries, predicates, joins, sorting, and data volume.
2. Review `EXPLAIN`, index types, partial indexes, expression indexes, and covering indexes.
3. Check JSONB, full-text search, constraints, and transaction behavior where relevant.
4. Recommend query/index changes with migration and write overhead considered.
5. Verify with plans and representative data.

## Output Format

```markdown
PostgreSQL review:
- Query/access pattern:
- Plan/index issues:
- PostgreSQL-specific options:
- Recommendation:
- Verification:
```
