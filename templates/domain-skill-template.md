# Domain Skill Template

```markdown
---
name: domain-task-name
description: Use when architecture guidance depends on a technical domain such as backend services, frontend state, databases, caches, search, or pipelines.
---

# Domain Skill Name

## When To Use

- The main decision is about domain boundaries, data flow, consistency, lifecycle, or operations.

## Domain Questions

- What owns the state or data?
- What are the read and write paths?
- What consistency guarantees are needed?
- What failure modes matter?
- What should be observable?

## Workflow

1. Identify the domain boundary.
2. Map data flow and ownership.
3. Identify consistency, latency, scale, and failure constraints.
4. Recommend the smallest architecture that fits the constraints.
5. Verify with tests, query plans, contract checks, or operational checks.

## Output Format

```markdown
Domain diagnosis:
- ...

Recommended architecture:
- ...

Tradeoffs:
- ...

Verification:
- ...
```
```
