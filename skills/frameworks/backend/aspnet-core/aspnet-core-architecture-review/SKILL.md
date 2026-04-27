---
name: aspnet-core-architecture-review
description: Use when reviewing ASP.NET Core application architecture, middleware pipeline, dependency injection, controller/minimal API boundaries, EF Core usage, and hosted services.
---

# ASP.NET Core Architecture Review

## When To Use

- The main decision is about ASP.NET Core project structure, middleware ordering, DI registration, EF Core transaction boundaries, or background service design.
- Reviewing controller vs minimal API choices, filter usage, or configuration management.

## Workflow

1. Identify project structure — are controllers/minimal APIs, services, and persistence separated?
2. Review middleware pipeline — is ordering logical and are error handling middleware in place?
3. Check dependency injection registration — are lifetimes correct and are there captive dependencies?
4. Review EF Core usage — are transaction and tracking boundaries explicit?
5. Check hosted service design — are failure, retry, and shutdown behaviors clear?
6. Review configuration and options pattern usage.
7. Recommend the smallest change that improves structure or reduces risk.

## Output Format

```markdown
ASP.NET Core architecture review:
- Project structure:
- Middleware pipeline:
- Dependency injection:
- EF Core boundaries:
- Hosted services:
- Configuration:
- Recommended change:
- Verification:
```
