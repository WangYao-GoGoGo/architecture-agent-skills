# Clojure Architecture Idioms

## Use When

- Reviewing Clojure namespace organization, data-oriented design, macro usage, or state management patterns.

## Heuristics

- Favor data-oriented design — model domain with plain maps, vectors, and sets.
- Use `defrecord`/`deftype` only when Java interop or protocol performance matters.
- Keep functions pure — isolate side effects with `atom`, `ref`, or `agent`.
- Use `->` and `->>` threading macros for readable transformation pipelines.
- Design namespaces around capabilities, not entity types.
- Use `spec` or `malli` for runtime data validation and generative testing.
- Prefer `clojure.core` functions over custom implementations.
- Use protocols for polymorphic dispatch when needed, multimethods for complex dispatch.

## Common Risks

- Overusing macros when a function would suffice — macros compose poorly.
- Mutable state via `atom`/`ref` leaking across component boundaries.
- Large namespaces that mix unrelated concerns.
- Over-abstraction with protocols and multimethods for simple cases.
- Java interop type hints missing in performance-critical paths.
