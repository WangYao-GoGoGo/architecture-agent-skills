---
name: tauri-app-architecture-review
description: Use when reviewing Tauri application architecture, Rust command design, web frontend integration, security permissions, and cross-platform behavior.
---

# Tauri App Architecture Review

## When To Use

- The main decision is about Tauri Rust command boundaries, frontend-backend communication, permission scoping, or security model.
- Reviewing packaging, auto-updater, deep links, or platform-specific behavior.

## Workflow

1. Identify the command architecture — Rust command functions, payload types, and return values.
2. Review permission scoping — capabilities, allowlists, and scope configuration.
3. Check frontend-backend communication patterns — invoke calls, event system, and state sharing.
4. Review security configuration — CSP, filesystem access, shell access, and protocol scoping.
5. Check auto-updater, deep link, and platform-specific plugin configuration.
6. Review packaging and distribution for target platforms.
7. Recommend the smallest structural change that improves security or maintainability.

## Output Format

```markdown
Tauri architecture review:
- Command architecture:
- Permission scoping:
- Frontend-backend communication:
- Security configuration:
- Platform features:
- Packaging:
- Recommended change:
- Verification:
```
