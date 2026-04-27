---
name: api-architecture-review
description: Use when reviewing API design, request/response shape, versioning, error contracts, pagination, idempotency, compatibility, and client/server boundaries.
---

# API Architecture Review

## Workflow

1. Identify API consumers and compatibility requirements.
2. Review resource names, request shape, response shape, errors, pagination, filtering, and idempotency.
3. Check whether API contracts leak internal persistence or framework details.
4. Identify versioning and migration concerns.
5. Recommend contract changes with backward compatibility in mind.

## Output Format

```markdown
API review:
- Consumers:
- Contract issues:
- Compatibility risks:
- Recommended shape:
- Verification:
```
