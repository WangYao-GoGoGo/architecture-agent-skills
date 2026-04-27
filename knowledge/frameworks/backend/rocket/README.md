# Rocket Knowledge

## Heuristics

- Keep route handlers focused on HTTP binding and delegate to service modules.
- Use request guards for cross-cutting concerns like authentication and validation.
- Keep data types at API boundaries separate from domain types.
- Implement `Responder` for consistent error-to-HTTP-response mapping.
- Keep templates presentation-only; move logic to helpers or service modules.

## Common Risks

- Route handlers owning business logic.
- Request guards with side effects beyond their concern.
- Data types leaking from API into domain layers.
