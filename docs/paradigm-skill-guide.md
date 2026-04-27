# Paradigm Skill Guide

Paradigm skills explain how to structure code according to a programming model.

## Supported Paradigm Packs

- Object-oriented: responsibilities, objects, encapsulation, polymorphism, SOLID, GRASP.
- Procedural: modules, functions, explicit data ownership, side-effect control.
- Functional: pure transformations, immutable flow, composition, error modeling.
- Systems-oriented: resource ownership, lifecycle, concurrency, failure handling.

## How To Write A Paradigm Skill

1. Start from the code's current dominant paradigm.
2. Avoid forcing another paradigm unless the user asks or the code is clearly suffering.
3. Define ownership rules for state, behavior, and dependencies.
4. Name common smells for that paradigm.
5. Provide refactoring moves that preserve behavior.

## Output Expectations

Paradigm skills should explain:

- what paradigm pressure exists
- what structure fits the codebase
- what tradeoff the structure introduces
- how to verify the result
