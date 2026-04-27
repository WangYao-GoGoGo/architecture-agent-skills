# Axum Knowledge

## Heuristics

- Keep handlers focused on HTTP binding and delegate to service modules.
- Use extractors for type-safe request parsing; implement custom extractors for shared patterns.
- Compose middleware using tower layers; review ordering for side effects.
- Use unified error types that implement `IntoResponse` for consistent error contracts.
- Wrap blocking operations in `tokio::task::spawn_blocking` to avoid starving the async runtime.

## Common Risks

- Handler functions owning business logic.
- Middleware ordering creating hidden behavior.
- Blocking I/O on the async runtime.
