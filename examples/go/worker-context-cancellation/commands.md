# Commands

## Run Original Code

```bash
go run before/main.go
```

## Run Refactored Code

```bash
go run after/main.go
```

## Run Tests

```bash
go test ./tests/ -v
```

## Validate Behavior Preservation

The refactoring adds context cancellation to worker goroutines. The original code leaks goroutines; the refactored code properly cancels them.

Validation Level: **Test-based validation** — Go tests can verify goroutine lifecycle.
