# Repository

## Intent
Mediate between the domain and data mapping layers, acting like an in-memory domain object collection.

## Use When
- You want to decouple domain logic from data access code.
- You need a collection-like interface for accessing domain objects.
- You want to centralize query logic and data access strategies.

## Structure
- Repository defines collection-like methods (Add, Remove, FindById, FindAll, Query).
- ConcreteRepository implements data access using a specific technology (SQL, NoSQL, in-memory).
- Domain objects are the entities managed by the Repository.

## Heuristics
1. **Collection-like interface**: Repository should look like a collection to the caller, not like a data access layer.
2. **One repository per aggregate root**: Each aggregate root gets its own Repository.
3. **Query methods**: Use specification objects or query objects for complex queries.
4. **Repository vs DAO**: Repository works with domain objects; DAO works with database tables/records.

## Common Risks
1. **Leaky abstraction**: If Repository exposes database-specific concepts (transactions, queries), the abstraction leaks.
2. **Performance**: Loading entire aggregate roots when only a subset is needed can be expensive.
3. **Over-fetching**: Repository methods that always load full objects waste resources.
4. **Transaction management**: Repository boundaries may not align with transaction boundaries.

## Related Patterns
- **Unit of Work**: Often used with Repository to track changes.
- **Specification**: Can be passed to Repository for query criteria.
- **Factory Method**: Repository can use Factory to create domain objects from data.
