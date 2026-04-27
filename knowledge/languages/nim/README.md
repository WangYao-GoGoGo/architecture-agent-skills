# Nim Architecture Idioms

## Use When

- Reviewing Nim macro usage, type system design, memory management strategy, or module organization.

## Heuristics

- Use `proc` with explicit `return` types — Nim infers but explicit is clearer.
- Leverage `macro` and `template` for code generation — but prefer templates for simple substitutions.
- Use `ref` for reference types, `ptr` for raw pointers, and value types by default.
- Use `object` with inheritance for OOP — use `method` for dynamic dispatch.
- Use `async`/`await` for I/O-bound concurrency.
- Use `seq` as the default dynamic collection type.
- Use `import` with explicit symbols to avoid namespace pollution.
- Use `concept` (Nim 2+) for generic constraints.

## Common Risks

- Over-using macros when a simpler abstraction (template, generic) would work.
- Memory safety issues from `ptr` usage without proper lifetime management.
- Compile-time slowdown from complex macro expansions.
- GC tuning issues in real-time or latency-sensitive applications.
- C interop type mismatches when using `{.importc.}`.
