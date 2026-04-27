# Qwik Knowledge

## Heuristics

- Design components for resumability; use `$` suffixes to mark lazy-loadable boundaries.
- Keep stores serializable; avoid storing functions or non-serializable values in stores.
- Use `routeLoader$` and `routeAction$` for server-side data loading and mutations.
- Keep serialization boundaries explicit; only pass serializable data across client/server boundaries.
- Use `useResource$` for async data with proper caching and invalidation.

## Common Risks

- Missing `$` suffixes on lazy boundaries.
- Non-serializable data crossing client/server boundaries.
- Components that are not designed for resumability.
