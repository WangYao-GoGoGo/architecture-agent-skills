# Architecture Decision Review Knowledge

## Use When

Evaluating or documenting an architecture decision with meaningful long-term consequences — pattern choice, service boundary, database choice, cache strategy, framework adoption, or refactoring direction.

## Heuristics

- State the decision in one sentence before analyzing alternatives.
- Capture context and constraints that are true today and likely to remain true.
- Compare at least two realistic alternatives; the "do nothing" option is always valid.
- Name consequences explicitly, including operational cost, migration effort, and reversibility.
- Define concrete verification signals that would confirm the decision was correct.
- Prefer decisions that can be reversed or migrated incrementally.
- Keep ADRs short: context, decision, consequences, verification, revisit trigger.

## Common Risks

- Alternatives are straw-man versions that make the preferred choice look better.
- Costs are hidden or deferred (e.g., "we'll fix it in production").
- Ownership is unclear after the decision is made.
- No revisit trigger is defined, so the decision becomes permanent by neglect.
