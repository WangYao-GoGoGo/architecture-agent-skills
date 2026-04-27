# Commands

## Run Original Code

```bash
ruby before/record.rb
```

## Run Refactored Code

```bash
ruby after/record.rb
```

## Run Tests

```bash
ruby tests/test_record.rb
```

## Validate Behavior Preservation

The refactoring replaces mixin-based behavior with explicit composition. The save behavior (validate → log → save) is preserved, but the execution order is now explicit rather than depending on include order.

Validation Level: **Test-based validation** — Ruby tests can verify behavior.
