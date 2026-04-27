---
name: thingsboard-iot-architecture
description: Use when reviewing or designing ThingsBoard IoT platform architecture, including device connectivity, telemetry, attributes, RPC, dashboards, rule chains, and ThingsBoard platform constraints.
---

# ThingsBoard IoT Architecture

## Knowledge To Use

- `knowledge/platform/iot-edge/`
- `knowledge/languages/java/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/platform/`

## Workflow

1. Identify IoT scenarios: device connectivity (MQTT, CoAP, HTTP), telemetry upload, attribute management, RPC calls, data visualization dashboards, rule chains, and device provisioning.
2. Map ThingsBoard contracts: MQTT topic format, telemetry/attribute key-value schema, RPC request/response format, rule chain node types, and dashboard widget data sources.
3. Check whether device logic, telemetry processing, attribute management, or rule chain logic are mixed with domain workflow logic.
4. Review operational concerns: device authentication (access tokens, X.509, basic MQTT), data retention, rule chain error handling, and tenant/entity hierarchy.
5. Recommend device client, telemetry handler, attribute synchronizer, and rule chain processor boundaries.
6. Verify with ThingsBoard device simulator, telemetry testing, RPC testing, and rule chain dry-run scenarios.

## Output Format

```markdown
ThingsBoard IoT architecture:
- IoT scenarios:
- Platform coupling:
- Data/rule-chain concerns:
- Proposed boundaries:
- Verification:
```
