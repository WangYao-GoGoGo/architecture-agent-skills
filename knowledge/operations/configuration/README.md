# Configuration Boundaries

## Use When

- Reviewing environment variables, config files, feature flags, secrets, or deployment settings.

## Heuristics

- Separate configuration from code, but validate it at startup or script entry.
- Keep secrets out of logs, examples, and generated reports.
- Define defaults only when safe.
- Prefer typed or schema-validated configuration for applications.
- Keep feature flag ownership and cleanup plans explicit.

## Common Risks

- Silent fallback to unsafe defaults.
- Environment-specific behavior hidden in scripts.
- Long-lived feature flags becoming permanent architecture.

