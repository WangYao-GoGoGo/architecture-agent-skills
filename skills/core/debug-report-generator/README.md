# Debug Report Generator

Generates a human-readable debugging report after a bug fix or validation task. Use to summarize the original problem, root cause, fix, validation results, and remaining risks.

## When To Use This Skill

- After a runtime error is diagnosed and fixed.
- After tests are run to validate a fix.
- After a behavior-preserving refactor is checked.
- When the user asks for a summary of debugging work.

Do **not** use this skill during active debugging — use [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) first.

## How It Works

1. **Describe** the original problem.
2. **Explain** the root cause.
3. **Summarize** the fix.
4. **List** files changed.
5. **Document** validation commands and results.
6. **Note** behavior preservation.
7. **List** remaining risks and follow-up recommendations.

## Knowledge Used

- [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) — for the diagnosis phase
- [`test-generation-planner`](../test-generation-planner/README.md) — for the test planning phase
- [`behavior-preservation-validator`](../behavior-preservation-validator/README.md) — for the validation phase

## Output

```markdown
# Debug Report

## 1. Original Problem

## 2. Root Cause

## 3. Fix Summary

## 4. Files Changed

## 5. Validation Commands

## 6. Validation Results

## 7. Behavior Preservation Notes

## 8. Remaining Risks

## 9. Follow-up Recommendations
```

## Related Skills

- [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) — to diagnose errors before generating a report.
- [`test-generation-planner`](../test-generation-planner/README.md) — to plan tests whose results feed into the report.
- [`behavior-preservation-validator`](../behavior-preservation-validator/README.md) — to verify behavior preservation for the report.
