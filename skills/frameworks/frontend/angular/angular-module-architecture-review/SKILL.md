---
name: angular-module-architecture-review
description: Use when reviewing Angular application architecture, modules/standalone components, services, dependency injection, RxJS streams, guards, and application structure.
---

# Angular Module Architecture Review

## When To Use

- The main decision is about Angular module/standalone component organization, service boundaries, RxJS stream design, dependency injection scoping, or guard/interceptor placement.
- Reviewing shared module design, lazy loading strategy, or observable error handling.

## Workflow

1. Identify module/standalone component organization — do they express feature boundaries?
2. Review service responsibilities — are services focused on specific domains or becoming dumping grounds?
3. Check dependency injection scoping — are providers at the right level (root, module, component)?
4. Review RxJS stream design — are subscriptions managed, errors handled, and streams cancellable?
5. Check guard and interceptor placement — are they at appropriate boundaries?
6. Review shared module design — is it a dumping ground or intentional?
7. Recommend the smallest change that clarifies module or service boundaries.

## Output Format

```markdown
Angular architecture review:
- Module organization:
- Service responsibilities:
- Dependency injection:
- RxJS streams:
- Guards & interceptors:
- Shared modules:
- Recommended change:
- Verification:
```
