# Command

## Use When

- Actions need queuing, undo, retry, logging, scheduling, or permission checks.
- UI, API, or job code should treat operations uniformly.

## Avoid When

- A direct method call is enough and actions do not need to be stored or composed.

## Core Idea

Represent an action as an object or function with a consistent execution interface.

## Agent Heuristics

- Use for workflows that must be delayed or retried.
- Pair with transaction or idempotency rules when commands change state.
- Keep commands focused on one action.
