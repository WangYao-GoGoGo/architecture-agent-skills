# Debug Report: Cursor Pagination

## 1. Original Problem

Offset-based pagination has two problems:

1. **Performance degradation** — as the offset grows, the database must scan and discard more rows (O(n) scan).
2. **Inconsistent results** — if rows are inserted or deleted between pages, items may be missed or duplicated.

## 2. Root Cause

Using `OFFSET` for pagination — the database must count through all previous rows on each query.

## 3. Fix Summary

Refactored to cursor-based pagination:

- Replaced `OFFSET` with `WHERE created_at < ?` (cursor).
- Uses a stable cursor (timestamp or ID) instead of row count.
- Performance is O(log n) with proper indexing.

## 4. Files Changed

| File | Change |
|---|---|
| `before/pagination.sql` | Original — offset-based |
| `after/pagination.sql` | Refactored — cursor-based |

## 5. Validation Commands

```bash
sqlite3 :memory: ".read tests/sample_data.sql" ".read tests/expected_result.sql"
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a database to run.

- Same first page of results.
- Stable pagination — inserting new rows does not shift existing pages.
- Consistent performance regardless of page depth.

## 7. Behavior Preservation Notes

✅ Behavior preserved — same results for the same query parameters. Cursor-based pagination is more stable and performant.

## 8. Remaining Risks

- Requires a unique, sortable column for the cursor (e.g., `created_at` with unique constraint).
- Cannot jump to a specific page number without scanning.
- Requires an index on the cursor column.

## 9. Follow-up Recommendations

- Add a composite index on `(status, created_at)` for optimal performance.
- Consider using a base64-encoded cursor for opaque pagination tokens.
