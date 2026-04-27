# Commands

## Run Original Code

```bash
# Execute the offset-based pagination queries against a database
# Example with SQLite:
sqlite3 :memory: ".read before/pagination.sql"
```

## Run Refactored Code

```bash
# Execute the cursor-based pagination queries
sqlite3 :memory: ".read after/pagination.sql"
```

## Run Tests

```bash
# Run the test queries against sample data
sqlite3 :memory: ".read tests/sample_data.sql" ".read tests/expected_result.sql"
```

## Validate Behavior Preservation

The refactoring replaces offset-based pagination with cursor-based pagination. The query results should be identical for the same page, but cursor-based pagination is stable and performant for large datasets.

Validation Level: **Static reasoning only** — requires a database to run.
