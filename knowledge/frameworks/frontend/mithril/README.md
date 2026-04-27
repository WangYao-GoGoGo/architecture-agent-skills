# Mithril Knowledge

## Heuristics

- Keep components focused on rendering; use models for data and services for business logic.
- Use Mithril's auto-redraw system; minimize manual `m.redraw()` calls.
- Keep XHR requests in models or services, not in component views.
- Use `m.request` for AJAX with proper error handling.
- Keep route resolution functions focused on data loading; delegate rendering to components.

## Common Risks

- Components owning business logic.
- Manual redraws causing performance issues.
- XHR requests scattered across components.
