---
name: fastapi-app-architecture-review
description: Use when reviewing FastAPI application architecture, route design, dependency injection, Pydantic schemas, async boundaries, and background tasks.
---

# FastAPI App Architecture Review

## When To Use

- The main decision is about FastAPI project structure, route organization, dependency injection, or async I/O boundaries.
- Reviewing Pydantic schema design, background task management, or startup/shutdown lifecycle.

## Workflow

1. Identify route organization — are routers grouped by domain or by CRUD?
2. Review dependency injection usage — are dependencies scoped correctly (request, session, global)?
3. Check Pydantic schema boundaries — are schemas used as API contracts or leaking into domain layers?
4. Review async boundaries — are blocking I/O calls wrapped in proper thread pools?
5. Check startup/shutdown lifecycle for clients, connection pools, and background tasks.
6. Review error handling and validation at API boundaries.
7. Recommend the smallest change that improves separation of concerns.

## Output Format

```markdown
FastAPI architecture review:
- Route organization:
- Dependency injection:
- Pydantic schema boundaries:
- Async I/O boundaries:
- Lifecycle management:
- Error handling:
- Recommended change:
- Verification:
```
