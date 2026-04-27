# AutoGen Knowledge

## Heuristics

- Separate conversation orchestration, agent roles, tools, termination rules, and evaluation.
- Keep code execution and external side effects behind explicit policies.
- Design handoff points and retry behavior as workflow contracts.
- Capture traces for debugging multi-agent behavior.

## Common Risks

- Conversation loops without reliable stop conditions.
- Agents sharing too much mutable context.
- Tool calls that are hard to reproduce or verify.
