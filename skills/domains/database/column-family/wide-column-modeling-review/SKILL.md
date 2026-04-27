---
name: wide-column-modeling-review
description: Use when reviewing wide-column or column-family data models for row keys, column families, access patterns, partitioning, hot spots, time-series data, and denormalization.
---

# Wide-Column Modeling Review

## Workflow

1. Identify access patterns and query keys.
2. Review row key design, partition distribution, column families, and sort order.
3. Check hot partitions, wide rows, TTLs, and compaction impact.
4. Confirm denormalization is intentional and update paths are clear.
5. Recommend model changes with operational tradeoffs.

## Output Format

```markdown
Wide-column review:
- Access patterns:
- Row key/partition design:
- Hot spot risks:
- Recommendation:
- Verification:
```
