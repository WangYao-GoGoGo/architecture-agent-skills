# Bytebase Knowledge

## Heuristics

- Keep schema change workflow reviewable and auditable.
- Separate DDL changes from DML changes in review process.
- Treat tenant management and multi-environment rollout as architecture.
- Add SQL review policies for consistency and safety.

## Common Risks

- Schema changes applied without proper review.
- Rollback scripts not prepared for failed migrations.
- Tenant-specific schema drift not detected.
