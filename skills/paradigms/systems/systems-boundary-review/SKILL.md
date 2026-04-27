---
name: systems-boundary-review
description: Use when reviewing systems-oriented code for resource ownership, concurrency, lifecycle, error handling, failure isolation, and observability boundaries.
---

# Systems Boundary Review

Use this skill when architecture depends on runtime behavior, resource ownership, and failure modes.

## Workflow

1. Identify owned resources: memory, files, sockets, connections, locks, processes, threads, buffers.
2. Map lifecycle: create, use, release, retry, shutdown.
3. Check concurrency boundaries and shared state.
4. Identify failure modes and observability points.
5. Recommend explicit ownership and cleanup rules.
6. Verify with tests, stress checks, or failure-path review.

## Output Format

```markdown
Systems boundary review:
- Resource ownership:
- Concurrency risks:
- Failure modes:
- Boundary changes:
- Verification:
```
