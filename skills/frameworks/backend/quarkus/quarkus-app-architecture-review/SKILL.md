---
name: quarkus-app-architecture-review
description: Use when reviewing Quarkus application architecture, CDI beans, reactive messaging, Panache ORM, extensions, configuration, and native-image compilation.
---

# Quarkus App Architecture Review

## When To Use

- The main decision is about Quarkus project structure, CDI bean organization, reactive messaging topology, Panache entity design, or extension usage.
- Reviewing native-image compilation considerations or configuration management.

## Workflow

1. Identify project structure — are REST endpoints, services, repositories, and messaging separated?
2. Review CDI bean scopes — are beans scoped correctly and are there circular dependencies?
3. Check reactive messaging design — are channels organized by domain and event type?
4. Review Panache entity design — do entities represent persistence or domain concepts?
5. Check extension usage — are extensions adding unnecessary dependencies?
6. Review native-image considerations — are reflection, serialization, and dynamic loading handled?
7. Recommend the smallest change that clarifies structure.

## Output Format

```markdown
Quarkus architecture review:
- Project structure:
- CDI bean scopes:
- Reactive messaging:
- Panache entities:
- Extension usage:
- Native-image:
- Recommended change:
- Verification:
```
