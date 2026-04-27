// Before: N+1 problem — each author is fetched with a separate query.

const typeDefs = `
  type Post {
    id: ID!
    title: String!
    author: Author!
  }

  type Author {
    id: ID!
    name: String!
  }

  type Query {
    posts: [Post!]!
  }
`;

const resolvers = {
  Query: {
    posts: async () => {
      const db = getDb();
      // 1 query
      return db.query('SELECT * FROM posts LIMIT 10');
    },
  },
  Post: {
    author: async (post) => {
      const db = getDb();
      // N queries — one per post!
      return db.query('SELECT * FROM authors WHERE id = ?', [post.author_id]);
    },
  },
};

// If you query 10 posts → 1 + 10 = 11 database queries.
// If you query 100 posts → 101 database queries.
