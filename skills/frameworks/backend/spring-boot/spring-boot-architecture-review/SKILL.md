---
name: spring-boot-architecture-review
description: Use when reviewing Spring Boot application architecture, auto-configuration, bean lifecycle, transaction boundaries, actuator endpoints, profiles, and production-ready structure.
---

# Spring Boot Architecture Review

## When To Use

- The main decision is about Spring Boot project structure, bean wiring, configuration management, or production readiness.
- Reviewing transaction boundaries, data source setup, or actuator exposure.

## Workflow

1. Identify the application's package structure and component responsibilities (controllers, services, repositories, configuration).
2. Review auto-configuration classes and conditional beans for unintended side effects.
3. Check transaction boundaries — are `@Transactional` annotations at the right layer?
4. Review profile-specific configuration and externalized properties.
5. Check actuator endpoint exposure and security.
6. Review bean lifecycle and dependency injection for circular dependencies.
7. Recommend the smallest structural change that improves clarity or reduces risk.

## Output Format

```markdown
Spring Boot architecture review:
- Package structure:
- Auto-configuration risks:
- Transaction boundaries:
- Configuration & profiles:
- Production readiness:
- Recommended change:
- Verification:
```
