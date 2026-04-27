---
name: service-boundary-review
description: Use when reviewing backend service boundaries, ownership, module/service splits, domain logic placement, transactions, integrations, and operational responsibilities.
---

# Service Boundary Review

## Workflow

1. Identify the business capability and data owned by each service or module.
2. Map synchronous calls, async events, database access, and cache use.
3. Check whether boundaries follow ownership or only technical layers.
4. Identify transaction, consistency, and failure-mode risks.
5. Recommend the smallest boundary change that reduces coupling.
6. Include migration and verification steps.

## Output Format

```markdown
Service boundary review:
- Ownership:
- Coupling:
- Data and transaction boundary:
- Recommended change:
- Verification:
```
