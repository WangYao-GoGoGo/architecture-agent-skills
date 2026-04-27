# Remix Knowledge

## Heuristics

- Organize routes by URL structure and domain; use nested routes for shared layouts.
- Keep loaders focused on data fetching; avoid business logic in loaders.
- Keep actions focused on mutations; delegate business workflows to service modules.
- Use error boundaries at route and layout levels for granular error handling.
- Make caching and revalidation strategy explicit with `headers` and `Cache-Control`.

## Common Risks

- Loaders fetching more data than needed.
- Actions owning business logic.
- Nested route data dependencies that are unclear.
