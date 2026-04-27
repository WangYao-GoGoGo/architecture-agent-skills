---
name: key-value-access-pattern-review
description: Use when reviewing key-value database access patterns, key design, TTLs, partitioning, hot keys, consistency, and read/write paths.
---

# Key-Value Access Pattern Review

## Workflow

1. Identify key shape, value shape, read/write paths, and TTL.
2. Check hot keys, partition distribution, atomicity, and consistency needs.
3. Determine whether the store is source of truth or derived data.
4. Recommend key and value structure changes.
5. Verify with load, consistency, and failure checks.

## Output Format

```markdown
Key-value review:
- Access pattern:
- Key/value shape:
- Consistency and TTL:
- Risks:
- Recommendation:
```
