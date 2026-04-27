# Echo Knowledge

## Heuristics

- Keep handlers focused on HTTP binding and delegate to service packages.
- Use middleware for cross-cutting concerns; review ordering for side effects.
- Use Echo's binding and validation at API boundaries; keep domain types separate.
- Keep error handling centralized with custom HTTP error handlers.
- Avoid passing `echo.Context` into service or domain layers.

## Common Risks

- Handler functions owning business logic.
- Passing `echo.Context` deep into service layers.
- Middleware ordering creating hidden behavior.
