# Ionic Knowledge

## Heuristics

- Separate web UI, state, native plugin access, and backend integration.
- Keep Capacitor or Cordova plugin calls behind capability services.
- Treat permissions, offline mode, push notifications, and app-store release constraints as architecture.
- Keep platform-specific behavior isolated from reusable frontend components.

## Common Risks

- UI components directly owning native plugin calls.
- Browser assumptions leaking into mobile runtime behavior.
- Offline and permission states handled as afterthoughts.
