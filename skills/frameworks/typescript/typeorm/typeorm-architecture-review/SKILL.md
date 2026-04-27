---
name: typeorm-architecture-review
description: Use when reviewing TypeORM entities, repositories, migrations, transactions, lazy loading, and service boundaries.
---

# TypeORM Architecture Review

## When To Use

- The main decision is about TypeORM entity design, repository patterns, migration strategy, or query optimization.
- Reviewing lazy relations, cascading behavior, or transaction boundaries.

## Workflow

1. Identify the entity model — decorators, relations, indexes, and column types.
2. Review repository patterns — custom repositories, `find` options, and query builder usage.
3. Check lazy relations and cascading — are they scoped appropriately?
4. Review transaction boundaries — `QueryRunner`, transaction decorators, and propagation.
5. Check migration strategy — generated migrations, rollback, and data migration safety.
6. Review query performance — relation loading, N+1 detection, and indexing.
7. Recommend the smallest structural change that improves performance or maintainability.

## Output Format

```markdown
TypeORM review:
- Entity model:
- Repository patterns:
- Lazy relations & cascading:
- Transaction boundaries:
- Migration strategy:
- Query performance:
- Recommended change:
- Verification:
```
