---
name: architecture-decision-review
description: Use when evaluating or documenting an architecture decision, including pattern choice, service boundary, database choice, cache strategy, frontend state model, framework adoption, or refactoring direction.
---

# Architecture Decision Review

Use this skill when a decision has meaningful long-term consequences.

## When To Use

- Choosing between architecture patterns or design patterns.
- Introducing a framework, database, cache, message queue, or service boundary.
- Changing a public API, schema, module boundary, or deployment shape.
- Writing or reviewing an ADR.

## Knowledge To Use

- `knowledge/architecture/decision-governance/` for ADR and fitness-function guidance.
- `knowledge/architecture/application-styles/` for in-process architecture choices.
- `knowledge/architecture/distributed-systems/` for service/deployment choices.
- `knowledge/architecture/integration-patterns/` for event, CQRS, saga, outbox, API gateway, and BFF choices.
- `knowledge/data-systems/`, `knowledge/api/`, or `knowledge/frameworks/` when the decision touches those areas.

## Workflow

1. State the decision in one sentence.
2. Capture context and constraints.
3. Compare realistic alternatives.
4. Name consequences, including operational and migration costs.
5. Define verification signals.
6. Recommend accept, revise, or reject.

## Review Criteria

- Does the decision solve a current or credible near-term problem?
- Are alternatives represented fairly?
- Are costs named, not hidden?
- Is ownership clear?
- Can the decision be reversed or migrated later?
- Are verification signals concrete?

## Output Format

```markdown
Decision review:
- Decision:
- Context:
- Alternatives:
- Recommendation:
- Consequences:
- Verification:
- Revisit trigger:
```
