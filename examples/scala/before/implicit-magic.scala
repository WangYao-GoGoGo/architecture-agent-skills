// Before: Implicit magic — implicit parameters are scattered and hard to trace.

object ImplicitConfig {
  implicit val defaultDb: DatabaseConfig = DatabaseConfig("localhost", 5432)
  implicit val defaultCache: CacheConfig = CacheConfig(60)
}

case class DatabaseConfig(host: String, port: Int)
case class CacheConfig(ttlSeconds: Int)

class UserRepository {
  def findById(id: String)(implicit db: DatabaseConfig): User = {
    println(s"Connecting to ${db.host}:${db.port}")
    User(id, "John Doe")
  }
}

class UserService {
  def getUser(id: String)(implicit db: DatabaseConfig, cache: CacheConfig): User = {
    println(s"Cache TTL: ${cache.ttlSeconds}s")
    val repo = new UserRepository()
    repo.findById(id) // implicit db is passed automatically
  }
}

// Usage: where do these implicits come from?
import ImplicitConfig._
val service = new UserService()
val user = service.getUser("123") // Which configs are used? Hard to tell.
