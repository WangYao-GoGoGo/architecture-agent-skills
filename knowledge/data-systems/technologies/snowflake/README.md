# Snowflake Knowledge

## Heuristics

- Choose warehouse size based on workload: XS for development, larger for production queries.
- Use clustering keys for large tables queried by specific columns.
- Use materialized views for pre-aggregated results on large tables.
- Use zero-copy cloning for development, testing, and data recovery.
- Separate compute from storage; warehouses can be suspended independently.
- Monitor credit usage by warehouse, query, and user for cost optimization.
- Use data sharing for cross-account access without data movement.
