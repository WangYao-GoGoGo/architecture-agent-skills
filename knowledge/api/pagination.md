# Pagination

## Use When

- Designing APIs that return lists, search results, feeds, or reports.

## Core Idea

Pagination is part of the API contract and data access architecture. It must define ordering, stability, limits, and filtering behavior.

## Agent Heuristics

- Prefer cursor pagination for large or changing datasets.
- Use stable sort keys.
- Define maximum page size.
- Keep filters aligned with indexes.
- Avoid offset pagination for deep pages on large tables unless acceptable.

## Verification

- Results do not duplicate or skip unexpectedly.
- Query plan supports filters and sort order.
- Clients can detect next/previous page availability.

