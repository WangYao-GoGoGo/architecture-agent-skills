---
name: python-clean-architecture
description: Use when applying clean architecture or dependency inversion in Python, especially around domain rules, use cases, repositories, external clients, frameworks, and tests.
---

# Python Clean Architecture

## Workflow

1. Identify domain rules, use cases, infrastructure, and delivery mechanisms.
2. Keep framework and vendor details at the edge.
3. Use small protocols or callables for ports only where substitution is useful.
4. Avoid creating excessive layers for simple scripts or CRUD flows.
5. Verify domain/use-case tests without external services.

## Output Format

```markdown
Python clean architecture review:
- Core policy:
- External details:
- Ports/adapters:
- Simplifications:
- Verification:
```
