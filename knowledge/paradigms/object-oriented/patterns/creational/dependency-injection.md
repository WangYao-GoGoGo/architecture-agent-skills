# Dependency Injection

## Intent
Provide dependencies to an object from the outside rather than having the object create them internally.

## Use When
- You want to decouple object creation from business logic.
- You need to swap implementations (test doubles, different environments).
- You want to make dependencies explicit and visible.

## Structure
- Client declares its dependencies (typically via constructor parameters).
- Injector (DI container or manual wiring) creates and provides the dependencies.
- Interface defines the contract between client and dependency.

## Forms
- **Constructor Injection**: Dependencies passed via constructor. Preferred — makes dependencies explicit and supports immutability.
- **Setter Injection**: Dependencies set via setter methods. Use for optional dependencies.
- **Interface Injection**: Client implements an interface that accepts the dependency.

## Heuristics
1. **Prefer constructor injection**: It makes dependencies explicit, supports immutability, and prevents partially initialized objects.
2. **Use DI containers sparingly**: Manual wiring (composition root) is often clearer than framework magic.
3. **Keep the composition root at the entry point**: Wire all dependencies in one place near the application entry point.
4. **Avoid service locator**: It hides dependencies and makes testing harder.

## Common Risks
1. **Container proliferation**: Leaking DI container references into business code creates framework coupling.
2. **Configuration complexity**: Large XML/annotation configurations become hard to maintain.
3. **Runtime errors**: Misconfigured dependencies are only discovered at runtime, not compile time.
4. **Over-injection**: Injecting too many dependencies indicates a class with too many responsibilities.

## Related Patterns
- **Factory Method**: Alternative for creating dependencies.
- **Service Locator**: Alternative lookup mechanism (generally discouraged).
- **Singleton**: DI can manage Singleton-scoped dependencies.
