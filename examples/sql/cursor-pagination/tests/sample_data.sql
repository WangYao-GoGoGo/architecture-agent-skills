-- Sample data for testing cursor-based pagination
-- Run before the pagination queries

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total REAL NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO orders (id, user_id, total, status, created_at) VALUES
    (1, 101, 29.99, 'completed', '2025-01-01T10:00:00Z'),
    (2, 102, 49.99, 'completed', '2025-01-02T10:00:00Z'),
    (3, 103, 19.99, 'completed', '2025-01-03T10:00:00Z'),
    (4, 104, 99.99, 'completed', '2025-01-04T10:00:00Z'),
    (5, 105, 39.99, 'completed', '2025-01-05T10:00:00Z'),
    (6, 106, 59.99, 'pending',   '2025-01-06T10:00:00Z'),
    (7, 107, 79.99, 'completed', '2025-01-07T10:00:00Z'),
    (8, 108, 14.99, 'completed', '2025-01-08T10:00:00Z'),
    (9, 109, 89.99, 'completed', '2025-01-09T10:00:00Z'),
    (10, 110, 24.99, 'completed', '2025-01-10T10:00:00Z');

CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);
