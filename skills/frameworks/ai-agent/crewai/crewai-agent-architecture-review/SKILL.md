---
name: crewai-agent-architecture-review
description: Use when reviewing CrewAI multi-agent architecture, agent roles, task delegation, tool integration, process flow, and collaboration patterns.
---

# CrewAI Agent Architecture Review

## When To Use

- The main decision is about CrewAI agent role design, task decomposition, tool assignment, process flow, or multi-agent collaboration.
- Reviewing agent communication, handoff patterns, or evaluation setup.

## Workflow

1. Identify the agent roles and their responsibilities — are they distinct and non-overlapping?
2. Review task decomposition — how tasks are assigned and dependencies managed.
3. Check tool assignment — which agents have access to which tools and side effects.
4. Review process flow — sequential, hierarchical, or custom orchestration.
5. Check agent communication and handoff patterns.
6. Review evaluation and traceability for multi-agent workflows.
7. Recommend the smallest structural change that improves role clarity or safety.

## Output Format

```markdown
CrewAI architecture review:
- Agent roles & responsibilities:
- Task decomposition:
- Tool assignment:
- Process flow:
- Agent communication:
- Evaluation & traces:
- Recommended change:
- Verification:
```
