# Next.js Knowledge

## Heuristics

- Treat routing, server components, client components, server actions, and API routes as architecture boundaries.
- Keep server-only code from leaking into client bundles.
- Separate rendering concerns from domain and persistence logic.
- Make caching, revalidation, and data fetching strategy explicit.
- Keep route handlers thin when business workflows grow.

## Common Risks

- Confusing server/client boundaries.
- Cache behavior hidden from feature code.
- Database or secret access leaking into client-side paths.

