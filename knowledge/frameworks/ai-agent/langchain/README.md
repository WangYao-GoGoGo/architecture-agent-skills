# LangChain Knowledge

## Heuristics

- Separate prompt design, tool definitions, retrieval, orchestration, and evaluation.
- Keep chains/graphs small enough to inspect.
- Treat tool side effects and credentials as architecture boundaries.
- Add tracing and test cases for important workflows.

## Common Risks

- Hidden behavior across nested chains.
- Tool calls without safety or idempotency.
- Retrieval quality not evaluated.

