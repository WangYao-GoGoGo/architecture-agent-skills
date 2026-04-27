# Singleton

## Use When

- A process truly needs one shared instance, and lifecycle is controlled.
- The shared object is stateless or safely manages concurrency.

## Avoid When

- It is being used to avoid dependency injection.
- Tests need isolated state.
- The instance hides configuration, time, network, or mutable global state.

## Core Idea

Ensure a single instance is used. Treat this as a lifecycle decision, not a convenience shortcut.

## Agent Warning

Prefer explicit dependency injection for most services. Singleton often makes tests and configuration harder.
