# Process And Filesystem Boundaries

## Use When

- Reviewing scripts or services that spawn processes, read/write files, manage locks, or depend on filesystem layout.

## Heuristics

- Make working directory assumptions explicit.
- Use temporary directories safely.
- Avoid race-prone lock files unless locking semantics are clear.
- Check process exit codes and stderr.
- Keep file ownership, permissions, and cleanup visible.

## Common Risks

- Relative paths that fail under cron or CI.
- Ignored subprocess failures.
- Partial writes without atomic rename.
- Permission assumptions that differ across environments.

