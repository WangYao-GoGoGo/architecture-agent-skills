# Offset Pagination → Cursor Pagination

Refactored from offset-based pagination to keyset (cursor) pagination for stable, O(log n) pagination.

## Design Pressure

- Offset pagination scans O(offset + limit) rows — unusable for large datasets.
- Insertions/deletions between pages cause missed or duplicate results.
- No way to paginate consistently when data changes.

## Applied Pattern

**Keyset pagination (cursor)** — use a `WHERE` clause on the last seen value with a covering index. No offset, no scan.

## After Code

```sql
-- First page: no cursor yet
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- Application remembers: last row has (created_at = '2025-01-15 10:30:00', id = 1042)

-- Next page: use cursor from last row
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
  AND (created_at, id) < ('2025-01-15 10:30:00', 1042)
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- Required index
CREATE INDEX idx_orders_status_created_id
ON orders (status, created_at DESC, id DESC);
```

## Key Changes

| Before | After |
|--------|-------|
| `LIMIT 20 OFFSET 19980` | `WHERE (created_at, id) < (cursor)` |
| Scans 20,000 rows | Scans exactly 20 rows (index seek) |
| O(n) performance | O(log n) performance |
| Non-deterministic under writes | Deterministic — cursor is stable |
| Cannot paginate backwards easily | Can paginate backwards with `>` |

## Verification

- Same first page results for both approaches.
- Page 1000 with cursor pagination is ~1000x faster than offset.
- Inserting a new row does not shift pagination boundaries.
- The covering index means the query never touches the table (index-only scan).
- Verify with `EXPLAIN ANALYZE` — should show "Index Only Scan" with zero offset.
