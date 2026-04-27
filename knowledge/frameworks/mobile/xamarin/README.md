# Xamarin Knowledge

## Heuristics

- Separate shared UI, platform-specific code, MVVM pattern, and native API access.
- Keep platform-specific implementations behind abstraction boundaries.
- Treat dependency injection, navigation, and lifecycle as architecture.
- Add proper handling for permissions, offline mode, and background execution.

## Common Risks

- Platform-specific code leaking into shared logic.
- Xamarin.Forms abstraction limiting native capabilities.
- Lifecycle events not handled for state preservation.
