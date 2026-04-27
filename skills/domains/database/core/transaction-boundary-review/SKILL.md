---
name: transaction-boundary-review
description: Use when reviewing transaction boundaries, consistency guarantees, isolation levels, retries, idempotency, distributed writes, and failure behavior.
---

# Transaction Boundary Review

## Workflow

1. Identify the business invariant that must remain consistent.
2. Map all reads and writes in the workflow.
3. Check transaction scope, isolation needs, locks, retries, and idempotency.
4. Identify cross-service or cross-database writes.
5. Recommend a consistency strategy and verification checks.

## Output Format

```markdown
Transaction review:
- Invariant:
- Read/write set:
- Boundary issues:
- Recommended strategy:
- Failure handling:
- Verification:
```
