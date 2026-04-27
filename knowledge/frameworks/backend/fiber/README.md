# Fiber Knowledge

## Heuristics

- Keep handlers focused on HTTP binding and delegate to service packages.
- Use middleware for cross-cutting concerns; review ordering for side effects.
- Use Fiber's `Ctx` methods for request parsing and response writing; avoid passing `Ctx` to service layers.
- Keep error handling centralized with custom error handlers.
- Use schema validation at API boundaries with go-playground/validator or similar.

## Common Risks

- Handler functions owning business logic.
- Passing `fiber.Ctx` deep into service layers.
- Middleware ordering creating hidden security or error-handling behavior.
