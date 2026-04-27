---
name: sql-query-structure
description: Use when reviewing SQL query readability, joins, filters, CTEs, aggregation, pagination, performance, and maintainable query shape.
---

# SQL Query Structure

## Workflow

1. Identify query purpose and expected result shape.
2. Review joins, filters, grouping, sorting, pagination, and null handling.
3. Use CTEs or subqueries to name meaningful stages, not to hide poor plans.
4. Check indexes and query plan expectations when performance matters.
5. Verify with sample results or explain plans.

## Output Format

```markdown
SQL query review:
- Query goal:
- Structure issues:
- Performance risks:
- Recommended query shape:
- Verification:
```
