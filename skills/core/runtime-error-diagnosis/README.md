# Runtime Error Diagnosis

Diagnoses code that fails at runtime. Use when code throws an exception, a build fails, or the program produces wrong output.

## When To Use This Skill

- The user provides an error message or stack trace.
- The code throws an exception at runtime.
- A build or test command fails.
- The program runs but produces obviously incorrect output.

Do **not** use this skill for static analysis, code smells, or design reviews without a specific runtime failure.

## How It Works

1. **Identify** the failing command or operation.
2. **Extract** the exact error message.
3. **Locate** the likely failing file, function, method, or query.
4. **Distinguish** root cause from downstream symptoms.
5. **Suggest** the smallest safe fix first.
6. **Avoid** rewriting unrelated code.
7. **Propose** validation commands after the fix.

## Knowledge Used

- [`knowledge/languages/`](../../../knowledge/languages/README.md) — language-specific error patterns
- [`knowledge/frameworks/`](../../../knowledge/frameworks/README.md) — framework-specific error handling

## Output

```markdown
# Runtime Error Diagnosis

## 1. Error Summary

## 2. Reproduction Context

## 3. Most Likely Root Cause

## 4. Evidence

## 5. Minimal Fix

## 6. Files Likely Affected

## 7. Validation Steps

## 8. Remaining Risks
```

## Related Skills

- [`test-generation-planner`](../test-generation-planner/README.md) — to plan tests after fixing a runtime error.
- [`debug-report-generator`](../debug-report-generator/README.md) — to generate a human-readable debugging report after diagnosis and fix.
- [`behavior-preservation-validator`](../behavior-preservation-validator/README.md) — to verify the fix did not change existing behavior.
