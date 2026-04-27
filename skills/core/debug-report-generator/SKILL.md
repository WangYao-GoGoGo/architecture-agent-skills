---
name: debug-report-generator
description: Use after a bug fix or validation task to generate a human-readable debugging report summarizing the original problem, root cause, fix, validation results, and remaining risks.
---

# Debug Report Generator

Use this skill after a bug fix or validation task to produce a structured, human-readable debugging report.

## When To Use

- After a runtime error is diagnosed and fixed.
- After tests are run to validate a fix.
- After a behavior-preserving refactor is checked.
- When the user asks for a summary of debugging work.

Do **not** use this skill during active debugging — use [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) first.

## Inputs To Inspect

- Original error or problem description
- Root cause analysis
- Fix description and files changed
- Validation commands and their output
- Behavior preservation notes
- Remaining risks

## Knowledge To Use

- [`runtime-error-diagnosis`](../runtime-error-diagnosis/README.md) — for the diagnosis phase
- [`test-generation-planner`](../test-generation-planner/README.md) — for the test planning phase
- [`behavior-preservation-validator`](../behavior-preservation-validator/README.md) — for the validation phase

## Workflow

1. **Describe the original problem.** What was the bug, error, or failing behavior?
2. **Explain the root cause.** What was the underlying cause?
3. **Summarize the fix.** What was changed and why?
4. **List files changed.** Which files were modified, added, or deleted?
5. **Document validation commands.** What commands were run to verify the fix?
6. **Report validation results.** Did the commands pass or fail?
7. **Note behavior preservation.** Did the fix change any existing behavior?
8. **List remaining risks.** What could still go wrong?
9. **Provide follow-up recommendations.** What should be done next?

## Decision Rules

- Be honest about what was verified and what was not.
- Do not claim tests passed unless they were actually run.
- If runtime validation is not possible, explain why.
- Use clear validation level labels: `Static reasoning only`, `Test-based validation`, `Golden master comparison`.

## Output Format

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

## Stop Conditions

- Original problem is described.
- Root cause and fix are documented.
- Validation results are reported.
- Remaining risks and follow-up recommendations are listed.
