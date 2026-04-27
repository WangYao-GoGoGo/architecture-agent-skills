# Commands

## Run Original Code

```bash
python before/monolith_service.py
```

Note: The original file defines a class only — it does not include a `__main__` block. To run it, add a temporary script or import it from a test file.

## Run Refactored Code

```bash
python after/*.py
```

Note: The refactored files define classes only — they do not include a `__main__` block.

## Run Tests

```bash
python -m pytest tests/ -v
```

## Validate Behavior Preservation

The refactoring separates user management, order processing, payment handling, inventory updates, and notifications into bounded contexts. The public API (`create_user_and_order()`) should remain compatible.

Validation Level: **Static reasoning only** — requires a database to run end-to-end.
