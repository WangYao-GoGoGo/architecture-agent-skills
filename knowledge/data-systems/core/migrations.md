# Database Migrations

## Use When

- Changing tables, columns, indexes, constraints, documents, keys, or derived data.

## Core Idea

Production-safe migrations are usually staged. Application code and database shape may need to support old and new versions during rollout.

## Common Pattern

1. Expand: add new nullable columns, tables, indexes, or fields.
2. Migrate: backfill and dual-write or adapt reads.
3. Contract: remove old fields after all code paths are moved.

## Agent Heuristics

- Separate schema changes from risky data backfills.
- Check locks and table size before adding indexes or constraints.
- Keep rollback and forward-fix options explicit.
- Verify application compatibility during rolling deploys.

