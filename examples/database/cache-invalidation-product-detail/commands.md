# Commands

## Run Original Code

```bash
# Review the cache invalidation design in before/ directory
```

## Run Refactored Code

```bash
# Review the refactored cache strategy in after/ directory
```

## Run Tests

```bash
# No executable tests — cache invalidation requires a running cache server
# Example with Redis:
redis-cli < tests/test_cache_invalidation.redis
```

## Validate Behavior Preservation

The refactoring addresses cache invalidation for product detail pages. The cache behavior (TTL, invalidation on update) should be preserved.

Validation Level: **Static reasoning only** — requires a cache server to run.
