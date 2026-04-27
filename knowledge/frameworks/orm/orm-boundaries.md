# ORM Boundaries

## Core Idea

ORMs simplify persistence, but entity lifecycle, lazy loading, transactions, and generated clients can leak persistence concerns into the whole application.

## Heuristics

- Keep transaction scope explicit.
- Avoid lazy-loading surprises in serialization, logging, or domain methods.
- Keep domain decisions from depending on persistence side effects.
- Use repositories or query services when they reduce coupling, not by habit.
- Review N+1 queries and cascading writes.

## Common Risks

- ORM entities used as public API contracts.
- Query performance hidden behind innocent property access.
- Migrations generated without human review.

