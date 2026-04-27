---
name: rust-ownership-architecture
description: Use when reviewing Rust ownership patterns, borrowing strategy, lifetime design, and memory safety architecture.
---

# Rust Ownership Architecture

## When To Use
- The main decision is about ownership model, borrowing strategy, or lifetime parameter design.
- Reviewing `Rc`/`Arc` usage, interior mutability patterns, or `unsafe` code.

## Workflow
1. Identify ownership chains — who owns each value and how is ownership transferred?
2. Review borrowing patterns — are references scoped correctly to avoid conflicts?
3. Check lifetime annotations — are they minimal and correct? Could elision apply?
4. Review `Rc`/`Arc` usage — is shared ownership justified? Could a borrow suffice?
5. Check interior mutability (`RefCell`/`Mutex`) — is it necessary or can the design be restructured?
6. Review `unsafe` blocks — are they justified, documented, and sound?
7. Recommend the simplest ownership model that satisfies safety and ergonomics.

## Output Format
```markdown
Rust ownership review:
- Ownership chains:
- Borrowing patterns:
- Lifetime annotations:
- Shared ownership (Rc/Arc):
- Interior mutability:
- Unsafe code:
- Recommended change:
- Verification:
```
