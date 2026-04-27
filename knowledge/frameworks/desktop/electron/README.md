# Electron Knowledge

## Heuristics

- Keep main process, preload bridge, renderer UI, and shared domain modules separated.
- Treat IPC contracts as API contracts with validation and versioning.
- Keep filesystem, shell, clipboard, and native capabilities behind explicit adapters.
- Design auto-update, local storage, crash reporting, and offline behavior as architecture concerns.

## Common Risks

- Renderer code gaining broad native access.
- IPC channels becoming untyped global command buses.
- Business logic split unpredictably between main and renderer processes.
