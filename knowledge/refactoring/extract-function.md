# Extract Function

## Use When

- A function or method mixes multiple phases or abstraction levels.

## Core Idea

Move a coherent step into a named function so the caller reads like a workflow.

## Agent Heuristics

- Extract around a domain concept, not arbitrary lines.
- Keep inputs and outputs explicit.
- Avoid extracting functions that need many mutable parameters.

