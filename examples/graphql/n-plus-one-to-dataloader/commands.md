# Commands

## Run Original Code

```bash
node before/resolvers.js
```

Note: The original file defines resolvers only — it does not include a server setup. To run it, add an Apollo Server or Express GraphQL setup.

## Run Refactored Code

```bash
node after/resolvers.js
```

## Run Tests

```bash
node tests/test_resolvers.js
```

## Validate Behavior Preservation

The refactoring adds DataLoader to batch author queries. The API behavior should remain identical — same data returned, but with fewer database queries.

Validation Level: **Static reasoning only** — requires a database to run end-to-end.
