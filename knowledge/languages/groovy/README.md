# Groovy Architecture Idioms

## Use When

- Reviewing Groovy DSL design, metaprogramming patterns, Gradle build scripts, or Grails application architecture.

## Heuristics

- Use Groovy's builder pattern (`MarkupBuilder`, `JsonBuilder`) for DSL construction.
- Leverage `@Canonical`, `@ToString`, `@EqualsAndHashCode` AST transforms for boilerplate reduction.
- Use `Closure` delegates for DSL scoping — `delegate` and `resolveStrategy` control resolution.
- Prefer `@CompileStatic` or `@TypeChecked` for performance-critical code.
- Use `GPath` expressions for nested collection traversal.
- Keep Gradle build scripts declarative — avoid imperative logic in `build.gradle`.
- Use `Spock` for specification-style testing with Groovy.
- Use `@Slf4j` AST transform for logging.

## Common Risks

- Runtime metaprogramming (`ExpandoMetaClass`, `methodMissing`) making code hard to trace.
- Performance overhead from dynamic dispatch in hot paths.
- Over-using Groovy's optional typing — missing type information reduces IDE support.
- AST transform ordering issues in complex scenarios.
- Gradle configuration cache incompatibility with dynamic Groovy patterns.
