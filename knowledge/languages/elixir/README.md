# Elixir Architecture Idioms

## Use When

- Reviewing Elixir OTP supervision trees, GenServer state management, Phoenix contexts, or concurrent patterns.

## Heuristics

- Use GenServer for managing state, but keep state minimal and focused.
- Design supervision trees with clear restart strategies — one-for-one vs one-for-all.
- Use Phoenix contexts to define bounded contexts — keep contexts independent.
- Leverage `|>` pipe operator for data transformation pipelines.
- Use `with` for sequential, short-circuiting operations.
- Prefer immutable data and pure functions — isolate side effects in processes.
- Use `Task.async`/`Task.await` for concurrent work, GenServer for long-lived state.
- Use `Registry` for process discovery instead of hardcoded PIDs.

## Common Risks

- GenServer processes accumulating unbounded state.
- Over-using `Process.send` instead of `GenServer.call`/`cast` for structured communication.
- Deeply nested `case` statements that should be `with` or function clauses.
- Not handling GenServer timeouts or crashes in supervision trees.
- Mixing Phoenix context boundaries leading to tight coupling between domains.
