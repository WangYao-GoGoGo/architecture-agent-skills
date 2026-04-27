# CrewAI Knowledge

## Heuristics

- Separate agents, tasks, tools, memory, retrieval, and evaluation cases.
- Keep tool side effects explicit and idempotent where possible.
- Treat role prompts and task delegation as architecture, not only prompt text.
- Add traces and representative task tests for important workflows.

## Common Risks

- Agents with overlapping responsibilities.
- Tool access that bypasses policy, permissions, or audit needs.
- Success judged only by fluent output rather than task evidence.
