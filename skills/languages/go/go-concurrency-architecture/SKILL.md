---
name: go-concurrency-architecture
description: Use when reviewing Go concurrency patterns, goroutine lifecycle, channel design, error group usage, and synchronization architecture.
---

# Go Concurrency Architecture

## When To Use
- The main decision is about goroutine lifecycle management, channel design, or synchronization strategy.
- Reviewing concurrent data access patterns, worker pools, or pipeline architecture.

## Workflow
1. Identify goroutine launch sites — are they tracked for lifecycle management?
2. Review channel ownership — who creates, writes, closes, and reads each channel?
3. Check for proper cancellation via `context.Context` — are goroutines cancellable?
4. Review error propagation — are errors from goroutines collected via `errgroup.Group`?
5. Check for data races — are shared mutable values protected by `sync.Mutex` or atomic ops?
6. Review `select` statements — are all channels handled, including cancellation?
7. Recommend the simplest concurrency primitive that solves the problem.

## Output Format
```markdown
Go concurrency review:
- Goroutine lifecycle:
- Channel design:
- Cancellation & context:
- Error propagation:
- Synchronization:
- Recommended change:
- Verification:
```
