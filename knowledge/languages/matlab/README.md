# MATLAB Architecture Idioms

## Use When

- Reviewing MATLAB code for numerical computing, signal processing, Simulink models, or data analysis pipelines.

## Heuristics

- Prefer vectorized operations over explicit loops for performance.
- Pre-allocate arrays with `zeros()`, `ones()`, or `NaN()` instead of growing dynamically.
- Use functions with explicit input/output arguments — avoid global variables.
- Use `parfor` for embarrassingly parallel loops with independent iterations.
- Organize code into modular functions and scripts — avoid monolithic scripts.
- Use `handle` classes for objects that need reference semantics.
- Use `cellfun`/`arrayfun` for element-wise operations on cell/struct arrays.
- Document functions with `help` header comments.

## Common Risks

- Dynamic array growth in loops causing memory reallocation overhead.
- Over-using `eval()` and `evalin()` which bypass optimization and are hard to debug.
- Mixing `int` and `double` types causing unexpected type conversion.
- Not clearing large variables from workspace causing memory pressure.
- Simulink model complexity from monolithic subsystems instead of modular hierarchy.
