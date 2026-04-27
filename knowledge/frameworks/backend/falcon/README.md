# Falcon Knowledge

## Heuristics

- Keep resource classes focused on HTTP method handling and delegate to service modules.
- Use hooks for cross-cutting concerns like authentication, validation, and caching.
- Keep middleware focused on request/response pipeline concerns; avoid business logic.
- Use custom error handlers for consistent error-to-HTTP-response mapping.
- Handle content negotiation explicitly at the resource or middleware level.

## Common Risks

- Resource classes owning business logic.
- Hooks with side effects beyond their concern.
- Error responses that are inconsistent across resources.
