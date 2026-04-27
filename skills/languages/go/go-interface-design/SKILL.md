---
name: go-interface-design
description: Use when reviewing Go interface boundaries, dependency inversion, mock strategy, and package coupling.
---

# Go Interface Design

## When To Use
- The main decision is about where to define interfaces, how many methods they should have, and how they affect testability.
- Reviewing package dependency direction and interface segregation.

## Workflow
1. Identify where interfaces are defined — consumer side (preferred) vs producer side.
2. Review interface size — are they small (1-3 methods) and focused?
3. Check for interface satisfaction — do concrete types implicitly satisfy interfaces?
4. Review testability — can interfaces be easily mocked or stubbed?
5. Check for package coupling — do interfaces create unwanted dependencies?
6. Review naming — are interfaces named for their behavior (e.g., `Reader`, `Writer`)?
7. Recommend interface boundaries that minimize coupling and maximize testability.

## Output Format
```markdown
Go interface review:
- Interface locations:
- Interface size & focus:
- Implicit satisfaction:
- Testability:
- Package coupling:
- Recommended change:
- Verification:
```
