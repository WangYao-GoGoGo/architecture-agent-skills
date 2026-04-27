---
name: database-architecture-review
description: Use when reviewing database architecture, data ownership, read/write paths, consistency, transactions, indexing, migrations, caching, and operational risks.
---

# Database Architecture Review

## Workflow

1. Identify data owners, read paths, write paths, and consistency needs.
2. Review schema/model shape against access patterns.
3. Check transaction boundaries, indexing, migration risks, and cache interaction.
4. Identify operational constraints: volume, latency, backup, observability, retention.
5. Recommend the smallest data architecture change.

## Output Format

```markdown
Database architecture review:
- Data ownership:
- Access patterns:
- Consistency and transactions:
- Indexing and migration risks:
- Recommended changes:
- Verification:
```
