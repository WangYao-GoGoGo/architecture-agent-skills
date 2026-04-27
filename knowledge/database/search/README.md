# Search Systems

## Use When

- Reviewing full-text search, filters, ranking, facets, autocomplete, or search indexes.

## Heuristics

- Separate source-of-truth data from search indexes.
- Define freshness requirements.
- Design mappings/analyzers from query behavior.
- Keep filters and sorting supported by index structure.
- Evaluate relevance with example queries, not only latency.

## Common Risks

- Search index treated as the only source of truth.
- No reindexing strategy.
- Relevance changes without regression examples.
- Metadata filters added after indexing without mapping support.

