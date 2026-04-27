# Ruby Architecture Idioms

## Use When

- Reviewing Ruby module organization, metaprogramming usage, block patterns, or Rails application structure.

## Heuristics

- Use modules for sharing behavior via mixins — prefer composition over inheritance.
- Leverage blocks and `yield` for callback and DSL patterns.
- Use `attr_reader`/`attr_accessor` intentionally — don't expose internal state by default.
- Keep methods short and focused — Ruby culture values clarity and intention.
- Use `freeze` on constants and string literals to avoid mutation surprises.
- Prefer `Enumerable` over manual iteration for collection operations.
- Use `Struct` and `Data` for simple value objects.
- Follow Rails conventions when in Rails, but extract plain Ruby objects for domain logic.

## Common Risks

- Overusing `method_missing` and `define_method` — they make code hard to trace.
- Monkey-patching core classes without understanding the impact.
- Block-level `return` causing `LocalJumpError` in lambdas vs procs.
- Mutable constants being modified at runtime.
- Over-reliance on global state through class variables (`@@`) or global singletons.
