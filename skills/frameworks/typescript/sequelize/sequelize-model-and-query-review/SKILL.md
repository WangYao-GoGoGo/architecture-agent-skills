---
name: sequelize-model-and-query-review
description: Use when reviewing Sequelize models, associations, migrations, transactions, scopes, and query boundaries.
---

# Sequelize Model & Query Review

## When To Use

- The main decision is about Sequelize model definitions, association design, migration strategy, or query optimization.
- Reviewing eager loading, N+1 behavior, or transaction propagation.

## Workflow

1. Identify the model definitions — attributes, options, indexes, and validation.
2. Review association design — `hasMany`, `belongsTo`, `belongsToMany`, and through tables.
3. Check query patterns — `include`, `where`, `attributes`, and scopes.
4. Review transaction boundaries — `sequelize.transaction`, propagation, and isolation.
5. Check migration strategy — migration files, seeders, and rollback.
6. Review hooks and lifecycle callbacks — are side effects visible and testable?
7. Recommend the smallest structural change that improves performance or maintainability.

## Output Format

```markdown
Sequelize review:
- Model definitions:
- Association design:
- Query patterns:
- Transaction boundaries:
- Migration strategy:
- Hooks & callbacks:
- Recommended change:
- Verification:
```
