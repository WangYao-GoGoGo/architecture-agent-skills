# Debug Report: N+1 to DataLoader

## 1. Original Problem

The `Post.author` resolver fetches each author with a separate database query. Querying 10 posts results in 11 queries (1 for posts + 10 for authors). This is the classic N+1 problem.

## 2. Root Cause

Per-row resolver execution — GraphQL calls the `author` resolver once per post, each triggering a separate database query.

## 3. Fix Summary

Added DataLoader to batch and cache author queries:

- Created an `AuthorLoader` that batches author IDs.
- The `author` resolver uses the loader instead of direct queries.
- 10 posts now require only 2 queries (1 for posts + 1 for authors).

## 4. Files Changed

| File | Change |
|---|---|
| `before/resolvers.js` | Original — N+1 queries |
| `after/resolvers.js` | Refactored — DataLoader batching |

## 5. Validation Commands

```bash
node tests/test_resolvers.js
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a database.

- Same data returned for the same input.
- Database query count reduced from N+1 to 2.
- Error handling preserved.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same data, fewer queries.

## 8. Remaining Risks

- DataLoader caching may return stale data within a single request.
- Requires DataLoader npm dependency.

## 9. Follow-up Recommendations

- Add query count monitoring to verify batching works.
- Consider cache invalidation strategy for long-running requests.
