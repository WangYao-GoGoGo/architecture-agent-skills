---
name: csharp-async-architecture
description: Use when reviewing C# async/await patterns, Task lifecycle, cancellation, and .NET asynchronous architecture.
---

# C# Async Architecture

## When To Use
- The main decision is about async method design, Task parallelism, cancellation strategy, or async disposal.
- Reviewing `async void`, `ValueTask` usage, or `ConfigureAwait` patterns.

## Workflow
1. Identify async method signatures — do they follow `Async` naming convention?
2. Review `async void` usage — is it limited to event handlers only?
3. Check cancellation token propagation — are tokens passed through the call chain?
4. Review `ConfigureAwait(false)` usage — is it used in library code, not in application code?
5. Check `Task` vs `ValueTask` — is `ValueTask` used only for hot paths with frequent synchronous completion?
6. Review `IAsyncDisposable` — are async resources properly disposed?
7. Recommend the correct async pattern for each scenario.

## Output Format
```markdown
C# async review:
- Async method signatures:
- async void usage:
- Cancellation propagation:
- ConfigureAwait strategy:
- Task vs ValueTask:
- Async disposal:
- Recommended change:
- Verification:
```
