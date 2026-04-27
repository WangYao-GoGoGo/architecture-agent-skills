-- Before: Offset pagination — slow and inconsistent for large datasets.
-- As the offset grows, the database must scan and discard more rows.

-- Page 1: first 20 orders
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
ORDER BY created_at DESC
LIMIT 20 OFFSET 0;

-- Page 2: next 20 orders (must re-scan first 20 rows)
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
ORDER BY created_at DESC
LIMIT 20 OFFSET 20;

-- Page 1000: next 20 orders (scans 20,000 rows, returns 20)
SELECT id, user_id, total, created_at
FROM orders
WHERE status = 'completed'
ORDER BY created_at DESC
LIMIT 20 OFFSET 19980;

-- Problems:
-- 1. Performance degrades as offset increases (O(n) scan).
-- 2. If rows are inserted/deleted between pages, items may be missed or duplicated.
-- 3. No stable cursor — pagination is not idempotent.
