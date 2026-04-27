# Procedural Patterns

Reusable structures for procedural and data-oriented code. These patterns apply when the primary unit of organization is the function or module, not the object.

## Patterns

| Pattern | Intent |
|---------|--------|
| **Layered Module** | Organize code into strict dependency layers where each layer only depends on the one below it |
| **Callback / Handler Chain** | Pass a request through a sequence of pluggable handler functions |
| **State Machine** | Model explicit states, transitions, and guarded actions without OO polymorphism |
| **Data-Oriented Design** | Organize data structures for cache-friendly sequential access |
| **Table-Driven Logic** | Replace long if-else chains with lookup tables or dispatch tables |
| **Stepwise Refinement** | Decompose a function into sub-functions at progressively lower abstraction levels |
| **Module with Internal State** | Encapsulate mutable state within a module using file-scoped variables and accessor functions |

## Use When

- The primary language does not support OO constructs (C, Fortran, Assembly)
- Performance-critical paths where vtable dispatch is too expensive
- Data transformation pipelines with clear input → process → output flow
- Systems where state is centralized (e.g., a single database connection, a hardware register)

## Related Knowledge

- [`knowledge/paradigms/procedural/`](../../paradigms/procedural/) — procedural design heuristics and risks
- [`knowledge/languages/c/`](../../languages/c/) — C language-specific patterns
- [`skills/paradigms/procedural/procedural-architecture-review/SKILL.md`](../../../skills/paradigms/procedural/procedural-architecture-review/SKILL.md) — skill for reviewing procedural code
