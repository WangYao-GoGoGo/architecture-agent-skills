# Commands

## Run Original Code

```bash
# CSS is not executable — review the specificity war in before/styles.css
```

## Run Refactored Code

```bash
# Review the utility-first approach in after/styles.css
```

## Run Tests

```bash
# CSS tests would use visual regression testing or stylelint
# Example:
npx stylelint before/styles.css
npx stylelint after/styles.css
```

## Validate Behavior Preservation

The refactoring replaces high-specificity selectors with utility classes. Visual behavior should be preserved.

Validation Level: **Static reasoning only** — CSS cannot be executed directly.
