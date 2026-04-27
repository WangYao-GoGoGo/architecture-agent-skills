# Frontend Frameworks

## Core Idea

Frontend frameworks shape component lifecycle, state, rendering, data fetching, and routing. Architecture should fit the framework while keeping ownership clear.

## Heuristics

- Place side effects where lifecycle is predictable.
- Keep reusable components free of page-specific data loading when possible.
- Separate server state from local UI state.
- Avoid framework-global state for every interaction.
- Use type and schema validation at API boundaries.

## Common Risks

- Component trees that hide state ownership.
- Effects that run too often or in unclear order.
- Router, data fetching, and UI concerns mixed into shared components.

