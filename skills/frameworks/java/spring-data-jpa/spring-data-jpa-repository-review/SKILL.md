---
name: spring-data-jpa-repository-review
description: Use when reviewing Spring Data JPA repository design, derived queries, entity boundaries, transactions, pagination, and query performance.
---

# Spring Data JPA Repository Review

## When To Use

- The main decision is about Spring Data JPA repository boundaries, derived query methods, entity associations, or transaction scoping.
- Reviewing N+1 queries, pagination strategy, or query performance.

## Workflow

1. Identify the repository structure — entity types, repository interfaces, and custom query methods.
2. Review derived query method names for readability and performance impact.
3. Check entity relationships and fetch strategies — are lazy associations handled properly?
4. Review transaction boundaries — `@Transactional` placement and propagation.
5. Check pagination and sorting — are they used correctly with large datasets?
6. Review custom `@Query` definitions for SQL correctness and performance.
7. Recommend the smallest structural change that improves clarity or performance.

## Output Format

```markdown
Spring Data JPA review:
- Repository structure:
- Derived query methods:
- Entity relationships:
- Transaction boundaries:
- Pagination:
- Custom queries:
- Recommended change:
- Verification:
```
