# Flutter Knowledge

## Heuristics

- Separate widgets, state management, domain/use cases, and data sources.
- Choose state management based on ownership and complexity, not trend.
- Keep platform channels and plugins behind boundaries.
- Treat navigation, async loading, error, and offline states as part of architecture.

## Common Risks

- Widget trees owning business workflows.
- Global state used for local screen state.
- Platform-specific code leaking into shared UI logic.

