---
name: wechat-mini-program-architecture
description: Use when reviewing or designing WeChat mini program architecture, including pages, components, services, wx APIs, cloud functions, login/session flows, backend contracts, subscription messages, uploads, and WeChat platform limits.
---

# WeChat Mini Program Architecture

## Knowledge To Use

- `knowledge/platform/wechat/`
- `knowledge/languages/javascript/`
- `knowledge/languages/typescript/`
- `knowledge/api/`

## Workflow

1. Identify pages, components, services/model modules, platform API calls, backend APIs, cloud functions, storage, and authentication/session flow.
2. Separate UI composition from workflow logic, platform adapters, and trusted backend behavior.
3. Check whether `wx.*`, cloud functions, payment/login/session details, or backend request details are scattered across page/component code.
4. Review platform constraints: permissions, package size, subpackages, version compatibility, review requirements, token/session lifecycle, and sensitive secrets.
5. Recommend page/component/service/backend boundaries with minimal added abstraction.
6. Verify with representative page flows, mocked platform adapters, backend contract checks, and duplicate callback or retry scenarios.

## Output Format

```markdown
WeChat mini program architecture:
- Current structure:
- Platform coupling:
- Proposed boundaries:
- Backend/security concerns:
- Verification:
```
