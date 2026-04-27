# Document Databases

## Use When

- Reviewing document schemas, embedding, references, aggregates, update consistency, and document growth.

## Heuristics

- Embed data read and updated together.
- Reference data with independent lifecycle or high update frequency.
- Keep document growth bounded.
- Index fields that match critical queries.
- Name duplication and stale-data risks explicitly.

## Common Risks

- Relational modeling copied into documents without aggregate thinking.
- Large unbounded arrays inside documents.
- Duplicated data without update ownership.
- Aggregation pipelines carrying too much business policy.

