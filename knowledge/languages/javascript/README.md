# JavaScript Architecture Idioms

## Use When

- Reviewing frontend or Node.js JavaScript without TypeScript.
- Refactoring modules, async workflows, shared utilities, or UI state.

## Heuristics

- Keep module exports small and intentional.
- Separate async side effects from pure transformation code.
- Prefer explicit validation at API and configuration boundaries.
- Avoid hidden mutation in shared objects.
- Use JSDoc or runtime schemas when type information would prevent mistakes.

## Common Risks

- Utility modules becoming dumping grounds.
- Promise chains hiding error paths.
- Framework lifecycle code mixed with domain rules.
- Runtime shape assumptions without validation.

