---
name: typescript-module-architecture
description: Use when reviewing or designing TypeScript module boundaries, type contracts, frontend/backend shared types, generated clients, discriminated unions, state ownership, and side-effect boundaries.
---

# TypeScript Module Architecture

## Knowledge To Use

- `knowledge/languages/typescript/`
- `knowledge/application-areas/frontend/` when UI state or components are involved.
- `knowledge/api/contract-design.md` when API contracts are involved.
- `knowledge/frameworks/frontend/frontend-frameworks.md` when framework lifecycle affects the design.

## Workflow

1. Inspect module boundaries, exported types, generated types, and call sites.
2. Identify whether the concern is domain contract, transport contract, UI state, server state, or infrastructure detail.
3. Keep generated ORM/API/client types from leaking broadly when they create coupling.
4. Use discriminated unions for stable variants and explicit state machines.
5. Keep side effects near framework, adapter, or service boundaries.
6. Verify with type checks, tests, and representative API/component usage.

## Output Format

```markdown
TypeScript architecture review:
- Contract boundary:
- Module/state ownership:
- Type risks:
- Recommended structure:
- Verification:
```
