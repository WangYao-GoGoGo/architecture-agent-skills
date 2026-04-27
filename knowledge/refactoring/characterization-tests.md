# Characterization Tests

## Use When

- Existing behavior is important but unclear.
- Refactoring risky code without adequate tests.

## Core Idea

Characterization tests capture what the system currently does before changing structure. They protect behavior even when the behavior is imperfect.

## Agent Heuristics

- Cover important happy paths, edge cases, and known bugs.
- Keep tests close to public behavior.
- Avoid locking down incidental implementation details.
- Use focused examples when full test setup is too expensive.

