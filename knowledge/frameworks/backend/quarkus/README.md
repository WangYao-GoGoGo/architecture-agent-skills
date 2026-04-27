# Quarkus Knowledge

## Heuristics

- Keep REST endpoints focused on HTTP transport and delegate to CDI service beans.
- Use reactive messaging for event-driven boundaries; organize channels by domain.
- Keep Panache entities focused on persistence; use separate domain objects for complex logic.
- Use Quarkus extensions deliberately; each extension adds build-time processing.
- Plan for native-image: avoid runtime reflection, dynamic proxies, and unbounded serialization.

## Common Risks

- REST endpoints owning business logic.
- Panache entities leaking into API contracts.
- Runtime reflection breaking native-image compilation.
