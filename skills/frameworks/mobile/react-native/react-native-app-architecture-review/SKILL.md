---
name: react-native-app-architecture-review
description: Use when reviewing React Native application architecture, component lifecycle, native module bridge, navigation, and app structure.
---

# React Native App Architecture Review

## When To Use

- The main decision is about React Native component structure, state management, native module boundaries, or navigation design.
- Reviewing offline behavior, permissions, or platform-specific code.

## Workflow

1. Identify the architecture pattern — component hierarchy, state management, and navigation.
2. Review native module boundaries — bridge calls, native events, and error handling.
3. Check state management — Redux, Zustand, Jotai, or React Context scoping.
4. Review navigation structure — React Navigation, deep linking, and screen composition.
5. Check offline and caching strategy — AsyncStorage, MMKV, or SQLite.
6. Review platform-specific code — iOS vs Android differences and conditional imports.
7. Recommend the smallest structural change that improves maintainability or reliability.

## Output Format

```markdown
React Native architecture review:
- Architecture pattern:
- Native module boundaries:
- State management:
- Navigation:
- Offline & caching:
- Platform-specific code:
- Recommended change:
- Verification:
```
