# Erlang Architecture Idioms

## Use When

- Reviewing Erlang OTP behaviors, process design, supervision strategies, or distributed Erlang patterns.

## Heuristics

- Use OTP behaviors (`gen_server`, `gen_statem`, `supervisor`) — never write raw receive loops.
- Design for failure — let processes crash and restart via supervision trees.
- Use pattern matching in function clauses and `case` expressions — let it fail early.
- Use immutable data — rebinding is not allowed; each variable is a single assignment.
- Use `list` as the primary data structure — they're linked lists optimized for pattern matching.
- Use `map` for key-value data (Erlang 17+) — records are legacy.
- Use `binary` for string and byte-level manipulation.
- Keep process state minimal — a process should own one responsibility.

## Common Risks

- Overloading a single process with too many responsibilities.
- Not handling `nodedown` messages in distributed Erlang setups.
- Deeply nested `case` expressions that obscure the happy path.
- Large message payloads causing memory pressure in process mailboxes.
- `after` clauses in `receive` blocks that mask timeout handling.
