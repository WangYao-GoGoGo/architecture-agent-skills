# Strategy

## Use When

- Behavior varies by type, provider, policy, mode, or runtime choice.
- A large conditional repeats the same shape across multiple places.
- Each variation has enough rules to deserve independent tests.

## Avoid When

- There are only one or two simple branches with no expected growth.
- The variation is purely data and can be handled with a lookup table.

## Core Idea

Define a common behavior interface and move each variation into its own implementation. The caller chooses or receives the strategy.

## Refactoring Moves

1. Add tests or characterization checks for each branch.
2. Extract one branch into a strategy.
3. Introduce a selector, factory, or dependency injection point.
4. Move remaining branches.
5. Remove the old conditional.

## Verification

- Existing branches return the same results.
- New behavior can be added without editing the coordinator.
