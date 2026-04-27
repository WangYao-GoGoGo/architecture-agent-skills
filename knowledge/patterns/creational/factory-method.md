# Factory Method

## Use When

- A class or module needs a hook for creating concrete objects.
- Callers should depend on a common type and not know construction details.

## Avoid When

- There is only one concrete type and no construction variation.

## Core Idea

Move object creation behind a method that can choose or be overridden.
