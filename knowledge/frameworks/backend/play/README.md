# Play Framework Knowledge

## Heuristics

- Keep controllers focused on HTTP coordination and delegate to service layers.
- Use action composition for cross-cutting concerns like auth and logging.
- Wrap blocking operations in custom execution contexts to avoid starving the Play thread pool.
- Keep templates presentation-only; move logic to helpers or services.
- Make Guice module bindings explicit and review for circular dependencies.

## Common Risks

- Controllers owning business logic.
- Blocking operations on the default execution context.
- Templates with embedded business logic.
