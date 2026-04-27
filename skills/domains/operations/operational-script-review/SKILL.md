---
name: operational-script-review
description: Use when reviewing operational automation such as Linux shell scripts, CI jobs, deployment scripts, cron jobs, maintenance tasks, backups, migrations, or cleanup workflows for idempotency, safety, configuration, permissions, and failure recovery.
---

# Operational Script Review

## Knowledge To Use

- `knowledge/application-areas/operations/`
- `knowledge/platform/shell/`
- `knowledge/platform/process/`
- `knowledge/platform/configuration/`
- `knowledge/languages/shell/` when the implementation is shell.

## Workflow

1. Identify the operational goal, target environment, permissions, and destructive actions.
2. Map phases: validate, plan, execute, verify, rollback, cleanup.
3. Check idempotency, retries, locking, temporary files, logs, secrets, and partial failure behavior.
4. Review environment variables, config files, working directory, and dependency assumptions.
5. Recommend safer structure with dry-run or confirmation where appropriate.
6. Verify with local dry runs, shellcheck if relevant, and failure-path checks.

## Output Format

```markdown
Operational script review:
- Goal and environment:
- Safety risks:
- Configuration/process assumptions:
- Recommended structure:
- Rollback or recovery:
- Verification:
```
