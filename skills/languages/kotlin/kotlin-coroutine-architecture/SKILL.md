---
name: kotlin-coroutine-architecture
description: Use when reviewing Kotlin coroutine usage, scope management, Flow design, and structured concurrency architecture.
---

# Kotlin Coroutine Architecture

## When To Use
- The main decision is about coroutine scope management, Flow data streams, or structured concurrency patterns.
- Reviewing `launch` vs `async`, `Dispatchers` selection, or coroutine cancellation.

## Workflow
1. Identify coroutine scopes — are they properly scoped to component lifecycles?
2. Review `launch` vs `async`/`await` usage — is `async` used only when results are needed?
3. Check `Dispatchers` selection — is the correct dispatcher used for each task type?
4. Review `Flow` design — are `StateFlow`/`SharedFlow` used appropriately for state vs events?
5. Check cancellation handling — are `isActive` checks or `ensureActive()` used in CPU-bound loops?
6. Review exception handling — are `CoroutineExceptionHandler` and `supervisorScope` used correctly?
7. Recommend the simplest coroutine structure.

## Output Format
```markdown
Kotlin coroutine review:
- Coroutine scopes:
- launch vs async:
- Dispatchers:
- Flow design:
- Cancellation:
- Exception handling:
- Recommended change:
- Verification:
```
