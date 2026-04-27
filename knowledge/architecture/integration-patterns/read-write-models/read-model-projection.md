# Read Model Projection

## Project Fit

Read model projections fit systems that derive query-optimized views from write-side events or state changes.

## Use When

- Query shape differs from write model.
- A UI, report, search page, or API needs denormalized data.
- The system can tolerate bounded staleness.

## Avoid When

- A direct query with proper indexes is enough.
- Stale data would break business correctness.
- Projection repair and rebuild are not planned.

## Core Idea

A projection consumes changes and builds a read model optimized for specific queries.

## Fits Best With

- CQRS, event-driven systems, search indexes, reporting views, materialized views.

## Verification

- Projection can be rebuilt.
- Lag and failures are observable.
- Source-of-truth ownership remains clear.
