---
name: swift-protocol-architecture
description: Use when reviewing Swift protocol-oriented design, value type strategy, async/await patterns, and SwiftUI architecture.
---

# Swift Protocol Architecture

## When To Use
- The main decision is about protocol design, value vs reference type selection, or SwiftUI data flow.
- Reviewing actor isolation, property wrapper usage, or Observable conformance.

## Workflow
1. Identify protocol boundaries — are protocols designed for real abstraction needs?
2. Review value vs reference type decisions — are structs used by default?
3. Check actor isolation — are `@MainActor`, custom actors, and `nonisolated` used correctly?
4. Review property wrapper usage — are `@State`, `@Binding`, `@ObservedObject`, `@EnvironmentObject` used appropriately?
5. Check async/await patterns — are `async` functions properly structured?
6. Review `Codable` conformance — is serialization handled correctly?
7. Recommend the simplest protocol and type design.

## Output Format
```markdown
Swift protocol review:
- Protocol boundaries:
- Value vs reference types:
- Actor isolation:
- Property wrappers:
- Async/await patterns:
- Codable conformance:
- Recommended change:
- Verification:
```
