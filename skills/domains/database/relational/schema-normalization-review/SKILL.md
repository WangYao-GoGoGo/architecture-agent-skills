---
name: schema-normalization-review
description: Use when reviewing relational schema normalization, denormalization, constraints, duplication, update anomalies, and query-driven tradeoffs.
---

# Schema Normalization Review

## Workflow

1. Identify entities, relationships, keys, constraints, and duplicated facts.
2. Check for update, insert, and delete anomalies.
3. Compare normalization benefits against query and operational needs.
4. Recommend normalization or intentional denormalization with ownership rules.
5. Include migration and verification steps.

## Output Format

```markdown
Normalization review:
- Model issues:
- Anomaly risks:
- Recommended schema:
- Denormalization tradeoffs:
- Verification:
```
