# Cross-Paradigm Decision Guide

## Core Idea

No single paradigm is universally best. The choice between object-oriented, procedural, functional, and systems-oriented design depends on the problem domain, team expertise, language capabilities, and long-term maintenance goals. Many successful systems use a mix of paradigms.

## Use When

- Deciding which paradigm to use for a new project or module.
- Reviewing whether the current paradigm choice is appropriate.
- Transitioning code from one paradigm to another (e.g., procedural to OO).
- Evaluating whether a mixed-paradigm approach is justified.

## Paradigm Comparison

| Aspect | Object-Oriented | Procedural | Functional | Systems-Oriented |
|--------|----------------|------------|------------|-----------------|
| **Primary unit** | Objects (data + behavior) | Functions + data structs | Pure functions + types | Modules + resources |
| **State management** | Encapsulated mutable state | Explicit parameters | Immutable by default | Explicit ownership |
| **Polymorphism** | Subtypes, interfaces | Function pointers | Higher-order functions | Traits, generics |
| **Code reuse** | Inheritance, composition | Function libraries | Function composition | Trait bounds, generics |
| **Best for** | Domain modeling, UI, business logic | Scripts, data transforms, embedded | Data pipelines, concurrency | Systems programming, performance |
| **Testing** | Mock objects, stubs | Input/output testing | Pure function testing | Integration + unit |
| **Learning curve** | Moderate (SOLID, patterns) | Low | Moderate-High (monads, functors) | High (borrow checker, lifetimes) |

## Heuristics For Choosing

1. **Start with the data flow**: If the problem is primarily about transforming data from one shape to another (ETL, API responses, reports), functional or procedural is often simpler than OO.
2. **Consider the domain complexity**: If the domain has many interacting rules with state changes (banking, booking, workflow), OO's encapsulation and polymorphism help manage complexity.
3. **Match the language's strengths**: Java/C#/C++ naturally express OO. C/Go naturally express procedural. Rust/OCaml naturally express functional+systems. Fighting the language's paradigm adds cost.
4. **Think about who maintains it**: Procedural code is easier to read for junior developers but harder to extend. OO code requires more design discipline but scales better with team size.
5. **Consider the change pattern**: If requirements change frequently and new variants appear, OO polymorphism or functional ADTs handle this well. If requirements are stable, procedural is simpler.
6. **Performance constraints**: Systems-oriented and procedural give the most predictable performance. OO has overhead from virtual dispatch and allocation. Functional can have allocation overhead from immutability.
7. **Concurrency needs**: Functional (immutability) and systems-oriented (ownership) are naturally safer for concurrency. OO requires careful design to avoid shared mutable state issues.

## Common Risks

1. **Paradigm dogmatism**: Insisting on pure OO or pure functional when the problem doesn't fit. Pragmatic mixes are usually better.
2. **Mixed-paradigm confusion**: Using OO patterns in procedural code (or vice versa) without understanding the trade-offs. Each paradigm has idioms that don't translate well.
3. **Over-engineering for flexibility**: Adding OO abstraction layers to a simple script that will never need polymorphism. Start simple, add abstraction when variation appears.
4. **Ignoring language defaults**: Every language has a "natural" paradigm. Fighting it (e.g., writing OO code in C, or procedural code in Java) creates friction.
5. **Premature paradigm shift**: Rewriting procedural code as OO (or vice versa) without clear evidence that the current paradigm is causing real problems.

## Verification

- Is the paradigm choice justified by the problem domain, not just personal preference?
- Can a new developer understand the code structure within 30 minutes?
- Are there places where the paradigm is being "fought" (e.g., workarounds for missing language features)?
- Is the testing strategy aligned with the paradigm (pure function tests for functional, mock-based for OO)?
- Would a different paradigm reduce the amount of boilerplate or ceremony?
