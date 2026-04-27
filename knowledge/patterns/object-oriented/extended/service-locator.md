# Service Locator

## Intent
Abstract the lookup of services, allowing clients to obtain dependencies without knowing their concrete implementations.

## Use When
- You want to decouple clients from service implementations.
- You need a central registry for services.
- Dependency injection is not feasible (legacy code, framework constraints).

## Structure
- ServiceLocator provides methods to locate services.
- Client asks ServiceLocator for a service by type or name.
- Service is the dependency being located.

## Heuristics
1. **Use with caution**: Service Locator is considered an anti-pattern by many because it hides dependencies.
2. **Configure at startup**: Register all services at application startup, not dynamically.
3. **Provide sensible defaults**: Return a default implementation if no service is registered.
4. **Thread safety**: Service Locator must be thread-safe.

## Common Risks
1. **Hidden dependencies**: Clients depend on the Service Locator, not on their actual dependencies. This makes testing harder.
2. **Runtime failures**: Missing service registrations are only discovered at runtime.
3. **Global state**: Service Locator is essentially a global registry, making code harder to reason about.
4. **Testing difficulty**: Tests must configure the Service Locator, creating shared state between tests.

## Related Patterns
- **Dependency Injection**: Preferred alternative to Service Locator.
- **Abstract Factory**: Can be used with Service Locator.
- **Singleton**: Service Locator is often a Singleton.
