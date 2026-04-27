---
name: alipay-mini-program-architecture
description: Use when reviewing or designing Alipay mini program architecture, including pages, components, my.* APIs, app lifecycle, cloud functions, login/auth flow, payment integration, and Alipay platform constraints.
---

# Alipay Mini Program Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/typescript/`
- `knowledge/api/`

## Workflow

1. Identify pages, components, services, `my.*` platform API calls, backend APIs, cloud functions, storage, and authentication/session flow.
2. Separate UI composition from workflow logic, platform adapters, and trusted backend behavior.
3. Check whether `my.*`, cloud functions, payment/login/session details, or backend request details are scattered across page/component code.
4. Review platform constraints: permissions, package size, subpackages, version compatibility, review requirements, token/session lifecycle, and sensitive secrets.
5. Recommend page/component/service/backend boundaries with minimal added abstraction.
6. Verify with representative page flows, mocked platform adapters, backend contract checks, and duplicate callback or retry scenarios.

## Output Format

```markdown
Alipay mini program architecture:
- Current structure:
- Platform coupling:
- Proposed boundaries:
- Backend/security concerns:
- Verification:
```
