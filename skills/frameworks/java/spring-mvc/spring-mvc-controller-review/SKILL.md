---
name: spring-mvc-controller-review
description: Use when reviewing Spring MVC controller boundaries, view resolution, interceptor chains, exception handling, validation, and request/response lifecycle.
---

# Spring MVC Controller Review

## When To Use

- The main decision is about Spring MVC controller design, request mapping, validation strategy, exception handling, or interceptor configuration.
- Reviewing view resolution, content negotiation, or response structure.

## Workflow

1. Identify the controller structure — request mappings, parameter binding, and response handling.
2. Review validation strategy — `@Valid`, custom validators, and error response structure.
3. Check exception handling — `@ControllerAdvice`, `@ExceptionHandler`, and error view resolution.
4. Review interceptor chain — logging, authentication, rate limiting, and cross-cutting concerns.
5. Check view resolution and content negotiation — JSON vs HTML, view resolvers, and message converters.
6. Review async request handling — `@Async`, `DeferredResult`, or `WebAsyncTask`.
7. Recommend the smallest structural change that improves clarity or consistency.

## Output Format

```markdown
Spring MVC review:
- Controller structure:
- Validation strategy:
- Exception handling:
- Interceptor chain:
- View resolution:
- Async handling:
- Recommended change:
- Verification:
```
