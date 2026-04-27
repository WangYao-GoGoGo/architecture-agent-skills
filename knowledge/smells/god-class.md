# God Class

## Use When

- One class or module coordinates many unrelated responsibilities.
- Many changes across the project require editing the same file.

## Why It Hurts

- Hidden coupling grows around one central object.
- Tests require too much setup.
- Ownership becomes unclear.

## Refactoring Moves

1. Identify clusters of behavior that change together.
2. Extract one responsibility behind a clear interface or helper.
3. Move data and behavior together when possible.
4. Keep a thin coordinator only if orchestration is still needed.

## Avoid

- Splitting everything at once.
- Creating many anemic classes that only move data around.
