---
name: sql-schema-refactor
description: Use when refactoring SQL schemas, tables, constraints, indexes, normalization, denormalization, migrations, and compatibility with application code.
---

# SQL Schema Refactor

## Workflow

1. Identify entities, relationships, constraints, and access patterns.
2. Review normalization, duplication, indexes, and foreign keys.
3. Plan expand/migrate/contract steps for risky changes.
4. Preserve application compatibility during rollout.
5. Verify with migrations, constraints, query plans, and sample data.

## Output Format

```markdown
SQL schema refactor:
- Current model:
- Issues:
- Target model:
- Migration steps:
- Verification:
```
