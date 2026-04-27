# Expo Knowledge

## Heuristics

- Separate managed workflow, development builds, native modules, and EAS services.
- Keep native module access behind capability abstractions.
- Treat EAS Build configuration, updates, and app store deployment as architecture.
- Add proper handling for permissions, offline mode, and push notifications.

## Common Risks

- Managed workflow limitations blocking required native features.
- EAS Update configuration not aligned with release strategy.
- Platform-specific behavior not tested on both iOS and Android.
