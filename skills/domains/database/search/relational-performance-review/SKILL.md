---
name: search-relational-performance-review
description: Use when reviewing search-like relational queries, full-text search, filtering, ranking, pagination, indexes, and when to move to a search engine.
---

# Search Relational Performance Review

## Workflow

1. Identify search requirements: full text, filters, ranking, facets, sorting, pagination.
2. Review current relational query and index support.
3. Check whether database-native full-text features are enough.
4. Recommend relational tuning or a search index only when justified.
5. Verify with query plans and relevance examples.

## Output Format

```markdown
Search performance review:
- Search requirements:
- Current query/index shape:
- Recommendation:
- Migration risk:
- Verification:
```
