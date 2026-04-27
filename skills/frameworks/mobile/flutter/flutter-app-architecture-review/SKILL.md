---
name: flutter-app-architecture-review
description: Use when reviewing Flutter application architecture, widget tree design, state management, platform channels, and app structure.
---

# Flutter App Architecture Review

## When To Use

- The main decision is about Flutter widget hierarchy, state management approach, platform channel design, or navigation structure.
- Reviewing offline behavior, error handling, or platform-specific code.

## Workflow

1. Identify the architecture pattern — BLoC, Provider, Riverpod, or GetX.
2. Review widget tree structure — is it well-composed or deeply nested?
3. Check state management — is state scoped appropriately (local vs global)?
4. Review platform channel design — method channels, event channels, and error handling.
5. Check navigation and routing — GoRouter, Navigator 2.0, or imperative navigation.
6. Review offline, error, and loading state handling.
7. Recommend the smallest structural change that improves maintainability or testability.

## Output Format

```markdown
Flutter architecture review:
- Architecture pattern:
- Widget tree structure:
- State management:
- Platform channels:
- Navigation:
- Error & loading states:
- Recommended change:
- Verification:
```
