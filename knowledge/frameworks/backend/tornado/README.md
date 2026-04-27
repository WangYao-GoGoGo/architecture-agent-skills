# Tornado Knowledge

## Heuristics

- Keep request handlers focused on HTTP coordination and delegate to service modules.
- Use `async`/`await` consistently; avoid mixing sync and async code in the same call chain.
- Use `IOLoop.add_callback` and `IOLoop.spawn_callback` for background tasks with clear error handling.
- Keep WebSocket handlers focused on connection lifecycle; delegate business logic to services.
- Wrap blocking I/O in `IOLoop.run_in_executor` to avoid blocking the event loop.

## Common Risks

- Handler functions owning business logic.
- Blocking I/O on the event loop.
- Unhandled exceptions in async callbacks.
