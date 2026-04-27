# Test Generation Planner

Plans minimal tests for generated, modified, or refactored code. Use before or after code changes to identify the smallest set of tests needed to validate behavior.

## When To Use This Skill

- New code has been generated and needs validation.
- Existing code has been refactored and behavior must be checked.
- A bug fix has been applied and needs regression tests.
- An example should include executable validation.

Do **not** use this skill for generating a full test suite by default. Prefer a small, meaningful regression test set.

## How It Works

1. **Identify** the behavior to validate.
2. **Review** existing test coverage.
3. **List** missing test cases (normal, empty, invalid, boundary, error).
4. **Define** the minimal test set.
5. **Describe** test data and commands.
6. **Document** expected results.

## Knowledge Used

- [`knowledge/refactoring/characterization-tests.md`](../../../knowledge/refactoring/characterization-tests.md) — for characterizing existing behavior when tests are missing
- [`knowledge/principles/`](../../../knowledge/principles/README.md) — for understanding testability principles

## Output

```markdown
# Test Generation Plan

## 1. Behavior to Validate

## 2. Existing Test Coverage

## 3. Missing Test Cases

## 4. Minimal Test Set

## 5. Edge Cases

## 6. Test Data

## 7. Commands to Run

## 8. Expected Results
```

## Related Skills

- [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) — to diagnose errors before writing tests.
- [`behavior-preservation-validator`](../behavior-preservation-validator/README.md) — to verify behavior preservation after refactoring.
- [`debug-report-generator`](../debug-report-generator/README.md) — to document test results in a debug report.
