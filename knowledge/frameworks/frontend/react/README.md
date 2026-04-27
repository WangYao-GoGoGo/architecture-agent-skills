# React Knowledge

## Heuristics

- Separate server state, local UI state, derived state, and global app state.
- Keep effects for synchronization with outside systems, not general control flow.
- Extract feature logic into hooks or modules when components become hard to read.
- Avoid over-generic components before repeated use cases exist.
- Treat routing and data loading as architecture boundaries.

## Common Risks

- Effects with unclear dependencies.
- Prop drilling that hides ownership issues.
- Components mixing rendering, data fetching, mutation, and domain policy.

