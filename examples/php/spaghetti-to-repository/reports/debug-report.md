# Debug Report: Spaghetti to Repository

## 1. Original Problem

The `UserController.show()` method mixes SQL queries, business logic, and response formatting in a single method. This makes it:

- Hard to test — cannot test business logic without a database.
- Hard to change — SQL changes risk breaking response formatting.
- Hard to reuse — queries cannot be reused by other controllers.

## 2. Root Cause

Separation of concerns violation — data access, business logic, and presentation are mixed.

## 3. Fix Summary

Extracted data access into a `UserRepository` class:

- `UserRepository.find()` — database query
- `UserRepository.getOrderCount()` — order count query
- `UserController.show()` — delegates to repository, handles response

## 4. Files Changed

| File | Change |
|---|---|
| `before/UserController.php` | Original — SQL mixed with controller logic |
| `after/UserController.php` | Refactored — delegates to repository |
| `after/UserRepository.php` | New — data access layer |

## 5. Validation Commands

```bash
php tests/test_user_controller.php
```

## 6. Validation Results

Validation Level: **Static reasoning only** — requires a database.

- Same data returned for the same user ID.
- Same error handling (404 for missing user).
- Same business logic (display_name, is_active, order_count).

## 7. Behavior Preservation Notes

✅ Behavior preserved — all outputs identical for the same inputs.

## 8. Remaining Risks

- Database connection is still hardcoded — should use dependency injection.
- No transaction management for multi-query operations.

## 9. Follow-up Recommendations

- Use dependency injection for the database connection.
- Add unit tests with a mock repository.
- Consider using an ORM for more complex queries.
