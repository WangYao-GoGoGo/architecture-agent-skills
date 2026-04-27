# Ktor Knowledge

## Heuristics

- Keep routes focused on HTTP transport and delegate use cases to application modules.
- Use plugins for cross-cutting concerns; review plugin ordering for side effects.
- Treat content negotiation and serialization as API contract boundaries.
- Keep suspending functions in the application layer; domain logic should be pure where possible.
- Use Ktor Client as a separate module with its own pipeline and serialization config.

## Common Risks

- Route handlers owning business logic.
- Plugin ordering creating hidden behavior.
- Serialization config leaking into domain types.
