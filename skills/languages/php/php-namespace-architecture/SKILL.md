---
name: php-namespace-architecture
description: Use when reviewing PHP namespace organization, PSR compliance, dependency injection, and modern PHP application architecture.
---

# PHP Namespace Architecture

## When To Use
- The main decision is about namespace structure, autoloading strategy, or dependency injection container design.
- Reviewing PSR compliance, service container usage, or framework architecture.

## Workflow
1. Identify namespace structure — does it follow PSR-4 and mirror the filesystem?
2. Review strict types — is `declare(strict_types=1)` used in all files?
3. Check type hints — are parameters and return types fully specified?
4. Review dependency injection — are dependencies injected, not fetched statically?
5. Check framework patterns — are controllers thin and services extracted?
6. Review testability — can classes be tested with mocked dependencies?
7. Recommend the cleanest namespace and DI structure.

## Output Format
```markdown
PHP namespace review:
- Namespace structure:
- Strict types:
- Type hints:
- Dependency injection:
- Framework patterns:
- Testability:
- Recommended change:
- Verification:
```
