---
name: hibernate-entity-and-fetch-review
description: Use when reviewing Hibernate entity mapping, fetch strategies, lazy loading, cascading, dirty checking, and transaction boundaries.
---

# Hibernate Entity & Fetch Review

## When To Use

- The main decision is about Hibernate entity design, fetch plan optimization, lazy/eager loading strategy, or cascade configuration.
- Reviewing N+1 query behavior, transaction boundaries, or persistence context management.

## Workflow

1. Identify the entity model — relationships, fetch types, and cascade settings.
2. Review fetch plans — are lazy associations loaded within the transaction scope?
3. Check for N+1 query patterns — use batch fetching, join fetch, or entity graphs.
4. Review cascade configuration — is cascading scoped appropriately?
5. Check dirty checking and flush behavior — are large collections or long transactions problematic?
6. Review transaction boundaries — are they aligned with use case boundaries?
7. Recommend the smallest structural change that improves performance or correctness.

## Output Format

```markdown
Hibernate review:
- Entity model & relationships:
- Fetch plans:
- N+1 query analysis:
- Cascade configuration:
- Dirty checking:
- Transaction boundaries:
- Recommended change:
- Verification:
```
