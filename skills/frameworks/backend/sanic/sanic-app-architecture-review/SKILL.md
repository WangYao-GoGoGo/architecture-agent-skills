---
name: sanic-app-architecture-review
description: Use when reviewing Sanic application architecture, async request handling, routing, blueprints, middleware, and application structure.
---

# Sanic App Architecture Review

## When To Use

- The main decision is about Sanic project structure, blueprint organization, async handler design, or middleware pipeline.
- Reviewing application factory pattern or background task management.

## Workflow

1. Identify project structure — are blueprints, handlers, services, and domain separated?
2. Review blueprint organization — do blueprints follow domain boundaries?
3. Check handler responsibilities — do handlers handle HTTP or also business logic?
4. Review middleware pipeline — is ordering logical and are side effects visible?
5. Check async boundaries — are blocking operations wrapped in appropriate executors?
6. Review background task management — are tasks properly started and stopped?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Sanic architecture review:
- Project structure:
- Blueprint organization:
- Handler responsibilities:
- Middleware pipeline:
- Async boundaries:
- Background tasks:
- Recommended change:
- Verification:
```
