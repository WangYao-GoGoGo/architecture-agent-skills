---
name: aws-iot-architecture
description: Use when reviewing or designing AWS IoT architecture, including device connectivity, shadows, rules engine, fleet provisioning, OTA updates, and AWS IoT Core constraints.
---

# AWS IoT Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/iot-edge/`
- `knowledge/platform-ecosystems/cloud/`
- `knowledge/languages/c/`
- `knowledge/languages/python/`
- `knowledge/platform/`

## Workflow

1. Identify IoT scenarios: device connectivity (MQTT, HTTP, LoRaWAN), device shadows, rules engine, fleet provisioning, OTA updates, device defender, and Greengrass edge computing.
2. Map AWS IoT contracts: MQTT topic structure, shadow document schema, rules engine SQL syntax, device certificate lifecycle, and job document format.
3. Check whether device logic, shadow state management, rule processing, or OTA logic are mixed with domain workflow logic.
4. Review operational concerns: device authentication (X.509, Cognito), offline behavior, shadow versioning, rule engine error handling, and fleet-scale topic routing.
5. Recommend device client, shadow synchronizer, rule processor, and OTA update manager boundaries.
6. Verify with AWS IoT device simulator, shadow testing, rule engine dry-run, and offline/online transition scenarios.

## Output Format

```markdown
AWS IoT architecture:
- IoT scenarios:
- Platform coupling:
- Security/offline concerns:
- Proposed boundaries:
- Verification:
```
