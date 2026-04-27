# Commands

## Run Original Code

```bash
# The monolithic component requires a React environment
# Example:
npx react-scripts start
```

## Run Refactored Code

```bash
npx react-scripts start
```

## Run Tests

```bash
npx react-scripts test tests/
```

## Validate Behavior Preservation

The refactoring decomposes the monolithic ProductPage into smaller components. The UI behavior should remain identical.

Validation Level: **Static reasoning only** — requires React testing environment.
