---
name: tornado-app-architecture-review
description: Use when reviewing Tornado application architecture, async request handling, routing, coroutine design, WebSocket support, and application structure.
---

# Tornado App Architecture Review

## When To Use

- The main decision is about Tornado project structure, async handler design, coroutine boundaries, or WebSocket event handling.
- Reviewing non-blocking I/O patterns or application lifecycle management.

## Workflow

1. Identify project structure — are handlers, services, and domain separated?
2. Review handler responsibilities — do handlers handle HTTP or also business logic?
3. Check coroutine design — are async functions used consistently and blocking calls avoided?
4. Review WebSocket handler design — are open/close/message events handled cleanly?
5. Check non-blocking I/O — are all I/O operations async or wrapped in thread pools?
6. Review application lifecycle — are startup/shutdown hooks managing resources?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Tornado architecture review:
- Project structure:
- Handler responsibilities:
- Coroutine design:
- WebSocket handling:
- Non-blocking I/O:
- Lifecycle management:
- Recommended change:
- Verification:
```
