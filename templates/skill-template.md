# Skill Template

```markdown
---
name: short-task-name
description: Use when the agent needs to <specific job>. Mention triggers, inputs, target domains, and when this skill should be preferred over nearby skills.
---

# Human Readable Skill Name

One short paragraph explaining the job this skill performs.

## When To Use

- Trigger condition 1.
- Trigger condition 2.
- Trigger condition 3.

Do not use this skill for <clear non-goal>.

## Inputs To Inspect

- Existing files, modules, schemas, or APIs.
- Tests, examples, logs, or docs.
- Relevant project conventions.

## Workflow

1. Inspect the current structure before proposing changes.
2. Name the architecture pressure or design problem.
3. Choose the smallest useful structure.
4. Plan changes in behavior-preserving steps.
5. Implement only after the plan is clear.
6. Verify with tests, focused checks, or review criteria.

## Decision Rules

- Rule that guides selection.
- Rule that prevents overengineering.
- Rule that preserves local conventions.

## Output Format

```markdown
Diagnosis:
- ...

Recommended design:
- ...

Implementation plan:
- ...

Verification:
- ...

Overengineering check:
- ...
```
```
