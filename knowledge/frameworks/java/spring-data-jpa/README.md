# Spring Data JPA Knowledge

## Heuristics

- Use repositories for persistence boundaries, not as a place for domain policy.
- Review derived query names for readability and performance.
- Keep pagination, sorting, and transaction boundaries explicit.
- Avoid leaking entities into public API contracts by default.

