# Debug Report: Sync to Async

## 1. Original Problem

The `UserService.FetchUserData()` method uses `.Result` to block on an async HTTP call. This causes thread pool starvation under load and poor scalability.

## 2. Root Cause

Synchronous blocking on I/O operations — `.Result` blocks the calling thread while waiting for the HTTP response, wasting a thread pool thread.

## 3. Fix Summary

Refactored to use proper async/await:

- Changed `FetchUserData` to `FetchUserDataAsync` returning `Task<string>`.
- Replaced `.Result` with `await`.
- Replaced `Thread.Sleep` with `Task.Delay`.
- Updated `Main` to use `await` with `Task.WhenAll`.

## 4. Files Changed

| File | Change |
|---|---|
| `before/UserService.cs` | Original — synchronous blocking |
| `after/UserService.cs` | Refactored — async/await |

## 5. Validation Commands

```bash
dotnet test tests/
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a real HTTP endpoint.

- Public API changed from `string FetchUserData(string)` to `Task<string> FetchUserDataAsync(string)` — intentional improvement.
- Return value behavior preserved: same HTTP response data.
- Error handling preserved: HTTP exceptions still propagate.

## 7. Behavior Preservation Notes

⚠️ Public API signature changed (sync to async) — this is the intended improvement. Return value content is preserved.

## 8. Remaining Risks

- Callers must now `await` the async method — breaking change for synchronous callers.
- No timeout handling added — long-running HTTP calls could still hang.

## 9. Follow-up Recommendations

- Add cancellation token support.
- Add timeout configuration for HTTP calls.
- Consider adding retry logic for transient HTTP failures.
