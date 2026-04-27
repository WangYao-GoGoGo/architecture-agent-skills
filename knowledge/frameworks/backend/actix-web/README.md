# Actix-web Knowledge

## Heuristics

- Keep handlers focused on HTTP binding and delegate to service modules.
- Use middleware for cross-cutting concerns; review ordering for side effects.
- Use extractors for type-safe request parsing at API boundaries.
- Keep error types consistent and implement `ResponseError` for automatic HTTP mapping.
- Wrap blocking synchronous operations in `web::block` to avoid starving the async runtime.

## Common Risks

- Handler functions owning business logic.
- Middleware ordering creating hidden behavior.
- Blocking I/O on the async runtime thread pool.
