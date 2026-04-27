# Julia Architecture Idioms

## Use When

- Reviewing Julia type hierarchies, multiple dispatch design, module organization, or parallel computing patterns.

## Heuristics

- Design around multiple dispatch — define generic functions, then specialize with types.
- Use abstract types for hierarchy roots, concrete types for leaf nodes.
- Prefer `struct` for immutable types and `mutable struct` only when mutation is required.
- Use `module`/`end` for namespace boundaries — export only the public API.
- Leverage `@generated` functions for type-specialized code generation.
- Use `Distributed` or `Threads` for parallelism — prefer `@threads` for shared memory.
- Use `DataFrames.jl` for tabular data, `Plots.jl` for visualization.
- Write type-stable code — avoid changing types within a function body.

## Common Risks

- Type instability from boxing/unboxing in hot loops.
- Over-using macros when a higher-order function would suffice.
- Compilation latency from loading many untyped functions at module load time.
- Global variables in performance-critical code causing type instability.
- Ignoring the `@inbounds` annotation for bounds-check elimination in hot paths.
