# Go Architecture Idioms

## Use When

- Reviewing Go packages, interfaces, goroutine usage, error handling, or concurrency patterns.

## Heuristics

- Use packages to enforce dependency direction — avoid circular imports.
- Accept interfaces, return structs.
- Use `error` as a value, not an exception — handle errors explicitly.
- Prefer composition over inheritance (Go has no classes).
- Use goroutines and channels for concurrency; avoid shared memory when possible.
- Keep `main` packages thin — move logic into library packages.
- Use `context.Context` for cancellation, deadlines, and request-scoped values.
- Favor small interfaces (1-2 methods) for maximum composability.

## Common Risks

- Overusing `interface{}` / `any` instead of concrete types.
- Goroutine leaks from missing cancellation or channel cleanup.
- Deep package hierarchies that create import cycles.
- Ignoring errors with `_` instead of handling them.
- Over-engineering with channels when a mutex would suffice.
