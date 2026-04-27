# Haskell Architecture Idioms

## Use When

- Reviewing Haskell type-level design, monad transformer stacks, effect systems, or module organization.

## Heuristics

- Make illegal states unrepresentable through algebraic data types.
- Use `newtype` for type-safe wrappers around primitive types.
- Structure monad transformer stacks with clear layering — `ReaderT` for config, `StateT` for state.
- Prefer `mtl` style (type class constraints) over concrete transformer stacks for flexibility.
- Use `lens` for deep immutable data access and updates.
- Keep `IO` at the edges — push pure computations to the center.
- Use `GADTs` for type-safe DSLs and `TypeFamilies` for type-level computation.
- Organize modules by domain concept, not by type class.

## Common Risks

- Over-engineering with advanced type system extensions for simple problems.
- Space leaks from lazy evaluation — use `deepseq`/`rnf` when needed.
- Monad transformer stack overflow from deep nesting.
- Orphan instances causing coherence issues.
- Cabal/Stack dependency hell from conflicting upper bounds.
