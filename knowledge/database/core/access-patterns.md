# Access Patterns

## Use When

- Designing schemas, documents, keys, indexes, caches, or search indexes.
- Choosing between normalization, denormalization, embedding, references, or materialized views.

## Core Idea

Data architecture should start from how data is read, written, updated, deleted, and retained. A model that looks clean but fights the access pattern will produce slow queries, awkward caches, or inconsistent writes.

## Agent Heuristics

- List read paths and write paths before proposing a model.
- Identify the source of truth before adding derived copies.
- Optimize for the most important access paths, not every possible query.
- For denormalized data, name the update path and stale-data risk.
- For high-volume systems, check partition keys, hot keys, and retention.

## Verification

- Critical reads can be expressed simply.
- Writes preserve required invariants.
- Indexes or keys match filters and sort order.
- Migration and backfill paths are clear.

