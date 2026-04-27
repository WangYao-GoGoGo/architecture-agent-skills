# CQRS

## Use When

- Read and write models have different shape, scale, or performance needs.
- Complex queries are making the write model awkward.

## Core Idea

Command Query Responsibility Segregation separates write operations from read models. The read model may be derived, denormalized, or optimized for queries.

## Heuristics

- Use CQRS for real read/write tension, not as default layering.
- Define how read models are updated and how stale they may be.
- Keep commands focused on business intent.
- Verify query improvements justify synchronization complexity.

## Risks

- Eventual consistency surprises users.
- Duplicated models without ownership.
- More moving parts than the domain needs.

