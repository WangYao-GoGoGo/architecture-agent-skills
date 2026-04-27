# Decorator

## Use When

- Behavior should be added around an object without changing the object.
- Cross-cutting additions like logging, metrics, retries, caching, or authorization can be composed.

## Avoid When

- The added behavior is essential domain logic that should be explicit.
- Composition order would be surprising or fragile.

## Core Idea

Wrap an object with another object that has the same interface and adds behavior before or after delegation.
