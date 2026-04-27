# N+1 Resolver → DataLoader Batch

Refactored from per-resolver database queries to batched loading with DataLoader.

## Design Pressure

- Each `Post.author` resolver executed a separate SQL query.
- 10 posts → 11 queries. 100 posts → 101 queries.
- No batching — database connection overhead for every row.
- No caching — same author loaded multiple times if referenced by multiple posts.

## Applied Pattern

**DataLoader** — batch all `author_id` values into a single `WHERE id IN (...)` query. Cache results per request.

## After Code

```javascript
const DataLoader = require('dataloader');

// Batch function: loads all authors in one query
const createAuthorLoader = (db) => {
  return new DataLoader(async (authorIds) => {
    const rows = await db.query(
      'SELECT * FROM authors WHERE id IN (?)',
      [authorIds]
    );
    // Map rows back to the order of authorIds
    const authorMap = new Map(rows.map(r => [r.id, r]));
    return authorIds.map(id => authorMap.get(id) || null);
  });
};

const resolvers = {
  Query: {
    posts: async (_, __, { db }) => {
      // 1 query — same as before
      return db.query('SELECT * FROM posts LIMIT 10');
    },
  },
  Post: {
    author: async (post, _, { loaders }) => {
      // 0 queries — batched into the DataLoader
      return loaders.authorLoader.load(post.author_id);
    },
  },
};

// Context factory: create fresh loaders per request
const createContext = (db) => ({
  db,
  loaders: {
    authorLoader: createAuthorLoader(db),
  },
});
```

## Key Changes

| Before | After |
|--------|-------|
| N queries for N posts | 1 batched query |
| No caching | Per-request cache (same author loaded once) |
| Database connection per resolver | Single batch query |
| O(N) database round trips | O(1) database round trips |
| No way to add more batched fields | Easy to add more DataLoaders |

## Verification

- Querying 10 posts with authors → 2 queries (posts + authors), not 11.
- Querying 100 posts with authors → 2 queries, not 101.
- Same author on multiple posts → loaded once, cached by DataLoader.
- Adding a new batched field (e.g., `Post.comments`) requires only a new DataLoader.
