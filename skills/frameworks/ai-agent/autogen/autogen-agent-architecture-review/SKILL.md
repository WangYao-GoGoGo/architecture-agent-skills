---
name: autogen-agent-architecture-review
description: Use when reviewing AutoGen multi-agent conversation architecture, agent roles, tool registration, termination conditions, and collaborative AI patterns.
---

# AutoGen Agent Architecture Review

## When To Use

- The main decision is about AutoGen agent role design, conversation orchestration, tool registration, termination logic, or multi-agent collaboration.
- Reviewing code execution safety, handoff patterns, or evaluation setup.

## Workflow

1. Identify the agent roles and their conversation participation patterns.
2. Review conversation orchestration — how messages flow between agents.
3. Check tool and code execution registration — safety, idempotency, and sandboxing.
4. Review termination conditions — are stop conditions reliable and observable?
5. Check agent handoff and context sharing boundaries.
6. Review evaluation and trace capture for debugging multi-agent behavior.
7. Recommend the smallest structural change that improves reliability or safety.

## Output Format

```markdown
AutoGen architecture review:
- Agent roles & participation:
- Conversation orchestration:
- Tool/code execution safety:
- Termination conditions:
- Context sharing:
- Evaluation & traces:
- Recommended change:
- Verification:
```
