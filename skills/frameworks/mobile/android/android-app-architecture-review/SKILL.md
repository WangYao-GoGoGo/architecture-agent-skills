---
name: android-app-architecture-review
description: Use when reviewing Android application architecture, Activity/Fragment lifecycle, MVVM, Jetpack Compose, dependency injection, and app structure.
---

# Android App Architecture Review

## When To Use

- The main decision is about Android project structure, lifecycle management, state handling, or dependency injection setup.
- Reviewing offline behavior, permission handling, or background work.

## Workflow

1. Identify the architecture pattern — MVVM, MVI, or Clean Architecture layers.
2. Review lifecycle management — Activity/Fragment lifecycle, ViewModel scoping, and configuration changes.
3. Check state management — StateFlow, LiveData, or Compose state hoisting.
4. Review dependency injection — Hilt, Koin, or manual DI setup.
5. Check offline and caching strategy — Room, DataStore, or network caching.
6. Review permission handling and background work — WorkManager, foreground services.
7. Recommend the smallest structural change that improves lifecycle safety or testability.

## Output Format

```markdown
Android architecture review:
- Architecture pattern:
- Lifecycle management:
- State management:
- Dependency injection:
- Offline & caching:
- Permissions & background work:
- Recommended change:
- Verification:
```
