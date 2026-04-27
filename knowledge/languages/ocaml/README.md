# OCaml / F# Architecture Idioms

## Use When

- Reviewing OCaml module signatures, functor usage, variant type design, or F# computation expressions.

## Heuristics

- Use `type` with variants (discriminated unions) for state machines and option types.
- Leverage the module system (`sig`/`struct`) for abstraction boundaries.
- Use functors for parameterized modules — prefer over first-class modules when possible.
- Use `match` with exhaustiveness checking — the compiler ensures all cases are handled.
- In F#, use computation expressions for async, sequence, and result workflows.
- Prefer immutable data by default — use `ref` or `mutable` only when performance demands it.
- Use `option` and `Result` types instead of exceptions for expected failure modes.
- Keep functions pure and composable — push side effects to the system boundary.

## Common Risks

- Over-using objects and classes when the functional/immutable approach is simpler.
- Deep module functor stacks that obscure the concrete type.
- Ignoring compiler warnings about non-exhaustive pattern matches.
- Mixing `async` and synchronous code without clear boundaries in F#.
- Over-relying on `printf`-based formatting instead of structured logging.
