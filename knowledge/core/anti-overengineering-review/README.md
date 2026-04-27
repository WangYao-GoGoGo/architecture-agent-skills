# Anti-Overengineering Review Knowledge

## Use When

A proposed architecture, design pattern, abstraction, framework, cache, service split, or refactor may be more complex than the current problem needs.

## Heuristics

- State the current problem and known future change before evaluating the design.
- List every new abstraction or moving part the proposal introduces.
- Ask what each abstraction protects from. If it protects from nothing real, remove or defer it.
- One implementation usually does not need an interface unless tests, plugins, or boundaries require it.
- Two branches do not automatically justify Strategy.
- A cache is not free; include invalidation and consistency rules.
- A service split is not free; include network, ownership, deployment, and observability costs.
- A generic framework is suspicious if only one use case exists.
- Keep explicit extension points only where change is likely or costly.

## Common Risks

- Designing for hypothetical future requirements that never materialize.
- Confusing "clean architecture" with "many layers."
- Adding patterns because they look good on a resume, not because they solve a current problem.
- Treating overengineering review as anti-design; the goal is practical design, not no design.
