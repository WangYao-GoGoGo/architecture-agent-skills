# Firestore Knowledge

## Heuristics

- Model collections and documents around query patterns, not relational normalization.
- Use subcollections for hierarchical data; avoid deeply nested documents.
- Design composite indexes for complex queries; watch index entry limits.
- Use security rules as the authorization boundary; test rules with the emulator.
- Plan for write limits per document (1 write/second); use sharding for hot documents.
- Use `onSnapshot` for real-time updates; batch writes for atomic multi-document operations.
