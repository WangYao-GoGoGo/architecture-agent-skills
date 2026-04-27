# Alpine.js Knowledge

## Heuristics

- Keep components focused on UI interactions; use `x-data` for local state.
- Use `x-init` for initialization logic; avoid complex logic in `x-init` expressions.
- Use Alpine stores for shared cross-component state; keep stores scoped by domain.
- Use `x-effect` for side effects with clear dependencies.
- Keep API calls in `x-init` or triggered by user interactions; avoid automatic data loading.

## Common Risks

- Components owning too much logic.
- Stores becoming global dumping grounds.
- Complex expressions in HTML attributes.
