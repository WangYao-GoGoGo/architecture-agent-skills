---
name: ionic-app-architecture-review
description: Use when reviewing Ionic application architecture, WebView bridge, Capacitor/Cordova plugins, lazy loading, and app structure.
---

# Ionic App Architecture Review

## When To Use

- The main decision is about Ionic project structure, native plugin integration, lazy loading strategy, or platform-specific behavior.
- Reviewing offline mode, permissions, or app-store release constraints.

## Workflow

1. Identify the architecture pattern — component structure, routing, and state management.
2. Review native plugin integration — Capacitor/Cordova plugin calls and capability service boundaries.
3. Check lazy loading and module structure — Angular lazy modules or React code splitting.
4. Review offline and caching strategy — service workers, local storage, or SQLite.
5. Check permission handling — camera, geolocation, and push notifications.
6. Review platform-specific behavior — iOS vs Android differences and browser assumptions.
7. Recommend the smallest structural change that improves maintainability or reliability.

## Output Format

```markdown
Ionic architecture review:
- Architecture pattern:
- Native plugin integration:
- Lazy loading:
- Offline & caching:
- Permission handling:
- Platform-specific behavior:
- Recommended change:
- Verification:
```
