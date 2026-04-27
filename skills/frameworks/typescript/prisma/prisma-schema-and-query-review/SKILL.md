---
name: prisma-schema-and-query-review
description: Use when reviewing Prisma schema modeling, migrations, relations, generated client boundaries, transactions, and query performance.
---

# Prisma Schema & Query Review

## When To Use

- The main decision is about Prisma schema design, relation modeling, migration strategy, or query optimization.
- Reviewing generated client usage, transaction boundaries, or N+1 behavior.

## Workflow

1. Identify the schema model — models, enums, relations, and indexes.
2. Review relation modeling — one-to-one, one-to-many, many-to-many, and referential actions.
3. Check query patterns — `include`, `select`, `where`, and relation loading.
4. Review transaction boundaries — interactive transactions, batch operations, and isolation.
5. Check migration strategy — schema drift detection, shadow database, and production migrations.
6. Review generated client boundaries — are Prisma types leaking into API contracts?
7. Recommend the smallest structural change that improves performance or maintainability.

## Output Format

```markdown
Prisma review:
- Schema model:
- Relation modeling:
- Query patterns:
- Transaction boundaries:
- Migration strategy:
- Client boundaries:
- Recommended change:
- Verification:
```
