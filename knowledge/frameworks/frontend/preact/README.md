# Preact Knowledge

## Heuristics

- Keep components focused on rendering; use hooks and signals for state management.
- Use Preact signals for fine-grained reactivity without full re-renders.
- Keep hooks focused on reusable logic; avoid hooks with unclear dependencies.
- Use `useMemo` and `useCallback` for expensive computations and callback stability.
- Keep component boundaries clear; avoid mixing data loading, business logic, and rendering.

## Common Risks

- Hooks with unclear dependencies.
- Signals used for every interaction instead of local state.
- Components owning too many concerns.
