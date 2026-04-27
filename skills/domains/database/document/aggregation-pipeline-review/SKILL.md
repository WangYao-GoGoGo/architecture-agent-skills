---
name: aggregation-pipeline-review
description: Use when reviewing document database aggregation pipelines for stage order, filtering, grouping, lookups, indexes, memory use, and maintainability.
---

# Aggregation Pipeline Review

## Workflow

1. Identify pipeline purpose and expected output shape.
2. Review stage order, early filtering, projections, grouping, sorting, and lookups.
3. Check index support and memory limits.
4. Look for business rules hidden in unreadable pipelines.
5. Recommend clearer stages and verification with sample data.

## Output Format

```markdown
Aggregation review:
- Goal:
- Stage issues:
- Performance risks:
- Recommendation:
- Verification:
```
