# Svelte Knowledge

## Heuristics

- Keep component state local unless sharing is needed.
- Use stores for cross-component state with clear ownership.
- Keep reactive statements simple and side effects explicit.
- Separate API clients and domain transformations from components.

## Common Risks

- Reactive declarations hiding expensive or side-effecting work.
- Stores becoming global state dumps.
- Components mixing data loading and business logic.

