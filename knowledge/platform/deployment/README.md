# Deployment And Rollback

## Use When

- Reviewing deployment scripts, release workflows, migration rollouts, or production changes.

## Heuristics

- Separate deploy, verify, rollback, and cleanup phases.
- Make health checks explicit.
- Keep database migrations compatible with rolling deploys.
- Define rollback or forward-fix behavior before release.
- Avoid hidden destructive steps in deploy scripts.

## Common Risks

- Code deploy and schema contract change shipped in the wrong order.
- Rollback path not tested.
- Secrets or environment assumptions hidden in CI.
- No verification after deployment.

