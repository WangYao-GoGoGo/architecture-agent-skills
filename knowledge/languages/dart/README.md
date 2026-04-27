# Dart Architecture Idioms

## Use When

- Reviewing Dart null safety usage, async patterns, stream handling, or Flutter widget architecture.

## Heuristics

- Leverage sound null safety — use `?` for nullable, `late` for deferred initialization.
- Use `async`/`await` for asynchronous operations — prefer `Stream` for event sequences.
- Use extension methods to add functionality to existing types without modification.
- Keep widgets small and focused — extract reusable widget methods or classes.
- Use `const` constructors wherever possible for performance.
- Prefer `sealed class` (Dart 3+) for union types and state modeling.
- Use `freezed` for immutable data classes with copy semantics.
- Organize code by feature, not by type (don't mix models, services, widgets across features).

## Common Risks

- Overusing `dynamic` type instead of proper type annotations.
- Deep widget build methods that should be extracted.
- Memory leaks from not canceling `StreamSubscription` in `dispose`.
- Using `BuildContext` across async gaps without checking `mounted`.
- Over-relying on `GlobalKey` instead of proper state management.
