# Gin Knowledge

## Heuristics

- Keep handlers focused on HTTP binding, validation, response mapping, and context cancellation.
- Put business workflows behind interfaces owned by application packages.
- Keep middleware behavior small, ordered, and observable.
- Use Go package boundaries to separate transport, use case, domain, persistence, and integration code.

## Common Risks

- Handler functions becoming full use cases.
- Passing framework context deep into domain logic.
- Middleware ordering creating hidden security or error-handling behavior.
