# Commands

## Run Original Code

```bash
elixir before/counter.exs
```

## Run Refactored Code

```bash
elixir after/counter.exs
```

## Run Tests

```bash
elixir -r tests/test_counter.exs -e "CounterTest.run()"
```

## Validate Behavior Preservation

The refactoring replaces raw `send()` with proper `GenServer.cast()` and enforces OTP encapsulation. The counter behavior (increment, get, reset) is preserved.

Validation Level: **Test-based validation** — Elixir tests can verify GenServer behavior.
