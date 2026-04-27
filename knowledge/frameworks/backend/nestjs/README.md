# NestJS Knowledge

## Heuristics

- Use modules to express capability boundaries, not just technical folders.
- Keep controllers transport-focused and providers/use cases focused.
- Avoid overusing decorators as a substitute for clear ownership.
- Make dependency injection and module imports visible.
- Review guards, interceptors, pipes, and filters as boundary mechanisms.

## Common Risks

- Circular module dependencies.
- Anemic providers with all logic in controllers.
- Framework decorators leaking into domain code unnecessarily.

