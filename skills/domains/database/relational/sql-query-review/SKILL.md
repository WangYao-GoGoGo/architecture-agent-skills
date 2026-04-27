---
name: relational-sql-query-review
description: Use when reviewing relational SQL queries for correctness, joins, filters, aggregation, pagination, index usage, query plans, and maintainability.
---

# Relational SQL Query Review

## Workflow

1. Identify the query goal and expected cardinality.
2. Review joins, filters, grouping, sorting, pagination, and null behavior.
3. Check whether indexes support the access pattern.
4. Look for accidental fanout, missing predicates, and unstable pagination.
5. Recommend a clearer query shape and verification with sample data or explain plan.

## Output Format

```markdown
Relational query review:
- Goal:
- Correctness risks:
- Performance risks:
- Recommendation:
- Verification:
```
