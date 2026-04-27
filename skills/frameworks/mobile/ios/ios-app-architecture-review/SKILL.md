---
name: ios-app-architecture-review
description: Use when reviewing iOS application architecture, ViewController/SwiftUI lifecycle, MVC/MVVM, state management, and app structure.
---

# iOS App Architecture Review

## When To Use

- The main decision is about iOS project structure, UI lifecycle management, state handling, or concurrency design.
- Reviewing offline behavior, permission handling, or background execution.

## Workflow

1. Identify the architecture pattern — MVC, MVVM, or SwiftUI + Combine.
2. Review lifecycle management — ViewController lifecycle, SwiftUI view lifecycle, and state restoration.
3. Check state management — ObservableObject, @Published, @State, or TCA.
4. Review concurrency design — async/await, Combine publishers, and main-thread boundaries.
5. Check offline and persistence strategy — CoreData, SwiftData, or file-based.
6. Review permission handling and background execution.
7. Recommend the smallest structural change that improves lifecycle safety or testability.

## Output Format

```markdown
iOS architecture review:
- Architecture pattern:
- Lifecycle management:
- State management:
- Concurrency design:
- Offline & persistence:
- Permissions & background:
- Recommended change:
- Verification:
```
