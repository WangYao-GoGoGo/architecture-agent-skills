# Architecture Decision Review

Reviews or documents architecture decisions, tradeoffs, alternatives, consequences, and verification signals.

## When To Use This Skill

- A significant architecture decision needs to be documented or reviewed.
- The team needs to choose between competing approaches (e.g., monolith vs microservices, sync vs async).
- An existing decision needs retrospective analysis.
- The decision has broad impact across multiple modules, services, or teams.

## How It Works

1. **Capture context**: what problem is being solved, what constraints exist.
2. **State the decision**: what was chosen and why.
3. **Document alternatives**: what was considered and why each was rejected.
4. **List consequences**: positive and negative tradeoffs.
5. **Define verification**: how to tell if the decision is working or needs revisiting.

## Knowledge Used

- [`knowledge/architecture/decision-governance/`](../../knowledge/architecture/decision-governance/README.md) — ADR structure, RFC process, fitness functions.
- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — when the decision involves application structure.
- [`knowledge/architecture/distributed-systems/`](../../knowledge/architecture/distributed-systems/README.md) — when the decision involves service boundaries or deployment.
- [`knowledge/architecture/integration-patterns/`](../../knowledge/architecture/integration-patterns/README.md) — when the decision involves communication between components.

## Output

An architecture decision record or review:

```markdown
## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[Problem, constraints, and forces]

## Decision
[What was chosen]

## Alternatives Considered
[Other options and why they were rejected]

## Consequences
[Positive and negative tradeoffs]

## Verification
[How to validate the decision]
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — for designing new features with explicit architecture.
- [`dependency-boundary-review`](../dependency-boundary-review/README.md) — for reviewing dependency direction between modules.
