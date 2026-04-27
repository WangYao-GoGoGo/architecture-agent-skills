# Astro Knowledge

## Heuristics

- Use islands architecture to minimize client-side JavaScript; only hydrate interactive components.
- Keep content collections with defined schemas for type-safe content management.
- Keep server-only code (database, secrets) out of client-side bundles.
- Use integrations deliberately; each integration adds build-time and runtime overhead.
- Fetch data at the page level and pass down to components for clear data flow.

## Common Risks

- Islands that are too large or too many.
- Server-only code leaking into client bundles.
- Content collections without defined schemas.
