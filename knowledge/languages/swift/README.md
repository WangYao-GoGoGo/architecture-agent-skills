# Swift Architecture Idioms

## Use When

- Reviewing Swift protocol design, value type usage, async/await patterns, or SwiftUI architecture.

## Heuristics

- Prefer value types (`struct`) by default; use `class` only when identity or reference semantics are needed.
- Use protocols with associated types for generic, reusable abstractions.
- Leverage `Result` type for explicit error handling in async contexts.
- Use `@MainActor` for UI-bound work and custom actors for state isolation.
- Prefer `Codable` for serialization — avoid manual JSON parsing.
- Use property wrappers (`@State`, `@Binding`, `@ObservedObject`, `@EnvironmentObject`) intentionally.
- Keep views small and composable — extract sub-views for clarity.
- Use `enum` for modeling state machines and option sets.

## Common Risks

- Reference cycles from strong closures capturing `self` without `[weak self]`.
- Over-engineering with complex protocol hierarchies before concrete usage.
- Mixing UIKit and SwiftUI lifecycle patterns without clear boundaries.
- Force unwrapping (`!`) in production code.
- Overuse of `@Published` properties causing unnecessary view re-renders.
