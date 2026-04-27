# Backbone.js Knowledge

## Heuristics

- Keep models focused on data and business logic; use collections for ordered sets.
- Keep views focused on rendering and user interaction; delegate business logic to models.
- Use routers for URL-based application state; keep route handlers thin.
- Use events for decoupled communication; namespace events to avoid collisions.
- Use `listenTo` for view event binding to ensure proper cleanup on view removal.

## Common Risks

- Views owning business logic.
- Global events creating hidden coupling.
- Router handlers owning too much logic.
