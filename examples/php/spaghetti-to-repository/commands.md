# Commands

## Run Original Code

```bash
php before/UserController.php
```

Note: The original file defines a class only — it does not include a call to `show()`. To run it, add a test script or serve it via a web server.

## Run Refactored Code

```bash
php after/UserController.php
```

## Run Tests

```bash
php tests/test_user_controller.php
```

## Validate Behavior Preservation

The refactoring extracts SQL queries from the controller into a repository layer. The API behavior should remain identical.

Validation Level: **Static reasoning only** — requires a database to run end-to-end.
