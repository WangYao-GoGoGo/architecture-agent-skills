---
name: java-spring-architecture
description: Use when reviewing Spring application architecture, controllers, services, repositories, dependency injection, transactions, configuration, validation, and framework boundary leakage.
---

# Java Spring Architecture

## Workflow

1. Map controllers, services, repositories, configuration, and external clients.
2. Check that controllers handle transport and services own use-case orchestration.
3. Review transaction boundaries and repository usage.
4. Keep domain rules from depending unnecessarily on Spring APIs.
5. Recommend package and dependency changes.

## Output Format

```markdown
Spring architecture review:
- Layer responsibilities:
- Transaction boundaries:
- Framework leakage:
- Recommended changes:
- Verification:
```
