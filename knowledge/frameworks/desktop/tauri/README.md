# Tauri Knowledge

## Heuristics

- Keep Rust commands, frontend UI, filesystem access, and plugin integration behind clear boundaries.
- Treat command payloads and permissions as API contracts.
- Keep native capabilities narrow and auditable.
- Make packaging, updater, deep links, and platform-specific behavior explicit.

## Common Risks

- Frontend code depending on ad hoc native commands.
- Permission scope wider than the feature requires.
- Platform-specific Rust code leaking into shared UI state.
