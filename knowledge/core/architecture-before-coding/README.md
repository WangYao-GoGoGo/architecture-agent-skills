# Architecture Before Coding Knowledge

## Use When

Implementing a new feature or non-trivial code change where responsibilities, boundaries, interfaces, data flow, and verification should be designed before writing code.

## Heuristics

- Inspect the existing codebase and identify local conventions before proposing structure.
- State the feature goal in one or two sentences.
- Identify responsibilities and assign an owner for each one.
- Define boundaries: public interfaces, internal helpers, data models, external services, persistence, and side effects.
- Decide whether a known pattern is justified. If unsure, prefer the simpler structure.
- Propose the smallest implementation sequence that keeps behavior verifiable.
- Use Strategy when behavior varies by type, mode, policy, or provider.
- Use Factory Method or Abstract Factory when object creation varies and callers should not know concrete classes.
- Use Builder when construction has many optional parts or validation steps.
- Use Adapter when integrating an incompatible external interface.
- Use Facade when callers need a simpler boundary over a complex subsystem.
- If none of these conditions is present, use plain classes or functions with clear names.

## Common Risks

- Designing for every possible future instead of the current requirement.
- Adding interfaces, factories, or abstractions before there is a second implementation.
- Making the design sketch too detailed, defeating its purpose as a lightweight planning tool.
- Skipping the architecture pass entirely for features that clearly need it.
