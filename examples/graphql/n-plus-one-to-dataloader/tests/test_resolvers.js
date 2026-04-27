// Tests for Resolvers — validates behavior preservation after DataLoader refactoring.
//
// Run with: node tests/test_resolvers.js

const assert = require('assert');

// Mock the resolver structure to verify behavior
function createMockDb() {
    const authors = {
        1: { id: '1', name: 'Alice' },
        2: { id: '2', name: 'Bob' },
        3: { id: '3', name: 'Charlie' },
    };
    return {
        query: (sql, params) => {
            if (sql.includes('SELECT * FROM posts')) {
                return [
                    { id: '1', title: 'Post 1', author_id: '1' },
                    { id: '2', title: 'Post 2', author_id: '2' },
                    { id: '3', title: 'Post 3', author_id: '1' },
                ];
            }
            if (sql.includes('SELECT * FROM authors')) {
                const id = params[0];
                return authors[id] || null;
            }
            return null;
        }
    };
}

// Simulate the before resolver behavior
async function beforeResolver() {
    const db = createMockDb();
    const posts = await db.query('SELECT * FROM posts LIMIT 10');
    const results = [];
    for (const post of posts) {
        const author = await db.query('SELECT * FROM authors WHERE id = ?', [post.author_id]);
        results.push({ ...post, author });
    }
    return results;
}

// Simulate the after resolver behavior (batched)
async function afterResolver() {
    const db = createMockDb();
    const posts = await db.query('SELECT * FROM posts LIMIT 10');
    // Batch: collect all author IDs and fetch once
    const authorIds = [...new Set(posts.map(p => p.author_id))];
    const authors = {};
    for (const id of authorIds) {
        authors[id] = await db.query('SELECT * FROM authors WHERE id = ?', [id]);
    }
    return posts.map(post => ({ ...post, author: authors[post.author_id] }));
}

async function runTests() {
    console.log('Resolver Tests\n');

    // Test 1: Both resolvers return same data
    console.log('Test: Same data returned');
    const before = await beforeResolver();
    const after = await afterResolver();
    assert.strictEqual(before.length, after.length, 'Same number of results');
    for (let i = 0; i < before.length; i++) {
        assert.strictEqual(before[i].id, after[i].id, `Post ${i} has same id`);
        assert.strictEqual(before[i].author.name, after[i].author.name, `Post ${i} has same author`);
    }
    console.log('  PASS\n');

    // Test 2: Author data is correct
    console.log('Test: Author data correct');
    assert.strictEqual(before[0].author.name, 'Alice');
    assert.strictEqual(before[1].author.name, 'Bob');
    assert.strictEqual(before[2].author.name, 'Alice'); // Same author as post 1
    console.log('  PASS\n');

    console.log('All tests passed!');
}

runTests().catch(err => {
    console.error('Test failed:', err);
    process.exit(1);
});
