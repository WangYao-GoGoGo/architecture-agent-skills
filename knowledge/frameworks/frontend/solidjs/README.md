# Solid.js Knowledge

## Heuristics

- Keep components focused on rendering; use signals and stores for state management.
- Use `createSignal` for local state, `createStore` for complex nested state, and context for shared state.
- Keep effects for synchronization with outside systems, not general control flow.
- Use `createMemo` for derived computations to avoid unnecessary recalculations.
- Use `createResource` for async data fetching with proper loading and error states.

## Common Risks

- Effects with unclear dependencies.
- Global signals used for temporary local state.
- Components mixing data fetching, business logic, and rendering.
