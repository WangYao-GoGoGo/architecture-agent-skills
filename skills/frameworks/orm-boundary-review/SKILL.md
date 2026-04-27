---
name: orm-boundary-review
description: Use when reviewing ORM architecture across Hibernate, Spring Data JPA, SQLAlchemy, Django ORM, Prisma, TypeORM, Sequelize, Mongoose, or similar tools, especially entity boundaries, sessions, transactions, lazy loading, generated types, repositories, and query performance.
---

# ORM Boundary Review

## Knowledge To Use

- `knowledge/frameworks/orm/orm-boundaries.md`
- `knowledge/database/core/access-patterns.md`
- `knowledge/database/core/consistency.md`
- `knowledge/database/core/migrations.md`

## Workflow

1. Identify ORM models/entities, sessions/contexts, repositories, transactions, and generated clients.
2. Check whether ORM types leak into API contracts, domain rules, or frontend state.
3. Review lazy/eager loading, N+1 risks, cascading writes, and transaction scope.
4. Decide whether repositories, query services, or direct ORM use are appropriate for the codebase.
5. Recommend the smallest boundary that improves testability, performance, or coupling.
6. Verify with tests, query logs, explain plans, or representative call paths.

## Output Format

```markdown
ORM boundary review:
- ORM surface:
- Coupling/performance risks:
- Transaction boundary:
- Recommended structure:
- Verification:
```
