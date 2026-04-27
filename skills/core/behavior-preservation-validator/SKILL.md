---
name: behavior-preservation-validator
description: Use after refactoring to check whether the refactored code preserves the original behavior — public API, input-output, side effects, error handling, and state changes.
---

# Behavior Preservation Validator

Use this skill after refactoring existing code to verify that behavior is preserved.

## When To Use

- After refactoring existing code.
- After applying a bug fix that changes internal structure.
- Before merging a refactoring change.
- When the user asks whether behavior changed after restructuring.

Do **not** use this skill for greenfield code generation or for trivial changes where behavior preservation is obvious.

## Inputs To Inspect

- Original code (before refactoring)
- Refactored code (after refactoring)
- Public API signatures (before and after)
- Test results (if available)
- Input/output examples
- Side effect descriptions

## Knowledge To Use

- [`knowledge/refactoring/`](../../../knowledge/refactoring/README.md) — refactoring moves and their behavior-preserving properties
- [`knowledge/refactoring/characterization-tests.md`](../../../knowledge/refactoring/characterization-tests.md) — for creating characterization tests when existing tests are missing

## Workflow

1. **Summarize the refactoring.** What changed and why?
2. **Compare public interfaces.** Are function/method names, parameters, and return types the same?
3. **Compare input-output behavior.** For each relevant input case, does the output match?
4. **Compare side effects.** Do file writes, database writes, API calls, logging, or cache updates behave the same?
5. **Compare error handling.** Do the same inputs produce the same errors or exceptions?
6. **Compare state changes.** Does internal or external state change in the same way?
7. **Review regression tests.** What tests were run or should be run?
8. **Determine final validation result.** Is behavior preserved, changed, or unknown?

## Decision Rules

- Public API compatibility is mandatory unless the user explicitly requests an API change.
- Input-output behavior must match for all documented cases.
- Side effects must match unless the refactoring intentionally changes them.
- Error handling must match — new errors should not appear for previously working inputs.
- If tests cannot be run, use static reasoning to compare behavior.
- If behavior is changed, document what changed and why.

## Output Format

```markdown
# Behavior Preservation Report

## 1. Refactoring Summary

## 2. Public Interface Comparison

## 3. Input-Output Behavior

## 4. Side Effects

## 5. Error Handling

## 6. State Changes

## 7. Regression Tests

## 8. Final Validation Result
```

## Stop Conditions

- Public interfaces are compared.
- Input-output behavior is verified (by test or reasoning).
- Side effects and error handling are reviewed.
- Final validation result is documented.
