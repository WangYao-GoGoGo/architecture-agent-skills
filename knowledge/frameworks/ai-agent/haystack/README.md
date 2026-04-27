# Haystack Knowledge

## Heuristics

- Separate pipeline components, document stores, retrievers, readers/generators, and evaluation.
- Keep custom component contracts small and testable.
- Treat document store schema and indexing strategy as architecture.
- Add evaluation for retrieval and generation quality.

## Common Risks

- Pipeline components with hidden side effects.
- Document store schema changes breaking existing indexes.
- Retrieval quality not evaluated with representative queries.
