# CouchDB Knowledge

## Heuristics

- Design documents for replication-friendly conflict resolution.
- Use MapReduce views for pre-computed indexes; avoid views as query engines.
- Use `_changes` feed for real-time data streaming and synchronization.
- Keep document size small and design for append-mostly patterns.
- Plan for eventual consistency; design conflict resolution logic at the application layer.
- Use `_rev` tokens for optimistic concurrency control.
