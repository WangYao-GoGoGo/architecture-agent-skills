# Indexing

## Use When

- Reviewing query performance, filters, joins, sort order, uniqueness, or pagination.

## Core Idea

Indexes speed specific access patterns but add write cost, storage cost, and migration risk. Add indexes for real queries, not for every column.

## Agent Heuristics

- Start from the query: equality filters, range filters, joins, sort order, and pagination.
- Prefer composite indexes that match common predicates and sort order.
- Consider uniqueness and constraints as architecture tools.
- Use explain plans when performance matters.
- Remove redundant indexes when they duplicate a broader useful index.

## Verification

- Query plan uses the intended index.
- Write overhead is acceptable.
- Pagination remains stable.

