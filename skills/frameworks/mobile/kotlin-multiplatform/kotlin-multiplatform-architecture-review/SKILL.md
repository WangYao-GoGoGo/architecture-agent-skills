---
name: kotlin-multiplatform-architecture-review
description: Use when reviewing Kotlin Multiplatform architecture, shared module boundaries, expect/actual pattern, platform-specific UI, and code sharing strategy.
---

# Kotlin Multiplatform Architecture Review

## When To Use

- The main decision is about KMP module structure, expect/actual API design, shared vs platform-specific code boundaries, or dependency management.
- Reviewing testing strategy, platform integration, or build configuration.

## Workflow

1. Identify the module structure — shared, common, android, ios, and desktop modules.
2. Review expect/actual API design — are platform ports stable and minimal?
3. Check shared code boundaries — domain, data, and presentation logic separation.
4. Review platform-specific UI integration — Compose Multiplatform vs native UI.
5. Check dependency injection and service locator patterns across platforms.
6. Review testing strategy — shared tests, platform-specific tests, and mock setup.
7. Recommend the smallest structural change that improves code sharing or maintainability.

## Output Format

```markdown
KMP architecture review:
- Module structure:
- Expect/actual API design:
- Shared code boundaries:
- Platform UI integration:
- Dependency injection:
- Testing strategy:
- Recommended change:
- Verification:
```
