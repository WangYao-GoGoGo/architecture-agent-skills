---
name: sqlalchemy-session-and-query-review
description: Use when reviewing SQLAlchemy model mapping, session lifecycle, transaction boundaries, lazy/eager loading, and query architecture.
---

# SQLAlchemy Session & Query Review

## When To Use

- The main decision is about SQLAlchemy model design, session management, query optimization, or transaction boundaries.
- Reviewing N+1 query behavior, relationship loading, or migration strategy.

## Workflow

1. Identify the model mapping — table definitions, relationships, and inheritance.
2. Review session lifecycle — session scope, commit/rollback patterns, and session per request.
3. Check query patterns — lazy loading, eager loading, joinedload, and subqueryload.
4. Review transaction boundaries — are they aligned with use case boundaries?
5. Check for N+1 query patterns in serialization or template rendering.
6. Review migration strategy — Alembic integration and schema evolution.
7. Recommend the smallest structural change that improves performance or correctness.

## Output Format

```markdown
SQLAlchemy review:
- Model mapping:
- Session lifecycle:
- Query patterns:
- Transaction boundaries:
- N+1 analysis:
- Migration strategy:
- Recommended change:
- Verification:
```
