# Nuxt Knowledge

## Heuristics

- Treat pages, composables, server routes, plugins, and middleware as distinct boundaries.
- Keep universal/client/server-only code separated.
- Make data fetching and caching behavior explicit.
- Use composables for reusable behavior without turning them into hidden globals.

## Common Risks

- Server-only assumptions leaking into client code.
- Plugin side effects that are hard to trace.
- Page components owning too much domain logic.

