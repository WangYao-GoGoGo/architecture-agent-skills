---
name: nintendo-platform-architecture
description: Use when reviewing or designing Nintendo Switch platform integration, including NintendoSDK, NX accounts, online services, achievements, and Nintendo platform certification constraints.
---

# Nintendo Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/cpp/`
- `knowledge/languages/c/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: NintendoSDK initialization, NX account integration, online service (Nintendo Network), achievements/badges, save data management, and Nintendo eShop integration.
2. Map Nintendo platform contracts: SDK lifecycle, account linking flow, online service API patterns, save data encryption requirements, and certification requirements (LotCheck).
3. Check whether game logic, account management, online service calls, or save data handling are mixed with platform SDK calls.
4. Review platform constraints: LotCheck (Lot Check) compliance, certification process, SDK version compatibility, devkit vs retail differences, and region-specific requirements.
5. Recommend game service adapters, account manager, online service client, and save data handler boundaries.
6. Verify with Nintendo devkit, LotCheck testing tools, online service sandbox, and certification dry-run.

## Output Format

```markdown
Nintendo platform architecture:
- Integration scenarios:
- SDK coupling:
- LotCheck/certification concerns:
- Proposed boundaries:
- Verification:
```
