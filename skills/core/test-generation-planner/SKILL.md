---
name: test-generation-planner
description: Use before or after code changes to identify the minimal set of tests needed to validate behavior, covering normal input, edge cases, error handling, and side effects.
---

# Test Generation Planner

Use this skill to plan minimal tests for generated, modified, or refactored code.

## When To Use

- New code has been generated.
- Existing code has been refactored.
- A bug fix has been applied.
- Behavior preservation needs to be checked.
- An example should include executable validation.

Do **not** use this skill for generating a full test suite by default. Prefer a small, meaningful regression test set.

## Inputs To Inspect

- Source code (before and after changes)
- Public API signatures
- Existing tests, if any
- Error handling paths
- Side effects (file writes, database queries, API calls)
- Input/output contracts

## Knowledge To Use

- [`knowledge/refactoring/characterization-tests.md`](../../../knowledge/refactoring/characterization-tests.md) — for characterizing existing behavior when tests are missing
- [`knowledge/principles/`](../../../knowledge/principles/README.md) — for understanding testability principles

## Workflow

1. **Identify behavior to validate.** List the public behaviors that must work correctly.
2. **Review existing test coverage.** What is already tested? What is missing?
3. **List missing test cases.** Cover normal input, empty input, invalid input, boundary values, and error cases.
4. **Define the minimal test set.** Choose the smallest number of tests that provide meaningful coverage.
5. **Describe test data.** What inputs are needed for each test?
6. **Define commands to run.** How to execute the tests.
7. **Describe expected results.** What should pass or fail.

## Decision Rules

- Prefer a small, meaningful regression test set over exhaustive coverage.
- Include at least one normal case, one edge case, and one error case.
- If the code has side effects (database, file system, API), test that they occur correctly.
- If tests cannot be run, describe the expected behavior and validation strategy clearly.
- Do not generate tests for trivial getters/setters unless they contain logic.

## Output Format

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

## Stop Conditions

- Minimal test set is defined.
- Test data is described.
- Commands and expected results are documented.
