# Knowledge Card Template

```markdown
# Concept Name

## Use When

- Situation where this concept helps.
- Design pressure it addresses.

## Avoid When

- Situation where this concept adds needless complexity.

## Core Idea

Short explanation in practical engineering language.

## Agent Heuristics

- If you see <signal>, consider this concept.
- If the code only has <small case>, keep it simple.

## Refactoring Moves

1. Preserve behavior with tests or characterization checks.
2. Isolate the responsibility or variation point.
3. Introduce the smallest useful boundary.
4. Move callers gradually.

## Verification

- Behavior remains unchanged.
- New structure has clearer ownership.
- Tests can target the responsibility directly.
```
