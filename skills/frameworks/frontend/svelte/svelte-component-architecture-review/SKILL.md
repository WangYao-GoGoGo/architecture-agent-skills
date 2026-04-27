---
name: svelte-component-architecture-review
description: Use when reviewing Svelte component architecture, reactivity, stores, component boundaries, lifecycle, transitions, and application structure.
---

# Svelte Component Architecture Review

## When To Use

- The main decision is about Svelte component organization, reactive statement design, store usage, or component boundary clarity.
- Reviewing SvelteKit-specific patterns (server/client boundaries, endpoints, form actions).

## Workflow

1. Identify component roles — page, feature, shared, and primitive components.
2. Review reactive statement design — are reactive declarations simple and side-effect-free?
3. Map state ownership — local component state, stores, and server state.
4. Check store organization — are stores scoped by domain or becoming global dumps?
5. Review component boundaries — do components mix data loading, business logic, and rendering?
6. Check SvelteKit-specific patterns — are server/client boundaries clear?
7. Recommend the smallest change that clarifies component or state ownership.

## Output Format

```markdown
Svelte architecture review:
- Component roles:
- Reactive statements:
- State ownership:
- Store organization:
- Component boundaries:
- SvelteKit boundaries:
- Recommended change:
- Verification:
```
