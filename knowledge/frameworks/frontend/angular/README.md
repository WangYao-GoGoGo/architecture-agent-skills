# Angular Knowledge

## Heuristics

- Use modules or standalone components to express feature boundaries.
- Keep components focused on UI and delegate use cases to services.
- Treat RxJS streams as architecture: ownership, lifetime, errors, and cancellation matter.
- Keep dependency injection scopes clear.
- Avoid shared modules becoming dumping grounds.

## Common Risks

- Services with unclear ownership.
- Complex observable chains without error handling.
- Feature boundaries blurred by global shared modules.

