# Spring Boot Knowledge

## Heuristics

- Keep controllers focused on HTTP transport.
- Keep application services responsible for use-case orchestration.
- Keep domain logic independent from Spring annotations where practical.
- Make transaction boundaries explicit.
- Review configuration, profiles, auto-configuration, and bean lifecycle as architecture concerns.

## Common Risks

- Fat services that own validation, domain policy, persistence, and integration.
- Entities leaking into API contracts.
- Hidden behavior through annotations or auto-configuration.

