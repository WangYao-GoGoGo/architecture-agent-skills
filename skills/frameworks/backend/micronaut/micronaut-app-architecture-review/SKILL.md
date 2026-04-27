---
name: micronaut-app-architecture-review
description: Use when reviewing Micronaut application architecture, AOT compilation, dependency injection, reactive streams, HTTP routing, and configuration management.
---

# Micronaut App Architecture Review

## When To Use

- The main decision is about Micronaut project structure, DI configuration, reactive stream design, HTTP client/server boundaries, or configuration management.
- Reviewing AOT compilation considerations or GraalVM native-image compatibility.

## Workflow

1. Identify project structure — are controllers, services, repositories, and configuration separated?
2. Review dependency injection — are bean scopes correct and are there circular dependencies?
3. Check reactive stream design — are reactive types used consistently at boundaries?
4. Review HTTP routing — are routes organized by domain?
5. Check configuration management — are `@ConfigurationProperties` used for external config?
6. Review AOT/native-image considerations — are reflection, proxies, and dynamic loading handled?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Micronaut architecture review:
- Project structure:
- Dependency injection:
- Reactive streams:
- HTTP routing:
- Configuration:
- AOT/native-image:
- Recommended change:
- Verification:
```
