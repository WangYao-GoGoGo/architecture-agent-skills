# Shell Script Architecture Idioms

## Use When

- Reviewing Bash, POSIX sh, CI scripts, deployment scripts, cron jobs, or Linux automation.

## Heuristics

- Separate argument parsing, validation, core workflow, and side-effecting commands.
- Prefer small functions with explicit inputs over long linear scripts.
- Use strict mode carefully; understand how `set -e` behaves with conditionals and pipelines.
- Quote variables unless word splitting is intended.
- Make scripts idempotent when used for deployment or operations.
- Log commands and failure context without leaking secrets.

## Common Risks

- Hidden dependency on current working directory.
- Unsafe globbing, word splitting, or unquoted paths.
- Partial changes after failure.
- Script behavior that differs between Bash and POSIX sh.

