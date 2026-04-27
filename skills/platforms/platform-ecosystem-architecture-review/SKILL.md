---
name: platform-ecosystem-architecture-review
description: Use when reviewing architecture that depends on external platform ecosystems, vendor SDKs, managed runtimes, app stores, webhooks, bot platforms, cloud services, IoT fleets, WeChat, robot platforms, or hardware controllers.
---

# Platform Ecosystem Architecture Review

## Knowledge To Use

- `knowledge/platform-ecosystems/`
- `knowledge/frameworks/core/framework-boundaries.md`
- `knowledge/api/`
- `knowledge/platform/`

## Workflow

1. Identify which parts are application-owned, platform-owned, vendor-SDK-owned, generated, or hardware-owned.
2. Map platform contracts: callbacks, events, permissions, tokens, review rules, deployment channels, SDK lifecycle, quotas, hardware commands, and failure modes.
3. Check whether platform concepts leak into domain logic, reusable modules, tests, or API contracts.
4. Recommend adapters, ports, local contracts, idempotent handlers, observability, and verification paths only where they reduce real coupling or risk.
5. Keep direct platform use when it is simple, local, and unlikely to create change or test friction.
6. Verify with platform simulators, sandbox accounts, replayed callbacks, contract tests, or hardware-in-the-loop where appropriate.

## Output Format

```markdown
Platform ecosystem review:
- Platform boundary:
- Platform-owned contracts:
- Coupling risks:
- Recommended structure:
- Verification:
```
