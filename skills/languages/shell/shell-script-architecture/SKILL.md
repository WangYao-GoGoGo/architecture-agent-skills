---
name: shell-script-architecture
description: Use when reviewing or writing Bash/POSIX shell scripts, Linux automation, CI jobs, deployment scripts, cron jobs, argument parsing, idempotency, quoting, error handling, cleanup, and filesystem/process boundaries.
---

# Shell Script Architecture

## Knowledge To Use

- `knowledge/languages/shell/`
- `knowledge/platform/shell/`
- `knowledge/platform/process/`
- `knowledge/platform/configuration/`

## Workflow

1. Identify target shell: Bash, POSIX sh, zsh, or CI-specific shell.
2. Inspect arguments, environment variables, dependencies, working directory, and permissions.
3. Separate parse, validate, plan, execute, and cleanup phases.
4. Check quoting, globbing, pipeline failures, temporary files, traps, and secrets in logs.
5. Make risky workflows idempotent or add dry-run and confirmation steps.
6. Verify with shellcheck when available and focused command-path tests.

## Output Format

```markdown
Shell architecture review:
- Runtime assumptions:
- Safety risks:
- Structure changes:
- Idempotency/failure handling:
- Verification:
```
