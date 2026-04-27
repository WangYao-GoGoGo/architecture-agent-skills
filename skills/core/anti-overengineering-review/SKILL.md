---
name: anti-overengineering-review
description: Use when a proposed architecture, design pattern, abstraction, framework, cache, service split, or refactor may be more complex than the current problem needs.
---

# Anti-Overengineering Review

Use this skill to keep architecture practical. The goal is not to reject design, but to make sure each abstraction pays rent.

## When To Use

- A solution introduces many new classes, layers, services, factories, interfaces, queues, caches, or frameworks.
- A pattern is proposed before the variation point is clear.
- The user asks whether a design is too complex.
- A simple feature is becoming a framework.

## Workflow

1. State the current problem and known future change.
2. List the new abstractions or moving parts.
3. Ask what each abstraction protects from.
4. Remove or defer abstractions that do not address current pain.
5. Keep explicit extension points only where change is likely or costly.
6. Recommend the simplest design that can evolve.

## Decision Rules

- One implementation usually does not need an interface unless tests, plugins, or boundaries require it.
- Two branches do not automatically justify Strategy.
- A cache is not free; include invalidation and consistency rules.
- A service split is not free; include network, ownership, deployment, and observability costs.
- A generic framework is suspicious if only one use case exists.

## Output Format

```markdown
Overengineering review:
- Current problem:
- Proposed complexity:
- Keep:
- Defer or remove:
- Simpler design:
- What would justify adding it later:
```
