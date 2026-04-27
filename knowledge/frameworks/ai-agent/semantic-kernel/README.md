# Semantic Kernel Knowledge

## Heuristics

- Separate skills/plugins, planners, prompts, tools, memory, and host application boundaries.
- Keep plugin contracts small and explicit.
- Treat external side effects as tool boundaries with validation.
- Add evaluation for planned workflows.

## Common Risks

- Planner actions that are hard to predict.
- Plugins exposing broad host internals.
- Weak tests for multi-step agent behavior.

