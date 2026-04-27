# Debug Report: GenServer OTP Design

## 1. Original Problem

The `Counter` GenServer uses `send()` for resetting state instead of `GenServer.cast()`. This breaks OTP encapsulation and makes the code inconsistent — some operations use `call`/`cast`, while `reset` uses raw message passing.

## 2. Root Cause

Inconsistent OTP usage — `send()` bypasses the GenServer API and uses raw `handle_info` instead of `handle_cast`.

## 3. Fix Summary

Refactored to use consistent OTP conventions:

- Changed `reset` from `send()` to `GenServer.cast()`.
- Removed `handle_info` for reset — now uses `handle_cast`.
- All state modifications go through the standard GenServer API.

## 4. Files Changed

| File | Change |
|---|---|
| `before/counter.exs` | Original — mixed send/cast/call |
| `after/counter.exs` | Refactored — consistent OTP API |

## 5. Validation Commands

```bash
elixir -r tests/test_counter.exs -e "CounterTest.run()"
```

## 6. Validation Results

Validation Level: **Test-based validation**.

- Counter behavior preserved: increment, get, reset.
- All operations now use consistent OTP API (call/cast).
- No raw message passing for state modification.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same counter operations, same results.

## 8. Remaining Risks

- If external code depended on `send()` to the GenServer, it will break.
- No timeout handling for `call` operations.

## 9. Follow-up Recommendations

- Add timeout to `GenServer.call()`.
- Consider adding a supervision tree for fault tolerance.
