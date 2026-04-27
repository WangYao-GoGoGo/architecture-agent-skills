---
name: c-header-interface-design
description: Use when reviewing or designing C header files, public APIs, opaque structs, ownership contracts, error handling, and module boundaries.
---

# C Header Interface Design

## Workflow

1. Identify public vs private types and functions.
2. Check whether headers expose implementation details unnecessarily.
3. Define ownership, lifetime, error codes, and thread-safety expectations.
4. Prefer opaque structs for stable module boundaries.
5. Verify callers can use the API without depending on internals.

## Output Format

```markdown
C interface review:
- Public API:
- Leaked internals:
- Ownership/lifetime:
- Recommended header shape:
- Verification:
```
