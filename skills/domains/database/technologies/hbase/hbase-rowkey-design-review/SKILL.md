---
name: hbase-rowkey-design-review
description: Use when reviewing HBase row key design, region distribution, scan patterns, salting, time-series layout, column families, and hot spot risks.
---

# HBase Rowkey Design Review

## Workflow

1. Identify primary access and scan patterns.
2. Review row key prefix, sort order, salting, and time component placement.
3. Check region hot spots, wide rows, TTL, and column family choices.
4. Recommend row key changes only with migration impact considered.
5. Verify with distribution and scan examples.

## Output Format

```markdown
HBase rowkey review:
- Access patterns:
- Current rowkey:
- Hotspot risks:
- Recommendation:
- Migration/verification:
```
