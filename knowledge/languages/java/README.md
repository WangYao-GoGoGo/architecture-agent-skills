# Java Architecture Idioms

## Use When

- Reviewing packages, interfaces, dependency injection, service boundaries, or OO refactors in Java.

## Heuristics

- Use packages to express architecture boundaries.
- Prefer constructor injection for required dependencies.
- Create interfaces when there is real substitution, boundary control, or test friction.
- Keep transaction boundaries visible in application/service methods.
- Avoid mixing controllers, domain rules, persistence, and external clients in one class.

## Common Risks

- Interface per implementation without value.
- Anemic domain model plus oversized services.
- Lazy-loading surprises in domain or serialization code.
- Static global service access.

