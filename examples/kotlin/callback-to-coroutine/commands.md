# Commands

## Run Original Code

```bash
# Compile and run the callback-based version
kotlinc before/UserRepository.kt -include-runtime -d before/app.jar
java -jar before/app.jar
```

## Run Refactored Code

```bash
# Compile and run the coroutine-based version
kotlinc after/*.kt -include-runtime -d after/app.jar
java -jar after/app.jar
```

## Run Tests

```bash
kotlinc tests/*.kt -include-runtime -d tests/test.jar
java -jar tests/test.jar
```

## Validate Behavior Preservation

The refactoring converts callback-based async to coroutines with `suspend` functions. The data loading sequence (user → orders → display) is preserved.

Validation Level: **Static reasoning only** — requires Kotlin coroutines library.
