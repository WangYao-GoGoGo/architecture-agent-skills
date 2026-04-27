---
name: flyway-migration-review
description: Use when reviewing Flyway migration strategy, versioned SQL migrations, repeatable migrations, rollout order, and application compatibility.
---

# Flyway Migration Review

## When To Use

- The main decision is about Flyway migration versioning, repeatable vs versioned migrations, baseline strategy, or out-of-order execution.
- Reviewing rollback strategy, migration testing, or deployment compatibility.

## Workflow

1. Identify the migration versioning scheme — naming convention, version gaps, and ordering.
2. Review versioned migrations for immutability after release.
3. Check repeatable migrations — are they used for views, functions, or reference data?
4. Review baseline and out-of-order configuration for existing databases.
5. Check rollback strategy — undo migrations, forward-fix, or recreate.
6. Review migration testing approach — representative schema and data.
7. Recommend the smallest structural change that improves migration safety.

## Output Format

```markdown
Flyway migration review:
- Versioning scheme:
- Versioned migration immutability:
- Repeatable migrations:
- Baseline & out-of-order:
- Rollback strategy:
- Migration testing:
- Recommended change:
- Verification:
```
