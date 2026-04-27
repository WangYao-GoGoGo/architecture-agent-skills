# Extract Class

## Use When

- One class or module owns multiple responsibilities that change independently.

## Core Idea

Move one responsibility and its data into a separate class or module with a clear name.

## Agent Heuristics

- Extract one responsibility at a time.
- Move behavior with the data it needs.
- Keep the original class as a thin coordinator only if orchestration remains useful.

