# Functional Patterns

Reusable structures for functional and declarative code. These patterns apply when the primary unit of organization is the function as a value, with an emphasis on immutability and purity.

## Patterns

| Pattern | Intent |
|---------|--------|
| **Functor** | Map a function over a wrapped value (e.g., `map` over `List`, `Optional`) |
| **Monad** | Chain computations that carry context (e.g., `Maybe` for optionality, `Either` for errors, `IO` for effects) |
| **Applicative** | Apply a wrapped function to a wrapped value, enabling independent effect combination |
| **Lens** | Provide immutable access and update of nested data structures |
| **Currying** | Transform a multi-argument function into a chain of single-argument functions |
| **Pattern Matching** | Dispatch behavior based on the shape and content of data structures |
| **Algebraic Data Types** | Model domain data using sum types (alternatives) and product types (records) |
| **Pure Pipeline** | Compose a sequence of pure transformations where data flows from one function to the next |
| **Recursion Scheme** | Abstract common recursive patterns (fold, unfold, map, filter) |
| **Effect Tracking** | Separate pure computation from side effects using type-level effect systems |

## Use When

- The primary language supports first-class functions and immutable data (Haskell, OCaml, Elixir, Clojure, Scala)
- The problem involves complex data transformations with clear composability requirements
- Correctness benefits from strong type guarantees and absence of side effects
- Concurrency is simplified by shared-nothing immutable state

## Related Knowledge

- [`knowledge/paradigms/functional/`](../../paradigms/functional/) — functional design heuristics and risks
- [`knowledge/languages/haskell/`](../../languages/haskell/) — Haskell-specific functional patterns
- [`knowledge/languages/elixir/`](../../languages/elixir/) — Elixir-specific functional patterns
- [`skills/paradigms/functional/functional-composition-review/SKILL.md`](../../../skills/paradigms/functional/functional-composition-review/SKILL.md) — skill for reviewing functional composition
