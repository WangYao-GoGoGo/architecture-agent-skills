---
name: azure-iot-architecture
description: Use when reviewing or designing Azure IoT architecture, including IoT Hub, device twins, direct methods, cloud-to-device messages, IoT Edge, and Azure IoT platform constraints.
---

# Azure IoT Architecture

## Knowledge To Use

- `knowledge/platform/iot-edge/`
- `knowledge/platform/cloud/`
- `knowledge/languages/c/`
- `knowledge/languages/csharp/`
- `knowledge/platform/`

## Workflow

1. Identify IoT scenarios: IoT Hub device connectivity, device twins, direct methods, cloud-to-device (C2D) messages, IoT Edge modules, DPS (Device Provisioning Service), and Time Series Insights.
2. Map Azure IoT contracts: MQTT/AMQP/HTTPS protocols, twin desired/reported properties, direct method request/response, C2D message format, and Edge module deployment manifest.
3. Check whether device logic, twin state management, method handling, or Edge module logic are mixed with domain workflow logic.
4. Review operational concerns: device authentication (SAS, X.509, DPS), offline behavior, twin versioning, message routing, and IoT Edge offline/online transition.
5. Recommend device client, twin synchronizer, method handler, and Edge module boundaries.
6. Verify with Azure IoT device simulator, twin testing, direct method testing, and offline/online transition scenarios.

## Output Format

```markdown
Azure IoT architecture:
- IoT scenarios:
- Platform coupling:
- Security/offline concerns:
- Proposed boundaries:
- Verification:
```
