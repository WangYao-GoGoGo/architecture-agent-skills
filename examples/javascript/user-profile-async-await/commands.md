# Commands

## Run Original Code

```bash
node before/user-profile.js
```

Note: The original file defines functions only — it does not include a call to `loadUserProfile`. To run it, add a test call or import it.

## Run Refactored Code

```bash
node after/user-profile.js
```

## Run Tests

```bash
node tests/test_user_profile.js
```

## Validate Behavior Preservation

The refactoring converts nested callbacks to async/await. The data loading sequence (user → posts → comments → likes → render) is preserved.

Validation Level: **Static reasoning only** — requires mock API endpoints to run end-to-end.
