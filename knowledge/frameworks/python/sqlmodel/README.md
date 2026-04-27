# SQLModel Knowledge

## Heuristics

- Keep model definitions aligned with both Pydantic validation and SQLAlchemy mapping.
- Review session management and transaction boundaries.
- Treat FastAPI integration points as architecture contracts.
- Use model inheritance carefully to avoid mapping conflicts.

## Common Risks

- Model definitions mixing validation and persistence concerns.
- Session lifecycle not aligned with request boundaries.
- Inheritance hierarchies causing unexpected table mappings.
