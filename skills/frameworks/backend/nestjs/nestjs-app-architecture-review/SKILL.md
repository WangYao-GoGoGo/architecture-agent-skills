---
name: nestjs-app-architecture-review
description: Use when reviewing NestJS application architecture, module boundaries, dependency injection, decorator usage, guards, interceptors, pipes, and filters.
---

# NestJS App Architecture Review

## When To Use

- The main decision is about NestJS module organization, dependency injection scope, decorator usage, or boundary mechanisms.
- Reviewing circular dependencies, provider responsibilities, or guard/interceptor/filter placement.

## Workflow

1. Identify module boundaries — do modules express capability domains or technical layers?
2. Review dependency injection — are providers scoped correctly and are circular dependencies present?
3. Check decorator usage — are decorators used for cross-cutting concerns or leaking into domain logic?
4. Review guards, interceptors, pipes, and filters — are they placed at appropriate boundaries?
5. Check controller responsibilities — are they transport-focused or owning business logic?
6. Review module imports and shared modules for unintended coupling.
7. Recommend the smallest change that clarifies module boundaries.

## Output Format

```markdown
NestJS architecture review:
- Module boundaries:
- Dependency injection:
- Decorator usage:
- Guards/Interceptors/Pipes/Filters:
- Controller responsibilities:
- Module coupling:
- Recommended change:
- Verification:
```
