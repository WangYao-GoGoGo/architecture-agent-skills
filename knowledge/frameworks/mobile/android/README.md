# Android Knowledge

## Heuristics

- Separate UI, view model/state, domain/use cases, and data sources.
- Treat lifecycle, permissions, background work, and offline behavior as architecture.
- Keep platform APIs at boundaries where possible.
- Use dependency injection and repositories only where they reduce coupling.

## Common Risks

- Activity or Fragment owning too much workflow logic.
- Lifecycle leaks.
- Offline and permission paths handled inconsistently.

