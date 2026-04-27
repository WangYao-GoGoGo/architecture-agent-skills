# Kotlin Architecture Idioms

## Use When

- Reviewing Kotlin coroutine usage, sealed class hierarchies, extension functions, or multiplatform project structure.

## Heuristics

- Use `sealed class` / `sealed interface` for modeling finite state sets.
- Prefer `data class` for value objects and `data object` for singletons.
- Use coroutines for async work — prefer `flow` for streams, `suspend` for single-shot.
- Use extension functions to add behavior without modifying existing classes.
- Favor immutability — use `val` over `var`, `listOf` over `mutableListOf` by default.
- Use `context receivers` or `@DslMarker` for type-safe DSL builders.
- Keep coroutine scopes explicit — avoid `GlobalScope` in application code.
- Use `Result<T>` or custom sealed results for operation outcomes.

## Common Risks

- Coroutine cancellation not being checked in CPU-bound loops.
- Overusing `!!` (non-null assertion) instead of safe calls or `?:` elvis.
- Leaking `Job` or `CoroutineScope` in long-lived components.
- Over-engineering with advanced Kotlin features (operator overloading, infix) for simple cases.
- Platform-specific `expect`/`actual` declarations leaking into shared business logic.
