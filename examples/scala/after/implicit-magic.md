# Implicit Magic → Given Instances

Refactored from scattered implicit parameters to explicit `given` instances with `using` clauses (Scala 3).

## Design Pressure

- Implicit parameters were defined in a separate object — hard to trace which ones applied.
- Adding a new implicit parameter could silently change behavior everywhere.
- No way to see at the call site which implicits were being used.
- Testing required carefully managing the implicit scope.

## Applied Pattern

**Given/using (Scala 3)** — make dependencies explicit with `using` clauses. Define `given` instances at the composition root.

## After Code

```scala
case class DatabaseConfig(host: String, port: Int)
case class CacheConfig(ttlSeconds: Int)

class UserRepository:
  def findById(id: String)(using db: DatabaseConfig): User =
    println(s"Connecting to ${db.host}:${db.port}")
    User(id, "John Doe")

class UserService:
  def getUser(id: String)(using db: DatabaseConfig, cache: CacheConfig): User =
    println(s"Cache TTL: ${cache.ttlSeconds}s")
    val repo = UserRepository()
    repo.findById(id) // using db is passed automatically

// Composition root — all dependencies defined in one place
object AppConfig:
  given db: DatabaseConfig = DatabaseConfig("localhost", 5432)
  given cache: CacheConfig = CacheConfig(60)

// Usage: explicit import makes dependencies visible
import AppConfig.{db, cache}
val service = UserService()
val user = service.getUser("123") // Clear which configs are used
```

## Key Changes

| Before | After |
|--------|-------|
| `implicit` keyword | `using` / `given` — clearer syntax |
| Implicits in companion object | Explicit `given` instances |
| Hidden dependency passing | Visible `using` clauses |
| Hard to test | Easy to override `given` for tests |
| Adding an implicit affects all callers | Adding a `using` is explicit |

## Verification

- Same behavior for the same inputs.
- At the call site, you can see exactly which `using` clauses are needed.
- Testing: override `given` instances in test scope without affecting production code.
- Compiler error if a required `using` parameter is not available — no silent fallback.
- Moving to explicit dependency injection (ZIO, Cats Effect) is straightforward.
