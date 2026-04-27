---
name: javascript-module-architecture
description: Use when reviewing or designing JavaScript module boundaries, async workflows, frontend or Node.js structure, runtime validation, side-effect boundaries, shared utilities, and framework leakage in projects without strong TypeScript coverage.
---

# JavaScript Module Architecture

## Knowledge To Use

- `knowledge/languages/javascript/`
- `knowledge/domains/frontend/` when UI state or components are involved.
- `knowledge/api/contract-design.md` when API contracts are involved.
- `knowledge/frameworks/frontend/frontend-frameworks.md` when framework lifecycle affects the design.

## Workflow

1. Inspect modules, exports, async workflows, shared utilities, and framework entry points.
2. Identify runtime data contracts that would benefit from validation or JSDoc.
3. Separate pure transformations from I/O, DOM, network, storage, or framework lifecycle side effects.
4. Keep shared utility modules focused; move domain or feature logic to named modules.
5. Review error handling for promises, retries, and partial failures.
6. Verify with tests, linting, and representative runtime inputs.

## Output Format

```markdown
JavaScript architecture review:
- Module ownership:
- Runtime contract risks:
- Async/side-effect risks:
- Recommended structure:
- Verification:
```

