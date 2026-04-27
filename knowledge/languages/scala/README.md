# Scala Architecture Idioms

## Use When

- Reviewing Scala type class design, implicit/given usage, Akka actor systems, or functional programming patterns.

## Heuristics

- Use `case class` for immutable data and pattern matching.
- Prefer `sealed trait` / `enum` for algebraic data types.
- Use `given`/`using` (Scala 3) or `implicit` (Scala 2) for type class instances.
- Keep `Future` usage explicit — prefer `ZIO` or `Cats Effect` for complex async.
- Use `for` comprehensions to sequence monadic operations cleanly.
- Favor pure functions with no side effects — push effects to the edges.
- Use `opaque types` (Scala 3) or value classes for type-safe primitives.
- Organize code into packages by domain, not by layer.

## Common Risks

- Over-engineering with complex type-level programming for simple problems.
- `implicit` resolution ambiguity causing mysterious compilation errors.
- Mixing `Future`-based code with effect system code without clear boundaries.
- Memory leaks from Akka actor mailbox backpressure issues.
- Binary compatibility issues from case class evolution in libraries.
