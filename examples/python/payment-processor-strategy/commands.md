# Commands

## Run Original Code

```bash
python before/payment_processor.py
```

Note: The original file defines classes only — it does not include a `__main__` block. To run it, add a temporary script or import it from a test file.

## Run Refactored Code

```bash
python after/payment_processor.py
```

Note: The refactored file defines classes only — it does not include a `__main__` block. To run it, add a temporary script or import it from a test file.

## Run Tests

```bash
python -m pytest tests/ -v
```

## Validate Behavior Preservation

```bash
python -m pytest tests/ -v
```

All test cases should pass identically for both the original and refactored implementations.
