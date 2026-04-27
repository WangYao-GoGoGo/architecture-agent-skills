-- Expected results for cursor-based pagination
-- Run after sample_data.sql

-- Expected: first page (3 completed orders, newest first)
-- Should return: id=10, id=9, id=8
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
ORDER BY created_at DESC
LIMIT 3;

-- Expected: second page (next 3 completed orders)
-- Cursor: '2025-01-08T10:00:00Z' (the created_at of the last item on page 1)
-- Should return: id=7, id=5, id=4
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
  AND created_at < '2025-01-08T10:00:00Z'
ORDER BY created_at DESC
LIMIT 3;

-- Expected: third page (next 3 completed orders)
-- Cursor: '2025-01-04T10:00:00Z'
-- Should return: id=3, id=2, id=1
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
  AND created_at < '2025-01-04T10:00:00Z'
ORDER BY created_at DESC
LIMIT 3;
