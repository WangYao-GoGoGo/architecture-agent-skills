# React Native Knowledge

## Heuristics

- Separate UI components, state/hooks, native modules, API clients, and domain logic.
- Treat bridge/native module boundaries as architecture.
- Keep platform-specific behavior isolated.
- Make offline, permissions, navigation, and release constraints explicit.

## Common Risks

- Native modules leaking platform details everywhere.
- React state patterns copied without mobile lifecycle awareness.
- Inconsistent behavior between iOS and Android.

