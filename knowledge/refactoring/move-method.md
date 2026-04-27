# Move Method

## Use When

- A method mostly uses data or behavior from another object or module.

## Core Idea

Move behavior to the unit that owns the relevant information or policy.

## Agent Heuristics

- Check callers before moving public methods.
- Preserve API compatibility when many callers exist.
- Prefer moving domain rules closer to domain data.

