# Template Method

## Use When

- An algorithm sequence is stable, but several steps vary.
- Subclasses or implementations should fill in specific steps.

## Avoid When

- The sequence is not stable.
- Composition or Strategy would make variation clearer.

## Core Idea

Put the fixed algorithm skeleton in one place and delegate variable steps to overridable methods.

## Risk

Inheritance can hide control flow. Prefer this pattern only when the skeleton is genuinely stable.
