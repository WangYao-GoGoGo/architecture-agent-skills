# Graph Databases

## Use When

- Reviewing node and relationship models, traversals, graph queries, and relationship-heavy domains.

## Heuristics

- Use graph models when relationships and traversals are first-class.
- Make relationship direction, cardinality, and properties explicit.
- Index entry-point nodes.
- Keep traversal depth and fanout under control.
- Avoid graph databases when joins are simple and relational access is enough.

## Common Risks

- Treating graph as a novelty instead of solving traversal problems.
- Unbounded traversals.
- Missing uniqueness rules for relationships.

