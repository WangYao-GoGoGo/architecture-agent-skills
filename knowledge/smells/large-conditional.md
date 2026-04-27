# Large Conditional

## Use When

- A function or method branches repeatedly by type, mode, provider, status, or feature.

## Why It Hurts

- Adding a new case requires editing the same conditional.
- Branches often mix validation, behavior, and side effects.
- Tests become broad and brittle.

## Refactoring Options

- Strategy when behavior varies by runtime selection.
- Polymorphism when each type owns stable behavior.
- Lookup table or dispatch map for simple data-driven cases.
- Keep the conditional when there are only a few stable cases and no duplication.

## Verification

- Existing cases still behave the same.
- Unknown cases still fail predictably.
- New cases can be added with fewer edits.
