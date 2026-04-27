# Debug Report: Callback to Coroutine

## 1. Original Problem

The `UserRepository` uses callback-based async with manual thread management. This causes:

- Nested callbacks for sequential operations.
- Manual thread creation (wasteful).
- Potential UI thread violations (callbacks run on background threads).

## 2. Root Cause

Callback-based asynchronous pattern with manual thread management.

## 3. Fix Summary

Refactored to use Kotlin coroutines:

- Changed `fetchUser` and `fetchOrders` to `suspend` functions.
- Replaced `Thread { ... }.start()` with `withContext(Dispatchers.IO)`.
- `loadProfile` uses a coroutine scope with sequential `await`.

## 4. Files Changed

| File | Change |
|---|---|
| `before/UserRepository.kt` | Original — callback-based |
| `after/UserRepository.kt` | Refactored — coroutine-based |

## 5. Validation Commands

```bash
kotlinc tests/*.kt -include-runtime -d tests/test.jar
java -jar tests/test.jar
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires Kotlin coroutines library.

- Same data loading sequence: user → orders → display.
- No manual thread creation.
- Proper coroutine context for IO operations.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same data returned, same loading sequence.

## 8. Remaining Risks

- Requires Kotlin coroutines dependency.
- Callers must be in a coroutine scope.

## 9. Follow-up Recommendations

- Add structured concurrency with `viewModelScope`.
- Add error handling with `try/catch` in coroutines.
