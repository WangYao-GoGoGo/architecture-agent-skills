# FastAPI Knowledge

## Heuristics

- Keep routers thin and delegate use cases to application modules.
- Treat Pydantic schemas as API contracts, not automatically domain models.
- Keep dependency injection explicit and testable.
- Separate async I/O boundaries from pure logic.
- Review startup/shutdown lifecycle for clients, pools, and background tasks.

## Common Risks

- Domain logic inside route handlers.
- Pydantic models leaking through every layer.
- Async functions hiding blocking I/O.

