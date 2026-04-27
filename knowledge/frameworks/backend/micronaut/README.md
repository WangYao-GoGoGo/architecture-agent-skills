# Micronaut Knowledge

## Heuristics

- Keep controllers focused on HTTP transport and delegate to service beans.
- Use `@Singleton`, `@Prototype`, `@RequestScope` deliberately based on state ownership.
- Use reactive types (Mono/Flux) at I/O boundaries; keep domain logic pure where possible.
- Use `@ConfigurationProperties` for externalized configuration with validation.
- Plan for AOT compilation: avoid runtime reflection, dynamic class loading, and proxies where possible.

## Common Risks

- Controllers owning business logic.
- Circular dependency injection.
- Runtime reflection breaking native-image compilation.
