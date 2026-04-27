# Operations Architecture Knowledge

## Heuristics

- Treat scripts, config, deployment, monitoring, and rollback as architecture surfaces.
- Make environment dependencies explicit.
- Prefer idempotent operational workflows.
- Separate dry-run, validation, execution, and cleanup steps.
- Do not hide destructive actions behind vague function names.

## Common Risks

- Manual-only rollback paths.
- Scripts that assume one machine, one user, or one current directory.
- Secrets in logs or command history.
- Missing health checks after deployment.

