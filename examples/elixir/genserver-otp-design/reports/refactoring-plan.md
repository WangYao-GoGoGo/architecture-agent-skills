# GenServer State Leak → OTP Design

Refactored from mixed call/cast/info patterns to a clean OTP design with consistent message passing.

## Design Pressure

- `reset/1` used `send/2` (raw message) instead of `GenServer.cast/2` — inconsistent API.
- No distinction between synchronous (`call`) and asynchronous (`cast`) operations.
- State transitions were implicit — hard to reason about.
- Adding logging or metrics required modifying every handler.

## Applied Pattern

**Consistent OTP conventions** — use `call` for queries, `cast` for commands. Never use `send` directly. Add a wrapper module for the public API.

## After Code

```elixir
defmodule Counter do
  use GenServer

  # Public API — all interactions go through GenServer
  def start_link(initial_value) do
    GenServer.start_link(__MODULE__, initial_value, name: __MODULE__)
  end

  def increment do
    GenServer.cast(__MODULE__, :increment)
  end

  def get do
    GenServer.call(__MODULE__, :get)
  end

  def reset do
    GenServer.cast(__MODULE__, :reset)
  end

  # Callbacks
  def init(initial_value) do
    {:ok, %{value: initial_value}}
  end

  def handle_cast(:increment, state) do
    {:noreply, %{state | value: state.value + 1}}
  end

  def handle_cast(:reset, _state) do
    {:noreply, %{value: 0}}
  end

  def handle_call(:get, _from, state) do
    {:reply, state.value, state}
  end
end
```

## Key Changes

| Before | After |
|--------|-------|
| `send(__MODULE__, ...)` — raw message | `GenServer.cast/2` — consistent API |
| `handle_info` for reset | `handle_cast(:reset, ...)` — explicit |
| State is a scalar (`state + 1`) | State is a map (`%{value: ...}`) — extensible |
| Mixed call/cast/info | Clear: `call` = query, `cast` = command |
| No logging hook | Easy to add logging in `handle_call`/`handle_cast` |

## Verification

- Same behavior for `increment`, `get`, and `reset`.
- All state transitions go through `handle_call` or `handle_cast` — no raw messages.
- Adding a new operation (e.g., `decrement`) requires only a new `handle_cast` clause.
- State is a map — adding new fields doesn't break existing handlers.
- OTP conventions are followed — the process can be supervised and restarted.
