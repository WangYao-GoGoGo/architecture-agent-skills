# CQRS

## Project Fit

CQRS fits systems where reads and writes have meaningfully different models, scale, validation, or performance needs.

## Use When

- Read and write models have different shape, scale, or performance needs.
- Complex queries are making the write model awkward.
- Read models can be derived and kept acceptably fresh.

## Avoid When

- Reads and writes are simple CRUD over the same shape.
- Eventual consistency would confuse users or business rules.
- The team cannot own projection freshness and repair.

## Core Idea

Command Query Responsibility Segregation separates write operations from read models. The read model may be derived, denormalized, or optimized for queries.

## Fits Best With

- Complex reporting, search/list screens, high-read systems, event-driven projections.

## Heuristics

- Use CQRS for real read/write tension, not as default layering.
- Define how read models are updated and how stale they may be.
- Keep commands focused on business intent.
- Verify query improvements justify synchronization complexity.

## Risks

- Eventual consistency surprises users.
- Duplicated models without ownership.
- More moving parts than the domain needs.

## Verification

- Read model freshness is measured or bounded.
- Commands protect write-side invariants.
- Query complexity actually decreases.
