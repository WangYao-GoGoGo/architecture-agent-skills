# SvelteKit Knowledge

## Heuristics

- Organize routes by URL structure and domain; use layout loads for shared data.
- Keep load functions focused on data fetching; avoid business logic in load functions.
- Keep form actions focused on mutations; delegate business workflows to service modules.
- Keep server-only code (database, secrets) out of client-side bundles.
- Use `invalidate` and `invalidateAll` for cache invalidation after mutations.

## Common Risks

- Load functions fetching more data than needed.
- Form actions owning business logic.
- Server-only code leaking into client bundles.
