# Frontend Architecture Knowledge

## Heuristics

- Separate page, feature, shared, and primitive component responsibilities.
- Distinguish local UI state, server state, derived state, and global app state.
- Keep data fetching and side effects at predictable boundaries.
- Avoid over-generic components before repeated use cases exist.
- Treat accessibility, loading, empty, and error states as part of component architecture.

## Common Risks

- Prop drilling that hides ownership issues.
- Global state used for temporary local UI state.
- Components mixing rendering, data fetching, business policy, and formatting.
- Backend data shapes leaking directly into every component.

