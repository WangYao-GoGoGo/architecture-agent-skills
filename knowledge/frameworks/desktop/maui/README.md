# .NET MAUI Knowledge

## Heuristics

- Separate page/shell structure, MVVM pattern, data binding, and platform-specific code.
- Keep platform-specific implementations behind abstractions.
- Treat navigation, dependency injection, and resource management as architecture.
- Add proper lifecycle handling for page and app states.

## Common Risks

- Platform-specific code leaking into shared UI logic.
- Data binding without proper change notification.
- Lifecycle events not handled for state preservation.
