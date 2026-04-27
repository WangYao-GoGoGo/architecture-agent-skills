---
name: database-migration-review
description: Use when reviewing database migrations for backward compatibility, rollout order, data backfills, locking, rollback, online changes, and application compatibility.
---

# Database Migration Review

## Workflow

1. Identify schema changes, data changes, and application code dependencies.
2. Check whether the migration is backward and forward compatible during rollout.
3. Review locking, table size, backfill strategy, and rollback.
4. Split risky migrations into expand, migrate, contract steps.
5. Define verification before and after deployment.

## Output Format

```markdown
Migration review:
- Change:
- Compatibility risks:
- Rollout plan:
- Backfill/rollback:
- Verification:
```
