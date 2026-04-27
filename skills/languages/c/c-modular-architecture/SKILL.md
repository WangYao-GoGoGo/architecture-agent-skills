---
name: c-modular-architecture
description: Use when refactoring C code into modules with clear ownership, file boundaries, state management, resource lifecycle, and testable functions.
---

# C Modular Architecture

## Workflow

1. Identify modules, shared state, resources, and call graph.
2. Separate public headers from private implementation details.
3. Move global state into explicit context structures where useful.
4. Separate pure logic from I/O and platform calls.
5. Verify with unit tests or small executable checks.

## Output Format

```markdown
C modular refactor:
- Module ownership:
- Public/private boundary:
- State and resources:
- Steps:
- Verification:
```
