# Duplicated Logic

## Use When

- The same rule, workflow, query condition, validation, or mapping appears in multiple places.

## Why It Hurts

- Fixes are applied inconsistently.
- Behavior diverges silently.
- Tests miss one of the copies.

## Refactoring Moves

- Extract shared policy when the duplication represents the same concept.
- Keep duplication when two similar snippets are likely to evolve differently.
- For queries, centralize reusable predicates carefully without hiding performance costs.

## Verification

- Callers share one source of truth for the rule.
- The extracted name describes the domain concept, not just the code shape.
