# Sanic Knowledge

## Heuristics

- Keep handlers focused on HTTP coordination and delegate to service modules.
- Organize blueprints by domain for clear feature boundaries.
- Use middleware for cross-cutting concerns; review ordering for side effects.
- Wrap blocking I/O in `loop.run_in_executor` to avoid blocking the async event loop.
- Use `app.add_task` for background tasks with proper error handling and cancellation.

## Common Risks

- Handler functions owning business logic.
- Blocking I/O on the async event loop.
- Blueprints that are too large or too fragmented.
