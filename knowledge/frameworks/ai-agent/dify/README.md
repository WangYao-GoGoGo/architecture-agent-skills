# Dify Knowledge

## Heuristics

- Separate application design, RAG pipeline, agent workflow, tool integration, and evaluation.
- Keep tool definitions and API key management explicit.
- Treat knowledge base chunking and retrieval as architecture.
- Add monitoring for cost, latency, and quality.

## Common Risks

- Overly complex agent workflows hard to debug.
- Tool credentials exposed or poorly scoped.
- Retrieval quality not validated against real user queries.
