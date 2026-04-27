---
name: electron-app-architecture-review
description: Use when reviewing Electron application architecture, main/renderer process boundaries, IPC design, native API access, packaging, and security.
---

# Electron App Architecture Review

## When To Use

- The main decision is about Electron process separation, IPC contract design, native module integration, or security boundaries.
- Reviewing auto-update, local storage, crash reporting, or packaging strategy.

## Workflow

1. Identify the process architecture — main process, preload scripts, renderer processes, and shared modules.
2. Review IPC contract design — channel naming, payload validation, and versioning.
3. Check native API access — filesystem, shell, clipboard, and child process usage.
4. Review security configuration — contextIsolation, nodeIntegration, sandbox, and CSP.
5. Check auto-update, crash reporting, and telemetry setup.
6. Review packaging and distribution strategy.
7. Recommend the smallest structural change that improves security or maintainability.

## Output Format

```markdown
Electron architecture review:
- Process architecture:
- IPC contracts:
- Native API access:
- Security configuration:
- Update & telemetry:
- Packaging:
- Recommended change:
- Verification:
```
