# Ada Architecture Idioms

## Use When

- Reviewing Ada code for safety-critical, real-time, or embedded systems using SPARK or Ravenscar profiles.

## Heuristics

- Use strong typing — define distinct types for distinct concepts, even if they share the same representation.
- Use `package` with `private`/`public` for encapsulation — hide implementation details.
- Use `task` and `protected objects` for concurrency — rendezvous for synchronization.
- Use `generic` packages for reusable, type-safe components.
- Use `range` constraints on scalar types to enforce valid values at compile/runtime.
- Use `exception` handling only for truly exceptional conditions — not for control flow.
- Use `pragma` for compiler directives (e.g., `pragma Suppress`, `pragma Restrictions`).
- Use SPARK Ada subset for formal verification of critical properties.

## Common Risks

- Unconstrained array bounds causing `Constraint_Error` at runtime.
- Task deadlock from improper rendezvous ordering.
- Over-using `use` clauses causing namespace pollution.
- Not handling `Storage_Error` in memory-constrained systems.
- Mixing `Ada.Real_Time` and `Ada.Calendar` timing models incorrectly.
