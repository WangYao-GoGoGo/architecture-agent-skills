# Linux Shell Architecture

## Use When

- Reviewing shell scripts, CI tasks, deployment commands, maintenance jobs, or local automation.

## Heuristics

- Define shell: Bash-specific or POSIX sh.
- Validate required commands, files, environment variables, and permissions.
- Separate parse, validate, plan, execute, and cleanup phases.
- Use traps for cleanup when temporary files or locks are involved.
- Prefer explicit dry-run support for risky operations.

## Verification

- Script handles missing dependencies.
- Paths with spaces are safe.
- Failure halfway through leaves a recoverable state.
- Logs explain what happened without exposing secrets.

