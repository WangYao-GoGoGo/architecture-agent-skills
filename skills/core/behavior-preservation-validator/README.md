# Behavior Preservation Validator

Checks whether refactored code preserves the behavior of the original code. Use after refactoring to verify that functionality remains the same.

## When To Use This Skill

- After refactoring existing code.
- After applying a bug fix that changes internal structure.
- Before merging a refactoring change.
- When the user asks whether behavior changed after restructuring.

Do **not** use this skill for greenfield code generation or trivial changes.

## How It Works

1. **Summarize** the refactoring.
2. **Compare** public interfaces (names, parameters, return types).
3. **Compare** input-output behavior for each relevant case.
4. **Compare** side effects (file writes, database writes, API calls, logging).
5. **Compare** error handling (same errors for same inputs).
6. **Compare** state changes.
7. **Review** regression tests.
8. **Determine** final validation result.

## Knowledge Used

- [`knowledge/refactoring/`](../../../knowledge/refactoring/README.md) — refactoring moves and their behavior-preserving properties
- [`knowledge/refactoring/characterization-tests.md`](../../../knowledge/refactoring/characterization-tests.md) — for creating characterization tests when existing tests are missing

## Output

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

## Related Skills

- [`architecture-quality-review`](../architecture-quality-review/README.md) — asks whether the architecture became better (complementary to behavior preservation).
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — asks whether the new design became unnecessarily complex.
- [`debug-report-generator`](../debug-report-generator/README.md) — to document validation results in a debug report.
