---
name: dart-flutter-architecture
description: Use when reviewing Dart null safety patterns, Flutter widget architecture, state management, and async patterns.
---

# Dart / Flutter Architecture

## When To Use
- The main decision is about Flutter widget tree organization, state management strategy, or async data flow.
- Reviewing null safety usage, stream subscriptions, or BLoC/Riverpod patterns.

## Workflow
1. Identify widget structure — are widgets small, focused, and composable?
2. Review state management — is the chosen approach (Riverpod, BLoC, Provider) used consistently?
3. Check null safety — are nullable types used correctly with `?` and `late`?
4. Review async patterns — are `StreamSubscription`s properly cancelled in `dispose`?
5. Check `const` constructors — are they used wherever possible for performance?
6. Review feature organization — is code organized by feature, not by type?
7. Recommend the simplest widget and state architecture.

## Output Format
```markdown
Dart/Flutter review:
- Widget structure:
- State management:
- Null safety:
- Async patterns:
- const constructors:
- Feature organization:
- Recommended change:
- Verification:
```
