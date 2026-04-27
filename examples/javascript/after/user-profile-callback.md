# Callback Hell → Async/Await

Refactored from nested callbacks to flat async/await with proper error handling.

## Design Pressure

- Four levels of nested callbacks made the code hard to read and maintain.
- Error handling was duplicated at every level.
- Adding a step required nesting another level.
- No way to run independent requests in parallel.

## Applied Pattern

**Async/await + Promise.all** — flatten the chain, use try/catch for errors, parallelize independent requests.

## After Code

```javascript
async function loadUserProfile(userId) {
  try {
    const user = await getUser(userId);
    const [posts, comments, likes] = await Promise.all([
      getPosts(user.id),
      getComments(user.id),
      getLikes(user.id),
    ]);
    renderProfile(user, posts, comments, likes);
  } catch (err) {
    console.error("Failed to load user profile:", err);
  }
}
```

## Key Changes

| Before | After |
|--------|-------|
| 4 levels of nesting | Flat, sequential reads |
| Duplicated `if (err)` checks | Single `try/catch` |
| Sequential waterfall | Parallel `Promise.all` for independent requests |
| Implicit data flow | Explicit destructuring |

## Verification

- Same data is loaded and rendered.
- Errors in any step are caught by the single `catch`.
- Independent requests (posts, comments, likes) run in parallel, improving performance.
- Adding a new data source is a one-line addition to the `Promise.all` array.
