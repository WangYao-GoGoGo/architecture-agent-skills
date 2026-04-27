---
name: play-app-architecture-review
description: Use when reviewing Play Framework application architecture, action composition, routing, template engine, async handling, and dependency injection.
---

# Play App Architecture Review

## When To Use

- The main decision is about Play Framework project structure, action composition, routing, or async request handling.
- Reviewing template engine usage, dependency injection, or module organization.

## Workflow

1. Identify project structure — are controllers, services, and domain layers separated?
2. Review action composition — are actions handling cross-cutting concerns or business logic?
3. Check routing organization — are routes grouped by domain?
4. Review async handling — are blocking operations wrapped in appropriate execution contexts?
5. Check dependency injection (Guice) — are bindings explicit and scoped correctly?
6. Review template engine usage — are templates presentation-only or owning logic?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Play architecture review:
- Project structure:
- Action composition:
- Routing:
- Async handling:
- Dependency injection:
- Template usage:
- Recommended change:
- Verification:
```
