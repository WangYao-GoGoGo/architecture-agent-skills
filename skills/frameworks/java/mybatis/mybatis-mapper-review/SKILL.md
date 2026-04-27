---
name: mybatis-mapper-review
description: Use when reviewing MyBatis mapper boundaries, SQL ownership, result maps, dynamic SQL, transactions, and query maintainability.
---

# MyBatis Mapper Review

## When To Use

- The main decision is about MyBatis mapper design, SQL organization, dynamic SQL complexity, or result map alignment.
- Reviewing transaction boundaries, injection safety, or query performance.

## Workflow

1. Identify the mapper structure — XML vs annotation, SQL ownership, and separation of concerns.
2. Review dynamic SQL for readability and injection safety — `<if>`, `<choose>`, `<foreach>` usage.
3. Check result maps — are they aligned with API/domain shape or leaking DB structure?
4. Review transaction boundaries — are they at the service layer, not in mappers?
5. Check complex queries with representative data and execution plans.
6. Review pagination and collection handling.
7. Recommend the smallest structural change that improves maintainability or safety.

## Output Format

```markdown
MyBatis mapper review:
- Mapper structure:
- Dynamic SQL safety:
- Result map alignment:
- Transaction boundaries:
- Query performance:
- Pagination:
- Recommended change:
- Verification:
```
