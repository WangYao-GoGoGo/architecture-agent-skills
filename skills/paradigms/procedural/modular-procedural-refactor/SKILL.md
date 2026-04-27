---
name: modular-procedural-refactor
description: Use when refactoring procedural code into clearer modules, functions, data ownership boundaries, and side-effect boundaries without forcing object-oriented design.
---

# Modular Procedural Refactor

Use this skill when procedural code should become more maintainable while staying procedural.

## Workflow

1. Identify the main data structures and the functions that operate on them.
2. Separate pure calculation from I/O and side effects.
3. Group functions by data ownership or workflow responsibility.
4. Move global state behind explicit parameters or a small context structure.
5. Keep module interfaces narrow.
6. Verify behavior with existing tests or focused examples.

## Output Format

```markdown
Procedural refactor:
- Data ownership:
- Side effects:
- Module boundaries:
- Steps:
- Verification:
```
