---
name: runtime-error-diagnosis
description: Use when code fails to run, throws an exception, produces an error log, or a build/test command fails — diagnose the root cause and suggest the smallest safe fix.
---

# Runtime Error Diagnosis

Use this skill when code fails at runtime and you need to identify the root cause before fixing it.

## When To Use

- The user provides an error message or stack trace.
- The code throws an exception.
- A build or test command fails.
- A tool reports a runtime error.
- The program runs but produces obviously wrong output.

Do **not** use this skill for static code analysis, code smells, or design reviews without a specific runtime failure.

## Inputs To Inspect

- Error message, stack trace, or exception type
- Failing command and its full output
- Relevant source file and line number from the error
- Input data that triggers the failure
- Environment context (language version, OS, dependencies)

## Knowledge To Use

- [`knowledge/languages/`](../../../knowledge/languages/README.md) — language-specific error patterns
- [`knowledge/frameworks/`](../../../knowledge/frameworks/README.md) — framework-specific error handling
- [`knowledge/refactoring/`](../../../knowledge/refactoring/README.md) — if the fix involves refactoring

## Workflow

1. **Identify the failing operation.** What command, function call, or query produced the error?
2. **Extract the exact error message.** Get the full text, not just a summary.
3. **Locate the failing file and line.** Use the stack trace or error output to find the exact location.
4. **Distinguish root cause from downstream symptoms.** The first error in a stack trace is often the root cause; subsequent errors may be cascading failures.
5. **Form a hypothesis.** What is the most likely root cause based on the error and the code?
6. **Suggest the smallest safe fix.** Prefer a minimal change that addresses the root cause without rewriting unrelated code.
7. **Propose validation commands.** Tell the user how to verify the fix works.

## Decision Rules

- Do **not** rewrite unrelated code while diagnosing a runtime error.
- Do **not** change public interfaces unless the bug is in the interface itself.
- If multiple errors appear, focus on the first one — later errors are often consequences.
- If the error is intermittent, consider race conditions, timing, or resource leaks.
- If the error is environment-specific, check dependency versions and configuration.

## Output Format

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

## Stop Conditions

- Root cause is identified and documented.
- Minimal fix is proposed.
- Validation steps are defined.
