---
name: procedural-architecture-review
description: Use when reviewing procedural code for module boundaries, data flow, side-effect isolation, function cohesion, and error handling discipline.
---

# Procedural Architecture Review

Use this skill to review procedural code structure — not just syntax or style, but how functions, modules, and data flow are organized. This complements the `modular-procedural-refactor` skill by focusing on architecture review rather than step-by-step refactoring.

## When To Use

- Reviewing a new procedural module or subsystem before it ships.
- Auditing existing procedural code for structural issues.
- Evaluating whether a procedural codebase is ready for a larger refactoring.
- Onboarding to a procedural codebase and assessing its architecture.

## Knowledge To Use

- [`knowledge/paradigms/procedural/`](../../../knowledge/paradigms/procedural/) — procedural design heuristics and risks
- [`knowledge/paradigms/cross-paradigm/`](../../../knowledge/paradigms/cross-paradigm/) — paradigm comparison and decision guide
- [`knowledge/languages/c/`](../../../knowledge/languages/c/) — C language idioms and constraints (if reviewing C code)
- [`knowledge/languages/go/`](../../../knowledge/languages/go/) — Go language idioms (if reviewing Go code)

## Workflow

1. **Map the module boundaries**: List all modules and their public functions. Check whether each module has a clear, single responsibility.
2. **Trace the data flow**: For a key workflow, trace how data enters the system, moves between modules, and produces output. Identify where data is modified.
3. **Identify side effects**: Mark every function that performs I/O, modifies global state, or changes a parameter. Assess whether side effects are isolated at the edges.
4. **Check error handling**: Verify that errors are handled consistently — same strategy (return codes, error structs, etc.) used throughout.
5. **Evaluate function cohesion**: Check whether any function mixes multiple levels of abstraction or handles unrelated responsibilities.
6. **Assess coupling**: Identify which modules depend on which. Look for circular dependencies, shared mutable state, and tight coupling to data structures.
7. **Review naming and documentation**: Check whether function names describe what they do and whether data flow is documented where non-obvious.

## Output Format

```markdown
Procedural architecture review:
- Module boundaries:
  - [module]: responsibility, public API size, cohesion
- Data flow:
  - Entry point → modules touched → output
  - Where data is modified:
- Side effects:
  - Isolated at edges? [yes/no]
  - Functions with hidden side effects:
- Error handling:
  - Strategy: [return codes / error structs / other]
  - Consistency: [consistent / mixed]
- Function cohesion issues:
  - [function]: [issue]
- Coupling concerns:
  - [module A] → [module B]: [nature of coupling]
- Recommendations:
  - [priority] [recommendation]
- Verification:
  - [how to verify each recommendation]
```
