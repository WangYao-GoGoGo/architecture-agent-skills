---
name: cpp-class-design
description: Use when reviewing C++ class hierarchies, RAII patterns, smart pointer usage, and modern C++ architecture.
---

# C++ Class Design

## When To Use
- The main decision is about class hierarchy design, memory management strategy, or template usage.
- Reviewing RAII compliance, rule of five, or STL container selection.

## Workflow
1. Identify class responsibilities — does each class have a single, clear responsibility?
2. Review special member functions — are destructors, copy/move constructors, and assignment operators correct?
3. Check RAII compliance — are all resources (memory, files, locks) managed by RAII wrappers?
4. Review smart pointer usage — `unique_ptr` for exclusive ownership, `shared_ptr` for shared.
5. Check inheritance design — is public inheritance used for "is-a" relationships only?
6. Review template usage — are concepts/constraints used to document template requirements?
7. Recommend the simplest class design that meets requirements.

## Output Format
```markdown
C++ class design review:
- Class responsibilities:
- Special member functions:
- RAII compliance:
- Smart pointer strategy:
- Inheritance design:
- Template usage:
- Recommended change:
- Verification:
```
