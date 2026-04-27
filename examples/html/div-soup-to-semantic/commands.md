# Commands

## Run Original Code

```bash
# Open before/index.html in a browser
open before/index.html
```

## Run Refactored Code

```bash
# Open after/index.html in a browser
open after/index.html
```

## Run Tests

```bash
# HTML validation
npx html-validate before/index.html
npx html-validate after/index.html
```

## Validate Behavior Preservation

The refactoring replaces `<div>` elements with semantic HTML5 elements. The visual layout should be preserved (with appropriate CSS).

Validation Level: **Static reasoning only** — HTML is markup, not executable code.
