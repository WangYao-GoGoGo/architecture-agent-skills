# Debug Report: Worker Context Cancellation

## 1. Original Problem

Worker goroutines are never cleaned up when `main()` returns early. The workers run forever in the background, causing goroutine leaks.

## 2. Root Cause

No cancellation mechanism — workers use an infinite loop without checking for a done signal.

## 3. Fix Summary

Added context-based cancellation:

- Created a `context.WithCancel` in `main()`.
- Workers check `ctx.Done()` in their loop.
- `cancel()` is called when the desired number of results is collected.

## 4. Files Changed

| File | Change |
|---|---|
| `before/main.go` | Original — goroutine leak |
| `after/main.go` | Refactored — context cancellation |

## 5. Validation Commands

```bash
go test ./tests/ -v
```

## 6. Validation Results

Validation Level: **Test-based validation**.

- Worker goroutines now exit when context is cancelled.
- Same results produced for the first 3 iterations.
- No goroutine leak after main exits.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same results for the first 3 iterations. Workers now exit cleanly instead of leaking.

## 8. Remaining Risks

- If `cancel()` is not called, workers still leak.
- Context cancellation does not handle in-flight work — workers may need to complete current iteration.

## 9. Follow-up Recommendations

- Add a timeout to the context for safety.
- Consider using `sync.WaitGroup` to wait for worker shutdown.
