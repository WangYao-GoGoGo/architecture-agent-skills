# Long Method

## Use When

- A method has multiple phases, nested conditionals, or mixed levels of abstraction.

## Why It Hurts

- Readers cannot see the main workflow.
- Tests must cover many unrelated branches.
- Local variables and side effects make change risky.

## Refactoring Moves

- Extract named steps.
- Separate validation, calculation, side effects, and formatting.
- Replace repeated branch logic with strategy or dispatch when variation is stable.

## Verification

- The top-level method reads like a workflow.
- Extracted methods have focused names and tests where useful.
