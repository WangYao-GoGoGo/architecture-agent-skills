# Express Knowledge

## Heuristics

- Keep middleware, routing, validation, use cases, and persistence separate.
- Make async error handling explicit.
- Treat request/response objects as transport details.
- Avoid broad shared utility modules for business logic.
- Use schema validation at API boundaries.

## Common Risks

- Business logic inside route handlers.
- Middleware order causing hidden behavior.
- Unhandled promise errors or inconsistent error contracts.

